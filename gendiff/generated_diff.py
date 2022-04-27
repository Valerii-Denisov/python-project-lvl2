"""The module forms the differences of two data string."""

from gendiff.file_reader import get_data_format
from gendiff.formaters import json, plain, stylish
from gendiff.generate_view_diff import get_view_diff
from gendiff.data_parser import getting_data


def generate_diff(first_data, second_data, format_diff='stylish'):
    """
    Generate a string with the differences between two data source.

    Parameters:
        first_data: str,
        second_data: str,
        format_diff: json, stylish, plain.

    Returns:
        String of deference.
    """
    first_data_string = getting_data(first_data, get_data_format(first_data))
    second_data_string = getting_data(second_data, get_data_format(second_data))
    diff_view = get_view_diff(first_data_string, second_data_string)
    if format_diff == 'stylish':
        return stylish.get_format(diff_view)
    elif format_diff == 'plain':
        return plain.get_format(diff_view)
    elif format_diff == 'json':
        return json.get_format(diff_view)
