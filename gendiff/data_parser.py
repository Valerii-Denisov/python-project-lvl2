"""The module read data."""

import json

import yaml
from gendiff.file_reader import get_raw_data
from yaml.loader import SafeLoader


def getting_data(data_path, data_format):
    """
    Read data.

    Parameters:
        data_path: str;
        data_format: str.

    Returns:
        Dict of data from file.
    """
    if data_format == 'json':
        return json.loads(get_raw_data(data_path))
    elif data_format in {'yaml', 'yml'}:
        return dict(yaml.load(get_raw_data(data_path), Loader=SafeLoader))
