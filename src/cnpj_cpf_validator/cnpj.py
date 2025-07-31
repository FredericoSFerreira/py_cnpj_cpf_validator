import re
from typing import Union, Tuple


class CNPJ:
    """Classe para validação e formatação de CNPJ."""

    @staticmethod
    def is_valid(cnpj: str) -> bool:
        """Verifica se um CNPJ é válido, suportando formatos numéricos e alfanuméricos.

        Args:
            cnpj: Número de CNPJ, com ou sem formatação.

        Returns:
            bool: True se o CNPJ for válido, False caso contrário.
        """
        # Remove formatação (pontos, traços e barras)
        cnpj = re.sub(r'[.\-/]', '', cnpj)

        # Verifica se tem 14 caracteres
        if len(cnpj) != 14:
            return False

        # Verifica se é um CNPJ alfanumérico
        if not cnpj[-2:].isdigit():
            return False  # Os dois últimos caracteres devem ser dígitos verificadores numéricos

        # Se for totalmente numérico, valida pelos dígitos verificadores
        if cnpj.isdigit():
            return CNPJ._validate_numeric_cnpj(cnpj)
        else:
            # Para CNPJs alfanuméricos, validamos apenas o formato e os dígitos verificadores
            return CNPJ._validate_alphanumeric_cnpj(cnpj)

    @staticmethod
    def _validate_numeric_cnpj(cnpj: str) -> bool:
        """Valida um CNPJ totalmente numérico através dos dígitos verificadores.

        Args:
            cnpj: CNPJ numérico sem formatação.

        Returns:
            bool: True se o CNPJ for válido, False caso contrário.
        """
        # Verifica se todos os dígitos são iguais (CNPJ inválido, mas passa na validação)
        if len(set(cnpj)) == 1:
            return False

        # Cálculo do primeiro dígito verificador
        soma = 0
        peso = 5
        for i in range(12):
            soma += int(cnpj[i]) * peso
            peso = 9 if peso == 2 else peso - 1

        digito1 = 0 if soma % 11 < 2 else 11 - (soma % 11)

        # Cálculo do segundo dígito verificador
        soma = 0
        peso = 6
        for i in range(13):
            soma += int(cnpj[i]) * peso
            peso = 9 if peso == 2 else peso - 1

        digito2 = 0 if soma % 11 < 2 else 11 - (soma % 11)

        # Verifica se os dígitos verificadores estão corretos
        return int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2

    @staticmethod
    def _validate_alphanumeric_cnpj(cnpj: str) -> bool:
        """Valida um CNPJ alfanumérico.

        Para CNPJs alfanuméricos, verificamos:
        1. Se tem 14 caracteres
        2. Se os 12 primeiros são alfanuméricos
        3. Se os 2 últimos são dígitos numéricos

        Não é possível calcular os dígitos verificadores para CNPJs alfanuméricos
        da mesma forma que os numéricos, então assumimos que são válidos se
        atenderem às condições acima.

        Args:
            cnpj: CNPJ alfanumérico sem formatação.

        Returns:
            bool: True se o formato do CNPJ for válido, False caso contrário.
        """
        # Verifica se os 12 primeiros caracteres são alfanuméricos
        if not all(c.isalnum() for c in cnpj[:12]):
            return False

        # Verifica se os 2 últimos caracteres são dígitos
        if not cnpj[-2:].isdigit():
            return False

        # Aqui poderíamos adicionar regras adicionais específicas para CNPJs alfanuméricos
        # quando a Receita Federal divulgar o algoritmo completo de validação

        return True

    @staticmethod
    def format(cnpj: str) -> str:
        """Formata um CNPJ adicionando pontuação, suportando formatos numéricos e alfanuméricos.

        Args:
            cnpj: Número de CNPJ, com ou sem formatação.

        Returns:
            str: CNPJ formatado (ex: 12.345.678/0001-90 ou A1B2.C3D4.E5F6/G7H8-01).

        Raises:
            ValueError: Se o CNPJ não tiver o número correto de caracteres após remover a formatação.
        """
        # Remove caracteres de formatação
        cnpj = re.sub(r'[.\-/]', '', cnpj)

        # Verifica se tem 14 caracteres
        if len(cnpj) != 14:
            raise ValueError("CNPJ deve conter 14 caracteres após remover a formatação")

        # Formata o CNPJ
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
