def get_cadastro_ferramentas():
    lista_cadastrado_ferramentas = [['1001', 'Chave Inglesa', 'John Deere', '110V', '1015-U521', '10', 'Polegadas',
                                     'Metal', '36', 'True'],
                                    ['1002', 'Chave de Fenda', 'John Deere', 'N/D', '1015-U522', '40', 'Metros',
                                     'Aluminio', '24', 'False']]

    return lista_cadastrado_ferramentas


def get_cadastro_tecnicos():
    lista_cadastrado_tecnicos = [['46794179865', 'Carmo Durante Neto', '16992180889', 'Manhã', 'Hell Fire'],
                                 ['12345678910', 'Jose Carlos', '1699111111', 'Noite', 'Titans']]

    return lista_cadastrado_tecnicos


def cadastrar_ferramenta(values):
    lista_ferramenta = [values['fDescricao'].strip()]

    return lista_ferramenta


