from rest_framework import serializers
from .models import Profile
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):

   #password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'phone', 'identification', 'thumbnail')
        extra_kwargs = {
            'password' : {'write_only' : True} 
        }
    def save(self):
        user = Profile(
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
            identification = self.validated_data['identification'],
            phone = self.validated_data['phone'],
            #thumbnail = self.validated_data['thumbnail'],
        )
        password = self.validated_data['password']
        #password2 = self.validated_data['password2']

        # if password != password2:
        #     raise serializers.ValidationError({'password' : 'passwords must match'})
        user.set_password(password)
        user.save()
        return user

        
class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username','email')     