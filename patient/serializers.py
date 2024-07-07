from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    
    # StringRelatedField for nested serializers
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Patient
        fields = '__all__'


# crating serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    # extra 'confirm password' field for UserRegistration
    confirm_password = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error' : "Password Doesn't Matched."})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error' : "Email Already Exists."})
        
        account = User(username = username, email = email, first_name = first_name, last_name = last_name)
        print(account)

        account.set_password(password)
        account.is_active = False   # initially set to False, will be true after activation link validation

        account.save()
        return account
    



# creating login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=20)
    password = serializers.CharField(required=True, max_length=20)

