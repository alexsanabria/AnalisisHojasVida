import nltk
from nltk.corpus import stopwords
import re
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('stopwords')
stopwords_sp = stopwords.words('spanish')
stopwords_en = stopwords.words('english')
spanishStemmer=SnowballStemmer("spanish")


texto="Hola a todos mis queridos amigos del facebook"

def preProcesador(texto):
    texto=texto.lower()
    texto=texto.split()
    for palabra in texto:             #Recorrer el array
        if '@' in palabra:# Identificar los mails buscando las palabras que contienen "@", para borrarlos                                        
            index=texto.index(palabra)    #Captura el indice donde se encuentra el correo
            texto.pop(index)
    texto=' '.join(texto)               #Volver a generar un string con las palabras
    texto=re.sub(r"[^a-zA-Z'áéíóúñ\s]", " ", texto) # Dejar solo letras
    texto=texto.split()                 # crear array con las palabras
    texto=[palabra for palabra in texto if palabra not in stopwords_sp] # Eliminar palabras vacias
    texto=[palabra for palabra in texto if palabra not in stopwords_en]
    texto=" ".join(texto)
    return texto



def imprimir():
    return "Hola desde el preprocesador"