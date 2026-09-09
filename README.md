# ByteStore

Loja demonstrativa de informática desenvolvida para o Mini-projeto 1 da Semana 6 de Programação para Internet. Voltada a estudantes, profissionais e entusiastas que desejam explorar produtos para seu setup.

**Produtos, modelos, especificações, preços e disponibilidade são fictícios.** As fotografias são ilustrativas. Não há compras, pagamentos, cadastro ou envio de mensagens.

## Tecnologias

- Python 3.13 usado na validação. Use Python 3.10 ou superior para compatibilidade com todas as versões de `requirements-lock.txt`.
- Flask 3.1.3: rotas e renderização das páginas.
- Jinja2: herança de templates, laços `for`, condições `if` e filtros.
- Bootstrap 5.3.8: navbar recolhível, grid responsivo, cards, badges e controles.
- HTML5 e CSS próprio.
- Git: histórico das etapas de construção.

## Como rodar no Windows

Com Python instalado, abra um terminal nesta pasta:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Se o comando `python` não estiver disponível, tente `py -3` na primeira linha. Não é necessário ativar o ambiente: os comandos acima usam diretamente seu executável.

Se preferir ativá-lo no PowerShell, use `.\.venv\Scripts\Activate.ps1`. No Prompt de Comando, use `.venv\Scripts\activate.bat`.

Abra **http://127.0.0.1:5000**. Encerre o servidor com `Ctrl+C`.

O ambiente `.venv` já foi preparado nesta máquina. Nele, basta executar `.\.venv\Scripts\python.exe app.py`. A instância de revisão foi iniciada em **http://127.0.0.1:5050**, porque havia outro servidor na porta 5000. Para usar a porta alternativa, execute `.\.venv\Scripts\python.exe -m flask --app app run --port 5050`. Após editar Python ou templates, reinicie a instância correspondente.

### Linux ou macOS

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

Para reproduzir as versões exatas da validação, instale `requirements-lock.txt` no lugar de `requirements.txt`.

Bootstrap, JavaScript e imagens estão em `static/`; depois da instalação das dependências, a navegação funciona sem acesso à internet. O servidor de desenvolvimento atende somente em `127.0.0.1` e não usa modo debug.

## Páginas e recursos

| Rota | Conteúdo |
| --- | --- |
| `/` | Apresentação, categorias automáticas e até quatro destaques disponíveis |
| `/catalogo` | Oito produtos, busca e filtro por categoria combináveis |
| `/ofertas` | Produtos disponíveis cujo preço anterior supera o atual |
| `/sobre` | Apresentação e perguntas frequentes |
| Caminho inexistente | Resposta HTTP 404 com template compartilhado |

A busca ignora acentos e diferenças entre maiúsculas e minúsculas. Usa nome, descrição, categoria e especificações. Os controles enviam parâmetros GET, sem banco de dados. “Ver especificações” expande as informações no próprio card.

## Estrutura

```text
app.py                       # Lista de dicionários, rotas e filtros
templates/
  base.html                  # Estrutura comum, navbar e rodapé
  inicio.html
  catalogo.html
  ofertas.html
  sobre.html
  404.html
  partials/produtos.html      # Cards com for e if
static/
  css/style.css              # Identidade visual e adaptações de tela
  img/                       # Fotografias ilustrativas locais
  vendor/                    # Bootstrap e sua licença
  favicon.svg
tests/test_app.py            # Testes de comportamento
docs/planejamento.md         # Planejamento
docs/apresentacao.md         # Roteiro do pitch e demonstração
docs/verificacao.md          # Resultados e pendências
docs/creditos.md             # Fontes de imagens e bibliotecas
requirements.txt
requirements-lock.txt
.gitignore
```

## Dados dinâmicos: teste do item novo

Todos os produtos estão na lista `produtos` do `app.py`. Acrescente um dicionário com um `id` único, seguindo este formato:

```python
{
    "id": 9,
    "nome": "Notebook de demonstração",
    "categoria": "Notebooks",
    "descricao": "Um novo item para mostrar o catálogo dinâmico.",
    "especificacoes": "14 polegadas · 16 GB RAM · SSD 512 GB",
    "preco": 250000,
    "preco_anterior": 300000,
    "disponivel": True,
    "destaque": False,
    "imagem": "notebook.jpg",
},
```

Os preços são inteiros em **centavos**: `250000` representa R$ 2.500,00. Use `None` em `preco_anterior` para um produto sem promoção.

Reinicie o servidor e recarregue o Catálogo. O novo produto aparecerá sem editar HTML. Se tiver desconto e estiver disponível, também aparecerá em Ofertas. O limite de quatro destaques vale apenas para a página inicial.

O laço `for` em `templates/partials/produtos.html` gera os cards. Os `if` exibem badges e disponibilidade, alternam o preço anterior e tratam a lista vazia. Todas as páginas usam `{% extends "base.html" %}`.

## Testes

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Os testes verificam rotas, arquivos estáticos, catálogo, filtros combinados, acentuação, escape de HTML, ofertas, listas vazias, formato monetário, página 404 e inclusão de um novo item sem alterar templates.

## Git e GitHub

O repositório Git foi criado localmente, com commits em etapas reais. `.gitignore` exclui ambiente virtual, arquivos temporários, segredos e a apostila de referência.

Repositório público: [wilsonvieiradeoliveira/pi_mini-projeto_1](https://github.com/wilsonvieiradeoliveira/pi_mini-projeto_1).

A revisão confirmou a publicação da versão `d1d12f4`. Alterações locais posteriores precisam ser enviadas ao GitHub para fazer parte da entrega remota.

O remoto `origin` está configurado e a branch principal é `main`. GitHub armazena o código; GitHub Pages não executa este servidor Flask. A apostila pede o código no GitHub, não a hospedagem pública do servidor; hospedar a aplicação é uma decisão opcional e separada.

## Referências

- [Instalação do Flask](https://flask.palletsprojects.com/en/stable/installation/)
- [Documentação do Jinja](https://jinja.palletsprojects.com/en/stable/templates/)
- [Download e uso do Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/download/)
- Apostila Semana 6 fornecida pelo usuário, mantida fora do versionamento.
