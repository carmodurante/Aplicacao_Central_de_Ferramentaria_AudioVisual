import webbrowser as web

import PySimpleGUI as sg

import functions.Functions_Cadastro as cadastros
import functions.Functions_Consulta as consulta
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
                               layout_principal(cadastros.get_cadastro_ferramentas(),
                                                cadastros.get_cadastro_tecnicos(),
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

                    elif event == 'URL_DEV5':
                        web.open(get_link_url_dev5())

                    # Filtrar
                    elif event == 'FiltrarFerramenta':
                        consulta.filtrar_ferramentas(window, values)

                    elif event == 'FiltrarTecnico':
                        consulta.filtrar_tecnicos(window, values)

                    elif event == 'FiltrarReserva':
                        consulta.filtrar_reservas(window, values)

                    # Limpar Tela
                    elif event == 'LimparFerramentaCON':
                        consulta.limpar_filtros(window, 'ferramenta_CON')

                    elif event == 'LimparFerramentaCAD':
                        consulta.limpar_filtros(window, 'ferramenta_CAD')

                    elif event == 'LimparTecnicoCON':
                        consulta.limpar_filtros(window, 'tecnico_CON')

                    elif event == 'LimparTecnicoCAD':
                        consulta.limpar_filtros(window, 'tecnico_CAD')

                    elif event == 'LimparReservaCAD':
                        consulta.limpar_filtros(window, 'reserva_CAD')

                    elif event == 'LimparReservaCON':
                        consulta.limpar_filtros(window, 'reserva_CON')


                except:
                    break
            window.close()
        else:
            exit()
    except:
        exit()
