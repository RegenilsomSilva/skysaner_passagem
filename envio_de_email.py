
import os
import smtplib
from email.message import EmailMessage
import imghdr
import time
from datetime import datetime
import random
from time import sleep
import glob


print(os.linesep)
print('============= *********************** =================')
print('============= ENVIO DE EMAIL EM MASSA =================')
print('============= ************************=================')
print(os.linesep)

class EnvioDeEmails:

    def __init__(self):
        # Configuração de login
        print(f'configuração de Login {os.linesep}')
        # self.ENDERECO_EMAIL = os.environ.get('EMAIL_REMETENTE')
        # self.SENHA_EMAIL = os.environ.get('SENHA_DO_EMAIL')
        self.ENDERECO_EMAIL = 'regenilsom.vcdevaprender@gmail.com'
        self.SENHA_EMAIL    = 'Pawlla77!'
        
        
        self.contatos = ['paula43oliveira@hotmail.com',
                         'regenilsomfeliz@outlook.com','regis@servgas.com','niniolegal@hotmail.com','regenilsom2015@gmail.com']

    # def Start_Send(self):

    #     self.Configurations_To_Envio()
    #     # self.Anexa_Files()
    #     self.Anexo_Imagens()
    #     self.To_Send_Email()

    def Configurations_To_Envio(self,mensagem_de_envio):

        # Criando o e-mail
        print(f'Criando um  E-mail para ser Enviado{os.linesep}.....Aguarde{os.linesep}')
        Mostrando_o_horario_que_enviou  = datetime.now().strftime('%d/%m/%Y  %H:%M')
        Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y')
        print(f'E-mail enviado as {Mostrando_o_horario_que_enviou[10:]} do dia {Mostra_a_data_do_ano}')
        self.mensagem = EmailMessage()
        self.mensagem['Subject'] = f'O Detetive de Preços encontra preços ótimos para você {Mostrando_o_horario_que_enviou[10:]} do Dia {Mostra_a_data_do_ano}'
        self.mensagem['From'] = self.ENDERECO_EMAIL
        self.mensagem['To'] = ', '.join(self.contatos)
        # self.mensagem.set_content(f' 🙌🙌🙌🙌 Olá Promoções de Destaque Corre que dura pouco  Boas Compras  ✔️ !!!',{mensagem_de_envio})
        # self.mensagem.set_content(f' 🙌🙌🙌🙌 Olá, Promoções em Destaque Corre, que dura pouco  Boas Compras  ✔️ !!! ' ,{mensagem_de_envio})
        # self.mensagem01 = [f' 🙌🙌🙌🙌 Olá, Promoções em Destaque Corre, que dura pouco  Boas Compras  ✔️ !!! ']
        self.mensagem.set_content(mensagem_de_envio)
        time.sleep(1)
        self.mensagem.add_alternative("""\
                <!DOCTYPE html>

                <html dir="ltr" lang="pt-br">
                <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    
                <!-- Stylesheets
                ============================================= -->
                <link rel="stylesheet" href="css/bootstrap.css" type="text/css" />
                <link rel="stylesheet" href="css/style.css" type="text/css" />
                <link rel="stylesheet" href="css/swiper.css" type="text/css" />
                <link rel="stylesheet" href="css/dark.css" type="text/css" />
                <link rel="stylesheet" href="css/font-icons.css" type="text/css" />
                
                <!-- Document Title
                ============================================= -->
                <title> REGIS AUTOMAÇÃO WEB  </title>
                <!--
                verde #0ff1ce
                rosa #bd257c
                -->
                </head>
                <body class="stretched">
                                <p>
                                <h2 style= 'text-align:center'> REGIS AUTOMAÇÃO WEB   </h2>
                                <span style="font-size: 1.5rem; color: red;">  🙌🙌🙌🙌 Olá, Promoções em Destaque Corre que dura pouco.  Boas Compras  ✔️ !!! .</span>
                            </div>
                            <h3 style="color: #0ff1ce;"> Copyrights © All Rights Reserved by REGIS AUTOMAÇÃO WEB S/A </h3><br>
                        </html>
        """,subtype='html')


# Configurar o anexo de imagens


    def Anexo_Imagens(self):

        print(f'⚙🔍 Configuração de Envio de Imagens para o E-mail...{os.linesep}....Aguarde ⚙🔍 {os.linesep}')

        # Estarei fazendo com que o sistema faça a integração caminho + o Diretório que se encontra as fotos .png
        targetPatter = os.path.join(os.getcwd() + os.sep + 'Arquivo_TEMPORARIO_de_print_do_site' + os.sep + '*.png')
        caminho_das_fotos = glob.glob(targetPatter)

        # Aqui estou fazendo um Loop, para que o Sistema Encontre minha extensão .png
        for caminho_das_foto in caminho_das_fotos:
            with open(caminho_das_foto, 'rb') as arquivo:
                dados = arquivo.read()
                extensao_imagem = imghdr.what(arquivo.name)
                nome_arquivo = arquivo.name
            self.mensagem.add_attachment(dados, maintype='image',subtype=extensao_imagem, filename=nome_arquivo)

            print(
                f'⏳ Acabamos de Fazer a Manipulação de imagens.... ⏳ {os.linesep}.....Aguarde')
            sleep(random.randint(1, 2))
            print(os.linesep)

   
    def To_Send_Email(self):
      # Fazendo  o envio de Emails
        
        Mostrando_o_horario_que_enviou  = datetime.now().strftime('%d/%m/%Y  %H:%M')
        Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y')
        print(f' 🙌🙌 Fazendo Envio Seguro de E-mail as {Mostrando_o_horario_que_enviou[10:]} do Dia {Mostra_a_data_do_ano}{os.linesep}......Aguarde{os.linesep}')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as sistema_de_envio:
            sistema_de_envio.login(self.ENDERECO_EMAIL, self.SENHA_EMAIL)
            sistema_de_envio.send_message(self.mensagem)
            sleep(random.randint(8, 10))

        print(f'🤖🤖TERMINOU AQUI !!!! {os.linesep}')
        print(f'🤖🤖Obrigado por usar o Nosso Boot🤖🤖🤖{os.linesep}')


