import tkinter
from tkinter import*
from tkinter import ttk

# Importando o Pillow
from PIL import Image,ImageTk
import random

# cores_________________________________________________

co0 = "#FFFFFF" # white
co1 = "#333333" # branca
co2 = "#fcc058" # orange
co3 = "#38576b" # valor
co4 = "#3297a8" # azul
co5 = "#fff873" # amarelo
co6 = "#e85151" # vermelho
co7 = "#fcc058" # orange
co8 = "#34eb3d" # + verde
fundo = "#3b3b3b"

# criando janela

janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo janela

frame_cima = Frame(janela,width=260,height=100,bg=co1, relief='raised')
frame_cima.grid(row=0,column=0,sticky=NW)

frame_baixo = Frame(janela,width=260,height=300,bg=co0, relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame cima

app_1 = Label(frame_cima,text="Você",height=1,anchor='center',font=('ivy 10 bold'),bg=co1,fg=co0)
app_1.place(x=10,y=70)
app_1_linha = Label(frame_cima,text="",height=10,anchor='center',font=('Ivy 10 bold'),bg=co0,fg=co0)
app_1_linha.place(x=0,y=0)

app_1_pontos = Label(frame_cima,text="0",height=1,anchor='center',font=('ivy 30 bold'),bg=co1,fg=co0)
app_1_pontos.place(x=50,y=20)

app_= Label(frame_cima,text=":",height=1,anchor='center',font=('ivy 30 bold'),bg=co1,fg=co0)
app_.place(x=125,y=20)

app_2_pontos = Label(frame_cima,text="0",height=1,anchor='center',font=('ivy 30 bold'),bg=co1,fg=co0)
app_2_pontos.place(x=170,y=20)
app_2 = Label(frame_cima,text="Boot",height=1,anchor='center',font=('ivy 10 bold'),bg=co1,fg=co0)
app_2.place(x=205,y=70)
app_2_linha = Label(frame_cima,text="",height=10,anchor='center',font=('Ivy 10 bold'),bg=co0,fg=co0)
app_2_linha.place(x=255,y=0)

app_linha = Label(frame_cima,text="",width=255,anchor='center',font=('Ivy 1 bold'),bg=co0,fg=co0)
app_linha.place(x=0,y=95)

app_pc = Label(frame_baixo,text="",height=1,anchor='center',font=('Ivy 10 bold'),bg=co0,fg=co1)
app_pc.place(x=190,y=10)

global voce
global pc 
global rondas 
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rondas = 5



# Função Logica do jogo

def jogar(i):
    global rondas 
    global pontos_voce
    global pontos_pc

    if rondas > 0:
        print(rondas)
        opcoes = ['Pedra','Papel','Tesoura']
        pc = random.choice(opcoes)
        voce = i
        app_pc['text'] = pc
        app_pc['fg'] = co1

        # caso for igual
        if voce == 'Pedra' and pc == 'Pedra':
            print('Empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co5

        elif voce == 'Papel' and pc == 'Papel':
            print('Empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co5
        
        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co5
        # para Frente
        elif voce == 'Pedra' and pc == 'Papel':
            print('PC ganhou!!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co8
            app_linha['bg'] = co0
            pontos_pc += 10

        elif voce == 'Papel' and pc == 'Pedra':
            print('Você ganhou!!')
            app_1_linha['bg'] = co8
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_voce += 10
        
        elif voce == 'Papel' and pc == 'Tesoura':
            print('PC ganhou!!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co8
            app_linha['bg'] = co0
            pontos_pc += 10

        elif voce == 'Tesoura' and pc == 'Papel':
            print('Você ganhou!!')
            app_1_linha['bg'] = co8 
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_voce += 10

        elif voce == 'Tesoura' and pc == 'Pedra':
            print('PC ganhou!!')
            app_1_linha['bg'] = co0 
            app_2_linha['bg'] = co8
            app_linha['bg'] = co0
            pontos_pc += 10

            

        elif voce == 'Pedra' and pc == 'Tesoura':
            print('Você ganhou!!')
            app_1_linha['bg'] = co8 
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_voce += 10
        # Atualizando os pontos
        app_1_pontos ['text'] = pontos_voce
        app_2_pontos ['text'] = pontos_pc

        # atualizando o numero de rondas
        rondas -=1

        
    else:
        fim_do_jogo()






# Função iniciar jogo

# configurando framebaixo

def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('img/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo,command=lambda:jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15,y=60)

    icon_2 = Image.open('img/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo,command=lambda:jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95,y=60)

    icon_3 = Image.open('img/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo,command=lambda:jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170,y=60)








# terminar o jogo

def fim_do_jogo():
    global rondas 
    global pontos_voce
    global pontos_pc
    
    # reiniciando as variaveis para zero
    pontos_voce = 0
    pontos_pc = 0
    rondas = 5

    # destruindo os botoes de opções
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    # definindo o vencedor
    jogodor_voce = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    if jogodor_voce > jogador_pc:
        app_vencedor = Label(frame_baixo,text="VICTORY!!!",height=1,anchor='center',font=('Ivy 30 bold'),bg=co0,fg=co8)
        app_vencedor.place(x=5,y=60)
    elif jogodor_voce < jogador_pc:
        app_vencedor = Label(frame_baixo,text="LOSER",height=1,anchor='center',font=('Ivy 30 bold'),bg=co0,fg=co6)
        app_vencedor.place(x=5,y=60)
    else:
        app_vencedor = Label(frame_baixo,text="EMPATE",height=1,anchor='center',font=('Ivy 30 bold'),bg=co0,fg=co2)
        app_vencedor.place(x=5,y=60)


    def jogar_denovo():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()

        b_jogar_denovo.destroy()

        iniciar_jogo()


    b_jogar_denovo = Button(frame_baixo,command=jogar_denovo, width=30, text='Jogar denovo',  bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5,y=151)







b_jogar = Button(frame_baixo,command=iniciar_jogo, width=30, text='Jogar',  bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5,y=151)
































janela.mainloop()