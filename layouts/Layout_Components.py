import PySimpleGUI as sg


def get_calendario(target_input):
    lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    calendario = sg.CalendarButton('📅', close_when_date_chosen=True,
                                   target=target_input, no_titlebar=False,
                                   format='%d/%m/%y', default_date_m_d_y=(9, None, 2022),
                                   month_names=lista_meses,
                                   auto_size_button=False,
                                   button_color=('white', 'black'),
                                   font='_ 12',
                                   size=3,
                                   title='Calendário')
    return calendario


def get_table_header(table_name):
    if table_name == 'Reserva':
        header_reservas = ['ID Reserva', 'ID Ferramenta', 'CPF do Técnico', 'Nome do Técnico', 'Descrição',
                           'Data Retirada', 'Hora Retirada', 'Minuto Retirada', 'Data Devolução', 'Hora Devolução',
                           'Minuto Devolução', 'Reserva Emergencial?']

        return header_reservas

    elif table_name == 'Ferramenta':
        header_ferramentas = ['ID Ferramenta', 'Descrição', 'Cód. Fabricante', 'Fabricante', 'Voltagem',
                              'Hora Max Reserva', 'Min. Max Reserva', 'Tamanho', 'Unidade Medida', 'Tipo', 'Material']

        return header_ferramentas

    elif table_name == 'Tecnico':
        header_tecnicos = ['CPF', 'Nome Técnico', 'Telefone/Celular', 'Turno/Período', 'Nome da Equipe']

        return header_tecnicos


def get_buttons(layout_name):
    if layout_name == 'CAD_RESERVA':
        buttons_cadastro_reserva = [[sg.Button('Reservar', key='ReservarReserva', pad=(15, 7), expand_x=True),
                                     sg.Button('Devolver', key='DevolverReserva', pad=(15, 7), expand_x=True),
                                     sg.Button('Excluir', key='ExcluirReserva', pad=(15, 7), expand_x=True),
                                     sg.Button('Limpar', key='LimparReservaCAD', pad=(15, 7), expand_x=True)]]
        return buttons_cadastro_reserva

    elif layout_name == 'CAD_FERRAMENTA':
        buttons_cadastro_ferramentas = [[sg.Button('Cadastrar', key='CadastrarFerramenta', pad=(15, 7), expand_x=True),
                                         sg.Button('Modificar', key='ModificarFerramenta', pad=(15, 7), expand_x=True),
                                         sg.Button('Eliminar', key='EliminarFerramenta', pad=(15, 7), expand_x=True, ),
                                         sg.Button('Limpar', key='LimparFerramentaCAD', pad=(15, 7), expand_x=True)]]
        return buttons_cadastro_ferramentas

    elif layout_name == 'CAD_TECNICO':
        buttons_cadastro_tecnico = [[sg.Button('Cadastrar', key='CadastrarTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Modificar', key='ModificarTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Eliminar', key='EliminarTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Limpar', key='LimparTecnicoCAD', pad=(15, 7), expand_x=True)]]
        return buttons_cadastro_tecnico

    elif layout_name == 'CON_RESERVA':
        buttons_consulta_reserva = [[sg.Button('Filtrar', key='FiltrarReserva', pad=(15, 7), expand_x=True),
                                     sg.Button('Limpar Filtros', key='LimparReservaCON', pad=(15, 7),
                                               expand_x=True),
                                     sg.In(visible=False, enable_events=True, key='ReservaCSV'),
                                     sg.FolderBrowse(button_text='Baixar CSV', pad=(15, 7), size=(45, 1))]]
        return buttons_consulta_reserva

    elif layout_name == 'CON_FERRAMENTA':
        buttons_consulta_ferramenta = [[sg.Button('Filtrar', key='FiltrarFerramenta', pad=(15, 7), expand_x=True),
                                        sg.Button('Limpar Filtros', key='LimparFerramentaCON', pad=(15, 7),
                                                  expand_x=True),
                                        sg.In(visible=False, enable_events=True, key='FerramentaCSV'),
                                        sg.FolderBrowse(button_text='Baixar CSV', pad=(15, 7), size=(45, 1))]]
        return buttons_consulta_ferramenta

    elif layout_name == 'CON_TECNICO':
        buttons_consulta_tecnico = [[sg.Button('Filtrar', key='FiltrarTecnico', pad=(15, 7), expand_x=True),
                                     sg.Button('Limpar Filtros', key='LimparTecnicoCON', pad=(15, 7), expand_x=True),
                                     sg.In(visible=False, enable_events=True, key='TecnicoCSV'),
                                     sg.FolderBrowse(button_text='Baixar CSV', pad=(15, 7), size=(45, 1))]]
        return buttons_consulta_tecnico


def get_tooltip_layout(key_field):
    text_tooltip = ''
    if key_field == 'rEmergencial':
        text_tooltip = 'Reserva Emergencial ignora as validações de tempo de reserva com 24h de ' \
                       'antecedência, podendo retirar a ferramenta no momento da reserva para ' \
                       'casos de emergência.'
    return text_tooltip


def get_horas_minutos(horas_minutos):
    lista_horario = []
    horas_minutos += 1
    for index, value in enumerate(range(horas_minutos)):
        if index < 10:
            lista_horario.append(f'0{value}')
        else:
            lista_horario.append(f'{value}')

    return lista_horario
