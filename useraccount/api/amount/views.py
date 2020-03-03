
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from useraccount.models import Amount
from useraccount.api.amount.serializers import AmountSerializer


@api_view(['GET'])
def get_user_all_payment(request, user):
    try:
        allAmountList = Amount.objects.all(user=user)
    except Amount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AmountSerializer(allAmountList, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_payment(request):
    try:
        allAmountList = Amount.objects.all()
    except Amount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AmountSerializer(allAmountList, many=True)
    return Response(serializer.data)
