from rest_framework import serializers
from clientes.models import Cliente
from .validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    # primeiro modo de fazer validações
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'Número de CPF inválido'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'Celular deve conter 11 caracteres'})
        return data

    # segundo modo de fazer validações
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('Não inclua números no nome')
        return nome

    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('RG deve conter 9 caracteres')
        return rg
