import tkinter as tk


calculation = ""


def dodaj_liczbe(liczba):
    global calculation
    calculation += str(liczba)
    tekst.delete(1.0, "end")
    tekst.insert(1.0, calculation)

def wyczysc():
    global calculation
    calculation = ""
    tekst.delete(1.0, "end")

def oblicz():
    global calculation
    try:

        calculation = str(eval(calculation))
        tekst.delete(1.0, "end")
        tekst.insert(1.0, calculation)
    
    except:
        wyczysc()
        tekst.insert(1.0, "Error")


okno = tk.Tk()
okno.title("Kalkulator")
okno.geometry("370x400")
okno.maxsize(370, 400)

tekst = tk.Text(okno, height=2, width=20, font=("Arial", 24))
tekst.grid(columnspan=5)


button1 = tk.Button(okno, text="1", command=lambda: dodaj_liczbe(1), width=5, height=1, font=("Arial, 14"))
button1.grid(row=1, column=0, pady=5, padx=5)

button2 = tk.Button(okno, text="2", command=lambda: dodaj_liczbe(2), width=5, height=1, font=("Arial, 14"))
button2.grid(row=1, column=1,  pady=5, padx=0)

button3= tk.Button(okno, text="3", command=lambda: dodaj_liczbe(3), width=5, height=1, font=("Arial, 14"))
button3.grid(row=1, column=2,  pady=5, padx=5)

button4= tk.Button(okno, text="4", command=lambda: dodaj_liczbe(4), width=5, height=1, font=("Arial, 14"))
button4.grid(row=2, column=0,  pady=0, padx=5)

button5= tk.Button(okno, text="5", command=lambda: dodaj_liczbe(5), width=5, height=1, font=("Arial, 14"))
button5.grid(row=2, column=1,  pady=0, padx=0)

button6= tk.Button(okno, text="6", command=lambda: dodaj_liczbe(6), width=5, height=1, font=("Arial, 14"))
button6.grid(row=2, column=2,  pady=0, padx=5)

button7= tk.Button(okno, text="7", command=lambda: dodaj_liczbe(7), width=5, height=1, font=("Arial, 14"))
button7.grid(row=3, column=0,  pady=5, padx=5)

button8= tk.Button(okno, text="8", command=lambda: dodaj_liczbe(8), width=5, height=1, font=("Arial, 14"))
button8.grid(row=3, column=1,  pady=5, padx=0)

button9= tk.Button(okno, text="9", command=lambda: dodaj_liczbe(9), width=5, height=1, font=("Arial, 14"))
button9.grid(row=3, column=2,  pady=5, padx=5)

button0= tk.Button(okno, text="0", command=lambda: dodaj_liczbe(0), width=12, height=1, font=("Arial, 14"))
button0.grid(row=4, column=0,  pady=5, padx=5, columnspan=2)

buttondot= tk.Button(okno, text=".", command=lambda: dodaj_liczbe("."), width=5, height=1, font=("Arial, 14"))
buttondot.grid(row=4, column=2,  pady=0, padx=5)

buttonplus= tk.Button(okno, text="+", command=lambda: dodaj_liczbe("+"), width=5, height=1, font=("Arial, 14"))
buttonplus.grid(row=1, column=3,  pady=5, padx=0)

buttonmin= tk.Button(okno, text="-", command=lambda: dodaj_liczbe("-"), width=5, height=1, font=("Arial, 14"))
buttonmin.grid(row=1, column=4,  pady=5, padx=5)

buttonmul= tk.Button(okno, text="*", command=lambda: dodaj_liczbe("*"), width=5, height=1, font=("Arial, 14"))
buttonmul.grid(row=2, column=3,  pady=5, padx=0)

buttondiv= tk.Button(okno, text="/", command=lambda: dodaj_liczbe("/"), width=5, height=1, font=("Arial, 14"))
buttondiv.grid(row=2, column=4,  pady=5, padx=5)

buttonmul2= tk.Button(okno, text="**", command=lambda: dodaj_liczbe("**"), width=5, height=1, font=("Arial, 14"))
buttonmul2.grid(row=3, column=3,  pady=5, padx=0)

buttondiv2= tk.Button(okno, text="//", width=5, command=lambda: dodaj_liczbe("//"), height=1, font=("Arial, 14"))
buttondiv2.grid(row=3, column=4,  pady=5, padx=5)

buttonotw= tk.Button(okno, text="(", width=5, command=lambda: dodaj_liczbe("("), height=1, font=("Arial, 14"))
buttonotw.grid(row=4, column=3,  pady=5, padx=0)

buttonzam= tk.Button(okno, text=")", command=lambda: dodaj_liczbe(")"), width=5, height=1, font=("Arial, 14"))
buttonzam.grid(row=4, column=4,  pady=5, padx=5)

buttonclear= tk.Button(okno, text="CLEAR", command= wyczysc, width=12, height=1, font=("Arial, 14"))
buttonclear.grid(row=5, column=0,  pady=5, padx=5, columnspan=2)

buttonenter= tk.Button(okno, text="ENTER", command= oblicz, width=18, height=1, font=("Arial, 14"))
buttonenter.grid(row=5, column=2,  pady=5, padx=5, columnspan=4)

okno.mainloop()
