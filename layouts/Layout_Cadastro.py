import PySimpleGUI as sg

from functions.Functions_Diversos import get_file_types
from layouts.Layout_Components import get_buttons
from layouts.Layout_Components import get_table_header


def layout_cadastro(lista_cadastrado_ferramentas, lista_cadastrado_tecnicos):
    # Define Layout Cadastro Ferramentas

    left_column_ferramentas = [[sg.Text('Descrição', size=(18, 1)), sg.Input('', key='fDescricao')],
                               [sg.Text('Nome do Fabricante', size=(18, 1)), sg.Input('', key='fFabricante', size=35)],
                               [sg.Text('Voltagem de Uso', size=(18, 1)),
                                sg.Combo(['220V', '110V', 'N/D'], default_value='110V', key='fVoltagem', size=10),
                                sg.Text('(Volts)', size=(7, 1))],
                               [sg.Text('Código no Fabricante', size=(18, 1)),
                                sg.Input('', key='fCodFabricante', size=20)],
                               [sg.Text('Tempo Max. de Reserva', size=(18, 1)),
                                sg.Input('', key='fTempoReserva', size=6, ),
                                sg.Text('(hh:mm)', size=(7, 1))]]

    right_column_ferramentas = [[sg.Text('Tamanho', size=(18, 1)), sg.Input('', key='fTamanho', size=20)],
                                [sg.Text('Unidade de Medida', size=(18, 1)), sg.Input('', key='fUnidade', size=15)],
                                [sg.Text('Tipo da Ferramenta', size=(18, 1)), sg.Input('', key='fTipo', size=20)],
                                [sg.Text('Material da Ferramenta', size=(18, 1)),
                                 sg.Input('', key='fMaterial', size=25)],
                                [sg.Text('Imagem da Ferramenta', size=(18, 1)), sg.Input('', key="fImagem"),
                                 sg.FileBrowse(file_types=get_file_types(), button_text='Carregar Imagem',
                                               auto_size_button=True)]]

    layout_cad_ferramentas = [[sg.Column(left_column_ferramentas, vertical_alignment='left'), sg.VSeparator(),
                               sg.Column(right_column_ferramentas, vertical_alignment='left')],
                              [sg.Frame('Opções de Cadastro de Ferramentas', layout=get_buttons('CAD_FERRAMENTA'),
                                        element_justification='left', expand_x=True, pad=(10, 10))],
                              [sg.Table(values=lista_cadastrado_ferramentas,
                                        headings=get_table_header('Ferramenta'),
                                        max_col_width=35,
                                        auto_size_columns=True,
                                        display_row_numbers=True,
                                        justification='left',
                                        num_rows=5,
                                        key='-TABLE_CAD_FERRAMENTAS-',
                                        row_height=35,
                                        enable_click_events=True,
                                        expand_x=True,
                                        vertical_scroll_only=False)]]

    # Define Layout Cadastro Tecnicos
    left_column_tecnicos = [[sg.Text('CPF', size=(18, 1)), sg.Input('', key='tCPF', size=15)],
                            [sg.Text('Nome', size=(18, 1)), sg.Input('', key='tNome')],
                            [sg.Text('Celular/Rádio', size=(18, 1)), sg.Input('', key='tTelefone', size=11)],
                            [sg.Text('Turno', size=(18, 1)), sg.Combo(['Manhã', 'Tarde', 'Noite'],
                                                                      default_value='Manhã', key='fTurno', size=9)],
                            [sg.Text('Nome da Equipe', size=(18, 1)), sg.Input('', key='tEquipe')]]
    right_column_tecnicos = [[sg.Text('Imagem do Técnico', size=(18, 1)), sg.Input('', key="tImagem"),
                              sg.FileBrowse(file_types=get_file_types(), button_text='Carregar Imagem',
                                            auto_size_button=True)]]
    layout_cad_tecnico = [[sg.Column(left_column_tecnicos, vertical_alignment='left'), sg.VSeparator(),
                           sg.Column(right_column_tecnicos, vertical_alignment='top')],
                          [sg.Frame('Opções de Cadastro de Técnicos', layout=get_buttons('CAD_TECNICO'),
                                    element_justification='botton', expand_x=True, pad=(10, 10),
                                    vertical_alignment='top')],
                          [sg.Table(values=lista_cadastrado_tecnicos,
                                    headings=get_table_header('Tecnico'),
                                    max_col_width=35,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='left',
                                    num_rows=5,
                                    key='-TABLE_CAD_TECNICOS-',
                                    row_height=35,
                                    enable_click_events=True,
                                    expand_x=True,
                                    vertical_scroll_only=False)]]

    # Define o TabGroup Cadastro
    tabgrp_cadastro = [[sg.TabGroup([[
        sg.Tab('Cadastro de Ferramentas', layout_cad_ferramentas, border_width=5, element_justification='left'),
        sg.Tab('Cadastro de Técnicos      ', layout_cad_tecnico, border_width=5, element_justification='left')
    ]], tab_location=sg.TAB_LOCATION_TOP_LEFT, border_width=7, font='_ 12')]]

    return tabgrp_cadastro
