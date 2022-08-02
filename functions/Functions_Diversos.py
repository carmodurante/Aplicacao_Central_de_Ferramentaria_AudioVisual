from validate_docbr import CPF


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


def validar_cpf(cpf_id):
    return CPF(cpf_id)


def validar_celular(celular):
    if 10 <= len(celular) <= 11:
        return True
    else:
        return False
