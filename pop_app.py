import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evolution.settings')

import django
from datetime import datetime

django.setup()

from evolution_app.models import *
from faker import Faker
import random
import decimal

fakegen = Faker()


def create_client():
    client = Cliente(
        cpf=fakegen.bothify(text='###########'),
        rg=fakegen.bothify(text='#########'),
        telefone=fakegen.phone_number(),
        celular=fakegen.phone_number(),
        nome=fakegen.name(),
        endereco=add_endereco()
    )
    client.save()


def create_dependente():
    dependente = Dependente(
        data_nascimento=datetime.now(),
        sexo='Masculino',
        tipo='Pai',
        nome=fakegen.name(),
        cliente=None
    )


def create_funcionario():
    funcionario = Funcionario(
        cpf=fakegen.bothify(text='###########'),
        rg=fakegen.bothify(text='#########'),
        telefone=fakegen.phone_number(),
        celular=fakegen.phone_number(),
        nome=fakegen.name(),
        endereco=add_endereco(),
        salario=decimal.Decimal(random.randrange(155, 900)),
        gerente=None
    )


def add_endereco():
    Endereco(logradouro=fakegen.address(),
             cidade='SP',
             cep=fakegen.bothify(text='#####-###'),
             estado='SP',
             numero=random.randint(0, 900),
             complemento='Teste')


def add_fornecedor():
    name = fakegen.name
    Fornecedor(nome=name,
               nome_fantasia=name + ' SA',
               cnpj=fakegen.bothify(text='##############'),
               descricao='Descricao de teste',
               data_cadastro=datetime.now()
               )


def add_diretor():
    return Diretor(nome=fakegen.name)


def add_contato():
    contato = Contato.get_.get_or_create()
    contato.save()
    return contato

def create_filme(diretor):
    Filme('Sinopse de um filme', fakegen.name, diretor)

def create_midia(filme):
    Midia(tipo='cd',
          situacao='Aberta',
          filme=filme)

def create_telefone(contato):
    Telefone('Telefone', fakegen.bothify(text='#####-####'), contato)

def create_estoque(filme):
    Estoque(quantidade=random.randint(0, 900),
            filme=filme)


def populate(N=5):
    for entry in range(1):
        create_client()

if __name__ == '__main__':
    print("populating script")
    # populate(20)
    print("complete")
