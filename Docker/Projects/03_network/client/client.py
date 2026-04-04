import urllib.request

def main():
    while True:
        escolha = input("Digite 'moeda' ou 'dado': ").strip().lower()

        match escolha:
            case "moeda":
                url = "http://server:8000/moeda"
            case "dado":
                url = "http://server:8000/dado"
            case "exit":
                break
            case _:
                print("Opção inválida")

        with urllib.request.urlopen(url) as response:
            resultado = response.read().decode()

        print("Resultado:", resultado)

if __name__ == "__main__":
    main()