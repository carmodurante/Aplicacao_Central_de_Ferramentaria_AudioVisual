import PySimpleGUI as sg

from layouts.Layout_Components import get_buttons
from layouts.Layout_Components import get_table_header


def layout_consulta(lista_consulta_ferramentas, lista_consulta_tecnicos, lista_consulta_reservas):
    # Define Layout Consulta Ferramentas
    left_column = [[sg.Text('ID Ferramenta', size=(18, 1)), sg.Input('', key='cfFerramenta', size=10),
                    sg.VerticalSeparator(pad=((143, 15), (1, 1))),
                    sg.Text('Descrição', size=(18, 1)), sg.Input('', key='cfDescricao')],
                   [sg.Text('Código do Fabricante', size=(18, 1)),
                    sg.Input('', key='cfCodFabricante', size=25),
                    sg.VerticalSeparator(pad=((38, 15), (1, 1))),
                    sg.Text('Nome do Fabricante', size=(18, 1)), sg.Input('', key='cfFabricante')],
                   [sg.Text('Tamanho', size=(18, 1)), sg.Input('', key='cfTamanho', size=20),
                    sg.VerticalSeparator(pad=((73, 15), (1, 1))),
                    sg.Text('Unidade de Medida', size=(18, 1)), sg.Input('', key='cfUnidade', size=25)],
                   [sg.Text('Reservado', size=(18, 1)), sg.Checkbox('', key='cfReservado', default=False)]]

    imagem_ferramenta = [[sg.Image(key="IMGFerramenta", expand_y=True, expand_x=True, pad=((1, 1), (5, 5)))]]

    right_column = [[sg.Frame('Imagem Ferramenta', layout=imagem_ferramenta,
                              element_justification='right', expand_x=True, expand_y=True)]]
    layout_con_ferramentas = [
        [sg.Column(left_column, vertical_alignment='top'), sg.VSeparator(),
         sg.Column(right_column, vertical_alignment='top', expand_x=True, expand_y=True)],
        [sg.Frame('Opções de Consulta de Ferramentas', layout=get_buttons('CON_FERRAMENTA'),
                  element_justification='center', expand_x=True, pad=(10, 10))],
        [sg.Table(values=lista_consulta_ferramentas,
                  headings=get_table_header('Ferramenta'),
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

    # Define Layout Consulta Tecnicos
    layout_con_tecnico = [[sg.Text('Highest Qualfication', size=(15, 1)), sg.Input('', key='eQual')],
                          [sg.Text('Year of Qualifying', size=(15, 1)), sg.Input('', key='eYoq')],
                          [sg.Text('Grade', size=(15, 1)), sg.Input('', key='eGrade')],
                          [sg.Text('University/College', size=(15, 1)), sg.Input('', key='eQUniv')],
                          [sg.Button('Save Education Details')]]

    # Define Layout Consulta Reservas
    layout_con_reserva = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
                          [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
                          [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
                          [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
                          [sg.Button('Save Experience Details')]]

    # Define o TabGroup Consulta
    tabgrp_consulta = [[sg.TabGroup([[
        sg.Tab('Consulta de Ferramentas', layout_con_ferramentas, border_width=5, element_justification='left'),
        sg.Tab('Consulta de Técnicos     ', layout_con_tecnico, border_width=5, element_justification='left'),
        sg.Tab('Consulta de Reservas     ', layout_con_reserva, border_width=5, element_justification='left')
    ]], tab_location=sg.TAB_LOCATION_TOP_LEFT, border_width=7, font='_ 12')]]

    return tabgrp_consulta
