"""
URLs mapping for the User API.
"""
from django.urls import path
from user import views

#this will be used for the reverse mapping in 'test_user_api.py' file
# the line CREATE_USER_URL = reverse('user:create') will find the url because
# we define the app_name = user here (inside urls.py)
app_name = 'user'

urlpatterns = [
    #here we define the create/ url, and those will be handled by the CreateUserView we created in 'views.py'
    #the .as_view() is to create the supported Django view from our custom view
    #note that the name we give it 'create' is the one we will look for in the reverse fucntion explained above
    path('create/', views.CreateUserView.as_view(), name='create'),

]

#dont forget to connect the view in our main app!!!!!!