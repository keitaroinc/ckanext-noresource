import re
from ckan import model
from ckan.plugins import toolkit
from ckan.common import c, _, request, config


def use_standard_package_type():
    return _parse_bool(config.get('ckanext.noresource.use_standard_package_type', 'true'))


def _parse_bool(val):
    if not val:
        return False
    return str(val).lower() in ("yes", "true", "t", "1")