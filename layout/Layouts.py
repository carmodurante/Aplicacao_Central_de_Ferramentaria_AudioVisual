import PySimpleGUI as sg


def layout_cadastro(lista_cadastrado_ferramentas, lista_cadastrado_tecnicos, lista_cadastrado_reservas):
    ############ Define Layout Cadastro Ferramentas ############
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
                               sg.VerticalSeparator(pad=((180,15), (1,1)) ),
                               sg.Text('Código no Fabricante', size=(18, 1)), sg.Input('', key='fFabricante', size=25)],
                              [sg.Text('Tamanho', size=(18, 1)), sg.Input('', key='fTamanho', size=20),  # Listbox
                               sg.VerticalSeparator(pad=((193, 15), (1, 1))),
                               sg.Text('Unidade de Medida', size=(18, 1)), sg.Input('', key='fUnidade', size=25)],  # Listbox
                              [sg.Text('Tipo da Ferramenta', size=(18, 1)), sg.Input('', key='fTipo', size=35),  # Listbox
                               sg.VerticalSeparator(pad=((88, 15), (1, 1))),
                               sg.Text('Material da Ferramenta', size=(18, 1)), sg.Input('', key='fMaterial')],
                              # Listbox
                              [sg.Text('Tempo Max. de Reserva', size=(18, 1)),
                               sg.Input('', key='fTempoReserva', size=6, ),
                               sg.Text('(Horas)', size=(7, 1)),
                               sg.VerticalSeparator(pad=((221, 15), (1, 1)))],

                              [sg.Frame('Opções de Cadastro de Ferramentas', layout=buttons_cadastro_ferramentas,
                                        element_justification='left', expand_x=True, pad=(10, 10))],
                              [sg.Table(values=lista_cadastrado_ferramentas,
                                        headings=header_cadastro_ferramentas,
                                        max_col_width=35,
                                        auto_size_columns=True,
                                        display_row_numbers=True,
                                        justification='left',
                                        num_rows=6,
                                        key='-TABLE_CAD_FERRAMENTAS-',
                                        row_height=35,
                                        enable_click_events=True,
                                        vertical_scroll_only=False)]]

    ############ Define Layout Cadastro Tecnicos ############
    header_cadastro_tecnicos = ['CPF', 'Nome Técnico', 'Telefone/Celular', 'Turno/Período', 'Nome da Equipe']

    buttons_cadastro_tecnico = [[sg.Button('Cadastrar', key='CadastrarTecnico', pad=(15, 7), expand_x=True),
                                 sg.Button('Modificar', key='ModificarTecnico', pad=(15, 7), expand_x=True),
                                 sg.Button('Eliminar', key='EliminarTecnico', pad=(15, 7), expand_x=True)]]

    layout_cad_tecnico = [[sg.Text('CPF', size=(18, 1)), sg.Input('', key='tCPF', size=15)],
                          [sg.Text('Nome', size=(18, 1)), sg.Input('', key='tNome')],
                          [sg.Text('Celular/Rádio', size=(18, 1)), sg.Input('', key='tTelefone', size=11)],
                          [sg.Text('Turno', size=(18, 1)), sg.Combo(['Manhã', 'Tarde', 'Noite'],
                                                                    default_value='Manhã', key='fTurno', size=9)],
                          [sg.Text('Nome da Equipe', size=(18, 1)), sg.Input('', key='tEquipe')],
                          [sg.Frame('Opções de Cadastro de Técnicos', layout=buttons_cadastro_tecnico,
                                    element_justification='left', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_cadastrado_tecnicos,
                                    headings=header_cadastro_tecnicos,
                                    max_col_width=35,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='left',
                                    num_rows=6,
                                    key='-TABLE_CAD_TECNICOS-',
                                    row_height=35,
                                    enable_click_events=True)]]

    ############ Define Layout Cadastro Reservas ############
    layout_cad_reserva = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
                          [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
                          [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
                          [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
                          [sg.Button('Save Experience Details')]]

    # Define o TabGroup Cadastro
    tabgrp_cadastro = [[sg.TabGroup([[
        sg.Tab('Cadastro de Ferramentas', layout_cad_ferramentas, border_width=5, element_justification='left'),
        sg.Tab('Cadastro de Técnicos      ', layout_cad_tecnico, border_width=5, element_justification='left'),
        sg.Tab('Cadastro de Reservas     ', layout_cad_reserva, border_width=5, element_justification='left')
    ]], tab_location=sg.TAB_LOCATION_TOP_LEFT, border_width=7, font='_ 12')]]

    return tabgrp_cadastro


def layout_consulta():
    ############ Define Layout Consulta Ferramentas ############
    layout_con_ferramentas = [[sg.Text('Name', size=(10, 1)), sg.Input('', key='eName')],
                              [sg.Text('Date of Birth', size=(10, 1)), sg.Input('', key='eDob')],
                              [sg.Text('Phone No', size=(10, 1)), sg.Input('', key='ePhone')],
                              [sg.Text('Email ID', size=(10, 1)), sg.Input('', key='eEmail')],
                              [sg.Button('Save Personal Details')]]

    ############ Define Layout Consulta Tecnicos ############
    layout_con_tecnico = [[sg.Text('Highest Qualfication', size=(15, 1)), sg.Input('', key='eQual')],
                          [sg.Text('Year of Qualifying', size=(15, 1)), sg.Input('', key='eYoq')],
                          [sg.Text('Grade', size=(15, 1)), sg.Input('', key='eGrade')],
                          [sg.Text('University/College', size=(15, 1)), sg.Input('', key='eQUniv')],
                          [sg.Button('Save Education Details')]]

    ############ Define Layout Consulta Reservas ############
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


def layout_principal(lista_cadastrado_ferramentas, lista_cadastrado_tecnicos, lista_cadastrado_reservas):
    ########## Definição Tela Principal ##########
    tabgroup_menu = [
        # Dados Cabeçalho
        [sg.T('Central de Ferramentaria AudioVisual', font='_ 16', justification='c', expand_x=True,
              border_width=10, background_color='white', text_color='black')],

        # Dados TabGroup Principal
        [sg.TabGroup([[
            # TabGroup de Cadastros
            sg.Tab('Cadastros', layout_cadastro(lista_cadastrado_ferramentas,
                                                lista_cadastrado_tecnicos,
                                                lista_cadastrado_reservas),
                   border_width=5, element_justification='left'),

            # TabGroup de Consultas
            sg.Tab('Consultas', layout_consulta(), border_width=5, element_justification='left')]],
            tab_location=sg.TAB_LOCATION_TOP, border_width=12, font='_ 12')],

        # Dados Footer
        [sg.Text('Usuário Logado:', size=(12, 1)), sg.Text('CarmoDurante', size=(18, 1), text_color='green'),
         sg.Text('Admin: ', size=(5, 1)), sg.Text('False', size=(18, 1), text_color='red'),
         sg.Push(), sg.Text('@DevTeam_05', size=(15, 1), text_color='purple')]]

    return tabgroup_menu
