from django.forms import ModelForm, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from library.models import Book
from library.models import Reservation

class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        exclude = ('book_id','date_created')
        widgets = {
            "member_name" : TextInput(attrs={"placeholder" : "Your Name"}),
            "email" : TextInput(attrs={"placeholder" : "Your Email"}),
        }
        labels = {
            "member_name": ("name"),
            "email": ("email"),
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Reserve a book',
                'member_name',
                'email'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
