#chute o numero 
#objetivo: criar um  algoritimo que gera um valor aleatorio e eu tenho que ficar tentando o numero ate eu acertar.

import random

class ChuteONumero:
  def __init__(self):
    self.valor_aleatorio = 0
    self.valor_minimo = 1 
    self.valor_maximo = 100
    self.tentar_novamente = True

  def Iniciar(self):
    self.GerarNumeroAleatorio()  
    self.PedirValorAleatorio()
    try:
       while self.tentar_novamente == True:
          if int(self.valor_do_chute) > self.valor_aleatorio:
           print('Chute um valor mais baixo!')
           self.PedirValorAleatorio()
          elif int(self.valor_do_chute) > self.valor_aleatorio:
            print('Chute um valor mais alto!') 
            self.PedirValorAleatorio()

            #CONCERTANDO O ERRO
          if int(self.valor_do_chute) == self.valor_aleatorio:     
           self.tentar_novamente = False
           print('PARABENS VOCE ACERTOU!!')  
    except:  
      print('favor digitar apenas numeros') 
      self.Iniciar()    

  def PedirValorAleatorio(self):
    self.valor_do_chute = input('chute um numero: ')

  def GerarNumeroAleatorio(self):
     self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)


# estanciando a clase
chute = ChuteONumero()   
chute.Iniciar()