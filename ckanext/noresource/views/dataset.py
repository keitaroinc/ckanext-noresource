from flask import Blueprint

from ckan.lib import base
from ckan.common import g, _, request, config
from ckan import logic
import ckan.model as model
import ckan.lib.helpers as h
from ckan.plugins import toolkit
import ckan.views.admin as admin

import ckan.views.dataset as dataset

import ckan.lib.navl.dictization_functions as dict_fns
from ckanext.requestdata.helpers import has_query_param
from ckanext.requestdata.utils import use_standard_package_type
from flask.views import MethodView
from ckan.views.home import CACHE_PARAMETERS

get_action = logic.get_action
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError
clean_dict = logic.clean_dict

redirect = h.redirect_to
abort = base.abort
tuplize_dict = logic.tuplize_dict
parse_params = logic.parse_params


noresource_dataset = Blueprint(u'noresource_dataset',
                                __name__,
                                url_prefix=u'/dataset',
                                url_defaults={u'package_type': u'dataset'}
)

noresource_admin = Blueprint(u'noresurce_admin', __name__, url_prefix=u'/ckan-admin')

def _get_noresurce_options():
    options = [{u'text':u'Default(Create dataset with resource)',
                u'value':u'1'},
                {u'text':u'Create dataset without resource',
                u'value':u'2'},
                {u'text':u'Let me chooose on dataset creation',
                u'value':u'3'}]

    return dict(options=options)

class NoResourceConfigView(MethodView):
    def get(self):
        print("This is adminNR get method")
        items = admin._get_config_options()
        options = _get_noresurce_options()
        schema = logic.schema.update_configuration_schema()
        data = {}
        for key in schema:
            data[key] = config.get(key)

        vars = dict(data=data, errors={}, **items, **options)

        return base.render(u'admin/config.html', extra_vars=vars)


    def post(self):
        try:
            req = request.form.copy()
            print(req)
            req.update(request.files.to_dict())
            data_dict = logic.clean_dict(
                dict_fns.unflatten(
                    logic.tuplize_dict(
                        logic.parse_params(req,
                                            ignore_keys=CACHE_PARAMETERS))))

            print("NESTO OVDE")
            del data_dict['save']
            print(data_dict)
            data = logic.get_action(u'config_option_update')({
                u'user': g.user
            }, data_dict)

        except logic.ValidationError as e:
            print("Are you here ??")
            items = admin._get_config_options()
            options = _get_noresurce_options()
            data = request.form
            errors = e.error_dict
            error_summary = e.error_summary
            vars = dict(data=data,
                        errors=errors,
                        error_summary=error_summary,
                        form_items=items,
                        **options,
                        **items)
            return base.render(u'admin/config.html', extra_vars=vars)

        return h.redirect_to(u'admin.config')



class CreateView(dataset.CreateView):
    def get(self, package_type, data=None, errors=None, error_summary=None):
        print("IN GET")
        # Handle metadata-only datasets
        if has_query_param('metadata'):
            package_type = package_type if use_standard_package_type() else 'requestdata-metadata-only'

        return super(CreateView, self).get(package_type, data,
                                           errors, error_summary)

    def post(self, package_type):

        # Handle metadata-only datasets
        if has_query_param('metadata'):
            package_type = package_type if use_standard_package_type() else 'requestdata-metadata-only'

            data_dict = dataset.clean_dict(
                dataset.dict_fns.unflatten(
                    dataset.tuplize_dict(dataset.parse_params(request.form))))
            context = self._prepare()
            data_dict['type'] = package_type

            try:
                package = get_action('package_create')(context, data_dict)

                url = h.url_for(u'{0}.read'.format(package_type), id=package['name'])

                return redirect(url)
            except NotAuthorized:
                abort(403, _('Unauthorized to create a dataset.'))
            except ValidationError as e:
                errors = e.error_dict
                error_summary = e.error_summary

                form_vars = {'errors': errors, 'dataset_type': package_type, 'action': 'new',
                             'error_summary': error_summary, 'stage': ['active'], 'data': data_dict}

                extra_vars = {
                    'form_vars': form_vars,
                    'form_snippet': 'package/new_package_form.html',
                    'dataset_type': package_type
                }

                return toolkit.render('package/new.html',
                                      extra_vars=extra_vars)
        else:
            return super(CreateView, self).post(package_type)


noresource_dataset.add_url_rule(u'/new', view_func=CreateView.as_view(str(u'new')))
noresource_admin.add_url_rule(u'/config', view_func=NoResourceConfigView.as_view(str(u'config')))

def get_blueprints():
    return [noresource_dataset]