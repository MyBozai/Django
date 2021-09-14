from django import forms
from travel.models import User,Search,PlaceAddress

class UserFormRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']

class UserFormLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class SearchPlace(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['place']

class FindPlace(forms.ModelForm):
    class Meta:
        model = PlaceAddress
        fields = ['find']