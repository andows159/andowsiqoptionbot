#o bot tem que esperar dar os horarios
#quando ele for ativado nos horarios deve pegar as informações da vela e mandar o comando 
#deve guardar a informação do valor inicial e do valor de compra de cada vela 

from iqoptionapi.stable_api import IQ_Option
import time, json, logging
from datetime import datetime
from dateutil import tz

#logging.disable(level=(logging.DEBUG)) ativar qnd for botar comercial

API = IQ_Option('canalandows@gmail.com','riacho2020')
API.connect()
API.change_balance('PRACTICE') #REAL

while True:
    if API.check_connect() == False:
        print("Erro ao se conectar")
    else:
        print("conectado com sucesso")
        break
    time.sleep(1)

def perfil():
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))

    return perfil

def timestamp_converter(x):
    hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    hora = hora.replace(tzinfo=tz.gettz('GMT'))
    
    return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]

def banca():
    return print(API.get_balance())

'''def payout(par,tipo):
    if tipo == 'turbo':
        a = API.get_all_profit()
        return int(100 * a[par]['turbo'])
    elif tipo == 'digital':
'''
        
par = 'EURUSD'

#vela = API.get_candles(par, 60, 10, time.time())

#print(x['name'])
#print(x['nickname'])
#print(x['currency'])
#print(timestamp_converter(x['created']))


#for velas in vela:
#    print('Hora inicio: '+str(timestamp_converter(velas['from']))+' Abertura:  '+str(velas['open']))


#AUla quatro ele fala como pegar muitas  velas anteriores só não quis escrever
#x = perfil()

#API.start_candles_stream(par,60,1)
#time.sleep(1)
#vela = API.get_realtime_candles(par, 60)

#for velas in vela:
    #print(vela[velas])
par = API.get_all_open_time()

for paridade in par['turbo']:
    if par['turbo'][paridade]['open'] == True:
        print(paridade)
print('\n')
for paridade in par['digital']:
    if par['digital'][paridade]['open'] == True:
        print(paridade)


