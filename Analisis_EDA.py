import pandas as pd
import matplotlib.pyplot as plt 

class Grafico:
    #Constructor
    def __init__(self, archivo, col1, col2):
        self.archivo = archivo
        self.col1 = col1
        self.col2 = col2
        self.dt = pd.read_csv(archivo)
    
    def grafico(self, tipo_grafico):
        fig, ax = plt.subplots()
        if tipo_grafico == "dispersion":
            ax.scatter(self.dt[self.col1], self.dt[self.col2])
        else:
            self.dt.plot(kind = tipo_grafico, ax = ax)
        ax.set_title('Grafico ' + tipo_grafico, loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel('')
        plt.savefig('Graficos/grafico' + ' - '.join(tipo_grafico) + '.png', bbox_inches='tight')