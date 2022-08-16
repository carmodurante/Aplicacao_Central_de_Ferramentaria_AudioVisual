import PySimpleGUI as sg

import layouts.Layout_Components as components


def layout_consulta_ferramentas(lista_consulta_ferramentas):
    # Define Layout Consulta Ferramentas
    left_column_ferramenta = [[sg.Text('ID Ferramenta', size=(18, 1)), sg.Input('', key='cfFerramenta', size=10)],
                              [sg.Text('Descrição', size=(18, 1)), sg.Input('', key='cfDescricao', size=27)],
                              [sg.Text('Código do Fabricante', size=(18, 1)),
                               sg.Input('', key='cfCodFabricante', size=25)],
                              [sg.Text('Nome do Fabricante', size=(18, 1)),
                               sg.Input('', key='cfFabricante', size=27)],
                              [sg.Text('Tamanho', size=(18, 1)), sg.Input('', key='cfTamanho', size=15)], ]

    center_column_ferramenta = [[sg.Text('Unidade de Medida', size=(18, 1)), sg.Input('', key='cfUnidade', size=20)]]

    imagem_ferramenta = [[sg.Image(key="IMGFerramenta", expand_y=True, expand_x=True, pad=((1, 1), (5, 5)))]]

    right_column_ferramenta = [[sg.Frame('Imagem Ferramenta', layout=imagem_ferramenta,
                                         element_justification='center', expand_x=True, expand_y=True)]]

    layout_con_ferramentas = [[sg.Column(left_column_ferramenta, vertical_alignment='top'),
                               sg.VSeparator(),
                               sg.Column(center_column_ferramenta, vertical_alignment='top'),
                               sg.Push(),
                               sg.VSeparator(),
                               sg.Column(right_column_ferramenta, vertical_alignment='top', expand_x=True,
                                         expand_y=True)],
                              [sg.Frame('Opções de Consulta de Ferramentas',
                                        layout=components.get_buttons('CON_FERRAMENTA'),
                                        element_justification='center', expand_x=True, pad=(10, 10))],
                              [sg.Table(values=lista_consulta_ferramentas,
                                        headings=components.get_table_header('Ferramenta'),
                                        max_col_width=35,
                                        auto_size_columns=True,
                                        display_row_numbers=True,
                                        justification='left',
                                        num_rows=5,
                                        key='-TABLE_CON_FERRAMENTAS-',
                                        row_height=35,
                                        enable_click_events=True,
                                        expand_x=True,
                                        vertical_scroll_only=False)]]

    return layout_con_ferramentas


def layout_consulta_tecnicos(lista_consulta_tecnicos):
    # Define Layout Consulta Tecnicos
    left_column_tecnico = [[sg.Text('CPF', size=(18, 1)), sg.Input('', key='ctCPF', size=15)],
                           [sg.Text('Nome Completo', size=(18, 1)), sg.Input('', key='ctNome')],
                           [sg.Text('Celular/Rádio', size=(18, 1)), sg.Input('', key='ctTelefone', size=11)],
                           [sg.Text('Turno', size=(18, 1)), sg.Combo(['Manhã', 'Tarde', 'Noite'],
                                                                     default_value='Manhã', key='cfTurno', size=9)],
                           [sg.Text('Nome da Equipe', size=(18, 1)), sg.Input('', key='ctEquipe')]]

    center_column_ferramenta = [[sg.Text('', size=20)]]

    imagem_tecnico = [[sg.Image(key="IMGTecnico", expand_y=True, expand_x=True, pad=((1, 1), (5, 5)))]]

    right_column_tecnico = [[sg.Frame('Imagem Técnico', layout=imagem_tecnico,
                                      element_justification='center', expand_x=True, expand_y=True)]]

    layout_con_tecnico = [[sg.Column(left_column_tecnico, vertical_alignment='top'),
                           sg.Column(center_column_ferramenta, vertical_alignment='rigth'),
                           sg.Push(),
                           sg.VSeparator(),
                           sg.Column(right_column_tecnico, vertical_alignment='top', expand_x=True, expand_y=True)],
                          [sg.Frame('Opções de Consulta de Técnicos', layout=components.get_buttons('CON_TECNICO'),
                                    element_justification='center', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_consulta_tecnicos,
                                    headings=components.get_table_header('Tecnico'),
                                    max_col_width=35,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='left',
                                    num_rows=5,
                                    key='-TABLE_CON_TECNICOS-',
                                    row_height=35,
                                    enable_click_events=True,
                                    expand_x=True,
                                    vertical_scroll_only=False)]]

    return layout_con_tecnico


