from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkscrolledframe import ScrolledFrame
from PIL import Image, ImageTk

import requests
from googletrans import Translator

# Definição das Cores
cor_de_fundo = "#f2f2f2" # Gelo
cor_texto = "#333333" # Cinza escuro
cor_destaque = "#1976D2" #Azul

janela = Tk()
janela.title("PyNews")
janela.geometry("612x600")
janela.configure(bg=cor_de_fundo)
janela.resizable(width=FALSE, height=FALSE)

# Divisoes da janela
frameCima = Frame(janela, width=612, height=55, bg=cor_de_fundo, relief="flat")
frameCima.grid(row=0, column=0, sticky=NSEW)

frameMeio = Frame(janela, width=590, height=50, bg=cor_de_fundo, relief="solid")
frameMeio.grid(row=1, column=0, sticky=NSEW)

frameBaixo = Frame(janela, width=590, height=450, bg=cor_de_fundo, relief="raised")
frameBaixo.grid(row=2, column=0, sticky=NSEW)

# Criando o Scroll
sf = ScrolledFrame(frameBaixo, width=590, height=450, bg=cor_de_fundo)
sf.grid(row=0, column=0, sticky=NSEW, padx=0, pady=5)
frameCanva = sf.display_widget(Frame, bg=cor_texto)

# Criando Logo
app_img = Image.open('imgs/news.png')
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=cor_de_fundo, fg=cor_destaque)
app_logo.place(x=5, y=8)
app_Titulo = Label(frameCima, text="PyNews", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 17 bold'), bg=cor_de_fundo, fg=cor_destaque)
app_Titulo.place(x=55, y=10)
app_Linha = Label(frameCima, width=612, relief=GROOVE, anchor=NW, font=('Verdana 1') , bg=cor_de_fundo, fg=cor_destaque)
app_Linha.place(x=-5, y=52)

# Criando a interface de procura


janela.mainloop()