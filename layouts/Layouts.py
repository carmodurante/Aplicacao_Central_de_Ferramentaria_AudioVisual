import PySimpleGUI as sg


def layout_reserva(lista_cadastrado_reservas):
    # Define Layout Cadastro Reservas
    header_reservas = ['ID Reserva', 'ID Ferramenta', 'CPF do Técnico', 'Data Reserva', 'Hora Reserva',
                       'Data Devolução', 'Hora Devolução', 'Data Devol. Efetiva', 'Hora Devol, Efetiva',
                       'Reserva Emergencial?']

    buttons_cadastro_reserva = [[sg.Button('Reservar', key='ReservarReserva', pad=(15, 7), expand_x=True),
                                 sg.Button('Modificar', key='ModificarReserva', pad=(15, 7), expand_x=True),
                                 sg.Button('Devolver', key='DevolverReserva', pad=(15, 7), expand_x=True)]]

    lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    layout_cad_reserva = [[sg.Text('ID Ferramenta', size=(18, 1)), sg.Input('', key='rFerramenta', size=13),
                           sg.VerticalSeparator(pad=((242, 15), (1, 1))),
                           sg.Text('CPF do Técnico', size=(18, 1)), sg.Input('', key='rCPF', size=13)],
                          [sg.Text('Data da Retirada', size=(18, 1)), sg.Input('', key='rDTRetirada', size=8),
                           sg.CalendarButton('Escolha a Data', close_when_date_chosen=True,
                                             target='rDTRetirada', no_titlebar=False,
                                             format='%d/%m/%y', default_date_m_d_y=(9, None, 2022),
                                             month_names=lista_meses,
                                             auto_size_button=True,
                                             title='Escolha a Data'),
                           sg.VerticalSeparator(pad=((168, 15), (1, 1))),
                           sg.Text('Data da Devolução', size=(18, 1)), sg.Input('', key='rDTDevol', size=8),
                           sg.CalendarButton('Escolha a Data', close_when_date_chosen=True,
                                             target='rDTDevol', no_titlebar=False,
                                             format='%d/%m/%y', default_date_m_d_y=(9, None, 2022),
                                             month_names=lista_meses,
                                             auto_size_button=True,
                                             title='Escolha a Data')],
                          [sg.Text('Horário da Retirada', size=(18, 1)), sg.Input('', key='rHRRetirada', size=5),
                           sg.Text('(hh:mm)'),
                           sg.VerticalSeparator(pad=((236, 15), (1, 1))),
                           sg.Text('Horário da Devolução', size=(18, 1)), sg.Input('', key='rHRDevol', size=5),
                           sg.Text('(hh:mm)')],
                          [sg.Text('Reserva Emergencial?', size=(18, 1)),
                           sg.Checkbox('', key='rEmergencial', default=False, font=16, size=(15, 1))],
                          [sg.Frame('Opções de Cadastro de Reserva', layout=buttons_cadastro_reserva,
                                    element_justification='left', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_cadastrado_reservas,
                                    headings=header_reservas,
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


def layout_cadastro(lista_cadastrado_ferramentas, lista_cadastrado_tecnicos):
    file_types = [("JPEG (*.jpeg)", "*.jpeg"),
                  ("JPG (*.jpg)", "*.jpg"),
                  ("PNG (*.png)", "*.png")]

    # Define Layout Cadastro Ferramentas
    header_cadastro_ferramentas = ['ID Ferramenta', 'Descrição', 'Fabricante', 'Voltagem', 'Cód. Fabricante',
                                   'Tamanho', 'Unidade Medida', 'Material', 'Tempo Max Reserva', 'Reservado?']

    buttons_cadastro_ferramentas = [[sg.Button('Cadastrar', key='CadastrarFerramenta', pad=(15, 7), expand_x=True),
                                     sg.Button('Modificar', key='ModificarFerramenta', pad=(15, 7), expand_x=True),
                                     sg.Button('Eliminar', key='EliminarFerramenta', pad=(15, 7), expand_x=True)]]

    layout_cad_ferramentas = [[sg.Text('Descrição', size=(18, 1)), sg.Input('', key='fDescricao'),
                               sg.VerticalSeparator(pad=((18, 15), (1, 1))),
                               sg.Text('Nome do Fabricante', size=(18, 1)), sg.Input('', key='fFabricante')],
                              [sg.Text('Voltagem de Uso', size=(18, 1)),
                               sg.Combo(['220V', '110V', 'N/D'], default_value='110V', key='fVoltagem', size=10),
                               sg.Text('(Volts)', size=(7, 1)),
                               sg.VerticalSeparator(pad=((180, 15), (1, 1))),
                               sg.Text('Código no Fabricante', size=(18, 1)), sg.Input('', key='fFabricante', size=25)],
                              [sg.Text('Tamanho', size=(18, 1)), sg.Input('', key='fTamanho', size=20),
                               sg.VerticalSeparator(pad=((193, 15), (1, 1))),
                               sg.Text('Unidade de Medida', size=(18, 1)), sg.Input('', key='fUnidade', size=25)],
                              [sg.Text('Tipo da Ferramenta', size=(18, 1)), sg.Input('', key='fTipo', size=35),
                               sg.VerticalSeparator(pad=((88, 15), (1, 1))),
                               sg.Text('Material da Ferramenta', size=(18, 1)), sg.Input('', key='fMaterial')],
                              [sg.Text('Tempo Max. de Reserva', size=(18, 1)),
                               sg.Input('', key='fTempoReserva', size=6, ),
                               sg.Text('(Horas)', size=(7, 1)),
                               sg.VerticalSeparator(pad=((221, 15), (1, 1))),
                               sg.Text('Imagem da Ferramenta', size=(18, 1)), sg.Input('', key="fImagem"),
                               sg.FileBrowse(file_types=file_types, button_text='Carregar Imagem',
                                             auto_size_button=True)],
                              [sg.Frame('Opções de Cadastro de Ferramentas', layout=buttons_cadastro_ferramentas,
                                        element_justification='left', expand_x=True, pad=(10, 10))],
                              [sg.Table(values=lista_cadastrado_ferramentas,
                                        headings=header_cadastro_ferramentas,
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
    header_cadastro_tecnicos = ['CPF', 'Nome Técnico', 'Telefone/Celular', 'Turno/Período', 'Nome da Equipe']

    buttons_cadastro_tecnico = [[sg.Button('Cadastrar', key='CadastrarTecnico', pad=(15, 7), expand_x=True),
                                 sg.Button('Modificar', key='ModificarTecnico', pad=(15, 7), expand_x=True),
                                 sg.Button('Eliminar', key='EliminarTecnico', pad=(15, 7), expand_x=True)]]

    layout_cad_tecnico = [[sg.Text('CPF', size=(18, 1)), sg.Input('', key='tCPF', size=15)],
                          [sg.Text('Nome', size=(18, 1)), sg.Input('', key='tNome')],
                          [sg.Text('Celular/Rádio', size=(18, 1)), sg.Input('', key='tTelefone', size=11)],
                          [sg.Text('Turno', size=(18, 1)), sg.Combo(['Manhã', 'Tarde', 'Noite'],
                                                                    default_value='Manhã', key='fTurno', size=9)],
                          [sg.Text('Nome da Equipe', size=(18, 1)), sg.Input('', key='tEquipe'),
                           sg.VerticalSeparator(pad=((18, 15), (1, 1))),
                           sg.Text('Imagem do Técnico', size=(18, 1)), sg.Input('', key="tImagem"),
                           sg.FileBrowse(file_types=file_types, button_text='Carregar Imagem', auto_size_button=True)],
                          [sg.Frame('Opções de Cadastro de Técnicos', layout=buttons_cadastro_tecnico,
                                    element_justification='left', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_cadastrado_tecnicos,
                                    headings=header_cadastro_tecnicos,
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


def layout_consulta():
    # Define Layout Consulta Ferramentas
    layout_con_ferramentas = [[sg.Text('Name', size=(10, 1)), sg.Input('', key='eName')],
                              [sg.Text('Date of Birth', size=(10, 1)), sg.Input('', key='eDob')],
                              [sg.Text('Phone No', size=(10, 1)), sg.Input('', key='ePhone')],
                              [sg.Text('Email ID', size=(10, 1)), sg.Input('', key='eEmail')],
                              [sg.Button('Save Personal Details')]]

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


def layout_principal(lista_cadastrado_ferramentas, lista_cadastrado_tecnicos, lista_cadastrado_reservas,
                     usuario_logado):
    # Definição Tela Principal
    if usuario_logado['admin'] == 'True':
        color = 'green'
    else:
        color = 'red'

    layout_cabecalho = [sg.T('Central de Ferramentaria AudioVisual', font='_ 16', justification='c', expand_x=True,
                             border_width=10, background_color='white', text_color='black')]

    layout_footer = [sg.Text('Usuário Logado:', size=(12, 1)),
                     sg.Text(usuario_logado['username'], size=(18, 1), text_color='green'),
                     sg.Text('Admin: ', size=(5, 1)), sg.Text(usuario_logado['admin'], size=(18, 1), text_color=color),
                     sg.Push(), sg.Text('@DevTeam_05', size=(15, 1), text_color='purple', enable_events=True, key='URL_DEV5',
                                        tooltip='Abrir Documentação no Github')]

    layout_cadastros = [sg.Tab('Cadastros', layout_cadastro(lista_cadastrado_ferramentas,
                                                            lista_cadastrado_tecnicos),
                               border_width=5, element_justification='left')]

    layout_consultas = [sg.Tab('Consultas', layout_consulta(), border_width=5, element_justification='left')]

    layout_reservas = [sg.Tab('Reservas', layout_reserva(lista_cadastrado_reservas), border_width=5,
                              element_justification='left')]

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
                         [sg.TabGroup([layout_consultas],
                                      tab_location=sg.TAB_LOCATION_TOP, border_width=12, font='_ 12')],
                         [layout_footer]]

        return tabgroup_menu
