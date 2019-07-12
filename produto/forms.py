from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from produto.models import Produto, Categoria
from projeto import settings


from produto.models import Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =('cliente_id','nome','sobrenome', 'email', 'senha')
    cliente_id = forms.CharField(widget=forms.HiddenInput(),required=False)
    nome = forms.CharField(
       error_messages={'required': 'Campo obrigatório.', },
       widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
       required=True)
    sobrenome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)
    email =forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)
    senha = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)
class RemoveProdutoForm(forms.Form):
    class Meta:
        fields = ('produto_id')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=True)

    def get_produto_id(self):
        return self.cleaned_data["produto_id"]


