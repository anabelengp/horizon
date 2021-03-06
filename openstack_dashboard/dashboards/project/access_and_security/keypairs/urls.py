# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from .views import CreateView
from .views import DownloadView
from .views import GenerateView
from .views import ImportView


urlpatterns = patterns('',
    url(r'^create/$', CreateView.as_view(), name='create'),
    url(r'^import/$', ImportView.as_view(), name='import'),
    url(r'^(?P<keypair_name>[^/]+)/download/$', DownloadView.as_view(),
            name='download'),
    url(r'^(?P<keypair_name>[^/]+)/generate/$', GenerateView.as_view(),
            name='generate'),
)
