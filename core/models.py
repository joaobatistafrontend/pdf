from django.db import models
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.platypus import Image

class Local(models.Model):
    cidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numeracao = models.CharField(max_length=255, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    mapa_link = models.URLField(max_length=1000, null=True, blank=True)
    telefone = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        logradouro = self.logradouro if self.logradouro else ''  # Use o logradouro se não for nulo, caso contrário, uma string vazia
        return f"{self.cidade} - {self.endereco} - {self.numeracao}"
      

class Opcoes(models.Model):
    opcoes = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.opcoes} - {self.valor}"
     
def gerar_protocolo():
    while True:
        protocolo = random.randint(1, 10000000000)
        if not Agenda.objects.filter(protocolo=protocolo).exists():
            return protocolo

class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=30, null=True, blank=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    opcao = models.ForeignKey(Opcoes, on_delete=models.CASCADE)
    horario = models.CharField(
        max_length=5,
        choices=[
            (f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
            for hour in range(8, 17) for minute in (0, 30)
        ]
    )
    data = models.DateField(verbose_name='Data de Agendamento')
    protocolo = models.CharField(max_length=100, default=gerar_protocolo)

