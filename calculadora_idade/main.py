from tkinter import*
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date


janela = Tk()
janela.title("AGE CALENDAR")
janela.geometry('310x400')
janela.iconbitmap('idade.ico')
janela.resizable(width=FALSE,height=FALSE)

# cores
cor1 = '#696969' # DimGray
cor2 = '#808080' # Gray
cor3 = '#F0F8FF' # AliceBlue
cor4 = '#FFD700' # Gold

# funcao calcular idade

def calcular():
    inicial = cal_1.get()    
    termino = cal_2.get()

   

    # separando os valores 
    dia_1, mes_1, ano_1 =[int(f) for f in inicial.split('/')]
    data_inicial = date(ano_1,mes_1,dia_1)

    dia_2, mes_2, ano_2 =[int(f) for f in termino.split('/')]
    data_nascimento = date(ano_2,mes_2,dia_2) 

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias

    

    
    


    


# criando frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_cima.grid(row=0,column=0)

frame_baixo = Frame(janela, width=310, height=260, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_baixo.grid(row=1,column=0)

# Criando label frame cima
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=cor1, fg=cor3)
l_calculadora.place(x=0,y=30)

l_calculadora = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Ariel 35 bold'), bg=cor1, fg=cor4)
l_calculadora.place(x=0,y=70)

# Criando label frame baixo
l_data_inicial = Label(frame_baixo, text="Data inicial",  height=1, padx=0, relief='flat', anchor=NW, font=('Ivy 11'), bg=cor2, fg=cor4)
l_data_inicial.place(x=20,y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_patter='dd/mm/y', y=2023)
cal_1.place(x=170,y=30)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_patter='dd/mm/y', y=2023)
cal_2.place(x=170,y=70)

l_data_nascimento = Label(frame_baixo, text="Data de nascimento",  height=1, padx=0, relief='flat', anchor=NW, font=('Ivy 11'), bg=cor2, fg=cor4)
l_data_nascimento.place(x=20,y=70)

l_data_inicial = Label(frame_baixo, text="Data inicial",  height=1, padx=0, relief='flat', anchor=NW, font=('Ivy 11'), bg=cor2, fg=cor4)
l_data_inicial.place(x=20,y=30)

l_app_anos = Label(frame_baixo, text="--",  height=1, padx=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor4)
l_app_anos.place(x=55,y=135)
l_app_anos_nome = Label(frame_baixo, text="ANOS",  height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor4)
l_app_anos_nome.place(x=50,y=175)

l_app_meses = Label(frame_baixo, text="--",  height=1, padx=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor4)
l_app_meses.place(x=140,y=135)
l_app_meses_nome = Label(frame_baixo, text="MESES",  height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor4)
l_app_meses_nome.place(x=130,y=175)

l_app_dias = Label(frame_baixo, text="--",  height=1, padx=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor4)
l_app_dias.place(x=220,y=135)
l_app_dias_nome = Label(frame_baixo, text="DIAS",  height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor4)
l_app_dias_nome.place(x=210,y=175)


# criando botao calcular

b_calcular = Button(frame_baixo, command=calcular, text="CALCULAR", width=20, height=1,  relief='raised', overrelief='ridge', font=('Ivy 10 bold'), bg=cor2, fg=cor4)
b_calcular.place(x=60,y=225)












janela.mainloop()