from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.CharField(max_length=200,db_index=True)
    destaque = models.BooleanField(default=False)
    outraCategoria=models.BooleanField(default=False)

    class Meta:
        db_table='categoria'

    def get_absolute_path(self):
        return reverse('produto:lista_produtos_por_categoria', args=[self.slug])

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.PositiveIntegerField()
    novidade = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    codigo = models.CharField(max_length=200, db_index=True)
    nota = models.IntegerField(db_index=True)

    class Meta:
        db_table = 'produto'

    def get_absolute_path(self):
        return reverse('produto:exibe_produto', args=[self.id, self.slug])

    def __str__(self):
        return self.nome
    def img_as_list(self):
        imagens = self.imagem.split(",")
        return imagens
class Cliente(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    sobrenome= models.CharField(max_length=200, db_index=True)
    email = models.CharField(max_length=200, db_index=True)
    senha = models.CharField(max_length=200, db_index=True)

    class Meta:
        db_table='cliente'
    def __str__(self):
        return self.nome + " "+ self.sobrenome