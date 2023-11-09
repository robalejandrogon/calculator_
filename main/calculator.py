from tkinter import Tk
from tkinter import *
from tkmacosx import Button
from tkinter import ttk


class calculator():

    def __init__(self):

        self.name = "Python Calculator"

        self.q = ''
        self.number = []
        self.resultado = 0
        self.equal_sign = False
        self.current_symbol = ''
        self.ops = {
            '+' : 0,
            '-' : 0,
            '*': 1,
            '/': 1
        }
        

        self.load_main_window()

    def load_main_window(self):

        self.window = Tk()
        self.window.title('Fosy Python calculator')
        self.window.config(bg='gray')
        self.label_frame = Frame(self.window)
        self.label_frame .config( relief="sunken", borderwidth=5)
        self.label_frame .pack(side = 'top', fill = 'x', expand = True)

        self.my_string_var = StringVar()
        self.my_string_var.set("-")
        
        self.my_label = Label(self.label_frame,
                        textvariable = self.my_string_var)
        self.my_label .pack()

        buttons_frame_1 = Frame(self.window)
        buttons_frame_1 .config(bg='gray')
        buttons_frame_1 .pack()

        B1 = Button(buttons_frame_1 , text='1', bg='#D8D8D8',
                    fg='#00203F', borderless = 1, command = self.number_1)
        B1.pack(side = 'left',  ipady=35 )

        B2 = Button(buttons_frame_1, text='2', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_2)
        B2.pack(side = 'left',  ipady=35 )

        B3 = Button(buttons_frame_1 , text='3', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_3)
        B3.pack(side = 'left',  ipady=35 )

        Bplus = Button(buttons_frame_1 , text='+', bg='#E69A8D',
                    fg='#00203F', borderless=1, command = self.suma)
        Bplus.pack(side = 'left',  ipady=35 )

        Bdiv = Button(buttons_frame_1 , text='÷', bg='#E69A8D',
                    fg='#00203F', borderless=1, command = self.divs)
        Bdiv.pack(side = 'left',  ipady=35 )

        buttons_frame_2 = Frame(self.window)
        buttons_frame_2 .config(bg='gray')
        buttons_frame_2 .pack()

        B4 = Button(buttons_frame_2 , text='4', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_4)
        B4.pack(side = 'left',  ipady=35,)

        B5= Button(buttons_frame_2 , text='5', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_5)
        B5.pack(side = 'left',  ipady=35 )

        B6 = Button(buttons_frame_2 , text='6', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_6)
        B6.pack(side = 'left',  ipady=35 )

        Bminus = Button(buttons_frame_2 , text='-', bg='#E69A8D',
                    fg='#00203F', borderless=1, command = self.resta)
        Bminus.pack(side = 'left',  ipady=35 )

        Bac = Button(buttons_frame_2, text='AC', bg='#E69A8D',
                    fg='#00203F', borderless=1, command = self.ac)
        Bac.pack(side = 'left',  ipady=35 )

        buttons_frame_3 = Frame(self.window)
        buttons_frame_3 .config(bg='gray')
        buttons_frame_3 .pack()

        B7 = Button(buttons_frame_3 , text='7', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_7)
        B7.pack(side = 'left',  ipady=35 )

        B8 = Button(buttons_frame_3 , text='8', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_8)
        B8.pack(side = 'left',  ipady=35 )

        B9 = Button(buttons_frame_3 , text='9', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.number_9)
        B9.pack(side = 'left',  ipady=35 )

        Bmul = Button(buttons_frame_3 , text='x', bg='#E69A8D',
                    fg='#00203F', borderless=1, command = self.mult)
        Bmul.pack(side = 'left',  ipady=35 )
        
        Beq = Button(buttons_frame_3 , text= '=', bg='#E69A8D',
                    fg='#00203F', borderless=1, command = self.res)
        Beq.pack(side = 'left',  ipady=35 )

        buttons_frame_4 = Frame(self.window)
        buttons_frame_4 .config(bg='gray')
        buttons_frame_4 .pack()

        B0 = Button(buttons_frame_4 , text='0', bg='#D8D8D8',
                    fg='#00203F', borderless=1,  command = self.number_0)
        B0.pack(side = 'left',  ipady=35 )

        Bd = Button(buttons_frame_4 , text='.', bg='#D8D8D8',
                    fg='#00203F', borderless=1, command = self.dot)
        Bd.pack(side = 'left',  ipady=35 )
       
        self.window.mainloop()

    def res(self):
        self.equal_sign = True
        if self.current_symbol == '+':
            acc = float(self.my_string_var.get()) + self.resultado
        elif self.current_symbol == '-':
            acc = self.resultado - float(self.my_string_var.get())
        elif self.current_symbol == 'x':
            acc = self.resultado * float(self.my_string_var.get())
        elif self.current_symbol == '÷':
            acc = self.resultado / float(self.my_string_var.get())
        
        self.my_string_var.set(
                ''.join(str(acc))
            )
    
    def ac(self):
        self.my_string_var.set("-")
        self.number = []
        self.resultado = 0
        self.ops = {
            '+' : 0,
            '-' : 0,
            '*': 0,
            '/': 0
        }

    def number_1(self):
        self.number.append('1')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_2(self):
        self.number.append('2')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_3(self):
        self.number.append('3')
        self.my_string_var.set(
            ''.join(self.number)
        )
    
    def number_4(self):
        self.number.append('4')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_5(self):
        self.number.append('5')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_6(self):
        self.number.append('6')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_7(self):
        self.number.append('7')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_8(self):
        self.number.append('8')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_9(self):
        self.number.append('9')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def number_0(self):
        self.number.append('0')
        self.my_string_var.set(
            ''.join(self.number)
        )

    def dot(self):
        if '.' not in self.number:
            self.number.append('.')
            self.my_string_var.set(
                ''.join(self.number)
            )

    def suma(self):
        self.current_symbol = '+'
        if self.equal_sign:
            self.resultado = float(self.my_string_var.get())
        else:
            self.resultado += float(self.my_string_var.get())
        self.number = []
        self.equal_sign = False

    def resta(self):
        self.current_symbol = '-'
        if self.equal_sign:
            self.resultado = float(self.my_string_var.get())
        else:
            self.resultado -= float(self.my_string_var.get())
        self.number = []
        self.equal_sign = False

    def mult(self):
        self.current_symbol = 'x'
        if self.equal_sign:
            self.resultado = float(self.my_string_var.get())
        else:
            self.resultado *= float(self.my_string_var.get())
        self.number = []
        self.equal_sign = False

    def divs(self):
        self.current_symbol = '÷'
        if self.equal_sign:
            self.resultado = float(self.my_string_var.get())
        else:
            if self.resultado == 0:
                self.resultado = float(self.my_string_var.get())
            else:
                self.resultado = float(float(self.my_string_var.get()) / self.resultado)
        self.number = []
        self.equal_sign = False


def main():
    s = calculator()

if __name__ == "__main__":
    main()
