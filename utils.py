import os
import tempfile


def get_temp_image_path(img):
    temp_dir = tempfile.gettempdir()
    file_name = img.name
    temp_file_path = os.path.join(temp_dir, file_name)
    os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
    with open(temp_file_path, "wb") as img_file:
        img_file.write(img.getbuffer())
    return temp_file_path


def get_temp_dir():
    return tempfile.mkdtemp()
