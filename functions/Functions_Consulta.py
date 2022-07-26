from PIL import Image
import io

def get_imagem_ferramenta(id_ferramenta):
    filename = f'content/images/ferramenta_{id_ferramenta}.jpg'
    image = Image.open(filename)
    image.thumbnail((100, 100))
    bio = io.BytesIO()
    image.save(bio, format='PNG')
    return bio
