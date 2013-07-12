from horizon import tabs
import utils
from horizon import exceptions

import json
from django import http
from django.utils.translation import ugettext_lazy as _


from .tables import FlockingInstancesTable
from .tabs import FlockingTabs

class IndexView(tabs.TabbedTableView):
    tab_group_class = FlockingTabs
    table_class = FlockingInstancesTable
    template_name = 'visualizations/flocking/index.html'

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            try:
                instances = utils.get_fake_instances_data(self.request)
            except:
                instances = []
                exceptions.handle(request,
                                  _('Unable to retrieve instance list.'))
            data = json.dumps([i._apiresource._info for i in instances])
            return http.HttpResponse(data)
        else:
            return super(IndexView, self).get(request, *args, **kwargs)