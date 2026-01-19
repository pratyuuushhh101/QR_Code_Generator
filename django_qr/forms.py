from django import forms


class QRCodeForm(forms.Form):
    restraunt_name=forms.CharField(
        max_length=150,
        label="Restraunt name",
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'enter restraunt name',
        })
    )
    url=forms.URLField(
        label="menu url",
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'enter url of the menu',
        })
        )