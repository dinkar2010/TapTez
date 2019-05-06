from taptez.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'id')



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ('user_first_name',
                  'user__last_name',
                  'user__username',
                  'user__email',
                  'id',
                  'district',
                  'state')