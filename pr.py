import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('DESA.csv')

"""Explicación del contexto:
    CSV, el cual registra los Desfibriladores semiautomáticos externos situados fuera del ámbito sanitario en la comunidad de galicia.

    Explicar las columnas:
    vcodequipo(Número del dispositivo), solicitante(El establecimiento que lo solicita), ubicacion(Nombre de establecimiento donde se encuentra el dispositivo), 
    municipio(Donde se encuentra el dispositivo), provincia(Donde se encuentra el dispositivo), lat(Latitud de la ubicación del dispositivo), 
    lon(Longitud de la ubicación del dispositivo), tipoInstalacion(Tipo de establecimiento donde se encuentra el dispositivo)
"""
#Cuántas filas hay
num_filas = len(df)
print(f'Número de filas en el dataset: {num_filas}')
#Se muestra la cantidad de filas en el conjunto de datos.

nas_por_columna = df.isna().sum()
print('Valores faltantes por columna:')
print(nas_por_columna)
#Se analizan los valores faltantes en cada columna del conjunto de datos.

#Outliers e inconsistencias

df_interes=df[df['provincia']== 'PONTEVEDRA']
print(df_interes)
#Se filtran los datos para la provincia de Pontevedra y se muestra el DataFrame resultante.

#Guarda el dataframe arreglado en un archivo CSV nuevo
df_interes.to_csv('equipos_pontevedra.csv',index=False)
#Se guarda el DataFrame filtrado en un archivo CSV llamado 'equipos_pontevedra.csv'.


# Preguntas
#1 ¿Cuál es la distribución geográfica de los equipos en la provincia de Pontevedra?

# Graficar la distribución geográfica
plt.scatter(df['lon'],df['lat'], color='#48bfe3')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Distribució Geográfica de Equipos')
plt.savefig('distribusion_geografica.png')
#Se genera un gráfico de dispersión para visualizar la distribución geográfica de los equipos en Pontevedra y se guarda como 'distribucion_geografica.png'.

#2 ¿Cuál es la cantidad de equipos por tipo de instalación?

# Graficar la cantidad de equipos por tipo de instalación
sns.countplot(data=df, x='tipoInstalacion', color='#72efdd')
plt.xticks(rotation=90)
plt.xlabel('Tipo de Instalación')
plt.xlabel('Cantidad de Equipos')
plt.xlabel('Cantidad de Equipos por Tipo de Instalación')
plt.savefig('equipos_por_tipo.png')
#Se crea un gráfico de barras para mostrar la cantidad de equipos por tipo de instalación y se guarda como 'equipos_por_tipo.png'.

#3 ¿Cuál es la ubicación con mayor concentración de equipos?

# Encontrar la ubicación con mayor concentración de equipos
ubicacion_con_mas_equipos = df['ubicacion'].value_counts().idxmax()
print(f'Ubicación con más equipos: {ubicacion_con_mas_equipos}')
#Se identifica la ubicación con la mayor concentración de equipos y se muestra en la salida.