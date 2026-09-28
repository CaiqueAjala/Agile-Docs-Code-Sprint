from conversor import converter_moeda

MOEDAS_DISPONIVEIS = {
    '1': 'BRL',
    '2': 'USD',
    '3': 'EUR'
}

def exibir_menu_moedas():
    print("\nEscolha uma moeda:")
    print("1 - Real (BRL)")
    print("2 - Dólar (USD)")
    print("3 - Euro (EUR)")

def main():
    while True:
        print("\n=== CONVERSOR DE MOEDAS ===")
        print("1 - Realizar Conversão")
        print("0 - Sair")
        
        opcao = input("Selecione uma opção: ").strip()

        if opcao == '0':
            print("Saindo do programa... Até mais!")
            break
        elif opcao != '1':
            print("Opção inválida! Tente novamente.")
            continue

        # Seleção da moeda de origem
        exibir_menu_moedas()
        origem_op = input("Moeda de ORIGEM: ").strip()
        if origem_op not in MOEDAS_DISPONIVEIS:
            print("Moeda de origem inválida!")
            continue

        # Seleção da moeda de destino
        exibir_menu_moedas()
        destino_op = input("Moeda de DESTINO: ").strip()
        if destino_op not in MOEDAS_DISPONIVEIS:
            print("Moeda de destino inválida!")
            continue

        # Entrada do valor com tratamento de erro
        try:
            valor = float(input("Digite o valor a ser convertido: ").replace(',', '.'))
            
            moeda_origem = MOEDAS_DISPONIVEIS[origem_op]
            moeda_destino = MOEDAS_DISPONIVEIS[destino_op]

            resultado = converter_moeda(valor, moeda_origem, moeda_destino)
            print(f"\n✅ Resultado: {valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")

        except ValueError as e:
            print(f"\n❌ Erro: {e}. Digite um valor numérico válido.")

if __name__ == "__main__":
    main()