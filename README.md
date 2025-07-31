# CNPJ/CPF Validator

Biblioteca Python para validação de CPF e CNPJ brasileiros, com suporte ao novo padrão alfanumérico de CNPJ (a partir de julho de 2026).

## Instalação

```bash
pip install cnpj-cpf-validator
```

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
CNPJ.is_valid("A1B2.C3D4.E5F6/G7H8-01")  # True
CNPJ.is_valid("A1B2C3D4E5F6G7H801")      # True

# Formatar um CNPJ
CNPJ.format("11222333000181")              # "11.222.333/0001-81"
CNPJ.format("A1B2C3D4E5F6G7H801")          # "A1B2.C3D4.E5F6/G7H8-01"
```

## Novo formato de CNPJ alfanumérico (a partir de julho de 2026)

A Receita Federal do Brasil anunciou mudanças no formato do CNPJ que começarão a valer a partir de julho de 2026. A principal alteração é a introdução do CNPJ alfanumérico, que incluirá letras, além dos números, na sua composição.

Como funcionará o novo CNPJ:

- **Formato Alfanumérico**: O CNPJ continuará tendo 14 caracteres, mas:
  - As oito primeiras posições (raiz do CNPJ) poderão conter tanto letras quanto números.
  - As quatro posições seguintes (ordem do estabelecimento) também serão alfanuméricas.
  - As duas últimas posições (dígitos verificadores) continuarão sendo exclusivamente numéricas.

- **Convivência de formatos**: Os CNPJs já existentes (apenas numéricos) permanecerão válidos. O novo formato alfanumérico será implementado apenas para novas inscrições a partir de julho de 2026. Os dois formatos (numérico e alfanumérico) vão coexistir.

## Licença

MIT
