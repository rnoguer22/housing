import pandas as pd
import matplotlib.pyplot as plt 

class Grafico:
    #Constructor
    def __init__(self, archivo, col1, col2):
        self.archivo = archivo
        self.col1 = col1
        self.col2 = col2
    