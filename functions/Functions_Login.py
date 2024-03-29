import traceback

import PySimpleGUI as sg


# Barra de Progresso
def progress_bar(texto_popup):
    sg.theme('Black')
    layout = [[sg.Text(texto_popup)],
              [sg.ProgressBar(1200, orientation='h', size=(30, 30), key='progbar')],
              [sg.Cancel()]]

    window = sg.Window('Executando...', layout)
    for i in range(1200):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


# Salvar Usuário em arquivo
def salvar_novo_usuario(username, password, email, admin):
    with open("content/data/usuarios.csv", "a", encoding='utf-8') as arquivo_usuarios:
        usuario_arquivo = [f'\n{username}', f';{password}', f';{email}', f';{admin}']
        arquivo_usuarios.writelines(usuario_arquivo)


# Carregar Usuários
def carregar_usuarios(username, password):
    admin = False
    lista_usuarios = []
    validado = False
    with open("content/data/usuarios.csv", "r", encoding='utf-8') as arquivo_usuarios:
        for linha in arquivo_usuarios:
            linha_limpa = linha.strip()
            lista_split = linha_limpa.split(';')
            lista_usuarios.append(lista_split)

    for linha in lista_usuarios:
        if username == linha[0] and password == linha[1]:
            validado = True
            admin = linha[3]

    usuario_validado = {'username': username, 'validado': validado, 'admin': admin}
    return usuario_validado


# Criar Conta
def create_account():
    sg.theme('Black')
    layout = [[sg.T("Cadastrar Usuário", size=(18, 1), font=40, justification='c', expand_x=True, border_width=10,
                    background_color='White', text_color='Black')],
              [sg.Text("E-mail", size=(19, 1), font=16), sg.InputText(key='EmailCadastro', font=16, size=25)],
              [sg.Text("Criar Usuário", size=(19, 1), font=16), sg.InputText(key='UsernameCadastro', font=16, size=25)],
              [sg.Text("Criar Senha", size=(19, 1), font=16),
               sg.InputText(key='PasswordCadastro', font=16, password_char='*', size=25)],
              [sg.Text('Usuário Administrador?', size=(19, 1), font=16),
               sg.Checkbox('', key='AdminCadastro', default=True, font=16, size=(15, 1))],
              [sg.Button("Cadastrar", pad=(35, 20), key='SubmitCadastro', expand_x=True),
               sg.Button("Cancelar", pad=(35, 20), key='CancelCadastro', expand_x=True)]]

    window = sg.Window("Cadastrar novo usuário", layout)

    while True:
        event, values = window.read()
        if event == 'CancelCadastro' or event == sg.WIN_CLOSED:
            break
        else:
            if event == "SubmitCadastro":
                try:
                    password = values['PasswordCadastro']
                    username = values['UsernameCadastro']
                    admin = values['AdminCadastro']
                    email = values['EmailCadastro']
                    if password.strip() != "" and username.strip() != "":
                        salvar_novo_usuario(username, password, email, admin)
                        progress_bar('Criando seu usuário...')
                        break
                    else:
                        sg.popup("Usuario e Senha são Obrigatórios", title='Error', font=8)

                except Exception:
                    traceback.print_exc()
                    sg.popup("Operação Cancelada", title='Error', font=8)
                    break
    window.close()


# Logar
def login():
    sg.theme("Black")

    layout = [[sg.T("Log In", size=(18, 1), font=40, justification='c', expand_x=True, border_width=5,
                    background_color='White', text_color='Black')],
              [sg.Text("Usuário:", size=(8, 1), font=16), sg.InputText(key='UsernameLogin', font=16, size=25)],
              [sg.Text("Senha:", size=(8, 1), font=16),
               sg.InputText(key='PasswordLogin', password_char='*', font=16, size=25)],
              [sg.Button("Log In", pad=(10, 20), key='SubmitLogin', auto_size_button=True, expand_x=True),
               sg.Button("Cancelar", pad=(10, 20), key='CancelLogin', auto_size_button=True, expand_x=True),
               sg.Button("Cadastrar", pad=(10, 20), key='CadastrarUsuario', auto_size_button=True, expand_x=True)]]

    window = sg.Window("Log In", layout)
    usuario_logado = {}
    while True:
        try:
            event, values = window.read()
            if event == "CancelLogin" or event == sg.WIN_CLOSED:
                usuario_logado = {'validado': False}
                break
            else:
                if event == "SubmitLogin":
                    usuario_logado = carregar_usuarios(values['UsernameLogin'], values['PasswordLogin'])
                    if usuario_logado['validado']:
                        print('logado')
                        break
                    else:
                        sg.popup("Login inválido", title='Erro Log In', font=8, )

                elif event == 'CadastrarUsuario':
                    create_account()
        except Exception:
            traceback.print_exc()
            sg.popup("Finalizando Aplicação", title='Information', font=8)
            break

    window.close()
    return usuario_logado
