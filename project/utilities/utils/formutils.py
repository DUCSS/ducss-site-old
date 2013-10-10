
from django import forms
from django.template.loader import render_to_string

def get_post_params(request):
    ''' Return a tuple of (GET|POST, FILES) params from a request. Where they are not set, return a tuple of Nones.

    The returned tuple is suitable for the construction of a form.
    '''
    if request.method == 'POST':
        return (request.POST, request.FILES)
    else:
        return (None, None)


def init_form(FormClass, request, *form_args, **form_kwargs):
    ''' Create an instance of the given FormClass, bound to post data if appropriate.

    FormClass -- The Django.forms.Form class to instantiate.
    request -- The HTTP request object.
    '''
    if request.method == 'POST':
        # Look for a form_ID in the POST data (see the get_form_ID_field function).
        form_id = request.POST.get('form_id')
        # If it's not set, or matches the given FormClass, bind the data to the form.
        if form_id in (None, FormClass.__name__):
            return FormClass(*form_args, data=request.POST, files=request.FILES, **form_kwargs)

    # All other cases, return an unbound form.
    return FormClass(*form_args, **form_kwargs)

class ColorPickerWidget(forms.TextInput):

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return rendered + render_to_string("utilities/color_picker.js", {'name': name})

