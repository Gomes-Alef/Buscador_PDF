from tkinter import *
from tkinter import ttk

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.entryArquivo.delete(0, END)
        self.entryPalavrasChave.delete(0, END)

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.result_frame2()
        root.mainloop()
    def tela(self):
        self.root.title("Buscador de palavras PDF - Inovação MTEC")
        self.root.configure(background='#273f4b')
        self.root.geometry("640x480")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=640, height=480)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg='#bbbbbb',
                             highlightbackground='#2e5169', highlightthickness=2.5)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#bbbbbb',
                             highlightbackground='#2e5169', highlightthickness=2.5)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):

        ##Label arquivo PDF
        self.lb_carregarArquivo = Label(self.frame_1, text="Arquivo PDF:", bg='#1d7881',
                                        fg='#d2dde0', font=('Helvetica', 11, 'bold'))
        self.lb_carregarArquivo.place(relx=0.03, rely=0.1, relwidth=0.16, relheight=0.13)

        ##Entry arquivo PDF
        self.entryArquivo = Entry(self.frame_1, bg='#d2dde0',
                                  highlightbackground='#1d7881', highlightthickness=1.5, font=('Helvetica', 11))
        self.entryArquivo.place(relx=0.19, rely=0.1, relwidth=0.5, relheight=0.13)

        ##Label palavras-chave
        self.lb_palavrasChave = Label(self.frame_1, text="Palavras:", bg='#1d7881',
                                        fg='#d2dde0', font=('Helvetica', 11, 'bold'))
        self.lb_palavrasChave.place(relx=0.03, rely=0.28, relwidth=0.16, relheight=0.13)

        ##Entry palavras-chave
        self.entryPalavrasChave = Entry(self.frame_1, bg='#d2dde0',
                                  highlightbackground='#1d7881', highlightthickness=1.5, font=('Helvetica', 11))
        self.entryPalavrasChave.place(relx=0.19, rely=0.28, relwidth=0.5, relheight=0.13)

        ##Butão de busca
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2.5, bg='#1d7881',
                                fg='#d2dde0', font=('Helvetica', 10, 'bold'))
        self.bt_buscar.place(relx=0.87, rely=0.1, relwidth=0.1, relheight=0.13)

        ##Butão de limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2.5, bg='#1d7881',
                                fg='#d2dde0', font=('Helvetica', 10, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.87, rely=0.28, relwidth=0.1, relheight=0.13)

    def result_frame2(self):
        self.resultadoBusca = ttk.Treeview(self.frame_2, height=1, columns=("col1"))
        self.resultadoBusca.heading("#0", text="Resultados:")
        self.resultadoBusca.column("#0", width=1)
        self.resultadoBusca.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.95)

        self.scroolResultado = Scrollbar(self.frame_2, orient='vertical')
        self.resultadoBusca.configure(yscrollcommand=self.scroolResultado.set)
        self.scroolResultado.place(relx=0.96, rely=0.02, relwidth=0.95, relheight=0.93)



Application()
