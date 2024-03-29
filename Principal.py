import traceback
import webbrowser as web

import PySimpleGUI as sg

import functions.Functions_Cadastro as cadastros
import functions.Functions_Consulta as consultas
import functions.Functions_Login as login
from functions.Functions_Utils import get_link_url
from layouts.Layout_Principal import layout_principal

# Define o tema
sg.theme('Black')

# Variaveis Globais
linha_selecionada = -1

if __name__ == '__main__':
    try:
        usuario_logado = login.login()
        if usuario_logado['validado']:  # Validado
            login.progress_bar('Entrando na aplicação...')

            # Define Window
            window = sg.Window('App Central de Ferramentaria AudioVisual',
                               layout_principal(cadastros.get_cadastrados('ferramenta'),
                                                cadastros.get_cadastrados('tecnico'),
                                                cadastros.get_cadastrados('reserva'),
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

                    elif event == 'CadastrarTecnico':  # Cadastrar Tecnico
                        cadastros.cadastrar_tecnico(values, sg)
                        window['-TABLE_CAD_TECNICOS-'].update(cadastros.get_cadastrados('tecnico'))

                    # Modificar
                    elif event == 'ModificarFerramenta':  # Modificar Ferramenta
                        if linha_selecionada >= 0:
                            cadastros.modificar_ferramenta(linha_selecionada, values, sg)
                            window['-TABLE_CAD_FERRAMENTAS-'].update(cadastros.get_cadastrados('ferramenta'))
                            consultas.limpar_filtros(window, 'ferramenta_CAD')
                            linha_selecionada = -1

                    elif event == 'ModificarTecnico':  # Modificar Tecnico
                        if linha_selecionada >= 0:
                            cadastros.modificar_tecnico(linha_selecionada, values, sg)
                            window['-TABLE_CAD_TECNICOS-'].update(cadastros.get_cadastrados('tecnico'))
                            consultas.limpar_filtros(window, 'tecnico_CAD')
                            linha_selecionada = -1

                    # Seleção Tabela Cadastro
                    elif type(event) is tuple and event[0] == '-TABLE_CAD_FERRAMENTAS-':
                        if event[2][0] is not None and event[2][
                            0] >= 0:  # Linha selecionada Tabela de Cadastro de Ferramentas
                            linha_selecionada = event[2][0]
                            cadastros.carregar_dados_tela(cadastros.get_cadastrados('ferramenta')[event[2][0]],
                                                          'cadastro_ferramenta', window)

                    elif type(event) is tuple and event[0] == '-TABLE_CAD_TECNICOS-':
                        if event[2][0] is not None and event[2][
                            0] >= 0:  # Linha selecionada Tabela de Cadastro de Tecnicos
                            linha_selecionada = int(event[2][0])
                            cadastros.carregar_dados_tela(cadastros.get_cadastrados('tecnico')[event[2][0]],
                                                          'cadastro_tecnico', window)

                    # Eliminar
                    elif event == 'EliminarFerramenta':  # Eliminar Ferramenta
                        if linha_selecionada >= 0:
                            cadastros.deletar_registro(linha_selecionada, 'ferramenta', sg)
                            window['-TABLE_CAD_FERRAMENTAS-'].update(cadastros.get_cadastrados('ferramenta'))
                            consultas.limpar_filtros(window, 'ferramenta_CAD')
                            linha_selecionada = -1

                    elif event == 'EliminarTecnico':  # Eliminar Tecnico
                        if linha_selecionada >= 0:
                            cadastros.deletar_registro(linha_selecionada, 'tecnico', sg)
                            window['-TABLE_CAD_TECNICOS-'].update(cadastros.get_cadastrados('tecnico'))
                            consultas.limpar_filtros(window, 'tecnico_CAD')
                            linha_selecionada = -1

                    # Limpar
                    elif event == 'LimparFerramentaCAD':  # Limpar Ferramenta Cadastro
                        consultas.limpar_filtros(window, 'ferramenta_CAD')

                    elif event == 'LimparTecnicoCAD':  # Limpar Tecnico Cadastro
                        consultas.limpar_filtros(window, 'tecnico_CAD')

                    # TODO: TELAS DE CONSULTA
                    # Filtrar
                    elif event == 'FiltrarFerramenta':  # Filtrar Ferramenta Consulta
                        consultas.filtrar_ferramentas(window, values)

                    elif event == 'FiltrarTecnico':  # Filtrar Tecnico Consulta
                        consultas.filtrar_tecnicos(window, values)

                    elif event == 'FiltrarReserva':  # Filtrar Reserva Consulta
                        consultas.filtrar_reservas(window, values)

                    # Seleção Tabela Consulta
                    elif type(event) is tuple and event[0] == '-TABLE_CON_FERRAMENTAS-':
                        if event[2][0] is not None and event[2][0] >= 0:
                            consultas.atualiza_imagem_selecao(
                                window['-TABLE_CON_FERRAMENTAS-'].get(), 'ferramenta', event[2][0], window)

                    elif type(event) is tuple and event[0] == '-TABLE_CON_TECNICOS-':
                        if event[2][0] is not None and event[2][0] >= 0:
                            consultas.atualiza_imagem_selecao(
                                window['-TABLE_CON_TECNICOS-'].get(), 'tecnico', event[2][0], window)

                    elif type(event) is tuple and event[0] == '-TABLE_CON_RESERVAS-':
                        if event[2][0] is not None and event[2][0] >= 0:
                            consultas.atualiza_imagem_selecao(
                                window['-TABLE_CON_RESERVAS-'].get(), 'reserva', event[2][0], window)

                    # Limpar Tela
                    elif event == 'LimparFerramentaCON':  # Limpar Ferramenta Consulta
                        consultas.limpar_filtros(window, 'ferramenta_CON')

                    elif event == 'LimparTecnicoCON':  # Limpar Tecnico Consulta
                        consultas.limpar_filtros(window, 'tecnico_CON')

                    elif event == 'LimparReservaCON':  # Limpar Reserva Consulta
                        consultas.limpar_filtros(window, 'reserva_CON')

                    # Baixar CSV
                    elif event == 'FerramentaCSV':
                        consultas.baixar_csv(window['-TABLE_CON_FERRAMENTAS-'].get(), values['FerramentaCSV'],
                                             'Ferramenta', sg)

                    elif event == 'TecnicoCSV':
                        consultas.baixar_csv(window['-TABLE_CON_TECNICOS-'].get(), values['TecnicoCSV'],
                                             'Tecnico', sg)

                    elif event == 'ReservaCSV':
                        consultas.baixar_csv(window['-TABLE_CON_RESERVAS-'].get(), values['ReservaCSV'],
                                             'Reserva', sg)

                    # TODO: TELA DE RESERVA
                    # Seleção Tabela Reserva
                    elif type(event) is tuple and event[0] == '-TABLE_CAD_RESERVAS-':
                        if event[2][0] is not None and event[2][0] >= 0:
                            linha_selecionada = event[2][0]

                    elif event == 'ReservarReserva':  # Cadastrar Reserva
                        cadastros.cadastrar_reserva(values, sg)
                        window['-TABLE_CAD_RESERVAS-'].update(cadastros.get_cadastrados('reserva'))

                    elif event == 'DevolverReserva':  # Devolver Reserva
                        if linha_selecionada >= 0:
                            cadastros.deletar_registro(linha_selecionada, 'reserva_hist', sg)
                            window['-TABLE_CAD_RESERVAS-'].update(cadastros.get_cadastrados('reserva'))
                            consultas.limpar_filtros(window, 'reserva_CAD')
                            linha_selecionada = -1

                    elif event == 'ExcluirReserva':  # Excluir Reserva
                        if linha_selecionada >= 0:
                            cadastros.deletar_registro(linha_selecionada, 'reserva', sg)
                            window['-TABLE_CAD_RESERVAS-'].update(cadastros.get_cadastrados('reserva'))
                            consultas.limpar_filtros(window, 'reserva_CAD')
                            linha_selecionada = -1

                    elif event == 'LimparReservaCAD':  # Limpar Reserva Cadastro
                        consultas.limpar_filtros(window, 'reserva_CAD')

                    # Links
                    elif event == 'URL_GITHUB':
                        web.open(get_link_url())


                except Exception:
                    traceback.print_exc()
                    sg.popup("Erro na Aplicacao", title='Error', font=8)

            window.close()

        else:
            exit()
    except Exception:
        traceback.print_exc()
        sg.popup("Erro na Aplicacao", title='Error', font=8)
