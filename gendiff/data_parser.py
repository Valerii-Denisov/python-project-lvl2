"""The module read data."""

import json

import yaml
from yaml.loader import SafeLoader


def getting_data(getting_object, data_format):
    """
    Read data.

    Parameters:
        getting_object: str;
        data_format: str.

    Returns:
        Dict of data from file.
    """
    if data_format == 'json':
        return json.loads(getting_object)
    elif data_format in {'yaml', 'yml'}:
        return dict(yaml.load(getting_object, Loader=SafeLoader))
