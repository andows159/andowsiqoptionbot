def colher_dados_entrada():
    dados_entrada = list()
    opcoes = ['entrada','par','direção','timeframe']
    for i in range(0,4):
        print(i)
        if i == 0 or i ==3:
             dado = int(input(f" A Digite: {opcoes[i]} e tecle enter"))
        else:
             dado = input(f"Digite: {opcoes[i]} e tecle enter")
             
        dados_entrada.append(dado)
   
        
colher_dados_entrada()
