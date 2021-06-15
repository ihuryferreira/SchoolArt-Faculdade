"""
ALUNO: IHURY E MANUEL

"""
import tkinter
from PIL import ImageTk
from menu import MenuRAD

  
class Application:
    def __init__(self):
        window = tkinter.Tk()
        window.minsize(1024, 1024)
        mb = MenuRAD(window)
        window.title('Sistema de Cadastro School (SISESC)')
        window.geometry('{}x{}+0+0'.format(*window.maxsize()))
        window.iconbitmap("Artc.ico")
        window.configure(background="#292826")
        imagem_ = ImageTk.PhotoImage(file="Arts.png")
        tkinter.Label(window, image=imagem_ ,bg='#292826',pady=0).place(x=475,y=110)
        window.mainloop()
        
if __name__ == '__main__':
    Application()