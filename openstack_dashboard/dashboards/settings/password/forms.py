# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Centrin Data Systems Ltd.
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

from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_variables

from horizon import exceptions
from horizon import forms
from horizon import messages
from horizon.utils import validators

from openstack_dashboard import api


class PasswordForm(forms.SelfHandlingForm):
    current_password = forms.CharField(label=_("Current password"),
                           widget=forms.PasswordInput(render_value=False))
    new_password = forms.RegexField(label=_("New password"),
               widget=forms.PasswordInput(render_value=False),
               regex=validators.password_validator(),
               error_messages={'invalid':
               validators.password_validator_msg()})
    confirm_password = forms.CharField(label=_("Confirm new password"),
                            widget=forms.PasswordInput(render_value=False))

    def clean(self):
        '''Check to make sure password fields match.'''
        data = super(forms.Form, self).clean()
        if 'new_password' in data:
            if data['new_password'] != data.get('confirm_password', None):
                raise ValidationError(_('Passwords do not match.'))
        return data

    # We have to protect the entire "data" dict because it contains the
    # oldpassword and newpassword strings.
    @sensitive_variables('data')
    def handle(self, request, data):
        user_is_editable = api.keystone.keystone_can_edit_user()

        if user_is_editable:
            try:
                passwd = api.keystone.user_update_own_password(request,
                                                    data['current_password'],
                                                    data['new_password'])
                messages.success(request, _('Password changed.'))
            except:
                exceptions.handle(request,
                                  _('Unable to change password.'))
                return False
        else:
            messages.error(request, _('Changing password is not supported.'))
            return False

        return True
