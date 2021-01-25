from rest_framework import serializers

from api_yarns.models import YarnsModels


class YarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = YarnsModels
        fields = '__all__'
