import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.noresource.views.dataset import noresource_dataset, noresource_admin, noresource_dataset_metadata
import ckanext.noresource.helpers as helpers

class NoresourcePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    def get_blueprint(self):
        return [noresource_dataset, noresource_admin, noresource_dataset_metadata]
    

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
            'noresource')

    # IConfigurer

    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator('ignore_missing')
        validators = [ignore_missing, str]
        schema.update({
            'ckan.noresource': validators
        })
        return schema

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'requestdata_has_query_param':
                helpers.has_query_param,
        }