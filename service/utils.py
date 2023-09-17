import re
from datetime import datetime

class Utils:
    @staticmethod
    def validar_formato_data_hora(data_hora_string):
        padrao = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$'
        return bool(re.match(padrao, data_hora_string))

    @staticmethod
    def validar_data_maior_que_atual(data_hora_string):
        padrao = r'^(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2})$'
        match = re.match(padrao, data_hora_string)

        if not match:
            return False

        dia = int(match.group(1))
        mes = int(match.group(2))
        ano = int(match.group(3))
        hora = int(match.group(4))
        minuto = int(match.group(5))

        data_da_string = datetime(ano, mes, dia, hora, minuto)
        data_atual = datetime.now()

        return data_da_string > data_atual
