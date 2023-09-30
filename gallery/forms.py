from django import forms
from gallery.models import Photo




class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['signature', 'image']
        widgets = {
            'signature': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_signature'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control mb-3', 'id': 'id_image'}),
        }