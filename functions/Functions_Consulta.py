import io
import os

from PIL import Image

import functions.Functions_Cadastro as cadastro


def get_keys_to_clean(tipo_consulta):
    chaves_para_limpar = []
    if tipo_consulta == 'ferramenta_CON':
        chaves_para_limpar = ['cfFerramenta', 'cfDescricao', 'cfCodFabricante', 'cfFabricante', 'cfTamanho',
                              'cfUnidade', 'IMGFerramenta']

    elif tipo_consulta == 'tecnico_CON':
        chaves_para_limpar = ['ctCPF', 'ctNome', 'cfTurno', 'ctEquipe', 'IMGTecnico', 'ctTelefone']

    elif tipo_consulta == 'reserva_CON':
        chaves_para_limpar = ['crFerramenta', 'crCPF', 'crNomeTecnico', 'crDescricao', 'crEmergencial', 'crDTRetirada',
                              'crDTDevol', 'crAtraso', 'crHRDevol', 'IMGTecnico_Reserva', 'IMGFerramenta_Reserva']

    elif tipo_consulta == 'ferramenta_CAD':
        chaves_para_limpar = ['fDescricao', 'fCodFabricante', 'fFabricante', 'fTamanho',
                              'fUnidade', 'fVoltagem', 'fTipo', 'fMaterial', 'fImagem']

    elif tipo_consulta == 'tecnico_CAD':
        chaves_para_limpar = ['tCPF', 'tNome', 'tTurno', 'tEquipe', 'tTelefone', 'tImagem']

    elif tipo_consulta == 'reserva_CAD':
        chaves_para_limpar = ['rFerramenta', 'rCPF', 'rNomeTecnico', 'rDescricao', 'rEmergencial', 'rDTRetirada',
                              'rDTDevol']

    return chaves_para_limpar


def get_imagem(tipo_consulta, identificador):
    filename = f'content/images/{tipo_consulta}_{identificador}.jpg'
    if not os.path.exists(filename):  # Se imagem nao existir, exibe uma generica
        filename = f'content/images/sem_imagem.jpg'

    image = Image.open(filename)
    image.thumbnail((100, 100))
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        data = output.getvalue()
        return data


def filtrar_ferramentas(window, values):
    lista_ferramentas = cadastro.get_cadastrados('ferramenta')

    if values['cfFerramenta'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: linha[0] == values['cfFerramenta'].strip(), lista_ferramentas))
    if values['cfDescricao'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: linha[1] == values['cfDescricao'].strip(), lista_ferramentas))
    if values['cfCodFabricante'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: linha[2] == values['cfCodFabricante'].strip(), lista_ferramentas))
    if values['cfTamanho'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: linha[7] == values['cfTamanho'].strip(), lista_ferramentas))
    if values['cfUnidade'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: linha[8] == values['cfUnidade'].strip(), lista_ferramentas))

    window['-TABLE_CON_FERRAMENTAS-'].update(lista_ferramentas)


# TODO: Fazer
def filtrar_tecnicos(window, values):
    lista_tecnicos = cadastro.get_cadastrados('tecnico')

    return lista_tecnicos


# TODO: Fazer
def filtrar_reservas(window, values):
    lista_ferramentas = cadastro.get_cadastrados('reserva')


def limpar_filtros(window, tipo_consulta):
    for chave in get_keys_to_clean(tipo_consulta):
        window[chave].update('')


def atualiza_imagem_selecao(lista, tipo, linha_selecionada, window):
    if tipo == "reserva":
        window["IMGTecnico_Reserva"].update(data="bio.getvalue()")
        window["IMGFerramenta_Reserva"].update(data='bio.getvalue()')
    else:
        identificador = lista[linha_selecionada][0]
        data = get_imagem(tipo, identificador)

        if tipo == 'ferramenta':
            window["IMGFerramenta"].update(data=data)

        elif tipo == 'tecnico':
            window['IMGTecnico'].update(data=data)
