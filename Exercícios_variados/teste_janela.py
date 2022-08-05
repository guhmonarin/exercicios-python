from tkinter import*
janela = Tk()
janela.title("Olá mundo")
janela.geometry('300x200')

label = Label(janela, text="Primeiro botao")
label.grid(column=0, row=0)


def ola():
    print("Ola Mundo, eu sou Angolano")
    label.configure(text="Olá Mundo, eu sou Angolano !!")


bot = Button(janela, text="Clica aqui", command=ola)
bot.grid(column=1, row=0)

janela.mainloop()