import datetime

from validate_docbr import CPF

import functions.Functions_Cadastro as cadastro


def get_link_url():
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
                if linha[0] == str(cpf_id):
                    return False
            return cpf.validate(cpf_id)
        else:
            return cpf.validate(cpf_id)
    else:
        return cpf.validate(cpf_id)


def validar_cpf_reserva(cpf_id):
    cpf = CPF()
    # validar se ja existe esse CPF
    if cpf.validate(cpf_id):
        for linha in cadastro.get_cadastrados('tecnico'):
            if linha[0] == str(cpf_id):
                return True
    else:
        return False
    return False


def validar_reserva(ferramenta, cpf, values, sg):
    valido = False

    if not validar_cpf_reserva(cpf):
        sg.popup("CPF Inválido ou Não Cadastrado.", title='Error', font=8)
        return False

    datatime_retirada = datetime.datetime(year=int(f'20{values["rDTRetirada"][6:]}'),
                                          month=int(values["rDTRetirada"][3:5]),
                                          day=int(values["rDTRetirada"][:2]),
                                          hour=int(values["rHRRetirada"]),
                                          minute=int(values["rMinRetirada"]))

    datatime_devol = datetime.datetime(year=int(f'20{values["rDTDevol"][6:]}'),
                                       month=int(values["rDTDevol"][3:5]),
                                       day=int(values["rDTDevol"][:2]),
                                       hour=int(values["rHRDevol"]),
                                       minute=int(values["rMinDevol"]))

    if datatime_retirada >= datatime_devol:
        sg.popup("Data de retirada deve ser anterior a de devolução.", title='Error', font=8)
        return False

    data_agora = datetime.datetime.now()
    data_diferenca = datatime_retirada - data_agora
    tempo_ate_retirada = data_diferenca.total_seconds()

    data_diferenca = datatime_devol - datatime_retirada
    tempo_reserva = data_diferenca.total_seconds()

    # Se selecionar uma data com menos de 24 horas para retirada
    if tempo_ate_retirada < 86400 and values['rEmergencial'] == False:  # Em segundos
        sg.popup("Data de Retirada deve ter no mínimo 24 horas de antecêndencia.", title='Error', font=8)
        return False

    erro = "Ferramenta selecionada não está cadastrada no sistema."
    for linha in cadastro.get_cadastrados('ferramenta'):
        # Ferramenta deve estar cadastrada
        if linha[0] == ferramenta:
            erro = "Tempo de Reserva da Ferramenta Excedido."
            tempo_max_reserva = (int(linha[5]) * 3600) + (int(linha[6]) * 60)
            # tempo de reserva nao pode ser maior que o tempo maximo de reserva da ferramenta
            if not tempo_reserva > tempo_max_reserva:
                valido = True
                break

    if valido:
        for linha in cadastro.get_cadastrados('reserva'):
            if linha[1] == ferramenta:
                datatime_retirada_db = datetime.datetime(year=int(f'20{linha[5][6:]}'),
                                                         month=int(linha[5][3:5]),
                                                         day=int(linha[5][:2]),
                                                         hour=int(linha[6]),
                                                         minute=int(linha[7]))

                datatime_devol_db = datetime.datetime(year=int(f'20{linha[8][6:]}'),
                                                      month=int(linha[8][3:5]),
                                                      day=int(linha[8][:2]),
                                                      hour=int(linha[9]),
                                                      minute=int(linha[101]))
                # Se a data de retirada estiver entre uma reserva
                if datatime_devol_db >= datatime_retirada >= datatime_retirada_db:
                    sg.popup("Data de Retirada possui períodos conflitantes com outra reserva.", title='Error', font=8)
                    return False
                # Se a data de devolucao estiver entre uma reserva
                if datatime_devol_db >= datatime_devol >= datatime_retirada_db:
                    sg.popup("Data de Devolução possui períodos conflitantes com outra reserva.", title='Error', font=8)
                    return False
    else:
        sg.popup(erro, title='Error', font=8)
        return False
    return valido


def validar_celular(celular):
    if 10 <= len(celular) <= 11:
        return True
    else:
        return False
