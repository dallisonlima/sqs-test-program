import boto3

nome_da_fila = 'OrigemSqsQueue'

cliente_sqs = boto3.client('sqs', region_name='us-east-1')

def enviar_mensagem():
    mensagem = input('Digite a mensagem que deseja enviar: ')
    resposta = cliente_sqs.send_message(QueueUrl=nome_da_fila, MessageBody=mensagem)
    print(f'\nMensagem enviada com sucesso. ID: {resposta["MessageId"]}\n')

def receber_mensagem():
    resposta = cliente_sqs.receive_message(QueueUrl=nome_da_fila, MaxNumberOfMessages=1)

    if 'Messages' in resposta:
        mensagem = resposta['Messages'][0]
        corpo_mensagem = mensagem['Body']
        receipt_handle = mensagem['ReceiptHandle']

        print(f'\nMensagem recebida: {corpo_mensagem}\n')

        excluir = input('Deseja excluir a mensagem da fila? (s/n): ').lower()
        if excluir == 's':
            cliente_sqs.delete_message(QueueUrl=nome_da_fila, ReceiptHandle=receipt_handle)
            print('Mensagem excluída da fila.\n')
        else:
            print('Mensagem não excluída da fila.\n')
    else:
        print('Nenhuma mensagem na fila.\n')

if __name__ == "__main__":
    while True:
        print("Escolha uma opção:")
        print("1. Enviar mensagem")
        print("2. Receber mensagem")
        print("3. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            enviar_mensagem()
        elif escolha == '2':
            receber_mensagem()
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
