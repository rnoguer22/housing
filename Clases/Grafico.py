import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import pyplot
import numpy as np

class Grafico:
    #Constructor
    def __init__(self, archivo):
        self.archivo = archivo
        self.dt = pd.read_csv(archivo)
    
    def grafico(self, tipo_grafico, col1, col2):

        def pearson():
            correl = np.corrcoef(self.dt[col1], self.dt[col2])
            correlacion = round(correl[0][1], 3)
            return correlacion
    
        print("Generando Grafico...")
        print("El coeficiente de correlacion de Pearson es {}".format(pearson()))

        fig, ax = plt.subplots()
        if tipo_grafico == "dispersion":
            ax.scatter(self.dt[col1], self.dt[col2])
        else:
            self.dt.groupby(col1)[col2].sum().plot(kind = tipo_grafico, ax = ax)
        ax.set_title('Grafico ' + tipo_grafico, loc = "center", fontdict = {'fontsize':14, 
        'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel('')
        plt.savefig('Graficos/grafico' + ' - '+ tipo_grafico + col1 + col2 + '.png', bbox_inches='tight')