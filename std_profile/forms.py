from django import forms

from .models import *


class Std_profileForm(forms.ModelForm):
    
    class Meta:
        model = Std_profile
        fields = ("image","first_name","last_name","date_of_birth","age","gender","state","city_street","postal_code","email","phone_number","secondary_rate","mother_lunguage","pyment_method","created_at","university_message",)