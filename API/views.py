from .serializers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions,generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile

# Create your views here.
@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def registration(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "success"
            data['email'] = user.email
            data['username'] = user.username
            data['phone'] = user.phone
            data['identification'] = user.identification
           # data['thumbnail'] = user.thumbnail
        else:
            data = serializer.errors
        return Response(data)

