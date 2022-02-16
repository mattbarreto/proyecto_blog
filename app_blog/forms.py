from django.forms import DateField, Form, ImageField, IntegerField, DecimalField, CharField, EmailField


class AvatarFormulario(Form):
    imagen = ImageField(required=True)