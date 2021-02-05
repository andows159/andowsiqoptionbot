from backendiqbotandows import IqOptionBotBackEnd as backend
import PySimpleGUI as sg
from time import sleep
from time import localtime


class IqOptionBotFrontEnd:

    def __init__(self):
        #sg.theme('DarkBlack')
        sg.theme('Reddit')
        #sg.theme("DarkTeal6")
        #sg.theme('DarkBlack1')
        self.layout1 = [
            
            
        [sg.Image('/p.png',size=(0,230))],
        
        [sg.Text("Login",size=(5,0)), sg.Input(key="login",size=(24,0))],
      
        
        [sg.Text("Senha",size=(5,0)), sg.Input(key="senha",password_char='*',size=(24,0))],
        
        [sg.Text("Data",size=(5,0)),sg.Input(size=(3,0)),sg.Text("/"),
         sg.Input(size=(3,0)),sg.Text("/"),sg.Input(size=(9,0))],
        
        [sg.Text("Hora",size=(5,0)),sg.Input(size=(3,0)),sg.Text(":")
         ,sg.Input(size=(3,0))],
        
        [sg.Radio('Simulação','opcoes', key='Simulação'),sg.Radio('Real','opcoes',key='Real')],
        
        [sg.Text("Valor da entrada"),sg.Input(key="entrada",size=(9,0))],
        
        [sg.Radio('Call','direcao', key='call'),sg.Radio('Pull','direcao',key='pull'),
         sg.Text(" "*1),sg.Button("Conectar")]
        
        ,[sg.Output(size=(28,8))]
        
            ]
       
        
        self.janela1 = sg.Window("Bot Opções binárias").Layout(self.layout1)
       
        
    def iniciarfront(self):
      
        botão, valores = self.janela1.Read()
        login = valores["login"]
        senha = valores["senha"]
        entrada = valores["entrada"]

            
        while True:
            if valores["Simulação"] == True:
                print("Simulação")
                break
            elif valores["Real"] == True:
                print("Real")
                break
                    
                              
                    
        backend().fazer_login(login,senha,2, 'EURUSD', 'call', 1)
        print("EFETUADO ÀS 03:33 DO DIA 16/06/2020")
            
            
                
            
                
            
            
a = IqOptionBotFrontEnd().iniciarfront()
