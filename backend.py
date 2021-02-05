from iqoptionapi.stable_api import IQ_Option
import time, json, logging
from datetime import datetime
from dateutil import tz

#o bot tem que esperar dar os horarios
#quando ele for ativado nos horarios deve pegar as informações da vela e mandar o comando 
#deve guardar a informação do valor inicial e do valor de compra de cada vela 

class IqOptionBotBackEnd:
          
    '''def __init__(self):
        self.login = "canalandows@gmail.com"
        self.senha = "riacho2020"
        self.dados_entrada = (2, 'EURUSD-OTC', 'call', 1)
        
    #Coleta os dados que serão inseridos  em "fazer_login()"
		          
    def colher_dados_login(self):
        self.login = input("Login : ")
        self.senha = input("Senha : ")
        
   # coleta os dados que serão inseridos na "dar_entrada()"
   
    def colher_dados_entrada(self):
        self.dados_entrada = list()
        opcoes = ['entrada','par','direção','timeframe']
        for i in range(0,4):
            print(i)
            if i == 0 or i ==3:
                 dado = int(input(f" A Digite: {opcoes[i]} e tecle enter"))
            else:
                 dado = input(f"Digite: {opcoes[i]} e tecle enter")
                 
            self.dados_entrada.append(dado)'''

    # Efetua a entrada nos pares de moeda e verifica o sucesso da negociação
    # também mostra os valores, positivos ou negativos resultantes
    
    def dar_entrada_digital(self,):
        Paridade = "EURUSD"
        Duracao = 1#minute 1 or 5
        Entrada = 1
        Direcao = "call"
        status,id = self.API.buy_digital_spot(Paridade, Entrada, Direcao, Duracao)

        if isinstance(id, int):
            while True:
                status,lucro = self.API.check_win_digital_v2(id)
		
                if status:
                    if lucro > 0:
                        print('RESULTADO: WIN / BALANÇO: '+str(round(lucro,2)))
                        break
                    else:
                        print('RESULTADO: LOSS / BALANÇO: -'+str(Entrada))
                        break
                    
                    
    def dar_entrada_binaria(self):
        status,id = self.API.buy(10, 'EURUSD-OTC', 'put', 1)
        
        if status:
            print("Comprada")
            resultado,lucro = self.API.check_win_v3(id)
	
            print('RESULTADO: '+resultado+' / LUCRO: '+str(round(lucro, 2)))
            
            
            
            
     
        
                
        
    #Faz a conversão do formato de hora e data dado pela API para o formato GMT
                    
    def timestamp_converter(hora):
        hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
        hora = hora.replace(tzinfo=tz.gettz('GMT'))
        return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

    #Escolhe se vai utilizar dinheiro real ou o modo demonstração do iqoption

    def escolher_modalidade(self,modalidade):
        
        if modalidade == 'Simulação':
            self.API.change_balance('PRACTICE')
            
        elif modalidade == 'Real':
            self.API.change_balance('REAL')
            
    #Consulta seu saldo total na plataforma
    #(vale lembrar que vai consultar no modo em que você está logado (Practice ou Real)
    
    def banca(self):
        return print(self.API.get_balance())

    def resetar_banca_simulacao(self):
        self.API.reset_practice_balance()

    #Consulta o humor dos traders nas opções binarias (Só tem como pegar humor na binaria

    def humor_binaria(self,par):
        self.API.start_mood_stream(par+"-OTC")
        x = self.API.get_traders_mood(par+"-OTC")
        print(x)
        self.API.stop_mood_stream(par+"-OTC")

    #consulta as paridades abertas nas binarias turbo
    
    def paridades_abertas_turbo(self):
        par = self.API.get_all_open_time()
        self.lista_paridades_turbo = list()
        for paridade in par ['turbo']:
            if par['turbo'][paridade]['open'] == True:
                self.lista_paridades_turbo.append(paridade)
        return print(self.lista_paridades_turbo)
    
    #consulta as paridades abertas nas digitais
    
    def paridades_abertas_digital(self):
        par = self.API.get_all_open_time()
        self.lista_paridades_digital = list()
        for paridade in par ['digital']:
            if par['digital'][paridade]['open'] == True:
                self.lista_paridades_digital.append(paridade)
        return self.lista_paridades_digital
        
    
    #Consulta o nome oficial da conta, o apelido e a moeda padrão

    def buscar_informações_perfil(self):
        perfil = json.loads(json.dumps(self.API.get_profile_ansyc()))
        x = perfil
        return x['name'], x['nickname'], x['currency']

    #Essa função recebe os dados de entrada e faz login na plataforma
           
    def fazer_login(self,login,senha):
        self.login = login
        self.senha = senha 
        self.API = IQ_Option(login,senha)
        print("conectando...")
        self.API.connect()
        
        while True:
            if self.API.check_connect() == False:
                print("Erro ao se conectar")
                self.API.connect()
            else:
                print("conectado com sucesso")
                break
            
            time.sleep(1)

    #Essa função chama todas as outras
            
    def iniciar_back(self):
        self.fazer_login(self.login, self.senha)
        self.API.change_balance('PRACTICE')
        self.paridades_abertas_turbo()
        self.dar_entrada_binaria()
        
       


        
#a = IqOptionBotBackEnd()
#a.iniciar_back()
        
