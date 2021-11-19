from .serializers import ProfileSerializer, GetUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from .models import Profile
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
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
            token,created=Token.objects.get_or_create(user=user)
            data['response'] = "success"
            data['email'] = user.email
            data['username'] = user.username
            data['phone'] = user.phone
            data['identification'] = user.identification
           # data['thumbnail'] = user.thumbnail
        else:
            data = serializer.errors
        return Response(data)

def GetUser(request):
    id=request.session['pk']
    print(id)
    user=Profile.objects.get(pk=id)
    serializer=GetUserSerializer(user,many=False)
    
    return Response(serializer.data)
    

 
    
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        self.request.session['pk']=user.pk
        print(request.session['pk'])
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username,
        })