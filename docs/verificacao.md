# Verificação da ByteStore

Validação realizada em 9 de setembro de 2026.

## Resultados

- 11 testes automatizados do Flask passaram.
- Quatro páginas principais com HTTP 200 e navegação completa.
- Página inexistente retorna HTTP 404 com layout compartilhado.
- Oito produtos no catálogo; quatro produtos disponíveis em oferta.
- Inclusão de item novo verificada sem modificar HTML, incluindo categoria nova e oferta.
- Busca sem acentos e sem distinção de maiúsculas, filtros combinados e lista vazia verificados.
- Entrada de busca com HTML escapada pelo Jinja2.
- Imagens, Bootstrap, CSS e favicon locais carregando corretamente.
- Testes em Chrome isolado: busca, categoria, especificações expansíveis e menu móvel.
- Ausência de rolagem horizontal nas quatro páginas em larguras de 375, 768, 1024 e 1440 pixels.
- Nenhum erro JavaScript capturado no teste.
- Capturas da página inicial em computador e celular inspecionadas visualmente.

## Revisão complementar

- Os 11 testes do Flask e os testes de navegador foram repetidos com sucesso.
- `pip check` não apontou dependências incompatíveis no ambiente instalado.
- Repositório público confirmado: https://github.com/wilsonvieiradeoliveira/pi_mini-projeto_1; a branch `main` remota estava em `d1d12f4` antes das correções desta revisão.
- Ambiente virtual, arquivos temporários e apostila estão fora dos arquivos versionados.
- Documentação corrigida: o conjunto de versões fixadas requer Python 3.10 ou superior, pois Click 8.5.0 exige essa versão.
- Encontrada rolagem horizontal em busca com palavra muito longa; corrigida a quebra de linha do resumo de resultados.
- Primeira parada de teclado confirmada no link “Pular para o conteúdo”.
- As pendências escolares abaixo dependem de realização ou confirmação pelo aluno/professor; não indicam falta de funcionalidade no site.

## Como repetir

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Os testes permanentes estão em `tests/test_app.py`. O teste de navegador e as capturas ficam em `tmp/qa/`, fora do Git; não são dependências da aplicação.

## Demonstração local

A instância preparada nesta sessão está em http://127.0.0.1:5050 porque havia outro servidor na porta 5000. Para executar nessa porta em outro momento:

```powershell
.\.venv\Scripts\python.exe -m flask --app app run --port 5050
```

O comando padrão `python app.py` continua usando a porta 5000. Após alterações no Python ou nos templates, reinicie o servidor: o modo debug está desativado.

## Itens humanos ou externos pendentes

- Enviar ao GitHub as correções locais desta revisão, após autorização do usuário.
- Validação docente da ficha, se exigida na aula.
- Autoavaliação individual e ensaio do pitch.
- Apresentação ao vivo.

Nenhuma nota foi atribuída e nenhuma dessas atividades foi declarada como concluída. Os commits correspondem às etapas reais desta sessão; o histórico não simula períodos de aula.
