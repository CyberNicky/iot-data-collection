import requests
import json
import time

# Função para coletar dados do sensor


def ler_sensor():
    # Código para ler o sensor e retornar os dados coletados
    temperatura = 25.5
    umidade = 60.2
    return temperatura, umidade

# Função para enviar dados para o server


def enviar_dados(temperatura, umidade):
    url = "http://127.0.0.1:5000"
    dados = {
        "temperatura": temperatura,
        "umidade": umidade
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(dados), headers=headers)
    if response.status_code == 200:
        print("Dados enviados com sucesso!")
    else:
        print("Falha ao enviar dados.")


# Loop principal
while True:
    # Ler os dados do sensor
    temperatura, umidade = ler_sensor()

    # Enviar os dados para o servidor
    enviar_dados(temperatura, umidade)

    # Aguardar um intervalo de tempo (por exemplo, 1 minuto)
    time.sleep(60)
