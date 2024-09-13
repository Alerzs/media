from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import SocialSerializer , PostSerializer
from .models import SocialUser , Post
from rest_framework.permissions import IsAuthenticated ,IsAdminUser ,AllowAny
from rest_framework.response import Response



class Login(TokenObtainPairView):
    pass


class Myfollowers(generics.ListAPIView):
    queryset = SocialUser.objects.all()
    serializer_class = SocialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        my_user = SocialUser.objects.get(user = self.request.user)
        return my_user.followers
    


class SocialPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "GET":
            self.permission_classes = [AllowAny]
        return super(SocialPost, self).get_permissions()

    def list(self, request, *args, **kwargs):
        if self.permission_classes == [IsAuthenticated]:
            my_user = SocialUser.objects.get(user = self.request.user)
            my_followers = my_user.followers
            show = []
            for item in my_followers:
                for pitem  in Post.objects.all():
                    if pitem.user == item:
                        show.append({
                            PostSerializer(pitem)
                        })
            return Response(show)
        else:
            return Post.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    

class Follow(generics.UpdateAPIView):
    queryset = SocialUser.objects.all()
    serializer_class = SocialSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        following = serializer.instance
        follower = SocialUser.objects.get(user = self.request.user)
        follower.followers = following
        serializer.save()
        return super().perform_update(serializer)


    
