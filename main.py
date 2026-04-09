from scraper import buscar_produto
from planilhas import salvar_dados

def main():
    termo = input("O que deseja buscar na Oasis Tabacaria? ")
    print("Iniciando busca, aguarde...")
    
    dados = buscar_produto(termo)

    if dados:
        salvar_dados(dados)
        print(f"Sucesso! {len(dados)} itens coletados.")
    else:
        print("Nada foi encontrado.")

if __name__ == "__main__":
    main()