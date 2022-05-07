import pandas as pd
import matplotlib.pyplot as plt 

class Grafico:
    #Constructor
    def __init__(self, archivo):
        self.archivo = archivo
        self.dt = pd.read_csv(archivo)
    
    def grafico(self, tipo_grafico, col1, col2):
        print("Generando Grafico...")
        fig, ax = plt.subplots()
        if tipo_grafico == "dispersion":
            ax.scatter(self.dt[col1], self.dt[col2])
        else:
            self.dt.groupby(col1)[col2].plot(kind = tipo_grafico, ax = ax)
        ax.set_title('Grafico ' + tipo_grafico, loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel('')
        plt.savefig('Graficos/grafico' + ' - '.join(tipo_grafico) + '.png', bbox_inches='tight')

grafica = Grafico("Dataset housing/USA_Housing.csv")
grafica.grafico("bar","Area Population","Price")