from rest_framework import serializers
from .models import Comercio
#from core.serializers import ComunidadeSerializer, CategoriaSerializer


class ComercioSerializer(serializers.ModelSerializer):
    #comunidade = ComunidadeSerializer()
    #listaCategorias =CategoriaSerializer(many = True)

    class Meta:
        model = Comercio
        fields = ('nomeDoProprietario', )
