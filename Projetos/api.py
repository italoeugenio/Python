import requests

def cambio():
    while True:
        print("------MENU------")
        print("1- Valor do Dólar (USD) para Real")
        print("2- Valor do Euro para Real")
        print("3- Sair do programa")

        escolha = input("Escolha a opção: ")
       
        if escolha == "1":
            valor = float(input("Digite o valor em USD que deseja converter para BRL: "))
            resposta = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
            dados = resposta.json()
            valor_brl = valor * dados["rates"]["BRL"]
            print(f"{valor} USD é igual a {valor_brl} BRL")
        elif escolha == "2":
            valor = float(input("Digite o valor em EUR que deseja converter para BRL: "))
            resposta = requests.get('https://api.exchangerate-api.com/v4/latest/EUR')
            dados = resposta.json()
            valor_brl = valor * dados["rates"]["BRL"]
            print(f"{valor} EUR é igual a {valor_brl} BRL")
        elif escolha == "3":
            break
        else:
            print("Opção inválida")

# Módulo e inicialização padrão 
if __name__ == "__main__":
    cambio()