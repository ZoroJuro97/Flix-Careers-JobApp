from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe 

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

        labels ={
            'fist_name' :_('Enter first name'),
            'last_name' :_('Enter last name'),
            'email' :_('Enter email')
        }

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)