import os 
import glob
from datetime import datetime
from time import sleep
import random

class exclusaoDeFotos:


    def deletando(self):
        
        print(os.linesep)
        print('============= ***********************    =================')
        print('============= EXCLUSÃO DE FOTOS EM MASSA =================')
        print('============= ************************   =================')
        print(os.linesep)
        # BUSCAR POR DIRETÓRIO VAI PROCURA PASTA QUE SE ENCONTRA AS FOTOS OU OS PRINTS '.PNG'
        targetPatter = os.path.join(os.getcwd() + os.sep + 'Arquivo_TEMPORARIO_de_print_do_site' + os.sep +   '*.png') 
        # VAMOS ATRIBUIR A UMA VARIÁVEL, PARA BUSCAR TODAS AS INFORMAÇÕES DO targetPatter
        caminho_do_diretorio = glob.glob(targetPatter)

        print(caminho_do_diretorio)
        print(os.linesep)
        print(os.linesep)

        # vamos aguardar um tempo para que o Sistema envie o E-mail com as Imagens e Depois os apague 
        # sleep(random.randint(20,35))
        sleep(random.randint(7,10))
        print(f'⏭ Vamos Excluir todas as Fotos com final .png{os.linesep}.....Aguarde{os.linesep}')

        for caminhos_dos_diretorios in caminho_do_diretorio:

            print(f'⏭  Vamos criar um Laço de Repetição  para poder resolver a questão da exclusão em Massa {os.linesep}')
            os.remove(caminhos_dos_diretorios)
            print(f'⏭  Excluimos com Sucesso {os.linesep}')
            
            Mostrando_o_horario_que_enviou  = datetime.now().strftime('%d/%m/%Y  %H:%M')
            Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y')
            print(f' 💯💯💯 Exclusão feitas as {Mostrando_o_horario_que_enviou[10:]} Do dia  {Mostra_a_data_do_ano}{os.linesep}')
            print(f'🤖🤖TERMINOU AQUI !!!! {os.linesep}')
            print(f'🤖🤖Obrigado por usar o Nosso Boot🤖🤖🤖{os.linesep}')

sendeee = exclusaoDeFotos()
sendeee.deletando()