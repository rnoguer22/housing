from Clases.Grafico import Grafico

if __name__ == "__main__":
    #Definimos grafica como instancia de la clase Grafico
    grafica = Grafico("Dataset housing/USA_Housing.csv")
    #Grafico para ver la relacion entre lo habitada que esta un area y su precio
    grafica.grafico("dispersion","Area Population","Price")
    #Grafico de dispersion para comparar el precio del area y el numero de dormitorios
    grafica.grafico("dispersion","Avg. Area Income","Avg. Area Number of Rooms")
    #A continuacion vamos a comparar el ingreso medio con el precio de la vivienda adquirida
    grafica.grafico("dispersion","Avg. Area Income","Price")
    #Aanalizamos el numero de dormitorios con el numero de habitaciones que tiene la vivienda
    grafica.grafico("dispersion","Avg. Area Number of Rooms","Avg. Area Number of Bedrooms")

    #Podemos observar que la correlacion corresponde a simple vista con cada grafico