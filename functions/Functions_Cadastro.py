import os

from PIL import Image


def get_cadastro_ferramenta():
    lista_cadastrado_ferramentas = []
    with open("content/data/ferramentas.csv", "r") as ferramentas:
        for linha in ferramentas:
            linha_separada = linha.split(";")
            lista_cadastrado_ferramentas.append(linha_separada)

    return lista_cadastrado_ferramentas


def get_cadastro_tecnico():
    lista_cadastrado_tecnicos = [['46794179865', 'Carmo Durante Neto', '16992180889', 'Manhã', 'Hell Fire'],
                                 ['12345678910', 'Jose Carlos', '1699111111', 'Noite', 'Titans']]

    return lista_cadastrado_tecnicos


def cadastrar_ferramenta(values, sg):
    # Pega sequencial de id_ferramenta
    id_ferramenta = 1000

    for ferramenta in get_cadastro_ferramenta():
        if int(ferramenta[0]) > id_ferramenta:
            id_ferramenta = int(ferramenta[0])

    id_ferramenta += 1

    try:
        with open("content/data/ferramentas.csv", "a") as ferramentas_arquivo:
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
    try:
        if os.path.exists(filename):
            image = Image.open(filename)
            image.save(fp=f'content/data/{tipo}_{id_number}.jpg', format='JPEG')
        else:
            sg.popup("Erro ao salvar caminho da imagem", title='Error', font=8)

    except:
        sg.popup("Erro ao salvar imagem", title='Error', font=8)
