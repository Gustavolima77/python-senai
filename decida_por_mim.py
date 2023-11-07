# projeto 4 decida por mim
# Faça um pergunta para o programa e ele tera que te dar uma resposta

import random
import PySimpleGUI as sg

class DecidaPorMim:
 def __init__(self):
    self.respostas = [
      'Com certeza, voce deve fazer isso',
      'Não sei, você que sabe',
      'Não faz isso não!',
      'Acho que tá na hora certa!'

    ]

 def Iniciar(self):
   # layout
    layout = [
      [sg.Text('Faça sua pergunta')],
      [sg.Input()],
      [sg.Output(size=(50,10))],
      [sg.Button('Decida por mim')]
    ]
     # Criar a janela
    self.janela = sg.Window('Decida por mim!',layout=layout)
    while True:
     # ler os valores
      self.eventos, self.valores = self.janela.Read()
     # Fazer algo com os valores
      if self.eventos == 'Decida por mim':
        print(random.choice(self.respostas))
      
  
decida = DecidaPorMim()
decida.Iniciar()