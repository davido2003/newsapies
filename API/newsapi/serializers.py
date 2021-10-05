from rest_framework import serializers
from . models import NewsApi
from django.db.models import fields 

class NewsApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsApi
        fields = [ 'title','images','description','date']
