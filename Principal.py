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

            ## Eventos
            while True:
                try:
                    event, values = window.read()
                    print(event)  # Somente para visualização
                    if event == sg.WIN_CLOSED:
                        break

                    # Cadastrar
                    elif event == 'CadastrarFerramenta':  # Cadastrar Ferramenta
                        cadastros.cadastrar_ferramenta(values, sg)

                    # Modificar
                    elif event == 'ModificarFerramenta':  # Modificar Ferramenta
                        a = 1
                    # Reservar

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
