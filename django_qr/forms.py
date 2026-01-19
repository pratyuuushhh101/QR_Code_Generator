from django import forms


class QRCodeForm(forms.Form):
    restaurant_name=forms.CharField(
        max_length=150,
        label="Restaurant name",
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'enter restaurant name',
        })
    )
    url=forms.URLField(
        label="menu url",
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'enter url of the menu',
        })
        )