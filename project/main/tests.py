from freezegun import freeze_time

from django.conf import settings
from django.core.urlresolvers import reverse

from main.forms import ContactForm
from utilities.utils import CleanTestCase

class ViewsTest(CleanTestCase):
    '''Tests for the views in the main app'''
    fixtures = [
        'events.json',
        'services.json'
    ]

    @freeze_time("2013-10-01")
    def test_home_page_view(self):
        '''Tests the home page view produces the right context 
        from the dev fixtures data.
        '''
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['home_page'])
        
        # test the test event data is being loaded
        events = resp.context['events']
        self.assertEqual(len(events), 4) # ensure max number is loaded
        self.assertEqual(events[0].id, 3) # ensure the date ordering has worked
        self.assertEqual(events[1].id, 2)
        
        # test that the test fixture services are being loaded into the context
        services = resp.context['services']
        self.assertEqual(len(services), 3)
        self.assertEqual(services[0].title, "Events")


class ContactFormTest(CleanTestCase):
    '''Tests the contact form'''

    def test_post(self):
        '''Test posting invalid data to the form handler returns
        the appropiate error message and that posting valid data
        return a 302 redirect.
        '''
        # post no data returns data required error message
        resp = self.client.post(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['contact_form']['name'].errors[0], "This field is required.")

        # post invalid email address returns invalid email error message
        data = {
            'name': 'Testing Client',
            'email': 'me.@example.com',
            'message': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
        }
        resp = self.client.post(reverse('home'), data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['contact_form']['email'].errors[0], "Enter a valid e-mail address.")

        # post expected data
        data = {
            'name': 'Testing Client',
            'email': 'me@example.com',
            'message': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
        }
        resp = self.client.post(reverse('home'), data)
        self.assertEqual(resp.status_code, 302) # redirect is done when the email is done