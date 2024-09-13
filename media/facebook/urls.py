from django.urls import path
from .views import Follow , SocialPost


urlpatterns = [
    path('follow/' , Follow.as_view()),
    path('poost/' , SocialPost.as_view()),
    
]