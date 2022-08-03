import PySimpleGUI as sg

from functions.Functions_Utils import get_color
from layouts.Layout_Cadastro import layout_cadastro_principal
from layouts.Layout_Consulta import layout_consulta_principal
from layouts.Layout_Reserva import layout_reserva


def layout_principal(lista_ferramentas, lista_tecnicos, lista_reservas,
                     usuario_logado):
    # Definição Tela Principal
    layout_cabecalho = [sg.T('Central de Ferramentaria AudioVisual', font='_ 16', justification='c', expand_x=True,
                             border_width=10, background_color='white', text_color='black')]

    layout_footer = [sg.Text('Usuário Logado:', size=(12, 1)),
                     sg.Text(usuario_logado['username'], size=(18, 1), text_color='green'),
                     sg.Text('Admin: ', size=(5, 1)),
                     sg.Text(usuario_logado['admin'], size=(18, 1), text_color=get_color(usuario_logado['admin'])),
                     sg.Push(),
                     sg.Text('@DevTeam_05', size=(15, 1), text_color='purple', enable_events=True, key='URL_DEV5',
                             tooltip='Abrir Documentação no Github')]

    layout_cadastros = [sg.Tab('Cadastros', layout_cadastro_principal(lista_ferramentas,
                                                                      lista_tecnicos),
                               border_width=5, element_justification='left')]

    layout_consultas = [sg.Tab('Consultas', layout_consulta_principal(lista_ferramentas,
                                                                      lista_tecnicos,
                                                                      lista_reservas),
                               border_width=5, element_justification='left')]

    layout_reservas = [sg.Tab('Reservas', layout_reserva(lista_reservas),
                              border_width=5, element_justification='left')]

    # Somente Administradores tem permissão para cadastrar e reservar
    if usuario_logado['admin'] == 'True':
        tabgroup_menu_admin = [layout_cabecalho,
                               [sg.TabGroup([
                                   layout_cadastros,
                                   layout_consultas,
                                   layout_reservas],
                                   tab_location=sg.TAB_LOCATION_TOP, border_width=12, font='_ 12')],
                               [layout_footer]]

        return tabgroup_menu_admin

    else:
        tabgroup_menu = [layout_cabecalho,
                         [sg.TabGroup([
                             layout_consultas],
                             tab_location=sg.TAB_LOCATION_TOP, border_width=12, font='_ 12')],
                         [layout_footer]]

        return tabgroup_menu
