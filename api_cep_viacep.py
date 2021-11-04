import json
import requests


def main():
    try:

        uf=input("Digite a UF: ")
        cidade=input("Digite a cidade: ")
        rua=input("Digite a rua: ")

        informa_via_cep = requests.get(f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/')
        via_cep = informa_via_cep.json()

        devolve_cep=json.dumps(via_cep, sort_keys=True, indent=2, ensure_ascii=False, separators=(""," => "))
        print(devolve_cep)

    except:
        print("Valores inválidos ou cep inexistente")


if __name__ == "__main__":
    main()