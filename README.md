# CNPJ/CPF Validator | Validador de CNPJ/CPF

![PyPI Version](https://img.shields.io/pypi/v/cnpj-cpf-validator.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/cnpj-cpf-validator.svg)
![Downloads](https://static.pepy.tech/badge/cnpj-cpf-validator/month)
![Publish Status](https://img.shields.io/github/actions/workflow/status/FredericoSFerreira/cnpj-cpf-validator/publish.yml?branch=main)
![Coverage](https://fredericosferreira.github.io/py_cnpj_cpf_validator/coverage.svg)

*Read this in: [English](#english) | [Português](#português)*


<a id="português"></a>

## Português

Biblioteca Python para validação de CPF e CNPJ brasileiros, com suporte ao novo padrão alfanumérico de CNPJ (a partir de julho de 2026).

### Instalação

```bash
pip install cnpj-cpf-validator
```

### Recursos

- Validação de CPF
- Formatação de CPF (adiciona pontuação)
- Validação de CNPJ (numérico e alfanumérico)
- Formatação de CNPJ (adiciona pontuação)
- Suporte ao novo formato alfanumérico de CNPJ (válido a partir de julho de 2026)

### Uso

#### Validação de CPF

```python
from cnpj_cpf_validator import CPF

# Verificar se um CPF é válido
CPF.is_valid("529.982.247-25")  # True
CPF.is_valid("52998224725")     # True
CPF.is_valid("529.982.247-26")  # False (dígito verificador inválido)

# Formatar um CPF
CPF.format("52998224725")       # "529.982.247-25"
```

#### Validação de CNPJ

```python
from cnpj_cpf_validator import CNPJ

# Verificar se um CNPJ é válido (formato numérico tradicional)
CNPJ.is_valid("11.222.333/0001-81")  # True
CNPJ.is_valid("11222333000181")      # True
CNPJ.is_valid("11.222.333/0001-80")  # False (dígito verificador inválido)

# Verificar se um CNPJ alfanumérico é válido (novo formato a partir de julho de 2026)
CNPJ.is_valid("12.ABC.345/01DE-35")  # True - Exemplo oficial do SERPRO
CNPJ.is_valid("12ABC34501DE35")      # True - Mesmo exemplo sem formatação

# Formatar um CNPJ
CNPJ.format("11222333000181")       # "11.222.333/0001-81"
CNPJ.format("12ABC34501DE35")       # "12.ABC.345/01DE-35"
```

### Novo formato de CNPJ alfanumérico (a partir de julho de 2026)

A Receita Federal do Brasil anunciou mudanças no formato do CNPJ que começarão a valer a partir de julho de 2026. A principal alteração é a introdução do CNPJ alfanumérico, que incluirá letras, além dos números, na sua composição.

Como funcionará o novo CNPJ:

- **Formato Alfanumérico**: O CNPJ continuará tendo 14 caracteres, mas:
  - As oito primeiras posições (raiz do CNPJ) poderão conter tanto letras quanto números.
  - As quatro posições seguintes (ordem do estabelecimento) também serão alfanuméricas.
  - As duas últimas posições (dígitos verificadores) continuarão sendo exclusivamente numéricas.

- **Algoritmo de validação**: O cálculo dos dígitos verificadores segue o algoritmo oficial do SERPRO:
  - Caracteres alfanuméricos são convertidos para valores numéricos (A=10, B=11, ..., Z=35)
  - Pesos específicos são aplicados da direita para a esquerda (2 a 9, recomeçando após o 8º caracter)
  - O resto da divisão por 11 é usado para calcular os dígitos verificadores

- **Convivência de formatos**: Os CNPJs já existentes (apenas numéricos) permanecerão válidos. O novo formato alfanumérico será implementado apenas para novas inscrições a partir de julho de 2026. Os dois formatos (numérico e alfanumérico) vão coexistir.

#### Exemplo de cálculo (SERPRO)

Para o CNPJ alfanumérico `12ABC34501DE`:

1. **Conversão dos caracteres**:
   - Valores: 1, 2, 10, 11, 12, 3, 4, 5, 0, 1, 13, 14

2. **Cálculo do primeiro dígito verificador**:
   - Pesos: 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2
   - Multiplicação: 5, 8, 30, 22, 108, 24, 28, 30, 0, 4, 39, 28
   - Somatório: 459
   - Resto da divisão por 11: 8
   - Primeiro dígito: 11 - 8 = 3

3. **Cálculo do segundo dígito verificador**:
   - Pesos: 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2
   - Somatório com o primeiro dígito: 424
   - Resto da divisão por 11: 6
   - Segundo dígito: 11 - 6 = 5

4. **Resultado final**: `12.ABC.345/01DE-35`

### Licença

MIT

## Recursos

- Validação de CPF
- Formatação de CPF (adiciona pontuação)
- Validação de CNPJ (numérico e alfanumérico)
- Formatação de CNPJ (adiciona pontuação)
- Suporte ao novo formato alfanumérico de CNPJ (válido a partir de julho de 2026)

## Uso

### Validação de CPF

```python
from cnpj_cpf_validator import CPF

# Verificar se um CPF é válido
CPF.is_valid("529.982.247-25")  # True
CPF.is_valid("52998224725")     # True
CPF.is_valid("529.982.247-26")  # False (dígito verificador inválido)

# Formatar um CPF
CPF.format("52998224725")       # "529.982.247-25"
```

### Validação de CNPJ

```python
from cnpj_cpf_validator import CNPJ

# Verificar se um CNPJ é válido (formato numérico tradicional)
CNPJ.is_valid("11.222.333/0001-81")  # True
CNPJ.is_valid("11222333000181")      # True
CNPJ.is_valid("11.222.333/0001-80")  # False (dígito verificador inválido)

# Verificar se um CNPJ alfanumérico é válido (novo formato a partir de julho de 2026)
CNPJ.is_valid("12.ABC.345/01DE-35")  # True - Exemplo oficial do SERPRO
CNPJ.is_valid("12ABC34501DE35")      # True - Mesmo exemplo sem formatação

# Formatar um CNPJ
CNPJ.format("11222333000181")       # "11.222.333/0001-81"
CNPJ.format("12ABC34501DE35")       # "12.ABC.345/01DE-35"
```

## Novo formato de CNPJ alfanumérico (a partir de julho de 2026)

A Receita Federal do Brasil anunciou mudanças no formato do CNPJ que começarão a valer a partir de julho de 2026. A principal alteração é a introdução do CNPJ alfanumérico, que incluirá letras, além dos números, na sua composição.

Como funcionará o novo CNPJ:

- **Formato Alfanumérico**: O CNPJ continuará tendo 14 caracteres, mas:
  - As oito primeiras posições (raiz do CNPJ) poderão conter tanto letras quanto números.
  - As quatro posições seguintes (ordem do estabelecimento) também serão alfanuméricas.
  - As duas últimas posições (dígitos verificadores) continuarão sendo exclusivamente numéricas.

- **Algoritmo de validação**: O cálculo dos dígitos verificadores segue o algoritmo oficial do SERPRO:
  - Caracteres alfanuméricos são convertidos para valores numéricos (A=10, B=11, ..., Z=35)
  - Pesos específicos são aplicados da direita para a esquerda (2 a 9, recomeçando após o 8º caracter)
  - O resto da divisão por 11 é usado para calcular os dígitos verificadores

- **Convivência de formatos**: Os CNPJs já existentes (apenas numéricos) permanecerão válidos. O novo formato alfanumérico será implementado apenas para novas inscrições a partir de julho de 2026. Os dois formatos (numérico e alfanumérico) vão coexistir.

### Exemplo de cálculo (SERPRO)

Para o CNPJ alfanumérico `12ABC34501DE`:

1. **Conversão dos caracteres**:
   - Valores: 1, 2, 10, 11, 12, 3, 4, 5, 0, 1, 13, 14

2. **Cálculo do primeiro dígito verificador**:
   - Pesos: 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2
   - Multiplicação: 5, 8, 30, 22, 108, 24, 28, 30, 0, 4, 39, 28
   - Somatório: 459
   - Resto da divisão por 11: 8
   - Primeiro dígito: 11 - 8 = 3

3. **Cálculo do segundo dígito verificador**:
   - Pesos: 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2
   - Somatório com o primeiro dígito: 424
   - Resto da divisão por 11: 6
   - Segundo dígito: 11 - 6 = 5

4. **Resultado final**: `12.ABC.345/01DE-35`

## Licença

MIT

<a id="english"></a>

## English

Python library for validating Brazilian CPF and CNPJ, with support for the new alphanumeric CNPJ standard (from July 2026).

### Installation

```bash
pip install cnpj-cpf-validator
```

### Features

- CPF validation
- CPF formatting (adds punctuation)
- CNPJ validation (numeric and alphanumeric)
- CNPJ formatting (adds punctuation)
- Support for the new alphanumeric CNPJ format (valid from July 2026)

### Usage

#### CPF Validation

```python
from cnpj_cpf_validator import CPF

# Check if a CPF is valid
CPF.is_valid("529.982.247-25")  # True
CPF.is_valid("52998224725")     # True
CPF.is_valid("529.982.247-26")  # False (invalid verification digit)

# Format a CPF
CPF.format("52998224725")       # "529.982.247-25"
```

#### CNPJ Validation

```python
from cnpj_cpf_validator import CNPJ

# Check if a CNPJ is valid (traditional numeric format)
CNPJ.is_valid("11.222.333/0001-81")  # True
CNPJ.is_valid("11222333000181")      # True
CNPJ.is_valid("11.222.333/0001-80")  # False (invalid verification digit)

# Check if an alphanumeric CNPJ is valid (new format from July 2026)
CNPJ.is_valid("12.ABC.345/01DE-35")  # True - Official SERPRO example
CNPJ.is_valid("12ABC34501DE35")      # True - Same example without formatting

# Format a CNPJ
CNPJ.format("11222333000181")       # "11.222.333/0001-81"
CNPJ.format("12ABC34501DE35")       # "12.ABC.345/01DE-35"
```

### New alphanumeric CNPJ format (from July 2026)

The Brazilian Federal Revenue Service has announced changes to the CNPJ format that will take effect from July 2026. The main change is the introduction of the alphanumeric CNPJ, which will include letters, in addition to numbers, in its composition.

How the new CNPJ will work:

- **Alphanumeric Format**: The CNPJ will continue to have 14 characters, but:
  - The first eight positions (CNPJ root) may contain both letters and numbers.
  - The next four positions (establishment order) will also be alphanumeric.
  - The last two positions (verification digits) will continue to be exclusively numeric.

- **Validation Algorithm**: The calculation of verification digits follows the official SERPRO algorithm:
  - Alphanumeric characters are converted to numeric values (A=10, B=11, ..., Z=35)
  - Specific weights are applied from right to left (2 to 9, restarting after the 8th character)
  - The remainder of division by 11 is used to calculate verification digits

- **Format Coexistence**: Existing CNPJs (numeric only) will remain valid. The new alphanumeric format will be implemented only for new registrations from July 2026. Both formats (numeric and alphanumeric) will coexist.

#### Calculation Example (SERPRO)

For the alphanumeric CNPJ `12ABC34501DE`:

1. **Character Conversion**:
   - Values: 1, 2, 10, 11, 12, 3, 4, 5, 0, 1, 13, 14

2. **First Verification Digit Calculation**:
   - Weights: 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2
   - Multiplication: 5, 8, 30, 22, 108, 24, 28, 30, 0, 4, 39, 28
   - Sum: 459
   - Remainder of division by 11: 8
   - First digit: 11 - 8 = 3

3. **Second Verification Digit Calculation**:
   - Weights: 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2
   - Sum including the first digit: 424
   - Remainder of division by 11: 6
   - Second digit: 11 - 6 = 5

4. **Final Result**: `12.ABC.345/01DE-35`

### License

MIT

