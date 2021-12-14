
from pymongo import MongoClient

client= MongoClient("localhost")


db= client["DiccionarioSlang"]

col = db['Diccionario']

#Creamos las funciones que manipularan las bases de datos

def insertar(a,b):
    diccionario_agg = ({'Palabra_Español':a,
                        'Palabra_Slang':b})
    col.insert_one(diccionario_agg)

def mostrarDatos():
    palabras = []
    for documentos in col.find({}):
        dicc = {}
        dicc['Palabra_Espanol'] = documentos['Palabra_Español']
        dicc['Palabra_Slang'] = documentos['Palabra_Slang']
        palabras.append(dicc)
    return palabras

def editarSignificado(PalabraV,SignificadoN):
    col.update_many({'Palabra_Español': PalabraV},{"$set": {"Palabra_Slang":SignificadoN}})

def eliminar(PalabraE):
    col.delete_one({'Palabra_Español': PalabraE})

def significadopalabra(palabrasig):
    palabra=[]
    for x in col.find({'Palabra_Español':palabrasig}):
        dicc = {}
        print(x)
        dicc['Palabra_Espanol'] = x['Palabra_Español']
        dicc['Palabra_Slang'] = x['Palabra_Slang']
        palabra.append(dicc)
        return palabra


print(significadopalabra('NOSE'))