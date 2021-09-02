
# control K + c Comentar
# control K + U

from selenium.webdriver import ActionChains
import schedule
from datetime import datetime
from selenium.common.exceptions import *
import random
import time
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import by
from selenium.webdriver.common import keys
from selenium.webdriver.common.actions.interaction import Pause
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import errorhandler
# PERMITE O USO DO TECLADO
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os
from math import e, exp
import pyautogui
from email.message import EmailMessage
from email.utils import make_msgid


    # como subir os driver com os PATH e os buldiPack para o heroku

# Class
# Importar Biblioteca
# Criar variavéis
# Criar Metodos
# instaciar as variasves
# Criar Funçôes
# Importar a Biblioteca (squedil)
# Dentro do Overview tem que ativar o projeto ser não ele não funciona
# all active

print(" ")
print("===============================================================================")
print("=====                                                                      ====")
print("============   AUTOMATIZANDO PREÇOS DE PASSAGENS ÁEREA   GOL       ============")
print("=====================                BOOT-REGIS                    ============")
print("===============================================================================")
print(" ")

# rodando dentro do servidor heroku


def Buscando_passagem_aerea():

    FireFox_options = Options();
    FireFox_options.add_argument("--lang=pt-BR");
    FireFox_options.add_argument("--disable-notifications");
    FireFox_options.add_argument("--disable-notifications");
    FireFox_options.add_argument("ignore-error-ssl");
    # configuração para roda em Segundo Plano
    FireFox_options.add_argument('--headless');
    FireFox_options.headless = True
    # configuração para rodar com pouca Memoria Ram, evitando erro de performasse
    FireFox_options.add_argument('--disable-dev-shm-usage');
    # configuração Usada para rodar no Servidor LINUX
    FireFox_options.add_argument('--no-sandbox');

    # VAMOS DEIXAR QUE O SERVIDOR ASSUMA A FUNÇÃO DO CHROME DRIVER
    # caminho_do_driver = os.environ.get('CHROMEDRIVER_PATH')
    # chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    FireFox_options.binary_location = os.environ.get('FIREFOX_BIN')
    caminho_do_driver = os.environ.get('GECKODRIVER_PATH')

    # driver = webdriver.Chrome(executable_path=r"./chromedriver.exe",  options=chrome_options)
    # driver = webdriver.Firefox(
        # executable_path=os.getcwd() + os.sep + 'geckodriver.exe')

    driver = webdriver.Firefox(executable_path=caminho_do_driver,  options=FireFox_options)

    # VAMOS CONFIGURAR PARA O HEROKU -> NOSSO SERVIDOR PARA RODAR ONLINE
    wait = WebDriverWait(
        driver=driver,
        timeout=15,
        poll_frequency=5,
        ignored_exceptions=[NoSuchElementException,
                            ElementNotVisibleException,
                            ElementNotSelectableException,
                            ]
    )

    # VAMOS CONFIGURAR PARA O HEROKU -> NOSSO SERVIDOR PARA RODAR OLINE

    driver.get('https://b2c.voegol.com.br/compra')
    driver.maximize_window()
    driver.get_window_size()

    try:
        print(os.linesep)
        # driver.get(driver.current_url) # Atualizando sempre a Página para descobri qual o valor está sendo recebido
        # driver.refresh()  # Atualizando sempre a Página para descobri qual o valor está sendo recebido

        fechar_politica = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
            )
        )
        if fechar_politica is not None:
            print('🙌 Encontramos A caixa de texto de Politica de Privacidade 🙌 !!')
            driver.execute_script('arguments[0].click()', fechar_politica)
            sleep(random.randint(1, 2))
            print(f'🔐 Fechamos a Politica de Privacidade.......{os.linesep}')
    except ValueError:

        print('Não Foi possivel Fechar 🔐 a Politica.....Talvez não exista mais....')
        pass

    escolher_trecho = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH,
             '//div[@class="m-select__focus"] //fieldset[@class="a-icon a-input m-select__fieldset"]')
        )
    )
    if escolher_trecho is not None:
        print('Encontramos a escolha do trecho ')
        escolher_trecho.click()

    trecho_so_ida = wait.until(
        expected_conditions.presence_of_all_elements_located(
            (By.XPATH,
             '//label[@class="a-radio__label"] //span[@class="m-select__list-anchor a-radio__label--orange"]')
        )
    )
    if trecho_so_ida is not None:
        print('Encontramos a opção de clicar em só ida')
        trecho_so_ida[1].click()

    try:
        Saindo_da_onde = wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//input[@id="input-saindo-de"]')

            )
        )
        if Saindo_da_onde is not None:
            print('🙌 Encontramos o Campo de Origem !!!! 🙌 ')
            driver.execute_script('arguments[0].click()', Saindo_da_onde)
            # campo_de_origem_aeroporto = 'salvador'
            print('📨  Estamos Digitando 📨')
            time.sleep(1)
            Saindo_da_onde.send_keys('salvador')

        Chegando_a_onde = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//input[@id="input-indo-para"]')
            )
        )
        if Chegando_a_onde is not None:
            print('🙌 Encontramos o campo de 📝 Digitar o Destino do Aeroporto..📝.\n')
            print(' 📝 Estamos Digitando 📝📝📝')
            time.sleep(1)

            # DigitarComoHumano(campo_de_destino, Destino_aeroporto)

        wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, '//div[@id="dropdown-saindo-de"]')
            )
        )
        campo_dropdawll = wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,
                 '//ul[@class="m-list-cta__list"] //li[@class="m-list-cta__item"] //button[@type="button"]')
            )
        )
        if campo_dropdawll is not None:
            print('🙏🙏🙏  Encontramos a CIDADE digitada....')
            time.sleep(1)
            campo_dropdawll[0].click()
            # campo_dropdawll.send_keys(Keys.TAB)
            # Chain = ActionChains(driver)
            # Chain.click(campo_dropdawll)
    except ValueError:
        print('Caiu dentro do EXCEPT.... Bloco cidade GUARULHOS')
        print(errorhandler)

    try:
        Indo_Para = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//input[@id="input-indo-para"]')
            )
        )
        if Indo_Para is not None:
            print('🙌 Encontramos o campo de 📝 Chegada ao Destino do Aeroporto..📝.\n')
            print(' 📝 Estamos Digitando 📝📝📝')
            driver.execute_script('arguments[0].click()', Indo_Para)
            print('Já cliclamos ▶ \n')
            Indo_Para.send_keys('SÃO PAULO')

        Segundo_dropdown = wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,
                 '//div[@class="m-dropdown__content m-dropdown--active"]  //li[@class="m-list-cta__item"]')
            )
        )
        if Segundo_dropdown is not None:
            print('🙏🙏🙏  Encontramos a CIDADE digitada.... SÂO PAULO')
            time.sleep(2)
            Segundo_dropdown[2].click()

    except:
        print('Caiu dentro do Excep..... Bloco CIDADE SÃO PAULO')
        print(errorhandler)

    time.sleep(2)

    try:
        Data_da_viagem_de_ida = wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//input[@placeholder="Quando?"]')
            )
        )
        if Data_da_viagem_de_ida is not None:
            print('Encontramos a Opção para Escolher o Mês de Viagem !!!')
            Data_da_viagem_de_ida.click()

        calendario = wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH,
                 '//button[@class="o-calendar__btn o-calendar__btn--next a-icon"]')
            )
        )
        if calendario is not None:
            print('Achamos o Calendario para ser Iniciado....')
            Chain = ActionChains(driver)
            #           COMANDO ANTIGO DO SITE DA GOL COM  Chain
            # Chain.click(calendario).pause(1).send_keys(Keys.PAGE_DOWN).pause(
            #     1).send_keys(Keys.PAGE_DOWN).pause(1).send_keys(Keys.PAGE_DOWN).perform()
            Chain.double_click(calendario)
            Chain.click()
            Chain.click()
            Chain.perform()

            print('🙌 ✔ 🖱 🖱 Estamos Clicando até chegar no Mês de Dezembro...... 🙌 ✔ ')

    except ValueError:
        print('Início  Caiu dentro do Except.........')
        print(ErrorInResponseException)
        
    try:

        escolha_data = wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,
                 '//li[@class="o-calendar__date o-calendar__date--price"]')
            )
        )
        if escolha_data is not None:

            print('✔ 🙌 Achamos a Opção de escolha de Data🙌')
            # driver.execute_script('arguments[29].click()',escolha_data)
            escolha_data[28].click()
            print('📅 ✅ foram marcada a Data 29 de Dezembro de 2021 📅 ✅ \n')
    except:
        print('A data não foi correspondida ao Dia 29/12/2021')
        print(errorhandler)
        print(ErrorInResponseException)
        
    wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//button[@type="submit"]')
            )
        )    

    try:
        campo_enviar_informacoes = wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//button[@type="submit"]')
            )
        )
        if campo_enviar_informacoes is not None:
            print(' 🙌 Encontramos o Campo de Enviar as Informações 🙌')
            driver.execute_script(
                'arguments[0].click()', campo_enviar_informacoes)
            print('Campo Validado !!!!! ✅ ')
            print(f'🤖 Até Mais........ 🤖🤖 {os.linesep}')

    except:
        print('Buscador de Voo não deu certo.... pode ser  que mudou.....')
        print(errorhandler)
        print(ErrorInResponseException)

    try:
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH,
                 '//span[@class="a-desc__value a-desc__value--price"]')
            )
        )
        preco_monitorado = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH,
                 '//span[@class="a-desc__value a-desc__value--price"]')
            )
        )
        # Verificar se o preço for  menor do que R$880,30
        # Verificar se o preço for  menor do que  R$ 1.202,32
        # time.sleep(2)
        # Comando para baixar 150 pixel para Baixo.......
        pyautogui.scroll(-450)
        if preco_monitorado.text <= 'a partir de R$  R$ 1.202,32':
            print(f' 🙌✔👌 O preço está igua ou Foi Alterado Para  {preco_monitorado.text} 😊 ')

        elif preco_monitorado.text <  'a partir de R$  R$ 1.202,32':
            print(f' 🙌✔👌 Preço Foi Alterado Para {preco_monitorado.text} 😊 ')

    except ValueError:
        print(" 😭🥺  Não conseguimos detectar os preços das passagens....I'm sorry.")
        print(errorhandler)
        print(ErrorInResponseException)

    try:    
        print('=======================Módulo Screeshort da página........===============================================')
        # TIRANDO PRINT DO SITE e
        print('****** TIRANDO SCREENSHOT DO SITE *******')
        time.sleep(2)
        for i in range(6):
            print('Estamos baixando em 570 in 570 Pixel')
            pyautogui.scroll(-670)
            time.sleep(1)
            print('Acabou de fazer o scroll') 
            nome_do_print_site = str(round(time.time() * 1000)) + '.png'
            print(f'Vamos Tira um screenshot ou print da Tela onde se encontra o valor {os.linesep}....Aguarde {os.linesep}')
            printe_ja_tirado_do_site = os.path.join('Arquivo_TEMPORARIO_de_print_do_site', nome_do_print_site)
            print(f'Print ou scrrehoot já tirado.....😊 {os.linesep}')
            driver.save_screenshot(printe_ja_tirado_do_site)
        print('************ TÉRMINIO DO  PRINT AQUI !!! ******************')
    
    except ValueError:
        print(" 😭🥺  Não foi possível tira o Screeshort da Página !!!!!  😭🥺  I'm sorry")

    

    print('====== ENVIANDO POR E-MAIL =========')
    time.sleep(25)
    from envio_de_email import EnvioDeEmails
    Send_Email = EnvioDeEmails()
    Mostrando_o_horario_que_enviou  = datetime.now().strftime('%d/%m/%Y  %H:%M')
    Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y') 
    mensagem = f' 🙌🙌🙌🙌 Confira os últimos preços para o voo do seu interesse: {preco_monitorado.text} Às:{Mostrando_o_horario_que_enviou[10:]} Do Dia {Mostra_a_data_do_ano}'
    Send_Email.Configurations_To_Envio(mensagem)
    Send_Email.Anexo_Imagens()
    Send_Email.To_Send_Email()
    print(os.linesep)


    print('============= EXCLUSÃO DE FOTOS EM MASSA =================')
    from exclusao_em_massa_de_arquivo import exclusaoDeFotos
    delite = exclusaoDeFotos()
    delite.deletando()
    print(f'🤖🤖TERMINOU AQUI !!!! {os.linesep}')
    print(f'🤖🤖Obrigado por usar o Nosso Boot🤖🤖🤖{os.linesep}')    



schedule.every(4).seconds.do(Buscando_passagem_aerea)
# schedule.every().friday.at('14:32:50').do(Buscando_passagem_aerea)

# schedule.every().days.at('07:00:56').do(Buscando_passagem_aerea)
# schedule.every().days.at('07:10:32').do(Buscando_passagem_aerea)
while True:
    schedule.run_pending()
    time.sleep(10)
