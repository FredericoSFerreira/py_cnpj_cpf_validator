import unittest
from cnpj_cpf_validator import CNPJ


class TestCNPJ(unittest.TestCase):
    def test_valid_numeric_cnpj(self):
        valid_cnpjs = [
            "11.222.333/0001-81",
            "11222333000181",
            "71.582.575/0001-08",
            "68.662.814/0001-25",
            "34.227.784/0001-07"
        ]
        for cnpj in valid_cnpjs:
            with self.subTest(cnpj=cnpj):
                self.assertTrue(CNPJ.is_valid(cnpj))

    def test_valid_alphanumeric_cnpj(self):
        valid_cnpjs = [
            "12.ABC.345/01DE-35",
            "12ABC34501DE35",
            "DL.VIG.R2R/0001-39",
            "DLVIGR2R000139",
            "HT.LUS.VAI/0001-89",
            "60.RQL.ECU/0001-48",
            "NE.S62.ZF8/0001-40"
        ]
        for cnpj in valid_cnpjs:
            with self.subTest(cnpj=cnpj):
                self.assertTrue(CNPJ.is_valid(cnpj))

    def test_invalid_cnpj(self):
        invalid_cnpjs = [
            "11.222.333/0001-80",  # Dígito verificador inválido
            "11.111.111/1111-11",  # Todos os dígitos iguais
            "11.222.333/0001",  # Número insuficiente de dígitos
            "11.222.333/0001-812",  # Número excessivo de dígitos
            "A1B2.C3D4.E5F6/G7H8",  # Faltando dígitos verificadores
            "A1B2.C3D4.E5F6/G7H8-XX",  # Dígitos verificadores não numéricos
            "12ABC3450/1DE-36",  # DV inválido para o exemplo SERPRO
        ]
        for cnpj in invalid_cnpjs:
            with self.subTest(cnpj=cnpj):
                self.assertFalse(CNPJ.is_valid(cnpj))

    def test_format_numeric_cnpj(self):
        format_tests = [
            ("11222333000181", "11.222.333/0001-81"),
            ("45448325000192", "45.448.325/0001-92"),
        ]
        for unformatted, expected in format_tests:
            with self.subTest(unformatted=unformatted):
                self.assertEqual(CNPJ.format(unformatted), expected)

    def test_format_alphanumeric_cnpj(self):
        # Formatação de CNPJs alfanuméricos
        format_tests = [
            ("12ABC34501DE35", "12.ABC.345/01DE-35"),  # Exemplo oficial do SERPRO
            ("ABCD23Z9XY4587", "AB.CD2.3Z9/XY45-87")   # Outro exemplo calculado pelo algoritmo SERPRO
        ]
        for unformatted, expected in format_tests:
            with self.subTest(unformatted=unformatted):
                self.assertEqual(CNPJ.format(unformatted), expected)

    def test_format_invalid_length(self):
        invalid_cnpjs = [
            "1122233300018",  # Menos de 14 dígitos
            "112223330001812",  # Mais de 14 dígitos
        ]
        for cnpj in invalid_cnpjs:
            with self.subTest(cnpj=cnpj):
                with self.assertRaises(ValueError):
                    CNPJ.format(cnpj)


if __name__ == "__main__":
    unittest.main()
