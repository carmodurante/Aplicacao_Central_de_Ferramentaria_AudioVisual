import webbrowser as web

import PySimpleGUI as sg

import functions.Functions_Cadastro as cadastros
import functions.Functions_Consulta as consultas
import functions.Functions_Login as login
import functions.Functions_Reserva as reservas
from functions.Functions_Diversos import get_link_url_dev5
from layouts.Layout_Principal import layout_principal

# Define o tema
sg.theme('Black')

# Variaveis Globais
linha_selecionada = -1

if __name__ == '__main__':
    try:
        usuario_logado = login.login()
        if usuario_logado['validado']:  # Validado
            # login.progress_bar('Entrando na aplicação...')

            # Define Window
            window = sg.Window('App Central de Ferramentaria AudioVisual',
                               layout_principal(cadastros.get_cadastrados('ferramenta'),
                                                cadastros.get_cadastrados('tecnico'),
                                                reservas.get_cadastro_reservas(),
                                                usuario_logado),
                               resizable=True, size=(1250, 670))

            # TODO: EVENTOS
            while True:
                try:
                    event, values = window.read()
                    print(event)  # Somente para visualização
                    if event == sg.WIN_CLOSED:
                        break

                    # TODO: TELAS DE CADASTRO
                    # Cadastrar
                    elif event == 'CadastrarFerramenta':  # Cadastrar Ferramenta
                        cadastros.cadastrar_ferramenta(values, sg)
                        window['-TABLE_CAD_FERRAMENTAS-'].update(cadastros.get_cadastrados('ferramenta'))
                    #TODO Fazer cadastro tecnico
                    elif event == 'CadastrarTecnico':  # Cadastrar Tecnico
                        # cadastros.cadastrar_tecnico(values, sg)
                        window['-TABLE_CAD_TECNICOS-'].update(cadastros.get_cadastrados('tecnico'))

                    # Modificar
                    elif event == 'ModificarFerramenta':  # Modificar Ferramenta
                        if linha_selecionada >= 0:
                            cadastros.modificar_ferramenta(linha_selecionada, values, sg)
                            window['-TABLE_CAD_FERRAMENTAS-'].update(cadastros.get_cadastrados('ferramenta'))
                            consultas.limpar_filtros(window, 'ferramenta_CAD')
                            linha_selecionada = -1
                    # TODO Fazer modificar tecnico
                    elif event == 'ModificarTecnico':  # Modificar Tecnico
                        if linha_selecionada >= 0:
                            # cadastros.modificar_ferramenta(linha_selecionada, values, sg)
                            window['-TABLE_CAD_TECNICOS-'].update(cadastros.get_cadastrados('tecnico'))
                            consultas.limpar_filtros(window, 'tecnico_CAD')
                            linha_selecionada = -1

                    # Seleção Tabela
                    elif type(event) is tuple and event[0] == '-TABLE_CAD_FERRAMENTAS-':
                        if event[2][0] >= 0:  # Linha selecionada Tabela de Cadastro de Ferramentas
                            linha_selecionada = event[2][0]
                            cadastros.carregar_dados_tela(cadastros.get_cadastrados('ferramenta')[event[2][0]],
                                                          'cadastro_ferramenta', window)
                    # TODO Validar
                    elif type(event) is tuple and event[0] == '-TABLE_CAD_TECNICOS-':
                        if event[2][0] >= 0:  # Linha selecionada Tabela de Cadastro de Tecnicos
                            linha_selecionada = int(event[2][0])
                            cadastros.carregar_dados_tela(cadastros.get_cadastrados('tecnico')[event[2][0]],
                                                          'cadastro_tecnico', window)

                    # Eliminar
                    elif event == 'EliminarFerramenta':  # Eliminar Ferramenta
                        if linha_selecionada >= 0:
                            cadastros.deletar_registro(linha_selecionada, 'ferramenta')
                            window['-TABLE_CAD_FERRAMENTAS-'].update(cadastros.get_cadastrados('ferramenta'))
                            consultas.limpar_filtros(window, 'ferramenta_CAD')
                            linha_selecionada = -1
                    # TODO Validar
                    elif event == 'EliminarTecnico':  # Eliminar Tecnico
                        if linha_selecionada >= 0:
                            cadastros.deletar_registro(linha_selecionada, 'tecnico')
                            window['-TABLE_CAD_TECNICOS-'].update(cadastros.get_cadastrados('tecnico'))
                            consultas.limpar_filtros(window, 'tecnico_CAD')
                            linha_selecionada = -1


                    # TODO: TELAS DE CONSULTA
                    # Filtrar
                    elif event == 'FiltrarFerramenta':  # Filtrar Ferramenta Consulta
                        consultas.filtrar_ferramentas(window, values)

                    elif event == 'FiltrarTecnico':  # Filtrar Tecnico Consulta
                        consultas.filtrar_tecnicos(window, values)

                    elif event == 'FiltrarReserva':  # Filtrar Reserva Consulta
                        consultas.filtrar_reservas(window, values)

                    # Limpar Tela
                    elif event == 'LimparFerramentaCON':  # Limpar Ferramenta Consulta
                        consultas.limpar_filtros(window, 'ferramenta_CON')

                    elif event == 'LimparFerramentaCAD':  # Limpar Ferramenta Cadastro
                        consultas.limpar_filtros(window, 'ferramenta_CAD')

                    elif event == 'LimparTecnicoCON':  # Limpar Tecnico Consulta
                        consultas.limpar_filtros(window, 'tecnico_CON')

                    elif event == 'LimparTecnicoCAD':  # Limpar Tecnico Cadastro
                        consultas.limpar_filtros(window, 'tecnico_CAD')

                    elif event == 'LimparReservaCON':  # Limpar Reserva Consulta
                        consultas.limpar_filtros(window, 'reserva_CON')

                    # TODO: TELA DE RESERVA
                    elif event == 'LimparReservaCAD':  # Limpar Reserva Cadastro
                        consultas.limpar_filtros(window, 'reserva_CAD')

                    # Baixar CSV

                    # Links
                    elif event == 'URL_DEV5':
                        web.open(get_link_url_dev5())


                except:
                    break
            window.close()
        else:
            exit()
    except:
        exit()
