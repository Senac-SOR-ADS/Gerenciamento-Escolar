import requests
import time



def getCep(cep):
    cep = input("Digite o CEP: ").replace("-", "").strip()

    url = f"https://viacep.com.br/ws/{cep}/json/"
    res = requests.get(url)
    dados = res.json()

    if "erro" in dados:
        print("CEP nao existe")
    else:
        print("CEP válido")
        print(f"Rua: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")





cep = input("Digite o CEP: ").replace("-", "").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"

inicio = time.time()  # começa a contar

res = requests.get(url)
dados = res.json()

fim = time.time()  # termina de contar

tempo = fim - inicio

print(f"Tempo de resposta: {tempo:.4f} segundos")

if "erro" in dados:
    print("CEP não existe")
else:
    print(f"Rua: {dados.get('logradouro')}")
    print(f"Bairro: {dados.get('bairro')}")

