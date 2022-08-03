from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
Builder.load_file('calc.kv')
class Tela(Widget):
    def button_press(self,button):
        previo=self.ids.calc_input.text
        if 'Error !' in previo:
            previo=''
        if previo == '0':
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'
        else:
            self.ids.calc_input.text=f'{previo}{button}'
    def sinal_recebido(self,sinal):
        previo=self.ids.calc_input.text
        self.ids.calc_input.text=f'{previo}{sinal}'
    def equals  (self):
        previo=self.ids.calc_input.text
        try:
            resposta=eval(previo)
            self.ids.calc_input.text=str(resposta)
        except:
            self.ids.calc_input.text='Error !'
    def ponto(self):
        previo=self.ids.calc_input.text
        num_list = previo.split('+')
        if '+' in previo and '.'not in previo[-1]:
            previo=f'{previo}.'
        elif "." in previo:
            pass
        else:
            previo=f'{previo}.'
            self.ids.calc_input.text=previo
    def remover(self):
        previo=self.ids.calc_input.text
        previo=previo[:-1]
        self.ids.calc_input.text=previo
    def pos_neg(self):
        previo=self.ids.calc_input.text
        if '-' in previo:
            self.ids.calc_input.text=f'{previo.replace("-","")}'
        else:
            self.ids.calc_input.text=f'-{previo}'

class Calc(App):
    def build(self):
        return Tela()
if __name__ == '__main__':
    Calc().run()