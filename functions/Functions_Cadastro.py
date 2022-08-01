import os

import shutil

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
    try:
        id_ferramenta = get_new_sequencial_id('ferramenta')
        with open("content/data/ferramenta.csv", "a") as ferramentas_arquivo:
            lista_ferramenta = [f'\n{id_ferramenta}',
                                f';{values["fDescricao"].strip()}',
                                f';{values["fCodFabricante"].strip()}',
                                f';{values["fFabricante"].strip()}',
                                f';{values["fVoltagem"].strip()}',
                                f';{values["fHRMaxReserva"].strip()}',
                                f';{values["fMinMaxReserva"].strip()}',
                                f';{values["fTamanho"].strip()}',
                                f';{values["fUnidade"].strip()}',
                                f';{values["fTipo"].strip()}',
                                f';{values["fMaterial"].strip()}',
                                ';False']  # Reservado? nasce como False.

            ferramentas_arquivo.writelines(lista_ferramenta)

        # Salvar Imagem da Ferramenta se existir
        if values['fImagem'].strip() != '':
            salvar_imagem('ferramenta', id_ferramenta, values['fImagem'], sg)

        return lista_ferramenta

    except:
        sg.popup("Erro ao salvar ferramenta", title='Error', font=8)

def salvar_imagem(tipo, id_number, filename, sg):
    try:
        if os.path.exists(filename):
            shutil.copyfile(filename, f'content/images/{tipo}_{id_number}.jpg')
        else:
            sg.popup("Erro ao salvar caminho da imagem", title='Error', font=8)
    except:
        sg.popup("Erro ao salvar imagem", title='Error', font=8)


def get_new_sequencial_id(tipo):
    id_number = 1000
    for linha in get_cadastrados(tipo):
        if int(linha[0]) > id_number:
            id_number = int(linha[0])

    id_number += 1

    return str(id_number)


def carregar_dados_tela(lista, tipo, window):
    if tipo == 'cadastro_ferramenta':
        list_keys = get_screen_keys(tipo)
        for index, campo in enumerate(lista):
            if index != 0 and index <= 10:
                window[list_keys[index - 1]].update(campo)

    elif tipo == 'cadastro_tecnico':
        list_keys = get_screen_keys(tipo)
        for index, campo in enumerate(lista):
            window[list_keys[index]].update(campo)


def get_screen_keys(tipo):
    lista_keys = []

    if tipo == 'cadastro_ferramenta':
        lista_keys = ['fDescricao', 'fCodFabricante', 'fFabricante', 'fVoltagem',
                      'fHRMaxReserva', 'fMinMaxReserva', 'fTamanho', 'fUnidade', 'fTipo',
                      'fMaterial']

    elif tipo == 'cadastro_tecnico':
        lista_keys = ['tCPF', 'tNome', 'tTelefone', 'tTurno', 'tEquipe']

    return lista_keys


def deletar_registro(index, tipo):
    if tipo == 'ferramenta':
        new_list = []
        with open(f'content/data/', "w") as lista_arquivo:
            for linhas in lista_arquivo:
                new_list.append(linhas)
            new_list.pop(index)
            lista_arquivo.writelines(linhas)
