import PySimpleGUI as sg

from layouts.Layout_Components import get_buttons
from layouts.Layout_Components import get_calendario
from layouts.Layout_Components import get_table_header


def layout_reserva(lista_cadastrado_reservas):
    # Define Layout Cadastro Reservas
    layout_cad_reserva = [[sg.Text('ID Ferramenta', size=(18, 1)), sg.Input('', key='rFerramenta', size=13),
                           sg.VerticalSeparator(pad=((242, 15), (1, 1))),
                           sg.Text('CPF do Técnico', size=(18, 1)), sg.Input('', key='rCPF', size=13)],
                          [sg.Text('Data da Retirada', size=(18, 1)), sg.Input('', key='rDTRetirada', size=8),
                           get_calendario('rDTRetirada'),
                           sg.VerticalSeparator(pad=((168, 15), (1, 1))),
                           sg.Text('Data da Devolução', size=(18, 1)), sg.Input('', key='rDTDevol', size=8),
                           get_calendario('rDTDevol')],
                          [sg.Text('Horário da Retirada', size=(18, 1)), sg.Input('', key='rHRRetirada', size=5),
                           sg.Text('(hh:mm)'),
                           sg.VerticalSeparator(pad=((236, 15), (1, 1))),
                           sg.Text('Horário da Devolução', size=(18, 1)), sg.Input('', key='rHRDevol', size=5),
                           sg.Text('(hh:mm)')],
                          [sg.Text('Reserva Emergencial?', size=(18, 1)),
                           sg.Checkbox('', key='rEmergencial', default=False, font=16, size=(15, 1))],
                          [sg.Frame('Opções de Cadastro de Reserva', layout=get_buttons('CAD_RESERVA'),
                                    element_justification='left', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_cadastrado_reservas,
                                    headings=get_table_header('Reserva'),
                                    max_col_width=35,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='left',
                                    num_rows=7,
                                    key='-TABLE_CAD_RESERVAS-',
                                    row_height=35,
                                    enable_click_events=True,
                                    vertical_scroll_only=False,
                                    expand_x=True)]]

    return layout_cad_reserva
