from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Está é uma mensagem automatica, Seja bem vindo ao meu GitHub"
        self.grupos = ["Bloco de notas", "ADS Alunos Uninove"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo_ou_pessoa in self.grupos:
            grupo = self.driver.find_element_by_class_name('_21S-L')
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('iq0m558w')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
