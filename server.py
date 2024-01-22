import boto3
import time

# Configurações do AWS SQS
fila_origem_url = 'Origem'
fila_destino_url = 'Destino'
region_name = 'us-east-1'

# Configuração do cliente SQS
sqs = boto3.client('sqs', region_name=region_name)

def processar_e_enviar_mensagem(message):
    # Converter todas as letras minúsculas para maiúsculas
    mensagem_processada = message['Body'].upper()

    # Enviar a mensagem processada para a nova fila
    sqs.send_message(
        QueueUrl=fila_destino_url,
        MessageBody=mensagem_processada
    )

    print(f"Mensagem Processada e Enviada: {mensagem_processada}")

# Loop principal do servidor
while True:
    # Receber mensagens da fila de origem
    response = sqs.receive_message(
        QueueUrl=fila_origem_url,
        AttributeNames=['All'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    # Verificar se há mensagens na fila de origem
    if 'Messages' in response:
        for message in response['Messages']:
            # Processar e enviar a mensagem para a nova fila
            processar_e_enviar_mensagem(message)

            # Excluir a mensagem da fila de origem depois de processada
            receipt_handle = message['ReceiptHandle']
            sqs.delete_message(
                QueueUrl=fila_origem_url,
                ReceiptHandle=receipt_handle
            )

    # Esperar por um curto período antes de verificar novamente
    time.sleep(1)
