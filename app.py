import os
import utils
import streamlit as st
import requests
from transformers import AutoFeatureExtractor, DeiTForImageClassificationWithTeacher
import base64

engine_id = "stable-diffusion-xl-1024-v1-0"
api_host = "https://api.stability.ai"
api_key = "sk-6BTVraIgMUvAbLaZhvAMDS1S2jtr4icjcYFKsyWMlheKMSVy"

from PIL import Image
import tempfile

st.set_page_config(
    page_title="Image Generation and Classification",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Título de la aplicación
st.title('Aplicacion')

# Crear un campo de entrada de texto
input_text = st.text_input('Ingrese algún texto')


@st.cache_resource
def load_model():
    # Cargar el extractor de características y el modelo de Hugging Face
    feature_extracto = AutoFeatureExtractor.from_pretrained('facebook/deit-small-distilled-patch16-224')
    modelo = DeiTForImageClassificationWithTeacher.from_pretrained('facebook/deit-small-distilled-patch16-224')
    return feature_extracto, modelo



feature_extractor, model = load_model()

# Inicializar image_counter en el estado de la sesión si no existe
if 'images' not in st.session_state:
    st.session_state['images'] = "0"

if 'flag' not in st.session_state:
    st.session_state['flag'] = False

if 'but_a' not in st.session_state:
    st.session_state.disabled = False


with st.sidebar:
    # if st.session_state.flag is False:
    st.title("Sube tu imagen ")
    image = st.file_uploader(label=" ", accept_multiple_files=False)
    if image is not None and st.session_state.flag is False:
        # st.session_state.images = st.session_state.images[0]

        st.session_state.images = utils.get_temp_image_path(image)
        st.session_state.flag = True
        image = Image.open(st.session_state.images)
        st.image(image, caption='Imagen Generada')

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    # Crear un botón
    if st.button('Mostrar Imagen', disabled=st.session_state.flag):

        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": input_text
                    }
                ],
                "cfg_scale": 7,
                "height": 1024,
                "width": 1024,
                "samples": 1,
                "steps": 30,
            },
        )
        data = response.json()
        temp_dir = tempfile.mkdtemp()
        temp_file_path_prev = os.path.join(temp_dir, f"imagen.png")

        for i, image in enumerate(data["artifacts"]):
            with open(temp_file_path_prev, "wb") as f:
                f.write(base64.b64decode(image["base64"]))
            st.session_state.images = temp_file_path_prev


        # Si se hace clic en el botón, mostrar la imagen
        st.image(temp_file_path_prev,
                 caption='Imagen Generada')


with col2:
    if st.button('Clasificar'):

        image = Image.open(st.session_state.images)
        st.image(image, caption='Imagen Generada')
        # Preprocesar la imagen y prepararla para el modelo
        inputs = feature_extractor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits

        # Obtener la clase con la mayor probabilidad
        predicted_class_idx = logits.argmax(-1).item()
        predicted_class = model.config.id2label[predicted_class_idx]

        st.session_state.images = []
        st.session_state.flag = False
        # Mostrar la clase predicha
        st.write(f"Clase predicha: {predicted_class}")

with col3:
    if st.button('Generar Imagen y Clasificiar', disabled=st.session_state.flag):

        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": input_text
                    }
                ],
                "cfg_scale": 7,
                "height": 1024,
                "width": 1024,
                "samples": 1,
                "steps": 30,
            },
        )
        data = response.json()
        temp_dir = tempfile.mkdtemp()
        temp_file_path_prev = os.path.join(temp_dir, f"imagen.png")

        for i, image in enumerate(data["artifacts"]):
            with open(temp_file_path_prev, "wb") as f:
                f.write(base64.b64decode(image["base64"]))
            st.session_state.images = temp_file_path_prev

        # Si se hace clic en el botón, mostrar la imagen
        st.image(temp_file_path_prev,
                 caption='Imagen Generada')

        image = Image.open(st.session_state.images)

        inputs = feature_extractor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        #
        # # Obtener la clase con la mayor probabilidad
        predicted_class_idx = logits.argmax(-1).item()
        predicted_class = model.config.id2label[predicted_class_idx]

        st.session_state.images = []
        st.session_state.flag = False
        # Mostrar la clase predicha
        st.write(f"Clase predicha: {predicted_class}")
