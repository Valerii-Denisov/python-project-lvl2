"""The module read data."""

import json

import yaml
from yaml.loader import SafeLoader


def getting_data(raw_data, data_format):
    """
    Read data.

    Parameters:
        raw_data: str;
        data_format: str.

    Returns:
        Dict of data from file.
    """
    if data_format == 'json':
        return json.loads(raw_data)
    elif data_format in {'yaml', 'yml'}:
        return dict(yaml.load(raw_data, Loader=SafeLoader))
