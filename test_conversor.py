import unittest
from conversor import converter_moeda 

class TestConversorMoedas(unittest.TestCase):

    # --- Testes de Cenários Positivos (Casos de Sucesso) ---

    def test_conversao_brl_para_usd(self):
        """Testa conversão de Real para Dólar."""
        resultado = converter_moeda(10.0, 'BRL', 'USD')
        self.assertEqual(resultado, 2.00)

    def test_conversao_usd_para_brl(self):
        """Testa conversão de Dólar para Real."""
        resultado = converter_moeda(10.0, 'USD', 'BRL')
        self.assertEqual(resultado, 50.00)

    def test_conversao_mesma_moeda(self):
        """Testa conversão para a mesma moeda de origem (deve manter o valor)."""
        resultado = converter_moeda(100.0, 'BRL', 'BRL')
        self.assertEqual(resultado, 100.00)

    def test_precisao_duas_casas_decimais(self):
        """Garante que o retorno tenha precisão e arredondamento corretos."""
        # Exemplo: 10.55 * 0.20 = 2.11
        resultado = converter_moeda(10.55, 'BRL', 'USD')
        self.assertEqual(resultado, 2.11)

    def test_case_insensitivity(self):
        """Verifica se aceita siglas em minúsculas (ex: 'brl', 'usd')."""
        resultado = converter_moeda(10.0, 'brl', 'usd')
        self.assertEqual(resultado, 2.00)

    # --- Testes de Cenários Negativos e Exceções ---

    def test_valor_negativo_lanca_excecao(self):
        """Verifica se lança ValueError ao passar um valor menor que zero."""
        with self.assertRaises(ValueError):
            converter_moeda(-50.0, 'BRL', 'USD')

    def test_moeda_invalida_lanca_excecao(self):
        """Verifica se lança ValueError ao passar moedas não suportadas."""
        with self.assertRaises(ValueError):
            converter_moeda(100.0, 'XYZ', 'USD')
        
        with self.assertRaises(ValueError):
            converter_moeda(100.0, 'BRL', 'ABC')

# Permite executar o script diretamente via terminal
if __name__ == '__main__':
    unittest.main()