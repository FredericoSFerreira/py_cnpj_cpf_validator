import re
from typing import Union


class CPF:
    """Classe para validação e formatação de CPF."""

    @staticmethod
    def is_valid(cpf: str) -> bool:
        """Verifica se um CPF é válido.

        Args:
            cpf: Número de CPF, com ou sem formatação.

        Returns:
            bool: True se o CPF for válido, False caso contrário.
        """
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)

        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais (CPF inválido, mas passa na validação)
        if len(set(cpf)) == 1:
            return False

        # Valida os dígitos verificadores
        for i in range(9, 11):
            valor = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
            digito = ((valor * 10) % 11) % 10
            if int(cpf[i]) != digito:
                return False

        return True

    @staticmethod
    def format(cpf: str) -> str:
        """Formata um CPF adicionando pontuação.

        Args:
            cpf: Número de CPF, com ou sem formatação.

        Returns:
            str: CPF formatado (ex: 123.456.789-09).

        Raises:
            ValueError: Se o CPF não tiver o número correto de dígitos após remover a formatação.
        """
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)

        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 dígitos numéricos")

        # Formata o CPF
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
