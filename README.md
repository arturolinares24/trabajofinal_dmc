# Mi Aplicación de Generación y Clasificación de Imágenes

Esta es una aplicación simple que te permite generar y clasificar imágenes utilizando un modelo de inteligencia artificial. La aplicación tiene tres botones principales y una funcionalidad adicional con la barra lateral:

## Funcionalidades Principales

1. **Generar Imagen:** Este botón genera una imagen basada en el texto que ingresas en el campo de entrada.
   
2. **Clasificar:** Una vez que has generado una imagen, puedes utilizar este botón para clasificarla y obtener información sobre su contenido.

3. **Generar y Clasificar:** Si deseas generar una imagen y clasificarla de inmediato, puedes usar este botón para hacer ambas cosas en un solo paso.

## Funcionalidad Adicional

- **Subir Imagen desde la Barra Lateral:** Si decides subir una imagen desde la barra lateral, el botón de "Generar Imagen" se deshabilitará automáticamente y deberás usar el botón "Clasificar" para obtener información sobre la imagen subida.

## Requerimientos

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar la aplicación:
- Python 3.x
- Streamlit
- Requests
- Transformers
- Tokenizers
- Pillow

## Ejecutar la Aplicación

### Con Docker

Para ejecutar la aplicación con Docker, sigue estos pasos:

1. Construye la imagen Docker ejecutando el siguiente comando en tu terminal:
    

    docker build -t streamlit .

2. Ejecuta el contenedor Docker con el siguiente comando:
    
    
    docker run -p 8501:8501 streamlit


### En Local

Para ejecutar la aplicación en local con Streamlit, simplemente ejecuta el siguiente comando en tu terminal:


    streamlit run app.py
