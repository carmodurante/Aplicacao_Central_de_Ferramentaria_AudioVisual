import PySimpleGUI as sg
from layouts.Layouts import layout_principal
from functions.Functions_Login import login

# Define o tema
sg.theme('Black')

## Dados Tabelas
lista_cadastrado_ferramentas = [['1001', 'Chave Inglesa', 'John Deere', '110V', '1015-U521', '10', 'Polegadas',
                                 'Metal', '36', 'True'],
                                ['1002', 'Chave de Fenda', 'John Deere', 'N/D', '1015-U522', '40', 'Metros',
                                 'Aluminio', '24', 'False']]

lista_cadastrado_tecnicos = [['46794179865', 'Carmo Durante Neto', '16992180889', 'Manhã', 'Hell Fire'],
                             ['12345678910', 'Jose Carlos', '1699111111', 'Noite', 'Titans']]

lista_cadastrado_reservas = [['1099', '1001', '46794179865', '25/07/22', '12:00', '27/07/22', '09:30', '', '', 'False'],
                             ['1100', '1002', '1111119865', '20/07/22', '11:00', '25/07/22', '12:30', '23/07/22', '09:00', 'False']]

if __name__ == '__main__':
    try:
        usuario_logado = login()
        if usuario_logado['validado']: # Validado
            # progress_bar_login()

            # Define Window
            window = sg.Window('App Central de Ferramentaria AudioVisual',
                               layout_principal( lista_cadastrado_ferramentas,
                                                 lista_cadastrado_tecnicos,
                                                 lista_cadastrado_reservas,
                                                 usuario_logado),
                               resizable=True, size=(1250,670))

            ## Eventos
            while True:
                # Read values entered by user
                try:
                    event, values = window.read()
                except:
                    break
                print(event)
                if event == sg.WIN_CLOSED:  # always, always give a way out!
                    break
    except:
        exit()

