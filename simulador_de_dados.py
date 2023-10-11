# simulador de dados
# simular o uso de um dado, gerando um valor de 1 a 6 

import random

class SimuladorDeDado:
  def __init__(self):
    self.valor_minimo = 1
    self.valor_maximo = 6
    self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

  def iniciar(self):
    resposta = input(self.mensagem)
    if resposta == 'sim':
        self.GerarValorDoDado()
    elif resposta == 'nao' or resposta == 'n':
      print('Agradecemos sua participação')
    else:
      print('favor digitar sim ou não')


  def GerarValorDoDado(self):
    print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.iniciar()
