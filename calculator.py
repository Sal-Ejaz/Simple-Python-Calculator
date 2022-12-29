from tkinter import *

def buttonPress():
    pass

def equals():
    pass

def clear():
    pass

def main():
    the_window = Tk()
    the_window.title("Calculator")
    the_window.geometry("600x600")
    equationText = ""
    equationLabel = StringVar()
    label = Label(the_window, textvariable=equationLabel, font=('consolas',20), bg="white", width=24, height=2,)
    label.pack()
    frame = Frame(the_window)
    frame.pack()

    button1 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(1))
    button1.grid(row=0, column=0)

    button2 = Button(frame, text=2, height=4, width=9, font=35, command= lambda: button_press(2))
    button2.grid(row=0, column=1)

    button3 = Button(frame, text=3, height=4, width=9, font=35, command= lambda: button_press(3))
    button3.grid(row=0, column=2)

    button4 = Button(frame, text=4, height=4, width=9, font=35, command= lambda: button_press(4))
    button4.grid(row=1, column=0)

    button5 = Button(frame, text=5, height=4, width=9, font=35, command= lambda: button_press(5))
    button5.grid(row=1, column=1)

    button6 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: button_press(6))
    button6.grid(row=1, column=2)

    button7 = Button(frame, text=7, height=4, width=9, font=35, command= lambda: button_press(7))
    button7.grid(row=2, column=0)

    button8 = Button(frame, text=8, height=4, width=9, font=35, command= lambda: button_press(8))
    button8.grid(row=2, column=1)

    button9 = Button(frame, text=9, height=4, width=9, font=35, command= lambda: button_press(9))
    button9.grid(row=2, column=2)

    button0 = Button(frame, text=0, height=4, width=9, font=35, command= lambda: button_press(0 ))
    button0.grid(row=3, column=0)

    plus_sign = Button(frame, text='+', height=4, width=9, font=35, command= lambda: button_press('+'))
    plus_sign.grid(row=0, column=3)

    minus_sign = Button(frame, text='-', height=4, width=9, font=35, command= lambda: button_press('-'))
    minus_sign.grid(row=1, column=3)

    multiplication_sign = Button(frame, text='*', height=4, width=9, font=35, command= lambda: button_press('*'))
    multiplication_sign.grid(row=2, column=3)

    division_sign = Button(frame, text='/', height=4, width=9, font=35, command= lambda: button_press('/'))
    division_sign.grid(row=3, column=3)

    equals_sign = Button(frame, text='=', height=4, width=9, font=35, command= lambda: equals)
    equals_sign.grid(row=3, column=2)

    decimal_sign = Button(frame, text='.', height=4, width=9, font=35, command= lambda: button_press('.'))
    decimal_sign.grid(row=3, column=1)

    clear_button = Button(the_window, text='C', height=4, width=18, font=35, command= clear)
    
    clear_button.pack()


    the_window.mainloop()
main()
    
