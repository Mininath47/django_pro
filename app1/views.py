# app1/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Item
from app1.serializers import ItemSerializer

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()  # get all items from the database
        serializer = ItemSerializer(items, many=True)  # serialize the data
        return Response(serializer.data)  # return JSON response with data
