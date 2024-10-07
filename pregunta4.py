import pandas as pd
from sklearn.preprocessing import Normalizer, StandardScaler # Import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import KBinsDiscretizer

print("############################################             Antes de label encoder")
print()
df  = pd.read_csv('pdf_malware.csv')
df_original = df.copy()
print(df)
label_encoder = LabelEncoder()
df['Text'] = label_encoder.fit_transform(df['Text'])
df['Class'] = label_encoder.fit_transform(df['Class'])
df['FileName'] = label_encoder.fit_transform(df['FileName'])
print("##########################################               Despues de label encoder")
print()
print(df)
#metodos = [('normalizar',Normalizer()),('escalado',StandardScaler())]
#tuberia = Pipeline(metodos)
#for i in range(2):
#  print(tuberia[i].fit_transform(df['Text']))
df = df_original
print("############################################             Antes de one hot")
print(df)
df_encoded = pd.get_dummies(df, columns =['Text','Class','FileName'])
print("##########################################               Despues de one hot")
print(df_encoded)


print("############################################             Antes de Normalizer")
normalizer = Normalizer(norm='l2')
#print(df.columns)
columnas = ['PdfSize','MetadataSize','Pages','XrefLength','TitleCharacters','isEncrypted','EmbeddedFiles','Images','PageNo']
print(df)
print("##########################################               Despues de Normalizer")
df_normalized = normalizer.fit_transform(df[columnas])
df[columnas] = df_normalized
print(df)


print("############################################             Antes de Discretizar")
df = df_original
scaler = StandardScaler()
columnas = ['PdfSize','MetadataSize','Pages','XrefLength','TitleCharacters','isEncrypted','EmbeddedFiles','Images','PageNo']
print(df)
print("##########################################               Despues de Discretizar")
df_scaler = scaler.fit_transform(df[columnas])
df[columnas] = df_scaler
print(df)
#print(preprocesamiento.fit_transform(df['PdfSize']))
#print(preprocesamiento.fit_transform(df['MetadataSize']))
#print(preprocesamiento.fit_transform(df['Pages']))
#print(preprocesamiento.fit_transform(df['XrefLength']))
#print(preprocesamiento.fit_transform(df['TitleCharacters']))
#print(preprocesamiento.fit_transform(df['isEncrypted']))
#print(preprocesamiento.fit_transform(df['EmbeddedFiles']))
#print(preprocesamiento.fit_transform(df['Images']))
#print(preprocesamiento.fit_transform(df['PagesNo']))
