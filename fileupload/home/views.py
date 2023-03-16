from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def download(request, uid):
    return render(request,'download.html',context = {'uid':uid})

# class HandleFileUpload(APIView):
#     def post(self,request):
#         try:
#             data = request.data
#             serializer = FileListSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 print(serializer.data)
#                 return Response({
#                     'status':200,
#                     'message':'files uploaded successfully',
#                     'data' : serializer.data
#                 })

#             return Response({
#                 'status': 400,
#                 'message':'something went wrong',
#                 'data':serializer.errors
#             })
#         except Exception as e:
#             print("asish",e)

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)
            if serializer.is_valid():
                folder = serializer.create(serializer.validated_data)['folder']
                return Response({
                    'status': 200,
                    'message': 'files uploaded successfully',
                    'data': {'folder': folder}
                })
            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print("asish", e)
