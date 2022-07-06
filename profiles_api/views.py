from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    """Testing API view"""  # based on APIView, defines app logic for our API's endpoint. We define a url (endpoint), assigning it to this view and django framework handles the rquest for the request it receives
    serializer_class = serializers.HelloSerializer #the serializer for this APIView

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_api_view = [
            'Uses HTTP methods as function (GET, POST, PATCH, PUT, DELETE)',
            'Is similar to a traditional Django view, but specifically to be used for APIs',
            'Gives you the most control over your application logic',
            'Mapped manually to URLs',
        ]
        return Response({
            'message': 'Hello', 'an_apiview' : an_api_view
        })

    def post(self,request):
        """Create a hello message with the received name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): # serialiser checks to see if the data it has is valid according to the specifications of the serializer class
            name = serializer.validated_data.get('name') # get the data inside the field titled 'name'
            message = f'Hello {name}. Nice to have you'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST ) # returns the errors that the serializer faced when it tried to validate input
    
    def put(self, request, pk=None): #pk is primary key which serves as the ID of an object to update
        """Handle updating an object"""
        return Response({"method":'PUT'})
    
    def patch(self, request, pk=None): #pk is primary key which serves as the ID of an object to update
        """Handle a partial update of an object"""
        return Response({"method": 'PATCH'})

    def delete(self, request, pk=None): #pk is primary key which serves as the ID of an object to update
        """Delete an object"""
        return Response({"method":'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ViewSet for test api"""
    serializer_class =  serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Usees actions (list, create, retrieve, update, partial_update", 'Automatically maps to URLs using routers', 'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data = request.data)
        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            return Response({'message': f"Hello {name}"})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST ) # returns the errors that the serializer faced when it tried to validate input

    def retrieve(self, request, pk=None):
        """Handle getting an object by ID"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self,request, pk=None):
        """Remove an object"""
        return Response({'http_method': 'DELETE'})

