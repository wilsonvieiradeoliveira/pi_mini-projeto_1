"""Verificações dos requisitos da apostila. Executar: python -m unittest discover -s tests -v."""
import re
import unittest
from unittest.mock import patch

from app import app, produtos, moeda


class ByteStoreTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def html(self, rota, **kwargs):
        response = self.client.get(rota, **kwargs)
        self.assertEqual(response.status_code, 200)
        return response.get_data(as_text=True)

    def test_paginas_menu_e_recursos_locais(self):
        for rota in ["/", "/catalogo", "/ofertas", "/sobre"]:
            with self.subTest(rota=rota):
                html = self.html(rota)
                self.assertIn('lang="pt-BR"', html)
                self.assertIn('aria-current="page"', html)
                self.assertIn("Loja demonstrativa", html)
                for destino in ["/", "/catalogo", "/ofertas", "/sobre"]:
                    self.assertIn(f'href="{destino}"', html)
                for arquivo in set(re.findall(r'(?:src|href)="(/static/[^"]+)"', html)):
                    with self.client.get(arquivo) as response:
                        self.assertEqual(response.status_code, 200, arquivo)

    def test_catalogo_exibe_todos_os_produtos(self):
        html = self.html("/catalogo")
        self.assertEqual(len(re.findall(r'<article class="card product-card', html)), len(produtos))
        for produto in produtos:
            self.assertIn(produto["nome"], html)

    def test_busca_ignora_acentos_e_maiusculas(self):
        html = self.html("/catalogo", query_string={"q": "  MECANICO  "})
        self.assertIn("Teclado mecânico Pulse", html)
        self.assertNotIn('id="produto-1"', html)
        self.assertIn("1 produto encontrado", html)

    def test_categoria_e_busca_combinadas(self):
        html = self.html("/catalogo", query_string={"categoria": "Periféricos", "q": "mouse"})
        self.assertIn("Mouse sem fio Flow", html)
        self.assertIn("Mouse Precision Pro", html)
        self.assertNotIn("Teclado mecânico Pulse", html)
        self.assertNotIn("Notebook Horizon 14", html)

    def test_busca_sem_resultados_e_categoria_inexistente(self):
        for params in [{"q": "produto-inexistente"}, {"categoria": "Inexistente"}]:
            html = self.html("/catalogo", query_string=params)
            self.assertIn("Nenhum produto encontrado.", html)
            self.assertIn("Limpar filtros", html)

    def test_busca_escapa_html(self):
        html = self.html("/catalogo", query_string={"q": '<script>alert("x")</script>'})
        self.assertNotIn('<script>alert("x")</script>', html)
        self.assertIn("&lt;script&gt;", html)

    def test_ofertas_excluem_itens_indisponiveis_e_preco_normal(self):
        html = self.html("/ofertas")
        self.assertIn("Notebook Horizon 14", html)
        self.assertIn("Teclado mecânico Pulse", html)
        self.assertNotIn("Mouse Precision Pro", html)
        self.assertNotIn("Mouse sem fio Flow", html)
        self.assertNotIn("Placa de vídeo Vertex 8", html)
        self.assertIn("24% OFF", html)

    def test_lista_vazia(self):
        with patch("app.produtos", []):
            for rota in ["/", "/catalogo", "/ofertas"]:
                self.assertIn("Nenhum produto encontrado.", self.html(rota))

    def test_item_novo_aparece_sem_alterar_template(self):
        novo = {
            **produtos[0], "id": 99, "nome": "Webcam de teste",
            "categoria": "Webcams", "preco": 10000, "preco_anterior": 20000,
        }
        with patch("app.produtos", produtos + [novo]):
            html = self.html("/catalogo")
            self.assertIn("Webcam de teste", html)
            self.assertIn('<option value="Webcams"', html)
            self.assertIn("Webcam de teste", self.html("/ofertas"))
            filtrado = self.html("/catalogo", query_string={"categoria": "Webcams"})
            self.assertIn("1 produto encontrado", filtrado)
            self.assertIn("Webcam de teste", filtrado)

    def test_preco_brasileiro_em_centavos(self):
        self.assertEqual(moeda(329900), "R$ 3.299,00")
        self.assertEqual(moeda(12990), "R$ 129,90")
        self.assertEqual(moeda(0), "R$ 0,00")

    def test_pagina_404(self):
        response = self.client.get("/caminho-inexistente")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Esse caminho não existe.", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
