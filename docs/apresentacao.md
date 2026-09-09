# Apresentação — roteiro de 1 minuto

## 0:00–0:15 — O que é e para quem

“A ByteStore é uma loja demonstrativa de informática para estudantes, profissionais e pessoas que querem conhecer produtos para seu setup. Usei Flask, Jinja2 e Bootstrap.”

## 0:15–0:45 — Tour

1. Mostrar a página inicial e o menu.
2. Abrir Catálogo, buscar “mecanico” e mostrar que o teclado aparece.
3. Limpar filtros e abrir as especificações de um card.
4. Abrir Ofertas e explicar o preço anterior e o badge.
5. Se houver tempo, mostrar o item extra preparado para a demonstração.

## 0:45–1:00 — Código

Abrir `templates/partials/produtos.html`:

“O for percorre a lista enviada pelo Flask e cria um card por produto. O if verifica disponibilidade e promoção para escolher o badge. Por isso, adicionar um dicionário em app.py atualiza o catálogo sem copiar HTML.”

Mostrar `{% extends "base.html" %}` em `catalogo.html`:

“A herança mantém o menu e o rodapé iguais em todas as páginas.”

## Preparação

- Executar os testes descritos no README.
- Deixar o site e os dois arquivos de código abertos.
- Seguir o teste do item novo no README; reiniciar o servidor depois da alteração.
- Ensaiar com cronômetro. O ensaio e a apresentação são atividades do aluno, não foram realizados pelo assistente.
- Preencher a autoavaliação da apostila com a própria percepção.
