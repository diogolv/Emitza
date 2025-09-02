from django.db import models
from django.contrib.auth.models import User

TIPO_CONTA_CHOICES = (('standard', 'Standard'), ('premium', 'Premium'))
TIPO_SERVICO_CHOICES = (('firewall', 'Firewall & Segurança'), ('backup', 'Backup'), ('consultoria', 'Consultoria em Segurança'), ('zabbix', 'Monitoramento (Zabbix)'), ('ia', 'Soluções de IA'), ('outro', 'Outro'))
PRIORIDADE_CHOICES = (('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta'))
STATUS_CHOICES = (('aberto', 'Aberto'), ('em_andamento', 'Em Andamento'), ('fechado', 'Fechado'))

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_conta = models.CharField(max_length=10, choices=TIPO_CONTA_CHOICES, default='standard')
    def __str__(self):
        return f"Perfil de {self.usuario.username}"

class Chamado(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    tipo_servico = models.CharField(max_length=20, choices=TIPO_SERVICO_CHOICES, default='outro')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='baixa')
    sistema_afetado = models.CharField(max_length=100, blank=True, null=True, help_text="Opcional: Qual sistema ou equipamento está com problema?")
    def __str__(self):
        return f"#{self.id} - {self.titulo}"