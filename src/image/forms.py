from django import forms
from .models import *
class PhotoForm(forms.ModelForm):
    """Form definition for Photo."""

    class Meta:
        """Meta definition for Photoform."""

        model = Photo
        fields = ('title', 'image', )
