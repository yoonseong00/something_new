from django import forms

from .models import Kakaomap

class KakaomapForm(forms.ModelForm):

    class Meta:
        model = Kakaomap
        fields = ('__all__')