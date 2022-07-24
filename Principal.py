import PySimpleGUI as sg
from layout.Layouts import layout_principal
from Login import login
from Login import progress_bar_login


# Define o tema
sg.theme('Black')

## Dados Tabelas
lista_cadastrado_ferramentas = [['1001', 'Chave Inglesa', 'John Deere', '110V', '1015-U521', '10', 'Polegadas',
                                 'Metal', '36', 'True'],
                                ['1002', 'Chave de Fenda', 'John Deere', 'N/D', '1015-U522', '40', 'Metros',
                                 'Aluminio', '24', 'False']]

lista_cadastrado_tecnicos = [['46794179865', 'Carmo Durante Neto', '16992180889', 'Manhã', 'Hell Fire'],
                             ['12345678910', 'Jose Carlos', '1699111111', 'Noite', 'Titans']]

lista_cadastrado_reservas = []

if __name__ == '__main__':
    try:
        usuario_logado = login()
        if usuario_logado['validado']: # Validado
            progress_bar_login()

            # Define Window
            window = sg.Window('App Central de Ferramentaria AudioVisual',
                               layout_principal( lista_cadastrado_ferramentas,
                                                 lista_cadastrado_tecnicos,
                                                 lista_cadastrado_reservas,
                                                 usuario_logado),
                               resizable=True)

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

