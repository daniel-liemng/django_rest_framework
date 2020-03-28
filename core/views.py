from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .models import Post


# Create your views here.

class TestView(APIView):
    # def get(self, request, *args, **kwargs):
    #     data = {
    #         'name': 'john',
    #         'age': 23
    #     }
    #     return Response(data)

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # serializer = PostSerializer(qs, many=True)

        post = qs.first()
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }

#     return JsonResponse(data)
