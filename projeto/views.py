from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from produto.forms import ClienteForm
from produto.models import Categoria, Produto, Cliente
from django.db.models import Q


def index(request):
    categorias =Categoria.objects.all().order_by("nome")
    produtos = Produto.objects.all().filter(destaque=True).order_by("id")
    categorias_importantes = Categoria.objects.all().filter(destaque=True).order_by('id')
    possiveis_notas = [1,2,3,4,5]
    return render(request,'index.html', {'categorias':categorias,
                                         'produtos':produtos,
                                         'categorias_importantes':categorias_importantes,
                                         "possiveis_notas":possiveis_notas})

def listaProduto(request,id,slug_do_produto):
    produto = get_object_or_404(Produto,id=id)
    categoria = produto.categoria
    produtos = Produto.objects.all().order_by("id")
    produtosSemelhantes = produtos.filter(categoria=categoria)
    possiveis_notas = [1, 2, 3, 4, 5]
    return render(request, 'product.html',{'produto':produto,
                                           'produtosSemelhantes': produtosSemelhantes,
                                           "possiveis_notas":possiveis_notas})
def outrasCategorias(request):
    categorias = Categoria.objects.all().filter(outraCategoria=True).order_by("nome")
    return render(request,'categories.html',{'categorias':categorias})

def cart(request):
    return render(request,'cart.html')



def cadastra_cliente(request):
    if request.POST:
        cliente_id = request.POST.get('cliente_id')
        if cliente_id:
            cliente = get_object_or_404(Produto, pk=cliente_id)
            cliente_form = ClienteForm(request.POST, instance=cliente)
        else:
            cliente_form = ClienteForm(request.POST)

        if cliente_form.is_valid():
            cliente = cliente_form.save()
            if cliente_id:
                messages.add_message(request, messages.INFO, 'Cliente alterado com sucesso!')
            else:
                messages.add_message(request, messages.INFO, 'Cliente cadastrado com sucesso!')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        cliente_form = ClienteForm()

    return render(request, 'create_client.html', {'form': cliente_form })

def search(request):
    template = 'listProducts.html'

    query = request.GET.get('q')
    produtos = Produto.objects.filter(Q(slug__icontains=query) | Q(nome__icontains=query))

    contexto = {'produtos':produtos}

    return render(request,template,contexto)

def editaSenha(request):
    email = request.POST.get('email')
    cliente = get_object_or_404(Cliente,email=email)
    novaSenha = request.POST.get('pwd')
    cliente.senha=novaSenha
    cliente.save()
    mensagem="Editado com sucesso!"
    return render(request,'edit_client.html',{'mensagem':mensagem})


def showEditaSenha(request):
    return render(request,'edit_client.html')
