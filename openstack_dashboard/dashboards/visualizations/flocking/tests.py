from django.core.urlresolvers import reverse
from django import http

from mox import IsA

from openstack_dashboard import api
from openstack_dashboard.test import helpers as test

INDEX_URL = reverse('horizon:visualizations:flocking:index')
class FlockingTests(test.TestCase):
    # Unit tests for flocking.

    def test_index(self):

        res = self.client.get(INDEX_URL)
        self.assertTemplateUsed(res, 'visualizations/flocking/index.html')
        #self.assertIn(res.context_data.tabgroup.slug, 'flocking'
        self.assertTrue(res.context_data['tab_group'].slug, 'flocking')
        tabs = res.context_data['tab_group'].tabs
        self.assertTrue(len(tabs), 2)
        self.assertTrue(tabs[0].slug, 'viz')
        self.assertTrue(tabs[1].slug, 'data')
