# IoT Data Collection

Este é um projeto de exemplo que demonstra a coleta e transmissão de dados de sensores de um dispositivo IoT para um servidor.

## Descrição

Foi um trabalho de Faculdade que me interessou bastante e fiquei feliz em desenvolve-lo.

O objetivo deste projeto é simular um dispositivo IoT que coleta informações de sensores, como temperatura e umidade, e envia esses dados para um servidor para processamento adicional. Ele consiste em dois componentes principais: o código do dispositivo IoT e o servidor Flask.

- O código do dispositivo IoT (localizado na pasta "dispositivo-iot") simula a leitura dos dados de sensores. Neste exemplo, ele retorna valores fixos para a temperatura e umidade, mas você pode substituir esse código pela lógica real de leitura dos dados do seu sensor.
- O servidor Flask (localizado na pasta "servidor-flask") é responsável por receber as informações enviadas pelo dispositivo IoT. Quando o dispositivo IoT faz uma solicitação POST para a rota principal, o servidor recebe os dados e pode realizar ações adicionais com base nesses dados.

## Configuração

### Requisitos

- Python 3.x
- Bibliotecas Python: `Flask`, `requests`

### Instalação

1. Clone este repositório em sua máquina local:

git clone https://github.com/seu-usuario/iot-data-collection.git


2. Navegue para a pasta do dispositivo IoT:

cd iot-data-collection/dispositivo-iot


## Uso

1. Inicie o servidor Flask:

python app.py


2. Em outra janela do terminal, execute o código do dispositivo IoT:

python infoGathering.py


O código do dispositivo IoT irá ler os dados do sensor e enviá-los para o servidor Flask.

3. No terminal onde o servidor Flask está em execução, você verá as mensagens indicando se os dados foram recebidos com sucesso ou se houve falha no envio.

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas, tiver ideias para melhorias ou quiser adicionar novos recursos, fique à vontade para abrir uma "issue" ou enviar uma "pull request".








