from django import forms
from .models import Chamado

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'tipo_servico', 'prioridade', 'sistema_afetado', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex: Problema ao acessar o sistema'}),
            'sistema_afetado': forms.TextInput(attrs={'placeholder': 'Ex: Servidor de Arquivos, PC da Recepção'}),
            'descricao': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Descreva o problema ou solicitação com o máximo de detalhes possível.'}),
        }