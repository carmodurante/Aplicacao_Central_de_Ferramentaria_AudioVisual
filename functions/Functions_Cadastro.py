import os
import shutil
import traceback

import functions.Functions_Diversos as util


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


def salvar_imagem(tipo, id_number, filename, sg):
    try:
        filename_destino = f'content/images/{tipo}_{id_number}.jpg'
        if os.path.exists(filename):
            if os.path.exists(filename_destino):  # Deleta imagem se ja existir
                os.remove(filename_destino)
            shutil.copyfile(filename, filename_destino)
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
    try:
        if tipo == 'cadastro_ferramenta':
            list_keys = get_screen_keys(tipo)
            for index, campo in enumerate(lista):
                if index != 0 and index <= 10:
                    window[list_keys[index - 1]].update(campo)

        elif tipo == 'cadastro_tecnico':
            list_keys = get_screen_keys(tipo)
            for index, campo in enumerate(lista):
                window[list_keys[index]].update(campo)
    except Exception:
        traceback.print_exc()


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
    new_list = []
    with open(file=f'content/data/{tipo}.csv', mode='r') as lista_leitura:
        for linhas in lista_leitura:
            new_list.append(linhas)
        new_list.pop(index)

    with open(file=f'content/data/{tipo}.csv', mode='w') as lista_gravacao:
        lista_gravacao.writelines(new_list)


def cadastrar_ferramenta(values, sg):
    try:
        id_ferramenta = get_new_sequencial_id('ferramenta')
        with open("content/data/ferramenta.csv", "a") as ferramentas_arquivo:
            lista_ferramenta = f'{id_ferramenta}' \
                               f';{values["fDescricao"].strip()}' \
                               f';{values["fCodFabricante"].strip()}' \
                               f';{values["fFabricante"].strip()}' \
                               f';{values["fVoltagem"].strip()}' \
                               f';{values["fHRMaxReserva"].strip()}' \
                               f';{values["fMinMaxReserva"].strip()}' \
                               f';{values["fTamanho"].strip()}' \
                               f';{values["fUnidade"].strip()}' \
                               f';{values["fTipo"].strip()}' \
                               f';{values["fMaterial"].strip()}\n'

            ferramentas_arquivo.writelines(lista_ferramenta)

        # Salvar Imagem da Ferramenta se existir
        if values['fImagem'].strip() != '':
            salvar_imagem('ferramenta', id_ferramenta, values['fImagem'], sg)
        else:
            filename = f'content/images/ferramenta_{id_ferramenta}.jpg'
            if os.path.exists(filename):  # Deleta imagem se ja existir
                os.remove(filename)

        return lista_ferramenta

    except:
        sg.popup("Erro ao salvar ferramenta", title='Error', font=8)


def cadastrar_tecnico(values, sg):
    try:
        # Validacoes de CPF e Celular/Telefone
        if not util.validar_cpf(values["tCPF"].strip()):
            sg.popup("CPF Inválido", title='Error', font=8)
            return
        if not util.validar_celular(values["tTelefone"].strip()):
            sg.popup("Celular/Telefone Inválido", title='Error', font=8)
            return

        with open("content/data/tecnico.csv", "a") as tecnico_arquivo:
            lista_tecnico = f'{values["tCPF"].strip()}' \
                            f';{values["tNome"].strip()}' \
                            f';{values["tTelefone"].strip()}' \
                            f';{values["tTurno"].strip()}' \
                            f';{values["tEquipe"].strip()}\n'

            tecnico_arquivo.writelines(lista_tecnico)

            # Salvar Imagem da Ferramenta se existir
        if values['tImagem'].strip() != '':
            salvar_imagem('tecnico', values["tCPF"].strip(), values['tImagem'], sg)
        else:
            filename = f'content/images/tecnico_{values["tCPF"].strip()}.jpg'
            if os.path.exists(filename):  # Deleta imagem se ja existir
                os.remove(filename)

        return lista_tecnico

    except:
        sg.popup("Erro ao salvar tecnico", title='Error', font=8)


def modificar_ferramenta(index, values, sg):
    try:
        with open("content/data/ferramenta.csv", "r") as ferramentas_leitura:
            new_list = []
            for linhas in ferramentas_leitura:
                new_list.append(linhas)
            id_ferramenta = new_list[index][0:4].strip()  # get id_ferramenta selecionado
            new_list.pop(index)  # Remove valor antigo
            ferramentas_leitura.close()

            lista_ferramenta = f'{id_ferramenta}' \
                               f';{values["fDescricao"].strip()}' \
                               f';{values["fCodFabricante"].strip()}' \
                               f';{values["fFabricante"].strip()}' \
                               f';{values["fVoltagem"].strip()}' \
                               f';{values["fHRMaxReserva"].strip()}' \
                               f';{values["fMinMaxReserva"].strip()}' \
                               f';{values["fTamanho"].strip()}' \
                               f';{values["fUnidade"].strip()}' \
                               f';{values["fTipo"].strip()}' \
                               f';{values["fMaterial"].strip()}\n'

        with open("content/data/ferramenta.csv", "w") as ferramentas_gravacao:
            new_list.insert(index, lista_ferramenta)  # Insere valor novo da tela
            ferramentas_gravacao.writelines(new_list)

        # Salvar Imagem da Ferramenta se existir
        if values['fImagem'].strip() != '':
            salvar_imagem('ferramenta', id_ferramenta, values['fImagem'], sg)
        else:
            filename = f'content/images/ferramenta_{id_ferramenta}.jpg'
            if os.path.exists(filename):  # Deleta imagem se ja existir
                os.remove(filename)

    except Exception:
        traceback.print_exc()
        sg.popup("Erro ao modificar ferramenta", title='Error', font=8)


def modificar_tecnico(index, values, sg):
    try:
        # Validacoes de CPF e Celular/Telefone
        if not util.validar_cpf(values["tCPF"].strip()):
            sg.popup("CPF Inválido", title='Error', font=8)
            return
        if not util.validar_celular(values["tTelefone"].strip()):
            sg.popup("Celular/Telefone Inválido", title='Error', font=8)
            return

        with open("content/data/tecnico.csv", "r") as tecnicos_leitura:
            new_list = []
            for linhas in tecnicos_leitura:
                new_list.append(linhas)
            tecnico_cpf = values["tCPF"].strip()
            new_list.pop(index)  # Remove valor antigo
            tecnicos_leitura.close()

            lista_tecnico = f'{tecnico_cpf}' \
                            f';{values["tNome"].strip()}' \
                            f';{values["tTelefone"].strip()}' \
                            f';{values["tTurno"].strip()}' \
                            f';{values["tEquipe"].strip()}\n'

        with open("content/data/tecnico.csv", "w") as tecnicos_gravacao:
            new_list.insert(index, lista_tecnico)  # Insere valor novo da tela
            tecnicos_gravacao.writelines(new_list)

        # Salvar Imagem do Tecnico se existir
        if values['tImagem'].strip() != '':
            salvar_imagem('tecnico', tecnico_cpf, values['tImagem'], sg)
        else:
            filename = f'content/images/tecnico_{tecnico_cpf}.jpg'
            if os.path.exists(filename):  # Deleta imagem se ja existir
                os.remove(filename)

    except Exception:
        traceback.print_exc()
        sg.popup("Erro ao modificar tecnico", title='Error', font=8)
