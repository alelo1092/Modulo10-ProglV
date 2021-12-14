from flask import Flask,jsonify,request
from bd import mostrarDatos, significadopalabra,editarSignificado,insertar,eliminar
app = Flask(__name__)


## Entrega de datos

@app.route('/palabras')
def obtenerpalabras():
    a = mostrarDatos()
    return jsonify(a)

@app.route('/palabras/<string:Palabra_Espanol>',methods =['GET'])
def get(Palabra_Espanol):
     a = significadopalabra(Palabra_Espanol)
     if a!=None:
         return jsonify(a)
     else:
         return jsonify({"message":'Palabra No encontrada'})

@app.route('/palabras',methods=['POST'])
def addpalabra():
     a=request.json['Palabra_Español']
     b = request.json["Palabra_Slang"]
     insertar(a,b)
     a = mostrarDatos()
     return jsonify({'message ':'Palabra añadida correctamente',"Palabras":a})

@app.route('/palabras/<string:Palabra_Espanol>',methods =['PUT'])
def editsignificado(Palabra_Espanol):
    a = significadopalabra(Palabra_Espanol)
    if a!=None:
        PalabraV = request.json['Palabra_Español']
        SignificadoN= request.json['Palabra_Slang']
        editarSignificado(PalabraV,SignificadoN)
        return jsonify({"message":'Palabra Modificada Correctamente'})
    else:
         return jsonify({"message":'Palabra No encontrada'})

@app.route('/palabras/<string:Palabra_Espanol>',methods=['DELETE'])
def deleteProduct(Palabra_Espanol):
    a = significadopalabra(Palabra_Espanol)
    if a!=None:
        PalabraE = request.json['Palabra_Español']
        eliminar(PalabraE)
        a = mostrarDatos()
        return jsonify({"message":'Palabra Eliminada Correctamente',"Palabras":a})
    else:
         return jsonify({"message":'Palabra No encontrada'})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
