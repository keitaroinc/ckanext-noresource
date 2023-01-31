import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.noresource.views.dataset import noresource_dataset, noresource_admin

class NoresourcePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    
    # IConfigurer

    def get_blueprint(self):
        return [noresource_dataset, noresource_admin]
    

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
            'noresource')
