from django import forms
from comcie.models import LogMessage, Musician

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        exclude = ()