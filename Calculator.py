# Armar una calculadora simple con tkinter

#importar todo del modulo tkinter
#abrir ventana y titulo siempre en tkinter
from tkinter import *

#declarar la expresion como variable
expression = ""


#funcion para actualizar expresion
#en la caja de ingresar texto

def press(num):
    #se;alar la expresion global variable
    global expression
    
    #concatenar el string
    expression = expression + str(num)
    
    #actualizar la expresion usando metodo set
    equation.set(expression)
    
    
#funcion para evaluar la expresion final
def equalpress():
    
    #el estatuto try se usa para manejar 
    #errores como division entre 0 etc

    try: 
     global expression 
    
    #--eval evalua la expresion 
    #y str convierte el resultado en string
    
     total = str(eval(expression))
    
     equation.set(total)
    
    #arrancar la variable expresion 
    #con un string vacio
        
     expression = ""
#si se genera error 
#pasa a manejar con el bloque except
    except:
        
        equation.set(" error ")
        expression = ""
        
#funcion para limpiar contenido de la entry box

def clear():
    global expression
    expression = ""
    equation.set("")
    
#driver
if __name__ == "__main__":
   
    #crear ventana GUI
    gui = Tk()
    
    #color del fondo GUI 
    gui.configure(background="grey")
    
    #titulo de ventana
    gui.title("Proyecto Calc <3")
    
    #definir perimetro ventana
    gui.geometry("270x150")
    
    #StringVar() es la class de variable
    #crear instancia de la class
    equation = StringVar()
    
    #caja de entrada de texto
    #para mostrar expression
    expression_field = Entry(gui, textvariable=equation)
    
    #grid se usa para poner objetos en sus respectivas
    #pocisiones de la widget en una estructura tabla
    expression_field.grid(columnspan=4, ipadx=70)
    
    #botones y posicionamiento en la ventana
    
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
                    command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                    command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                    command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                    command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                    command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                    command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                    command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                    command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                    command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                    command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
 
    plus = Button(gui, text=' + ', fg='black', bg='red', 
                command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
 
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(gui, text=' * ', fg='black', bg='red', 
                    command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(gui, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
 
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
 
    clear = Button(gui, text='Clear', fg='black', bg='red', 
                command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
 
    Decimal= Button(gui, text='.', fg='black', bg='red', 
                    command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=0) 
    
    #arrancar el GUI 
    gui.mainloop()