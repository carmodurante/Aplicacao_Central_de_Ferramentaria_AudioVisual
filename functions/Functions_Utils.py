from validate_docbr import CPF

import functions.Functions_Cadastro as cadastro


def get_link_url_dev5():
    url_aplication_git = 'https://github.com/carmodurante/Aplicacao_Central_de_Ferramentaria_AudioVisual'
    return url_aplication_git


def get_file_types():
    file_types = [("JPG (*.jpg)", "*.jpg")]
    return file_types


def get_color(string_boleana):
    if string_boleana == 'True':
        return 'green'
    else:
        return 'red'


def validar_cpf(cpf_id, cadastrar):
    cpf = CPF()
    # Quando cadastro, validar se ja existe esse CPF
    if cpf.validate(cpf_id):
        if cadastrar:
            for linha in cadastro.get_cadastrados('tecnico'):
                if linha[:12] == str(cpf_id):
                    return False
            return cpf.validate(cpf_id)
        else:
            return cpf.validate(cpf_id)

    else:
        return cpf.validate(cpf_id)


def validar_celular(celular):
    if 10 <= len(celular) <= 11:
        return True
    else:
        return False
