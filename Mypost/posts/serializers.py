from rest_framework import serializers
from .models import *



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('text', 'pub_date')