def layout_consulta_reservas(lista_consulta_reservas):
    # Define Layout Consulta Reservas
    left_column_reserva = [[sg.Text('ID Reserva', size=(18, 1)), sg.Input('', key='crReserva', size=13)]
                           [sg.Text('ID Ferramenta', size=(18, 1)), sg.Input('', key='crFerramenta', size=13)],
                           [sg.Text('CPF do Técnico', size=(18, 1)), sg.Input('', key='crCPF', size=13)],
                           [sg.Text('Nome do Técnico', size=(18, 1)), sg.Input('', key='crNomeTecnico', size=35)],
                           [sg.Text('Descrição da Solicitação', size=(18, 1)),
                            sg.Input('', key='crDescricao', size=35)]]

    center_column_reserva = [[sg.Text('Data da Retirada', size=(18, 1)), sg.Input('', key='crDTRetirada', size=8),
                              components.get_calendario('crDTRetirada')],
                             [sg.Text('Data da Devolução', size=(18, 1)), sg.Input('', key='crDTDevol', size=8),
                              components.get_calendario('crDTDevol')],
                             [sg.Text('Reserva Emergencial?', size=(18, 1),
                                      tooltip=components.get_tooltip_layout('rEmergencial')),
                              sg.Checkbox('', key='crEmergencial', default=False)]
                             [sg.Text('Reservas em Atraso?', size=(18, 1)),
                              sg.Checkbox('', key='crAtraso', default=False)]]

    imagem_tecnico = [[sg.Image(key="IMGTecnico_Reserva", expand_y=True, expand_x=True, pad=((1, 1), (5, 5)))]]

    imagem_ferramenta = [[sg.Image(key="IMGFerramenta_Reserva", expand_y=True, expand_x=True, pad=((1, 1), (5, 5)))]]

    right_column_reserva = [[sg.Frame('Imagem Técnico', layout=imagem_tecnico,
                                      element_justification='left', expand_x=True, expand_y=True),
                             sg.VSeparator(),
                             sg.Frame('Imagem Ferramenta', layout=imagem_ferramenta,
                                      element_justification='right', expand_x=True, expand_y=True)]]

    layout_con_reserva = [[sg.Column(left_column_reserva, vertical_alignment='top', element_justification='left'),
                           sg.VSeparator(),
                           sg.Column(center_column_reserva, vertical_alignment='top', element_justification='left'),

                           sg.VSeparator(),
                           sg.Column(right_column_reserva, vertical_alignment='top', element_justification='center',
                                     expand_y=True, expand_x=True)],
                          [sg.Frame('Opções de Cadastro de Reserva', layout=components.get_buttons('CON_RESERVA'),
                                    element_justification='left', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_consulta_reservas,
                                    headings=components.get_table_header('Reserva'),
                                    max_col_width=35,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='left',
                                    num_rows=5,
                                    key='-TABLE_CON_RESERVAS-',
                                    row_height=35,
                                    enable_click_events=True,
                                    vertical_scroll_only=False,
                                    expand_x=True)]]

    return layout_con_reserva


def layout_consulta_principal(lista_consulta_ferramentas, lista_consulta_tecnicos, lista_consulta_reservas):
    # Define o TabGroup Consulta
    tabgrp_consulta = [[sg.TabGroup([[
        sg.Tab('Consulta de Ferramentas', layout_consulta_ferramentas(lista_consulta_ferramentas), border_width=5,
               element_justification='left'),
        sg.Tab('Consulta de Técnicos     ', layout_consulta_tecnicos(lista_consulta_tecnicos), border_width=5,
               element_justification='left'),
        sg.Tab('Consulta de Reservas     ', layout_consulta_reservas(lista_consulta_reservas), border_width=5,
               element_justification='left')
    ]], tab_location=sg.TAB_LOCATION_TOP_LEFT, border_width=7, font='_ 12')]]

    return tabgrp_consulta
