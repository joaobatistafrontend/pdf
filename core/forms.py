from django import forms
from .models import Agenda
from django.utils.safestring import SafeString


class AgendaForm(forms.ModelForm):
    # Função que coloca uma classe nas divs dos inputs
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='input-div'>"))
    
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': '', 'class': 'form-data'}),
        label=''
    )
    horario = forms.ChoiceField(
        choices=[
            (f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
            for hour in range(8, 17) for minute in (0, 30)
        ] + [('', 'Selecione um horário')],
        widget=forms.Select(attrs={'class': 'form-hora'}),
        label=''
    )
    class Meta:
        model = Agenda
        fields = ['nome', 'telefone', 'email', 'locais', 'produtos', 'horario','data']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            'locais': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': '', # Rótulo vazio para 'nome'
            'telefone': '',  # Rótulo vazio para 'telefone'
            'email': '',  # Rótulo vazio para 'email'
            'locais': '',  # Rótulo vazio para 'local'
            'produtos': '',  # Rótulo vazio para 'opcao'
            'data': '',  # Rótulo vazio para 'data'
        }  
        
    def __init__(self, *args, **kwargs):
        super(AgendaForm, self).__init__(*args, **kwargs)
        self.fields['locais'].empty_label = 'Escolha um local'
        self.fields['produtos'].empty_label = 'Escolha um produto'

