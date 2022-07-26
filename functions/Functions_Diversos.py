def get_link_url_dev5():
    url_aplication_git = 'https://github.com/carmodurante/Aplicacao_Central_de_Ferramentaria_AudioVisual'
    return url_aplication_git

def get_file_types():
    file_types = [("JPEG (*.jpeg)", "*.jpeg"),
                  ("JPG (*.jpg)", "*.jpg"),
                  ("PNG (*.png)", "*.png")]
    return file_types

def get_color_admin(string_boleana):
    if string_boleana == 'True':
        return 'green'
    else:
        return 'red'