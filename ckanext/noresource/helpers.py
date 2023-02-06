from ckan.common import c, _, request, config


def has_query_param(param):
    # Checks if the provided parameter is part of the current URL query params

    params = request.args

    if param in params:
        return True

    return False