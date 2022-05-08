# housing

[Pinche aqui para acceder al link de este repositorio](https://github.com/rnoguer22/housing.git)

---

*Queda resuelta la tarea "EDA sobre dataset USA_Housing" del portal de la asignatura. Para ello hemos hecho uso de librerias para generar graficos (matplotlib) y para trabajar con el propio dataset se ha hecho uso de pandas, todo ello utilizando la programacion orientada a objetos de python (POO).*

---

## Indice
### Clases
* [Grafico](#1)
### Graficos
* [grafico - dispersionArea PopulationPrice](#2)
* [grafico - dispersionAvg  Area IncomeAvg  Area Number of Rooms](#3)
* [grafico - dispersionAvg  Area IncomePrice](#4)
* [grafico - dispersionAvg  Area Number of RoomsPrice](#5)

---

## Grafico.py<a name="1"></a>
```python3
import pandas as pd
import matplotlib.pyplot as plt
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
            plt.scatter(self.dt[col1], self.dt[col2])
        else:
            self.dt.groupby(col1)[col2].sum().plot(kind = tipo_grafico, ax = ax)
        ax.set_title('Grafico ' + tipo_grafico, loc = "center", fontdict = {'fontsize':14, 
        'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel('')
        plt.savefig('Graficos/grafico' + ' - '+ tipo_grafico + col1 + col2 + '.png', bbox_inches='tight')
```

---

## grafico - dispersionArea PopulationPrice<a name="2"></a>

Podemos observar que la correlacion es alta, por lo que estara proxima a 1

![grafico - dispersionArea PopulationPrice](https://user-images.githubusercontent.com/91721762/167291350-db33065a-a84f-425d-a8ec-2c55ea4755ab.png)

---

## grafico - dispersionAvg  Area IncomeAvg  Area Number of Rooms<a name="3"></a>

En este caso podemos observar que la correlacion esta proxima al valor 0, ya que los datos no estan relacionados

![grafico - dispersionAvg  Area IncomeAvg  Area Number of Rooms](https://user-images.githubusercontent.com/91721762/167291375-6508d21c-7308-44c8-8efd-f31aa9537c0d.png)

---

## grafico - dispersionAvg  Area IncomePrice<a name="4"></a>

Podemos observar que la correlacion es alta, por lo que estara proxima a 1

![grafico - dispersionAvg  Area IncomePrice](https://user-images.githubusercontent.com/91721762/167291429-4e050350-035d-4b14-aeb9-4a1bd36c014e.png)

---

## grafico - dispersionAvg  Area Number of RoomsPrice<a name="5"></a>

Podemos observar que la correlacion es alta, por lo que estara proxima a 1

![grafico - dispersionAvg  Area Number of RoomsPrice](https://user-images.githubusercontent.com/91721762/167291465-b31a0323-2bf5-493e-9c41-711a31786e4a.png)

---
