"""
Views for the user API.
"""
#Views define how we handle requests
from django.shortcuts import render

#rest_framework handles a lot of the logic we need to create objects in our database for us
#it does that by providing a bunch of base classes that we can configure for our views that will handle the request
#in a default standarize way, also it give us the ability to override some of that behavior so we can modify it if we need it
from rest_framework import generics

#the custom serializer class we created in serializer.py
from user.serializers import UserSerializer

# Create your views here.

#the CreateAPIView handles an http POST request that is designed for creating objects in our database
#all we need to do is to define the custom serializer and then set the serializer class on this view so DjangoRES framwork knows what serializer we want to use
#recall the serializer has the model define so we know to wich model we creating objects to
#
#once we get a http request, this one goes through the URL (wich is mapped to this View) so this view calls the serializer and create the object and then
#return the appropiate response
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer