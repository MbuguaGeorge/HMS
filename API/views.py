from .serializers import ProfileSerializer, ListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from .models import Profile
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Create your views here.
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def registration(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            data['response'] = "success"
            data['email'] = user.email
            data['username'] = user.username
            data['phone'] = user.phone
            data['identification'] = user.identification
            data['token']=token.key
           # data['thumbnail'] = user.thumbnail
        else:
            data = serializer.errors
        return Response(data)

class userList(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListSerializer

    def get_queryset(self):
        return Profile.objects.all()
