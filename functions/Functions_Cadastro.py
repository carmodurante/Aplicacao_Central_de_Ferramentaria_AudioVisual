import io
import os

from PIL import Image


def get_cadastrados(tipo):
    lista_cadastrados = []
    try:
        with open(f'content/data/{tipo}.csv', "r") as cadastrados_arquivo:
            for linha in cadastrados_arquivo:
                linha_separada = linha.split(";")
                lista_cadastrados.append(linha_separada)

        return lista_cadastrados

    except:
        return lista_cadastrados

def cadastrar_ferramenta(values, sg):
    id_ferramenta = ''
    try:
        id_ferramenta = get_new_sequencial_id('ferramenta')
        with open("content/data/ferramenta.csv", "a") as ferramentas_arquivo:
            lista_ferramenta = [f'\n{id_ferramenta}',
                                f';{values["fDescricao"].strip()}',
                                f';{values["fCodFabricante"].strip()}',
                                f';{values["fCodFabricante"].strip()}',
                                f';{values["fFabricante"].strip()}',
                                f';{values["fVoltagem"].strip()}',
                                f';{values["fHRMaxReserva"].strip()}',
                                f';{values["fMinMaxReserva"].strip()}',
                                f';{values["fTamanho"].strip()}',
                                f';{values["fUnidade"].strip()}',
                                f';{values["fTipo"].strip()}',
                                f';{values["fMaterial"].strip()}']

            ferramentas_arquivo.writelines(lista_ferramenta)

    except:
        sg.popup("Erro ao salvar ferramenta", title='Error', font=8)

    # Salvar Imagem da Ferramenta se existir
    if values['fImagem'].strip() != '':
        salvar_imagem('ferramenta', id_ferramenta, values['fImagem'], sg)

    return lista_ferramenta


def salvar_imagem(tipo, id_number, filename, sg):
    # try:
    if os.path.exists(filename):
        image = Image.open(filename)
        caminho = f'content/images/{tipo}_{id_number}.jpg'
        image.thumbnail((180, 180))
        bio = io.BytesIO()
        image.save(bio, format='PNG')
        image.save(fp=caminho, format='JPG')
    else:
        sg.popup("Erro ao salvar caminho da imagem", title='Error', font=8)


# except:
#     sg.popup("Erro ao salvar imagem", title='Error', font=8)


def get_new_sequencial_id(tipo):
    id_number = 1000

    for linha in get_cadastrados(tipo):
        if int(linha[0]) > id_number:
            id_ferramenta = int(linha[0])

    id_number += 1

    return str(id_number)
