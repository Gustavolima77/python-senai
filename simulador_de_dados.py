# simulador de dados
# simular o uso de um dado, gerando um valor de 1 a 6 

import random 
import PySimpleGUI as sg

class SimuladorDeDado:
  def __init__(self):
    self.valor_minimo = 1
    self.valor_maximo = 6
    #layot
    self.layout = [
      [sg.Text('jogar o dado?')],
      [sg.Button('Sim'),sg.Button('Não')]
    ]
    #criar uma janela
    self.janela = sg.Window('Simiulador de Dado',layout=self.layout)
    #ler os valores da tela
    self.eventos, self.valores = self.janela.read()
    #fazer alguma coisa com esses valores

  def iniciar(self):
     #criar uma janela
    self.janela = sg.Window('Simiulador de Dado',layout=self.loyout)
    #ler os valores da tela
    self.eventos, self.valores = self.janela.Read()
    #fazer alguma coisa com esses valores
    while True:
        try:
           if self.eventos == 'sim' or self.eventos == 's':
            self.GerarValorDoDado()
           elif self.eventos == 'nao' or self.eventos == 'n':
            print('Agradecemos sua participação')
           else:
            print('favor digite sim ou não')
        except:
            print('Ocorreu um erro  ao receber sua resposta')


  def GerarValorDoDado(self):
    print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.iniciar()
