import PySimpleGUI as sg


def get_calendario(target_input):
    lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    calendario = sg.CalendarButton('Escolha a Data', close_when_date_chosen=True,
                                   target=target_input, no_titlebar=False,
                                   format='%d/%m/%y', default_date_m_d_y=(9, None, 2022),
                                   month_names=lista_meses,
                                   auto_size_button=True,
                                   title='Calendário')
    return calendario


def get_table_header(table_name):
    if table_name == 'Reserva':
        header_reservas = ['ID Reserva', 'ID Ferramenta', 'CPF do Técnico', 'Data Reserva', 'Hora Reserva',
                           'Data Devolução', 'Hora Devolução', 'Data Devol. Efetiva', 'Hora Devol, Efetiva',
                           'Reserva Emergencial?']

        return header_reservas

    elif table_name == 'Ferramenta':
        header_ferramentas = ['ID Ferramenta', 'Descrição', 'Fabricante', 'Voltagem', 'Cód. Fabricante',
                              'Tamanho', 'Unidade Medida', 'Material', 'Tempo Max Reserva', 'Reservado?']

        return header_ferramentas

    elif table_name == 'Tecnico':
        header_tecnicos = ['CPF', 'Nome Técnico', 'Telefone/Celular', 'Turno/Período', 'Nome da Equipe']

        return header_tecnicos


def get_buttons(layout_name):
    if layout_name == 'CAD_RESERVA':
        buttons_cadastro_reserva = [[sg.Button('Reservar', key='ReservarReserva', pad=(15, 7), expand_x=True),
                                     sg.Button('Modificar', key='ModificarReserva', pad=(15, 7), expand_x=True),
                                     sg.Button('Devolver', key='DevolverReserva', pad=(15, 7), expand_x=True)]]
        return buttons_cadastro_reserva

    elif layout_name == 'CAD_FERRAMENTA':
        buttons_cadastro_ferramentas = [[sg.Button('Cadastrar', key='CadastrarFerramenta', pad=(15, 7), expand_x=True),
                                         sg.Button('Modificar', key='ModificarFerramenta', pad=(15, 7), expand_x=True),
                                         sg.Button('Eliminar', key='EliminarFerramenta', pad=(15, 7), expand_x=True)]]
        return buttons_cadastro_ferramentas

    elif layout_name == 'CAD_TECNICO':
        buttons_cadastro_tecnico = [[sg.Button('Cadastrar', key='CadastrarTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Modificar', key='ModificarTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Eliminar', key='EliminarTecnico', pad=(15, 7), expand_x=True)]]
        return buttons_cadastro_tecnico

    elif layout_name == 'CON_RESERVA':
        return True
    elif layout_name == 'CON_FERRAMENTA':
        buttons_consulta_ferramenta = [[sg.Button('Filtrar', key='FiltrarFerramenta', pad=(15, 7), expand_x=True),
                                        sg.Button('Limpar Filtros', key='LimparFerramenta', pad=(15, 7), expand_x=True),
                                        sg.Button('Imprimir', key='ImprimirFerramenta', pad=(15, 7), expand_x=True)]]
        return buttons_consulta_ferramenta

    elif layout_name == 'CON_TECNICO':
        buttons_consulta_tecnico = [[sg.Button('Filtrar', key='FiltrarTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Limpar Filtros', key='LimparTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Imprimir', key='ImprimirTecnico', pad=(15, 7), expand_x=True)]]
        return buttons_consulta_tecnico
