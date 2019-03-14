from django import forms
from .models import Contacto

class FormularioContacto(forms.ModelForm):

    class Meta:
        model = Contacto

        fields = [
            'name',
            'email',
            'message',
        ]
        labels = {
            'name':'Name',
            'Email':'Email',
            'Message':'Message',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={}),
            'correo': forms.TextInput(attrs={}),
            'mensaje': forms.Textarea(attrs={}),

}
