import pandas as pd
import io
from google.colab import files

uploaded = files.upload ()

DataFrame = pd.read_csv(io.StringIO(uploaded['titanic.csv'].decode('latin-1')))

DataFrame
#Muestra la froma de un conjunto de datos usando shape
DataFrame.shape

print(len(DataFrame))

print(DataFrame.shape[1])

#Tipos de datos
DataFrame.dtypes

#Para ver las primeras 5 filas del dataframe
DataFrame.head()

#Para ver las ultimas filas de dataframe
DataFrame.tail()

#Especificar la columna nombre
DataFrame[['Nombre', 'Edad']]

DataFrame['Nombre']

DataFrame.Edad

DataFrame['Nombre']=DataFrame['Nombre'].str.upper()
DataFrame
