import matplotlib.pyplot as plt
import tkinter as tk



# estruture no tkinter um sistema de visualização através do clique, MOSTRE:
# METRICAS
# GRAFICO DE BARRAS


def grafico():
    pib=[150,300,500,800,150,300,900]
    estados=['SP','RS','BA','PE','ES','MT','MS']
    plt.bar(estados, pib)
    plt.title('PIB DOS ESTADOS')
    plt.xlabel(estados)
    plt.ylabel(pib)
    plt.show()

janela = tk.Tk()
janela.geometry('300x300')
janela.title('PIB DOS ESTADOS')

btn1 = tk.Button(janela, text='Grafico', command=grafico)
btn1.pack(pady=30)

janela.mainloop()