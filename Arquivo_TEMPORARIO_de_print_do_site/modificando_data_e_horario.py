import os
from datetime import datetime

Mostrando_o_horario_que_enviou = datetime.now().strftime('%d%m%Y %H:%M')
mensagem_de_envio = f'O Preço da passagem  Foi Alterado: {os.linesep}....Às...: {Mostrando_o_horario_que_enviou[9:]}'
print(mensagem_de_envio)

print(os.linesep)
print(os.linesep)

# print(datetime.now())
mostar_a_data_do_ano = datetime.now().strftime('%d-%m-%Y')
print(mostar_a_data_do_ano)