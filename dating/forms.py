from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'user_my_gender', 'user_ur_gender', 'user_description', 'user_login_id', 'user_login_pw')
