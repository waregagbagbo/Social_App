from django import forms
from .models import SocialTweet
from django.contrib.auth.forms import UserCreationForm
''''class SocialForm(forms.ModelForm):
    bod = forms.CharField(required=True, widget = forms.Textarea(attrs={
        "placeholder": "social something...",
        "class": "textarea is so cool..", 
           }      
            ),
        label="",
    )

    class Meta:
        model = SocialTweet
        exclude = ('user',)'''

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
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)