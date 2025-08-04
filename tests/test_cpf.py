import unittest
from cnpj_cpf_validator import CPF


class TestCPF(unittest.TestCase):
    def test_valid_cpf(self):
        valid_cpfs = [
            "529.982.247-25",
            "52998224725",
            "111.444.777-35",
            "48648876168",
            "55505939120",
            "19994413627",
            "82135109762",
            "29873345671",
            "190.152.548-18",
            "047.564.108-63",
            "795.092.547-70",
            "489.179.332-54",
            "633.635.431-82",
        ]
        for cpf in valid_cpfs:
            with self.subTest(cpf=cpf):
                self.assertTrue(CPF.is_valid(cpf))

    def test_invalid_cpf(self):
        invalid_cpfs = [
            "529.982.247-26",
            "111.111.111-11",
            "123.456.789-00",
            "529.982.247",
            "529.982.247-253",
            "AAA.BBB.CCC-DD",
        ]
        for cpf in invalid_cpfs:
            with self.subTest(cpf=cpf):
                self.assertFalse(CPF.is_valid(cpf))

    def test_format_cpf(self):
        format_tests = [
            ("52998224725", "529.982.247-25"),
            ("11144477735", "111.444.777-35"),
        ]
        for unformatted, expected in format_tests:
            with self.subTest(unformatted=unformatted):
                self.assertEqual(CPF.format(unformatted), expected)

    def test_format_invalid_length(self):
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
