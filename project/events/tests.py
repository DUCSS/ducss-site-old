from django.core.urlresolvers import reverse

from utilities.utils import CleanTestCase

class ViewsTest(CleanTestCase):
	'''Tests for all the views in the events app'''
	fixtures = [
        'events.json'
    ]

	def test_event_page_view(self):
		'''Tests the context for the page that shows
		all the details about a certain event
		'''
		resp = self.client.get(reverse('events:event', args=('event1',)))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue(resp.context['event_page'])

	def test_no_event_view_return_404(self):
		'''Tests that if you request an event that doesn't exist
		a HTTP 404 error is returned
		'''
		resp = self.client.get(reverse('events:event', args=('nope',)))
		self.assertEqual(resp.status_code, 404)