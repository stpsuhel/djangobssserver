from rest_framework import serializers
from useraccount.models import Amount


class AmountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Amount
        fields = '__all__'
