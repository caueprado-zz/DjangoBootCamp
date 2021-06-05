from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=264, unique=True)
    cidade = models.CharField(max_length=264, unique=True)
    cep = models.CharField(max_length=9, unique=True)
    estado = models.CharField(max_length=2, unique=True)
    complemento = models.CharField(max_length=100, unique=True)
    numero = models.IntegerField()

    def __str__(self):
        return self.logradouro


class Pessoa(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    telefone = models.CharField(max_length=9, unique=True)
    celular = models.CharField(max_length=9, unique=True)
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


class Cliente(Pessoa):
    pass


class Funcionario(Pessoa):
    gerente = models.ForeignKey('self', on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)


class Dependente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=256, unique=True)
    tipo = models.CharField(max_length=256, unique=True)
    sexo = models.TextChoices('Masculino', 'Feminino')
    data_nascimento = models.DateField()


class Diretor(models.Model):
    nome = models.CharField(max_length=256, unique=True)


class Filme(models.Model):
    descricao = models.CharField(max_length=256, unique=True)
    titulo = models.CharField(max_length=256, unique=True)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)


class Midia(models.Model):
    tipo = models.CharField(max_length=256, unique=True)
    situacao = models.CharField(max_length=10)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)


class Aluguel(models.Model):
    data = models.DateTimeField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    midia = models.ManyToManyField(Midia)


class Estoque(models.Model):
    quantidade = models.IntegerField()
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)


class Fornecedor(models.Model):
    nome = models.CharField(max_length=256, unique=True)
    nome_fantasia = models.CharField(max_length=256, unique=True)
    cnpj = models.CharField(max_length=256, unique=True)
    descricao = models.CharField(max_length=256, unique=True)
    data_cadastro = models.DateTimeField()


class MidiaCompra(models.Model):
    midia = models.ForeignKey(Midia, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(max_length=10)
    data_pedido = models.DateField()
    data_entrega = models.DateField()
    quantidade = models.IntegerField()


class Contato(models.Model):
    nome = models.CharField(max_length=256, unique=True)
    email = models.EmailField()
    data_contato = models.DateTimeField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    tipo = models.CharField(max_length=256, unique=True)
    numero = models.CharField(max_length=256, unique=True)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)

##qunatidade disponivel total em estoque menos alugados e não devolvidos