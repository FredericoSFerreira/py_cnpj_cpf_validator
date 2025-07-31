import unittest
from cnpj_cpf_validator import CPF


class TestCPF(unittest.TestCase):
    def test_valid_cpf(self):
        # CPFs válidos com diferentes formatações
        valid_cpfs = [
            "529.982.247-25",
            "52998224725",
            "111.444.777-35",
        ]
        for cpf in valid_cpfs:
            with self.subTest(cpf=cpf):
                self.assertTrue(CPF.is_valid(cpf))

    def test_invalid_cpf(self):
        # CPFs inválidos
        invalid_cpfs = [
            "529.982.247-26",  # Dígito verificador inválido
            "111.111.111-11",  # Todos os dígitos iguais
            "123.456.789-00",  # Inválido
            "529.982.247",     # Número insuficiente de dígitos
            "529.982.247-253", # Número excessivo de dígitos
            "AAA.BBB.CCC-DD",  # Não numérico
        ]
        for cpf in invalid_cpfs:
            with self.subTest(cpf=cpf):
                self.assertFalse(CPF.is_valid(cpf))

    def test_format_cpf(self):
        # Formatação de CPFs
        format_tests = [
            ("52998224725", "529.982.247-25"),
            ("11144477735", "111.444.777-35"),
        ]
        for unformatted, expected in format_tests:
            with self.subTest(unformatted=unformatted):
                self.assertEqual(CPF.format(unformatted), expected)

    def test_format_invalid_length(self):
        # Teste de formatação com CPF de tamanho inválido
        invalid_cpfs = [
            "5299822472",      # Menos de 11 dígitos
            "529982247255",    # Mais de 11 dígitos
        ]
        for cpf in invalid_cpfs:
            with self.subTest(cpf=cpf):
                with self.assertRaises(ValueError):
                    CPF.format(cpf)


if __name__ == "__main__":
    unittest.main()
