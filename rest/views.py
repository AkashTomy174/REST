from rest_framework.decorators import api_view
from rest_framework.response import Response  
from . models import Person
from rest_framework.views import APIView
from .serializers import PersonSerializer
from rest_framework import viewsets


# class Persons(APIView):
#     def get(self,request):
#         obj=Person.objects.all()
#         serializer=PersonSerializer(obj,many=True)
#         return Response(serializer.data)
 

#     def post(self,request):
#         data=request.data
#         serializer=PersonSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     def put(self,request):
#         data=request.data
#         obj=Person.objects.get(id=data['id'])
#         serializer=PersonSerializer(obj,data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     def patch(self,request):
#         data=request.data
#         obj=Person.objects.get(id=data['id'])
#         serializer=PersonSerializer(obj,data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     def delete(self,request):
#         data=request.data
#         obj=Person.objects.get(id=data['id'])
#         obj.delete()
#         return Response({'message':'person deleted'})
     


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def home(request):
    if request.method=="POST":
        data={
       'course':'python', 
       'toutor':'vidhya' 
        }
        print('for post')
        data=request.data
        print(data)
        return Response(data)
    elif request.method=="GET":
        data={
       'course':'python', 
       'toutor':'vidhya' 
        }
        print('for get')
        return Response(data)
  
# @api_view(['GET','POST','PUt','PATCH','DELETE'] ) 
# def person(request):
#     if request.method=="GET":
#         obj=Person.objects.all()
#         serializer=PersonSerializer(obj,many=True)
#         return Response(serializer.data)
#     elif request.method=="POST":
#         data=request.data
#         serializer=PersonSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method=="PUT":
#         data=request.data
#         obj=Person.objects.get(id=data['id'])
#         serializer=PersonSerializer(obj,data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method=="PATCH":
#         data=request.data
#         obj=Person.objects.get(id=data['id'])
#         serializer=PersonSerializer(obj,data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     else:
#         data=request.data
#         obj=Person.objects.get(id=data['id'])
#         obj.delete()
#         return Response({'message':'person deleted'})
    
    
    
class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
     
