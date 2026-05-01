from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('cliente','Cliente'),
        ('funcionario','Funcionario'),
        ('gestor','Gestor'),
    ]
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='cliente'        
    )
    telefone= models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, blank= True, unique=True, null=True)
    rg = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    
    cep = models.CharField(max_length=10, blank=True)
    logradouro = models.CharField(max_length=200, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    
    foto = models.ImageField(upload_to='fotos_perfil/', null =True, blank=True)
    
    class Meta:
        verbose_name ='Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f'{self.get_fullname() or self.username} ({self.get_tipo_display()})'

    @property
    def is_cliente(self):
        return self.tipo == 'cliente'
    @property
    def is_funcionario(self):
        return self.tipo == 'funcionario'

    @property
    def is_gestor(self):
        return self.tipo == 'gestor'