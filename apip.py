#!/usr/bin/python
from flask import Flask, request
from m09_model_P2 import predict_precio

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def preciopredict():
    return {
         "result": predict_precio(request.args.get('feat'))
        }, 200


@app.route('/hola', methods=['GET'])
def hola():
    return {
         "result": "todo bien"
        }, 200


@app.route('/nombre', methods=['GET'])
def nombre():
    return {
         "nombre": request.args.get('NOMBRE'),
         "apellido": request.args.get('APELLIDO')
        }, 200


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)

