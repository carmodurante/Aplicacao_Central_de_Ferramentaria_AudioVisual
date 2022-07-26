import webbrowser as web

import PySimpleGUI as sg

import functions.Functions_Cadastros as cadastros
import functions.Functions_Reservas as reservas
import functions.Functions_Login as login
from functions.Functions_Diversos import get_link_url_dev5
from layouts.Layouts import layout_principal

# Define o tema
sg.theme('Black')

if __name__ == '__main__':
    try:
        usuario_logado = login.login()
        if usuario_logado['validado']:  # Validado
            login.progress_bar('Entrando na aplicação...')

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
                except:
                    break
            window.close()
        else:
            exit()
    except:
        exit()
