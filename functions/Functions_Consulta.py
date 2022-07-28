import io

from PIL import Image


def get_keys_to_clean(tipo_consulta):
    chaves_para_limpar = []
    if tipo_consulta == 'ferramenta_CON':
        chaves_para_limpar = ['cfFerramenta', 'cfDescricao', 'cfCodFabricante', 'cfFabricante', 'cfTamanho',
                              'cfUnidade', 'cfReservado', 'IMGFerramenta']

    elif tipo_consulta == 'tecnico_CON':
        chaves_para_limpar = ['ctCPF', 'ctNome', 'cfTurno', 'ctEquipe', 'IMGTecnico', 'ctTelefone']

    elif tipo_consulta == 'ferramenta_CAD':
        chaves_para_limpar = ['fDescricao', 'fCodFabricante', 'fFabricante', 'fTamanho',
                              'fUnidade', 'fVoltagem', 'fTipo', 'fMaterial', 'fTempoReserva', 'fImagem']

    elif tipo_consulta == 'tecnico_CAD':
        chaves_para_limpar = ['tCPF', 'tNome', 'fTurno', 'tEquipe', 'tTelefone', 'tImagem']

    elif tipo_consulta == 'reserva_CAD':
        chaves_para_limpar = ['rFerramenta', 'rCPF', 'rNomeTecnico', 'rDescricao', 'rEmergencial', 'rDTRetirada',
                              'rHRRetirada', 'rDTDevol', 'rHRDevol']

    return chaves_para_limpar


def get_imagem(identificador, tipo_consulta):
    filename = f'content/images/{tipo_consulta}_{identificador}.jpg'
    image = Image.open(filename)
    image.thumbnail((100, 100))
    bio = io.BytesIO()
    image.save(bio, format='PNG')
    return bio


def filtrar_ferramentas(window, values):
    lista_ferramentas = []
    bio = get_imagem('1001', 'ferramenta')
    window["IMGFerramenta"].update(data=bio.getvalue())

    return lista_ferramentas


def filtrar_tecnicos(window, values):
    lista_tecnicos = []
    bio = get_imagem('46794179865', 'tecnico')
    window["IMGTecnico"].update(data=bio.getvalue())

    return lista_tecnicos


def limpar_filtros(window, tipo_consulta):
    for chave in get_keys_to_clean(tipo_consulta):
        window[chave].update('')
