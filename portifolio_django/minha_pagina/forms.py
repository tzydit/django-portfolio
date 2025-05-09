from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class': 'form-control'}))
