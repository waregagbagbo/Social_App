from django import forms
from .models import SocialTweet,Profile
from django.contrib.auth.forms import UserCreationForm


class SocialTweetForm(forms.ModelForm):
    body = forms.CharField(required=True, widget = forms.Textarea(attrs ={
        "placeholder":"social something...",
        "class": "textarea is so cool...",
        }
        ),
        label = "",
    )

    class Meta:
        model = SocialTweet
        exclude =('user',)

        

class CustomUserCreationForm(UserCreationForm):

   # class Meta:
       # fields = ['username','email','password1','password2']

   
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)