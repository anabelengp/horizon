from .tables import FlockingInstancesTable
from horizon import tabs
from django.utils.translation import ugettext_lazy as _
from horizon import exceptions
import utils

class DataTab(tabs.TableTab):
    name = _("Data")
    slug = "data"
    table_classes = (FlockingInstancesTable,)
    template_name = "horizon/common/_detail_table.html"
    preload = True

    def get_instances_data(self):
        try:
            instances = utils.get_fake_instances_data(self.tab_group.request)
        except:
            instances = []
            exceptions.handle(self.tab_group.request,
                              _('Unable to retrieve instance list.'))
        return instances

class VizTab(tabs.Tab):
    name = _("Visualization")
    slug = "viz"
    template_name = "visualizations/flocking/_flocking.html"

    def get_context_data(self, request):
        return None

class FlockingTabs(tabs.TabGroup):
    slug = "flocking"
    tabs = (VizTab, DataTab)