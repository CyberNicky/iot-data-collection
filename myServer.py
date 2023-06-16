from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota criada para receber os dados enviados pelo dispositivo IoT


@app.route('/', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    temperatura = dados['temperatura']
    umidade = dados['umidade']

    return jsonify({'message': 'Dados recebidos com sucesso'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
