# Guia de Contribuição

Obrigado pelo interesse em contribuir para a biblioteca `cnpj_cpf_validator`! Este documento fornece diretrizes para contribuir com este projeto.

## Fluxo de Desenvolvimento

1. Fork este repositório
2. Clone seu fork para sua máquina local
3. Crie um branch para sua contribuição (`git checkout -b feature/sua-funcionalidade` ou `git checkout -b fix/seu-bug`)
4. Faça suas alterações
5. Execute os testes (`pytest`)
6. Faça commit de suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
7. Envie para o GitHub (`git push origin feature/sua-funcionalidade`)
8. Abra um Pull Request

## Diretrizes de Código

- Siga o estilo PEP 8 para código Python
- Adicione docstrings para novas funções e classes
- Mantenha a compatibilidade com Python 3.8+
- Escreva testes para novas funcionalidades
- Mantenha a cobertura de código alta

## Testes

Execute os testes com pytest:

```bash
pytest tests/
```

Para verificar a cobertura de código:

```bash
pytest --cov=src/cnpj_cpf_validator tests/
```

## Publicação de Novas Versões

Para contribuidores com acesso de publicação:

1. Atualize a versão no arquivo `pyproject.toml`
2. Atualize o CHANGELOG.md com as alterações
3. Faça commit das alterações
4. Crie uma tag com o formato `v{version}` (ex: `v0.2.0`)
5. Envie a tag para o GitHub (`git push origin v0.2.0`)
6. O GitHub Actions irá construir e publicar automaticamente no PyPI

## Relatando Bugs

Por favor, use o modelo de issue de bug para relatar problemas.

## Solicitando Funcionalidades

Por favor, use o modelo de issue de funcionalidade para solicitar novas funcionalidades.
