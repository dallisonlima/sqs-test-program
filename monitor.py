import boto3
import time

# Substitua 'sua_fila_url' pelo URL da sua fila SQS
fila_url = 'DestinoSqsQueue'
regiao_aws = 'us-east-1'  # Substitua pela região AWS desejada

# Configuração do cliente SQS
cliente_sqs = boto3.client('sqs', region_name=regiao_aws)

def consumir_fila():
    print('Aguardando mensagens...')
    while True:
        # Recebe as mensagens da fila
        response = cliente_sqs.receive_message(
            QueueUrl=fila_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=1,
            MessageAttributeNames=['All'],
            VisibilityTimeout=0,
            WaitTimeSeconds=20  # Aumente o tempo de espera se necessário
        )

        # Verifica se há mensagens na fila
        mensagens = response.get('Messages', [])
        if mensagens:
            # Exibe as mensagens na tela
            for mensagem in mensagens:
                corpo_mensagem = mensagem['Body']
                print(f'Mensagem Recebida: {corpo_mensagem}')

                # Apaga a mensagem da fila
                receipt_handle = mensagem['ReceiptHandle']
                cliente_sqs.delete_message(
                    QueueUrl=fila_url,
                    ReceiptHandle=receipt_handle
                )
        else:
            print('Nenhuma mensagem na fila. Aguardando...')
            time.sleep(5)  # Pausa por 5 segundos antes de verificar novamente

if __name__ == '__main__':
    consumir_fila()
