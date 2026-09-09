"""ByteStore: cat?logo did?tico com Flask, Jinja2 e Bootstrap."""
import unicodedata

from flask import Flask, render_template, request

app = Flask(__name__)

# ?nica fonte de dados: adicionar um dicion?rio faz o cat?logo crescer sozinho.
# Valores monet?rios em centavos evitam imprecis?o de ponto flutuante.
# Todos os modelos, pre?os e estoques abaixo s?o fict?cios.
produtos = [
    {
        "id": 1, "nome": "Notebook Horizon 14", "categoria": "Notebooks",
        "descricao": "Leve para levar. Potente para criar.",
        "especificacoes": "Tela de 14 polegadas ? 16 GB RAM ? SSD 512 GB",
        "preco": 329900, "preco_anterior": 379900,
        "disponivel": True, "destaque": True, "imagem": "notebook.jpg",
    },
    {
        "id": 2, "nome": "Teclado mec?nico Pulse", "categoria": "Perif?ricos",
        "descricao": "Precis?o em cada tecla, personalidade no seu setup.",
        "especificacoes": "Formato compacto ? Conex?o USB ? Ilumina??o RGB",
        "preco": 24990, "preco_anterior": 32990,
        "disponivel": True, "destaque": True, "imagem": "teclado.jpg",
    },
    {
        "id": 3, "nome": "Mouse sem fio Flow", "categoria": "Perif?ricos",
        "descricao": "Mais liberdade e conforto para o dia inteiro.",
        "especificacoes": "Conex?o sem fio 2,4 GHz ? 1.600 DPI ? 3 bot?es",
        "preco": 12990, "preco_anterior": None,
        "disponivel": True, "destaque": False, "imagem": "mouse.jpg",
    },
    {
        "id": 4, "nome": "Fone de ouvido Studio", "categoria": "?udio",
        "descricao": "Entre no ritmo. Deixe as distra??es de lado.",
        "especificacoes": "Over-ear ? Conex?o P2 ? Almofadas acolchoadas",
        "preco": 18990, "preco_anterior": 24990,
        "disponivel": True, "destaque": True, "imagem": "headset.jpg",
    },
    {
        "id": 5, "nome": "Monitor Vision 24", "categoria": "Monitores",
        "descricao": "Mais espa?o para suas ideias ganharem vida.",
        "especificacoes": "24 polegadas ? Full HD ? 75 Hz ? HDMI",
        "preco": 89990, "preco_anterior": 109990,
        "disponivel": True, "destaque": True, "imagem": "monitor.jpg",
    },
    {
        "id": 6, "nome": "Placa de v?deo Vertex 8", "categoria": "Componentes",
        "descricao": "Um novo n?vel de possibilidades para o seu PC.",
        "especificacoes": "8 GB de mem?ria ? PCI Express ? Sa?das HDMI e DisplayPort",
        "preco": 179990, "preco_anterior": None,
        "disponivel": True, "destaque": False, "imagem": "componentes.jpg",
    },
    {
        "id": 7, "nome": "Notebook Horizon Pro 15", "categoria": "Notebooks",
        "descricao": "Espa?o e desempenho para projetos maiores.",
        "especificacoes": "Tela de 15,6 polegadas ? 32 GB RAM ? SSD 1 TB",
        "preco": 489900, "preco_anterior": None,
        "disponivel": False, "destaque": False, "imagem": "notebook.jpg",
    },
    {
        "id": 8, "nome": "Mouse Precision Pro", "categoria": "Perif?ricos",
        "descricao": "Controle e agilidade em cada movimento.",
        "especificacoes": "Conex?o USB ? 6.400 DPI ? 6 bot?es",
        "preco": 17990, "preco_anterior": 21990,
        "disponivel": False, "destaque": False, "imagem": "mouse.jpg",
    },
]


def normalizar(texto):
    """Busca ignora acentos, mai?sculas e espa?os nas extremidades."""
    return "".join(
        caractere for caractere in unicodedata.normalize("NFD", texto.casefold().strip())
        if not unicodedata.combining(caractere)
    )


def em_oferta(produto):
    anterior = produto.get("preco_anterior")
    return bool(produto["disponivel"] and anterior and anterior > produto["preco"])


@app.template_filter("moeda")
def moeda(centavos):
    inteiro, decimal = divmod(centavos, 100)
    return f"R$ {inteiro:,}".replace(",", ".") + f",{decimal:02d}"


@app.template_filter("desconto")
def desconto(produto):
    if not em_oferta(produto):
        return 0
    return (produto["preco_anterior"] - produto["preco"]) * 100 // produto["preco_anterior"]


@app.context_processor
def utilitarios_template():
    return {"em_oferta": em_oferta}


@app.route("/")
def inicio():
    categorias = sorted({p["categoria"] for p in produtos})
    destaques = [p for p in produtos if p["destaque"] and p["disponivel"]][:4]
    return render_template("inicio.html", produtos=destaques, categorias=categorias)


@app.route("/catalogo")
def catalogo():
    busca = request.args.get("q", "").strip()
    categoria = request.args.get("categoria", "").strip()
    categorias = sorted({p["categoria"] for p in produtos})
    encontrados = [
        p for p in produtos
        if (not categoria or p["categoria"] == categoria)
        and (not busca or normalizar(busca) in normalizar(
            f'{p["nome"]} {p["descricao"]} {p["categoria"]} {p["especificacoes"]}'
        ))
    ]
    return render_template(
        "catalogo.html", produtos=encontrados, categorias=categorias,
        busca=busca, categoria=categoria,
    )


@app.route("/ofertas")
def ofertas():
    selecionados = [p for p in produtos if em_oferta(p)]
    return render_template("ofertas.html", produtos=selecionados)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
