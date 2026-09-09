# Planejamento — ByteStore

## Identidade

Loja demonstrativa de informática para estudantes, pessoas que trabalham no computador e entusiastas de tecnologia. Nome de trabalho: ByteStore. Tema aprovado pelo usuário.

## Páginas

| Rota | Conteúdo |
| --- | --- |
| `/` | Apresentação, categorias e produtos em destaque |
| `/catalogo` | Todos os produtos, busca e filtro por categoria |
| `/ofertas` | Produtos disponíveis com preço promocional |
| `/sobre` | Proposta da loja e perguntas frequentes |

## Dados e comportamento

Lista de oito dicionários no `app.py`: id, nome, categoria, descrição, preço em centavos, preço anterior opcional, disponibilidade, destaque e imagem.

Jinja2: todas as páginas herdam `base.html`; `for` gera os cards; `if` controla promoção, disponibilidade, destaque e lista vazia. Ao adicionar um produto à lista, catálogo e categorias são atualizados automaticamente.

Bootstrap 5: navbar recolhível no celular, grid responsivo, cards, badges e formulários de busca GET. CSS próprio para identidade visual verde-escura e verde-lima.

## Limites

Produtos, preços e disponibilidade fictícios. Sem pagamento, cadastro, banco de dados ou envio de mensagens. Escopo adequado à Semana 6. Publicação no GitHub será discutida após a revisão local; não há aprovação docente registrada.

## Etapas

1. Ambiente, estrutura inicial e `.gitignore`.
2. Template compartilhado, quatro páginas e navegação.
3. Dados dinâmicos, filtros e estados condicionais.
4. Acabamento, testes, README e roteiro de apresentação.

Commits registrarão etapas reais da implementação, sem alterar datas para simular o cronograma da aula.
