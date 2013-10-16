from django import forms
from django.conf import settings
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, ButtonHolder, Row, Hidden, HTML, Div

class ContactForm(forms.Form):
    '''Contact us email form'''

    name = forms.CharField(
            max_length=100,
            label="Name",
            widget=forms.TextInput(attrs={'placeholder':"Name"})
        )
    email = forms.EmailField(
            max_length=200,
            label="Email",
            widget=forms.TextInput(attrs={'placeholder':"Email"})
        )
    message = forms.CharField(
            max_length=10000,
            widget=forms.Textarea(attrs={'placeholder':"Write your message here..."})
        )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = 'hidden' # hide the labels as we have defined placeholders for this form
        self.helper.add_input(Submit('submit', 'Send Message'))

    def save(self):
        '''Send the email using the validated form data'''
        name = self.cleaned_data.get('name')
        message = self.cleaned_data.get('message')
        from_email = self.cleaned_data.get('email')
        
        send_mail('CONTACT from %s' % name, message, from_email,
            [settings.CONTACT_US_EMAIL], fail_silently=False)