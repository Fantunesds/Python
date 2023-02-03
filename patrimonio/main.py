from tkinter import*
from tkinter import Tk, ttk
# importando pillow
from PIL import Image,ImageTk

#cores

co0 = "#2e2d2b" # Preto
co1 = "#feffff" # Branca
co2 = "#4fa882" # verde
co3 = "#38576b"  # valor
co4 = "#403d3d" # letra
co5 = "#e06636" #-profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # +verde
co9 = "#e9edf5" # +verde
co10 = "#6e8faf"
co11 = "#f2f4f2"


# criando janela

janela = Tk()
janela.title("")
janela.geometry("380x500")
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# Frames-------------------------------
frameCima = Frame(janela, width=380, height=50, bg=co1)
frameCima.grid(row=0, column=0, columnspan=2)

frameResultado = Frame(janela, width=380, height=50, bg=co3)
frameResultado.grid(row=1, column=0, pady=10)

frameBaixo = Frame(janela, width=380, height=400, bg=co1)
frameBaixo.grid(row=2, column=0, pady=10)

# dividindo framebaixo

frameAtivo = Frame(frameBaixo, width=180, height=370, bg=co9)
frameAtivo.grid(row=0, column=0, pady=5)

framePassivos = Frame(frameBaixo, width=180, height=370, bg=co9)
framePassivos.grid(row=0, column=1,)

# logo ---------------------

# abrindo img
app_img = Image.open('money.png')
app_img = app_img.resize((48,48))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text='Calculadora de patrimônio liquido',width=900, compound=LEFT, padx=5, anchor=NW,font=('ivy,12'), bg=co1, fg=co4)
app_.place(x=55,y=0)

l_linha = Label(frameCima, width=300, anchor=NW,font=('Verdana'), bg=co3, fg=co1)
l_linha.place(x=0,y=47)

# funçao patrimonio liquido
def calcular():
    # Obtendo os valores ativos
    ativo_1 = e_valor_casa.get()
    ativo_2 = e_valor_imoveis.get()
    ativo_3 = e_valor_veiculos.get()
    ativo_4 = e_valor_investimentos.get()
    ativo_5 = e_valor_outros.get()

    # Obtendo valores Passivos
    passivo_1 = e_valor_hipoteca.get()
    passivo_2 = e_valor_carro.get()
    passivo_3 = e_valor_estudante.get()
    passivo_4 = e_valor_dividas.get()

    # verificando entrada se estão vazias
    if ativo_1=='' or ativo_2=='' or ativo_3=='' or ativo_4=='' or ativo_5=='' or passivo_1=='' or passivo_2=='' or passivo_3=='' or passivo_4=='':
        print("Preencha os campos vazios")
        return
    else:
        #calculando total de arivos
        Total_ativos = float(ativo_1) + float(ativo_2) + float(ativo_3) + float(ativo_4) + float(ativo_5)

        #calculando total passivos
        Total_passivo = float(passivo_1) + float(passivo_2) + float(passivo_3) + float(passivo_4)

        # calculando o patrimonio liquido
        Patrimonio_liquido = Total_ativos - Total_passivo

        l_resultado['text'] = 'R${:,.2f}'.format(Patrimonio_liquido)





# Entrando Ativos--------------------------------------
l_nome = Label(frameAtivo, text='Entrada de Ativos', padx=10, width=35, height=1,anchor=NW, font=('verdana 11'),bg=co2,fg=co1)
l_nome.place(x=0,y=0)

# valor da casa
l_nome = Label(frameAtivo, text='Valor casa', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=40)
e_valor_casa = Entry(frameAtivo,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_casa.place(x=10,y=65)

# valor da imoveis
l_nome = Label(frameAtivo, text='Imóveis', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=105)
e_valor_imoveis = Entry(frameAtivo,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_imoveis.place(x=10,y=125)

# veiculos
l_nome = Label(frameAtivo, text='Veiculos', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=165)
e_valor_veiculos = Entry(frameAtivo,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_veiculos.place(x=10,y=195)

# Ivestimentos
l_nome = Label(frameAtivo, text='Investimentos', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=230)
e_valor_investimentos = Entry(frameAtivo,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_investimentos.place(x=10,y=255)

# Outros ativos
l_nome = Label(frameAtivo, text='Outros Ativos', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=295)
e_valor_outros = Entry(frameAtivo,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_outros.place(x=10,y=315)

# Entrando Passivos--------------------------------------
l_nome = Label(framePassivos, text='Entrada de Passivos', padx=10, width=35, height=1,anchor=NW, font=('verdana 11'),bg=co5,fg=co1)
l_nome.place(x=0,y=0)

# Ipoteca
l_nome = Label(framePassivos, text='Hipoteca', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=40)
e_valor_hipoteca = Entry(framePassivos,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_hipoteca.place(x=10,y=65)

# Emprestimo de carros
l_nome = Label(framePassivos, text='Emprestimo de carros', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=105)
e_valor_carro = Entry(framePassivos,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_carro.place(x=10,y=125)

# Emprestimo Faculdade
l_nome = Label(framePassivos, text='Emprestimo Faculdade', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=165)
e_valor_estudante = Entry(framePassivos,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_estudante.place(x=10,y=195)

# Outra Dividas
l_nome = Label(framePassivos, text='Outras Dividas', anchor=E, font=('verdana 9'),bg=co9,fg=co0)
l_nome.place(x=10,y=230)
e_valor_dividas = Entry(framePassivos,width=10,font=('Ivy 12'),justify='center',relief='solid')
e_valor_dividas.place(x=10,y=255)

# Resultado-----------------------------

l_resultado = Label(frameResultado, text='R${:,.2f}'.format(00),padx=10,width=15, anchor=NE, font=('verdana 25 bold'),bg=co3,fg=co1)
l_resultado.place(x=0,y=7)

l_calcular = Button(framePassivos, command=calcular,text='Calcular'.upper(),padx=10,width=12, anchor=CENTER, font=('Ivy 9 bold'),bg=co1,fg=co0)
l_calcular.place(x=10,y=310)





janela.mainloop()
