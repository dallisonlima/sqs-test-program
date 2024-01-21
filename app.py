# app.py
from flask import Flask, render_template, request, jsonify
import boto3

app = Flask(__name__)

nome_da_fila_origem = 'Origem'
nome_da_fila_destino = 'Destino'

cliente_sqs = boto3.client('sqs', region_name='us-east-1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    mensagem = request.form['mensagem']
    resposta = cliente_sqs.send_message(QueueUrl=nome_da_fila_origem, MessageBody=mensagem)
    return f'Mensagem enviada com sucesso. ID: {resposta["MessageId"]}'

@app.route('/receber')
def receber():
    resposta = cliente_sqs.receive_message(QueueUrl=nome_da_fila_destino, MaxNumberOfMessages=1)

    if 'Messages' in resposta:
        mensagem = resposta['Messages'][0]
        corpo_mensagem = mensagem['Body']
        receipt_handle = mensagem['ReceiptHandle']
        message_id = mensagem['MessageId']

        return jsonify({'message': f'Mensagem recebida: {corpo_mensagem}', 'messageId': message_id, 'receiptHandle': receipt_handle})

    return jsonify({})  # Retorna uma resposta vazia se não houver mensagens

@app.route('/deletar', methods=['POST'])
def deletar():
    mensagem_id = request.form['messageId']
    receipt_handle = request.form['receiptHandle']

    cliente_sqs.delete_message(QueueUrl=nome_da_fila_destino, ReceiptHandle=receipt_handle)
    return 'Mensagem excluída com sucesso.'

# Rota para a página de mensagens recebidas
@app.route('/monitor')
def monitor():
    return render_template('monitor.html')

if __name__ == '__main__':
    app.run(debug=True)
