import datetime
import io
import os

from PIL import Image

import functions.Functions_Cadastro as cadastro
import layouts.Layout_Components as components


def get_keys_to_clean(tipo_consulta):
    chaves_para_limpar = []
    if tipo_consulta == 'ferramenta_CON':
        chaves_para_limpar = ['cfFerramenta', 'cfDescricao', 'cfCodFabricante', 'cfFabricante', 'cfTamanho',
                              'cfUnidade', 'IMGFerramenta']

    elif tipo_consulta == 'tecnico_CON':
        chaves_para_limpar = ['ctCPF', 'ctNome', 'cfTurno', 'ctEquipe', 'IMGTecnico', 'ctTelefone']

    elif tipo_consulta == 'reserva_CON':
        chaves_para_limpar = ['crReserva', 'crFerramenta', 'crCPF', 'crNomeTecnico', 'crDescricao', 'crEmergencial',
                              'crDTRetirada', 'crDTDevol', 'crAtraso', 'crDevolvido', 'IMGTecnico_Reserva',
                              'IMGFerramenta_Reserva']

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
        lista_ferramentas = list(filter(lambda linha: values['cfFerramenta'].strip() in linha[0], lista_ferramentas))
    if values['cfDescricao'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: values['cfDescricao'].strip() in linha[1], lista_ferramentas))
    if values['cfCodFabricante'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: values['cfCodFabricante'].strip() in linha[2], lista_ferramentas))
    if values['cfFabricante'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: values['cfFabricante'].strip() in linha[3], lista_ferramentas))
    if values['cfTamanho'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: values['cfTamanho'].strip() in linha[7], lista_ferramentas))
    if values['cfUnidade'].strip() != '':
        lista_ferramentas = list(filter(lambda linha: values['cfUnidade'].strip() in linha[8], lista_ferramentas))

    window['-TABLE_CON_FERRAMENTAS-'].update(lista_ferramentas)


def filtrar_tecnicos(window, values):
    lista_tecnicos = cadastro.get_cadastrados('tecnico')

    if values['ctCPF'].strip() != '':
        lista_tecnicos = list(filter(lambda linha: values['ctCPF'].strip() in linha[0], lista_tecnicos))
    if values['ctNome'].strip() != '':
        lista_tecnicos = list(filter(lambda linha: values['ctNome'].strip() in linha[1], lista_tecnicos))
    if values['ctTelefone'].strip() != '':
        lista_tecnicos = list(filter(lambda linha: values['ctTelefone'].strip() in linha[2], lista_tecnicos))
    if values['cfTurno'].strip() != '':
        lista_tecnicos = list(filter(lambda linha: values['cfTurno'].strip() in linha[3], lista_tecnicos))
    if values['ctEquipe'].strip() != '':
        lista_tecnicos = list(filter(lambda linha: values['ctEquipe'].strip() in linha[4], lista_tecnicos))

    window['-TABLE_CON_TECNICOS-'].update(lista_tecnicos)


# TODO: Fazer
def filtrar_reservas(window, values):
    lista_reservas = cadastro.get_cadastrados('reserva')

    if values['crDevolvido']:
        lista_reservas_hist = cadastro.get_cadastrados('reserva_hist')
        if lista_reservas_hist:
            lista_reservas.extend(lista_reservas_hist)
            lista_reservas.sort()

    if values['crAtraso']:
        data_agora = datetime.datetime.now()
        lista_reservas = list(filter(lambda linha: data_agora > datetime.datetime(year=int(f'20{linha[8][6:]}'),
                                                                                  month=int(linha[8][3:5]),
                                                                                  day=int(linha[8][:2]),
                                                                                  hour=int(linha[9]),
                                                                                  minute=int(linha[10])),
                                     lista_reservas))

    if values['crReserva'].strip() != '':
        lista_reservas = list(filter(lambda linha: values['crReserva'].strip() in linha[0], lista_reservas))
    if values['crFerramenta'].strip() != '':
        lista_reservas = list(filter(lambda linha: values['crFerramenta'].strip() in linha[1], lista_reservas))
    if values['crCPF'].strip() != '':
        lista_reservas = list(filter(lambda linha: values['crCPF'].strip() in linha[2], lista_reservas))
    if values['crNomeTecnico'].strip() != '':
        lista_reservas = list(filter(lambda linha: values['crNomeTecnico'].strip() in linha[3], lista_reservas))
    if values['crDescricao'].strip() != '':
        lista_reservas = list(filter(lambda linha: values['crDescricao'].strip() in linha[4], lista_reservas))
    if values['crDTRetirada'].strip() != '':
        lista_reservas = list(filter(lambda linha: values['crDTRetirada'].strip() in linha[5], lista_reservas))
    if values['crDTDevol'].strip() != '':
        lista_reservas = list(filter(lambda linha: values['crDTDevol'].strip() in linha[8], lista_reservas))
    if values['crEmergencial'] != '' and (values['crEmergencial']) == True:
        lista_reservas = list(filter(lambda linha: str(values['crEmergencial']) in linha[11], lista_reservas))

    window['-TABLE_CON_RESERVAS-'].update(lista_reservas)


def limpar_filtros(window, tipo_consulta):
    for chave in get_keys_to_clean(tipo_consulta):
        window[chave].update('')


def atualiza_imagem_selecao(lista, tipo, linha_selecionada, window):
    if tipo == "reserva":

        identificador = lista[linha_selecionada][2]
        data = get_imagem('tecnico', identificador)
        window["IMGTecnico_Reserva"].update(data=data)

        identificador = lista[linha_selecionada][1]
        data = get_imagem('ferramenta', identificador)
        window["IMGFerramenta_Reserva"].update(data=data)

    else:
        identificador = lista[linha_selecionada][0]
        data = get_imagem(tipo, identificador)

        if tipo == 'ferramenta':
            window["IMGFerramenta"].update(data=data)

        elif tipo == 'tecnico':
            window['IMGTecnico'].update(data=data)


def baixar_csv(lista, caminho, tipo, sg):
    lista_csv = [f"{';'.join(components.get_table_header(tipo))}" + '\n']  # Header
    for linha in lista:
        linha_formatada = ';'.join(linha)
        lista_csv.append(linha_formatada)  # Linhas

    if os.path.exists(caminho):
        with open(file=f'{caminho}/{tipo}.csv', mode='w') as csv_gravacao:
            csv_gravacao.writelines(lista_csv)
