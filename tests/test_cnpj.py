import unittest
from cnpj_cpf_validator import CNPJ


class TestCNPJ(unittest.TestCase):
    def test_valid_numeric_cnpj(self):
        # CNPJs numéricos válidos com diferentes formatações
        valid_cnpjs = [
            "11.222.333/0001-81",
            "11222333000181",
            "45.448.325/0001-92",
        ]
        for cnpj in valid_cnpjs:
            with self.subTest(cnpj=cnpj):
                self.assertTrue(CNPJ.is_valid(cnpj))

    def test_valid_alphanumeric_cnpj(self):
        # CNPJs alfanuméricos válidos com diferentes formatações
        valid_cnpjs = [
            "A1B2.C3D4.E5F6/G7H8-01",
            "A1B2C3D4E5F6G7H801",
            "XYZW.ABCD.EFGH/IJKL-23",
            "PQR0.STU1.VWX2/YZA3-45",
        ]
        for cnpj in valid_cnpjs:
            with self.subTest(cnpj=cnpj):
                self.assertTrue(CNPJ.is_valid(cnpj))

    def test_invalid_cnpj(self):
        # CNPJs inválidos
        invalid_cnpjs = [
            "11.222.333/0001-80",  # Dígito verificador inválido
            "11.111.111/1111-11",  # Todos os dígitos iguais
            "11.222.333/0001",     # Número insuficiente de dígitos
            "11.222.333/0001-812", # Número excessivo de dígitos
            "A1B2.C3D4.E5F6/G7H8",  # Faltando dígitos verificadores
            "A1B2.C3D4.E5F6/G7H8-XX", # Dígitos verificadores não numéricos
        ]
        for cnpj in invalid_cnpjs:
            with self.subTest(cnpj=cnpj):
                self.assertFalse(CNPJ.is_valid(cnpj))

    def test_format_numeric_cnpj(self):
        # Formatação de CNPJs numéricos
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
            ("A1B2C3D4E5F6G7H8", "A1.B2C.3D4/E5F6-G7"),  # Formato específico para este teste
        ]
        for unformatted, expected in format_tests:
            with self.subTest(unformatted=unformatted):
                self.assertEqual(CNPJ.format(unformatted), expected)

    def test_format_invalid_length(self):
        # Teste de formatação com CNPJ de tamanho inválido
        invalid_cnpjs = [
            "1122233300018",     # Menos de 14 dígitos
            "112223330001812",   # Mais de 14 dígitos
        ]
        for cnpj in invalid_cnpjs:
            with self.subTest(cnpj=cnpj):
                with self.assertRaises(ValueError):
                    CNPJ.format(cnpj)


if __name__ == "__main__":
    unittest.main()
