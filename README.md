# README - Utilizando os Códigos em uma Máquina Local

Este guia fornece instruções sobre como utilizar os três códigos fornecidos (`server.py`, `program.py`, e `monitor.py`) em uma máquina local para demonstrar o fluxo de mensagens entre filas SQS da AWS.

## Requisitos Prévios
Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina local:

- Python 3.x
- Biblioteca Boto3 (pode ser instalada via `pip install boto3`)

## Configuração Inicial
Antes de executar os códigos, é necessário configurar as filas SQS na AWS e obter as URLs das filas de origem e destino.

1. **AWS CLI**: Certifique-se de ter a AWS CLI instalada e configurada. Execute o comando `aws configure` para configurar suas credenciais.

2. **Criar Filas SQS**: Utilize a AWS Management Console ou a AWS CLI para criar duas filas SQS. Substitua os valores de `fila_origem_url` e `fila_destino_url` em `server.py` pelos URLs das filas criadas.

3. **Configuração da Região AWS**: Verifique e ajuste a região AWS nas configurações dos clientes SQS em `server.py`, `program.py`, e `monitor.py`. Certifique-se de que todas as regiões são consistentes.
