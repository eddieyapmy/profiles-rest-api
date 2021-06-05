from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Return a list of APIView Features"""
        
        an_apiview = [
            
                'Uses HTTP as function (get, post, patch, put, delete)',
                'Is similar to a traditional Django View',
                'Give you the most control over your application logic',
                'Is mapped manually to URLs'
                ]   
        
        return Response({'message':'Hello','an_apiview': an_apiview}) 
    
    def post (self, request):
        """Create a Hello message with our name"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        
    def put (self, request,pk=None):
        """Handle updating an object"""
        
        return Response({'method':'PUT'})
    
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Handle a delete of an object"""
        
        return Response({'method':'DELETE'})
    
        
    
class HelloViewSet(viewsets.ViewSet):
    """Test APi Viewset"""
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return a hello meesage"""
        
        a_viewset = [
            'Users actions (list, create, retrieve, update, paetial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        
        return Response({'message':'Hello','a+viewset':a_viewset})
    
    
    def create(self, request):
        """Create a new hello message"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
            
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Handle update an object by its ID"""
            
        return Response({'http_method':'PUT'})
        
    def partial(self, request, pk=None):
        """Handle partial update an object by its ID"""
            
        return Response({'http_method':'PATCH'})
 
 
    def destroy(self, request, pk=None):
        """Handle remove an object by its ID"""
            
        return Response({'http_method':'DELETE'})       
    
    
    
    
    
    
        
    
    
    
    
        

        
        
        
        
        
        
        
        
        


