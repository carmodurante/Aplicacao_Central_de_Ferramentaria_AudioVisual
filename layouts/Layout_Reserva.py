import PySimpleGUI as sg

import layouts.Layout_Components as components


def layout_reserva(lista_cadastrado_reservas):
    # Define Layout Cadastro Reservas
    left_column_reserva = [[sg.Text('ID Ferramenta', size=(18, 1)), sg.Input('', key='rFerramenta', size=13)],
                           [sg.Text('CPF do Técnico', size=(18, 1)), sg.Input('', key='rCPF', size=13)],
                           [sg.Text('Nome do Técnico', size=(18, 1)), sg.Input('', key='rNomeTecnico', size=35)],
                           [sg.Text('Descrição da Solicitação', size=(18, 1)),
                            sg.Input('', key='rDescricao', size=35)],
                           [sg.Text('Reserva Emergencial?', size=(18, 1),
                                    tooltip=components.get_tooltip_layout('rEmergencial')),
                            sg.Checkbox('', key='rEmergencial', default=False, font=16, size=(15, 1))]]

    right_column_reserva = [[sg.Text('Data da Retirada', size=(18, 1)), sg.Input('', key='rDTRetirada', size=8),
                             components.get_calendario('rDTRetirada')],
                            [sg.Text('Horário da Retirada', size=(18, 1)),
                             sg.Spin(values=components.get_horas_minutos(24), key='rHRRetirada', initial_value='12'),
                             sg.Text(':', auto_size_text=True),
                             sg.Spin(values=components.get_horas_minutos(59), key='rMinRetirada', initial_value='30')],
                            [sg.Text('Data da Devolução', size=(18, 1)), sg.Input('', key='rDTDevol', size=8),
                             components.get_calendario('rDTDevol')],
                            [sg.Text('Horário da Devolução', size=(18, 1)),
                             sg.Spin(values=components.get_horas_minutos(24), key='rHRDevol', initial_value='12'),
                             sg.Text(':', auto_size_text=True),
                             sg.Spin(values=components.get_horas_minutos(59), key='rMinDevol', initial_value='30')]]

    layout_cad_reserva = [[sg.Column(left_column_reserva, vertical_alignment='top', element_justification='left'),
                           sg.VSeparator(),
                           sg.Column(right_column_reserva, vertical_alignment='top', element_justification='left')],
                          [sg.Frame('Opções de Cadastro de Reserva', layout=components.get_buttons('CAD_RESERVA'),
                                    element_justification='left', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_cadastrado_reservas,
                                    headings=components.get_table_header('Reserva'),
                                    max_col_width=35,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='left',
                                    num_rows=6,
                                    key='-TABLE_CAD_RESERVAS-',
                                    row_height=35,
                                    enable_click_events=True,
                                    vertical_scroll_only=False,
                                    expand_x=True)]]

    return layout_cad_reserva
