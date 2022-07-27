import io

from PIL import Image


def get_imagem_ferramenta(id_ferramenta):
    filename = f'content/images/ferramenta_{id_ferramenta}.jpg'
    image = Image.open(filename)
    image.thumbnail((100, 100))
    bio = io.BytesIO()
    image.save(bio, format='PNG')
    return bio


def filtrar_ferramentas(window, values):
    lista_ferramentas = []
    bio = get_imagem_ferramenta('1001')
    window["IMGFerramenta"].update(data=bio.getvalue())

    return lista_ferramentas


def limpar_filtro_ferramentas(window):
    chaves_para_limpar = ['cfFerramenta', 'cfDescricao', 'cfCodFabricante', 'cfFabricante', 'cfTamanho', 'cfUnidade',
                          'cfReservado', 'IMGFerramenta']
    for chave in chaves_para_limpar:
        window[chave].update('')
