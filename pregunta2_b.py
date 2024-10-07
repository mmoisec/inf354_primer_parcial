import matplotlib
from scipy import stats
import seaborn as sns
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import pandas as pd
def interpolacion(index,data):
    index = index - 1
    if index.is_integer():
            return data[int(index)]
    else:
        parte_entera = int(index)
        parte_decimal = index - parte_entera
        valor_bajo = data[parte_entera]
        valor_alto = data[parte_entera + 1]

        return valor_bajo + parte_decimal * (valor_alto - valor_bajo)

def get_percentil(data,k,nombre):
    n = len(data)
    sorted_data = sorted(data)
    index = k * n
    print(nombre)
    print(' ',"Percentil: ",interpolacion(index,data))

def get_cuartil(data,nombre):
    n = len(data)
    sorted_data = sorted(data)
    primer_cuartil = 1/4 * (n)
    segundo_cuartil = 1/2 * (n)
    tercer_cuartil = 3/4 * (n)
    print(nombre)   
    print(' ',"Primer cuartil: ",primer_cuartil," ",interpolacion(primer_cuartil,sorted_data))
    print(' ',"Segundo cuartil: ",segundo_cuartil," ",interpolacion(segundo_cuartil,sorted_data))
    print(' ',"Tercer cuartil: ",tercer_cuartil," ",interpolacion(tercer_cuartil,sorted_data))

def plot_histogram(data, bins=30, title='Histograma', xlabel='Valores', ylabel='Frecuencia', color='blue'):
    plt.figure(figsize=(10, 6))  # Tamaño de la figura
    plt.hist(data, bins=bins, color=color, alpha=0.7, edgecolor='black')  # Crear el histograma
    plt.title(title)  # Título del histograma
    plt.xlabel(xlabel)  # Etiqueta del eje X
    plt.ylabel(ylabel)  # Etiqueta del eje Y
    plt.grid(axis='y', alpha=0.75)  # Activar la cuadrícula solo en el eje Y
    plt.show()  # Mostrar el histograma

def plot_heatmap(data, cmap='coolwarm', annot=True, title='Mapa de Calor', xlabel='Columnas', ylabel='Filas'):
    """
    Función para graficar un mapa de calor a partir de un array.

    Parámetros:
    - data: array o matriz de datos (2D)
    - cmap: paleta de colores para el mapa de calor (por defecto 'coolwarm')
    - annot: si se deben mostrar los valores en las celdas (por defecto True)
    - title: título del mapa de calor (por defecto 'Mapa de Calor')
    - xlabel: etiqueta del eje X (por defecto 'Columnas')
    - ylabel: etiqueta del eje Y (por defecto 'Filas')
    """
    plt.figure(figsize=(10, 8))  # Tamaño de la figura
    sns.heatmap(data, cmap=cmap, annot=annot, linewidths=0.5)  # Crear el mapa de calor
    
    plt.title(title)  # Título del mapa de calor
    plt.xlabel(xlabel)  # Etiqueta del eje X
    plt.ylabel(ylabel)  # Etiqueta del eje Y
    plt.show()  # Mostrar el gráfico


file_path = './pdf_malware.csv'
data = pd.read_csv(file_path, names=['FileName','PdfSize','MetadataSize','Pages','XrefLength','TitleCharacters',"isEncrypted",'EmbeddedFiles', "Images", "Text", "PageNo", "Class"],index_col=False,skiprows=1)

get_percentil(data['PdfSize'].tolist(),0.25,'PdfSize')
get_percentil(data['MetadataSize'].tolist(),0.25,"MetadataSize")
get_percentil(data['Pages'].tolist(),0.25,"Pages")
get_percentil(data['XrefLength'].tolist(),0.25,"XrefLength")
get_percentil(data['TitleCharacters'].tolist(),0.25,"TitleCharacters")
get_percentil(data['EmbeddedFiles'].tolist(),0.25,"EmbeddedFiles")
get_percentil(data['Images'].tolist(),0.25,"Images")
get_percentil(data['PageNo'].tolist(),0.25,"PageNo")

get_cuartil(data['PdfSize'].tolist(),"PdfSize")
get_cuartil(data['MetadataSize'].tolist(),"MetadataSize")
get_cuartil(data['Pages'].tolist(),"Pages")
get_cuartil(data['XrefLength'].tolist(),"XrefLength")
get_cuartil(data['TitleCharacters'].tolist(),"TitleCharacters")
get_cuartil(data['EmbeddedFiles'].tolist(),"EmbeddedFiles")
get_cuartil(data['Images'].tolist(),"Images")
get_cuartil(data['PageNo'].tolist(),"PageNo")


binsN = 1000
#plot_histogram(data['PdfSize'].tolist(), bins=binsN, title='Histograma de PdfSize', xlabel='Valores', ylabel='Frecuencia', color='cyan')
#plot_histogram(data['MetadataSize'].tolist(), bins=binsN, title='Histograma de PdfSize', xlabel='Valores', ylabel='Frecuencia', color='cyan')
#plot_histogram(data['Pages'].tolist(), bins=binsN, title='Histograma de Pages', xlabel='Valores', ylabel='Frecuencia', color='cyan')
#plot_histogram(data['XrefLength'].tolist(), bins=binsN, title='Histograma de XrefLength', xlabel='Valores', ylabel='Frecuencia', color='cyan')
#plot_histogram(data['TitleCharacters'].tolist(), bins=binsN, title='Histograma de TitleCharacters', xlabel='Valores', ylabel='Frecuencia', color='cyan')
#plot_histogram(data['EmbeddedFiles'].tolist(), bins=binsN, title='Histograma de EmbeddedFiles', xlabel='Valores', ylabel='Frecuencia', color='cyan')
#plot_histogram(data['Images'].tolist(), bins=binsN, title='Histograma de Images', xlabel='Valores', ylabel='Frecuencia', color='cyan')
###################
plot_histogram(data['PageNo'].tolist(), bins=binsN, title='Histograma de PageNo', xlabel='Valores', ylabel='Frecuencia', color='cyan')



#b) De al menos tres columnas seleccionadas por usted indique que datos son relevantes de estas, grafique la misma (puede ser dispersión o mapa de calor, otros), indique al menos 4 características por columna seleccionada.
selected_columns = data[['PdfSize','MetadataSize','Pages']]
print(selected_columns)
plt.figure(figsize=(8,6))
sns.heatmap(selected_columns.corr(), annot=True)
plt.title("Mapa de de calor de 3 columnas")
plt.show()


#c) Obteniendo la media, mediana, moda con el uso de librerías, grafique un diagrama de cajas-bigote de al menos 3 columnas. Explique el resultado.
media = selected_columns.mean()

mediana = selected_columns.median()

moda = selected_columns.apply(lambda x: stats.mode(x))  

print("Media:\n", media)
print("\nMediana:\n", mediana)
print("\nModa:\n", moda)


