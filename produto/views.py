from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto

def lista_produtos(request, slug_da_categoria=None):
    categoria = None
    categorias = Categoria.objects.all().order_by("nome")
    produtos = Produto.objects.all().filter(disponivel=True).order_by("nome")
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria,slug=slug_da_categoria)
        produtos = produtos.filter(categoria=categoria)


    return render(request, 'produto/lista.html', {'categorias': categorias,
                                                  'produtos': produtos,
                                                  'categoria': categoria})


def exibe_produto(request, id, slug_do_produto):
    # Esta view espera receber o id do produto e seu slug para recuperar o produto
    # Podemos recuperar o produto apenas com o seu id uma vez que ele é unique.
    # Incluímos o slug para podermos construir 'SEO friendly URLs'.
    # SEO = Search Engine Optimization.
    # Exemplo: http://www.dominio.com.br/produto?id=721 <== Ruim
    # Exemplo: http://www.dominio.com.br/721/notebook-del-vostro-3458-i3 <== Bom
    produto = get_object_or_404(Produto,id=id, disponivel=True)


    return render(
        request, 'produto/exibe.html', {'produto': produto})

    # Esta view é utilizada para exibir um determinado produto
    # Este URLconf trata requisições para http://localhost:8000/6/smartphone-samsung-galaxy-s8-plus/
    # url(r'^(?P<id>\d+)/(?P<slug_do_produto>[-\w]+)/$', views.exibe_produto, name='exibe_produto'),
