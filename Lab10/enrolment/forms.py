from django import forms
from validate_email import validate_email


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Input email')
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        em = self.cleaned_data['email']
        if not validate_email(em):
            raise forms.ValidationError('Invalid email!')
        return em
