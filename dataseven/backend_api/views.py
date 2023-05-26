from django.shortcuts import render
from rest_framework.views import APIView
from .models import OneTest
from .serializer import OneTestSerializer
from rest_framework.response import Response
# Create your views here.


class OneTestView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "channel": output.channel
            } for output in OneTest.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = OneTestSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer)
