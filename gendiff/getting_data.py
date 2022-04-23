"""The module read data from file."""

import json

import yaml
from yaml.loader import SafeLoader


def getting_file_format(path_file):
    """
    Read file path.

    Parameters:
        path_file: str.

    Returns:
        File format.
    """
    _, file_format = path_file.split('.', 1)
    return file_format


def getting_data(path_file):
    """
    Read data from file.

    Parameters:
        path_file: str.

    Returns:
        Dict of data from file.
    """
    if getting_file_format(path_file) == 'json':
        with open(path_file) as file_data:
            return json.load(file_data)
    elif getting_file_format(path_file) in {'yaml', 'yml'}:
        with open(path_file) as file_data:
            return dict(yaml.load(file_data, Loader=SafeLoader))
