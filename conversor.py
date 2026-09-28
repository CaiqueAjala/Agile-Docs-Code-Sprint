TAXAS_DE_CAMBIO = {
    'BRL': {'USD': 0.20, 'EUR': 0.18, 'BRL': 1.0},
    'USD': {'BRL': 5.00, 'EUR': 0.90, 'USD': 1.0},
    'EUR': {'BRL': 5.55, 'USD': 1.11, 'EUR': 1.0}
}

def converter_moeda(valor: float, origem: str, destino: str) -> float:
    """
    Converte um valor entre BRL, USD e EUR.
    Garante precisão e arredondamento em 2 casas decimais.
    """
    if valor < 0:
        raise ValueError("O valor para conversão não pode ser negativo.")
    
    origem = origem.upper()
    destino = destino.upper()

    if origem not in TAXAS_DE_CAMBIO or destino not in TAXAS_DE_CAMBIO[origem]:
        raise ValueError("Moeda não suportada.")

    taxa = TAXAS_DE_CAMBIO[origem][destino]
    resultado = valor * taxa
    
    return round(resultado, 2)