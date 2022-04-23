"""The module forms the differences of two flat files."""

from gendiff.formaters import json, plain, stylish
from gendiff.generate_view_diff import get_view_diff
from gendiff.getting_data import getting_data


def generate_diff(first_file, second_file, format_diff='stylish'):
    """
    Generate a string with the differences between two files.

    Parameters:
        first_file: str,
        second_file: str,
        format_diff: json, stylish, plain.

    Returns:
        String of deference.
    """
    first_data_string = getting_data(first_file)
    second_data_string = getting_data(second_file)
    diff_view = get_view_diff(first_data_string, second_data_string)
    if format_diff == 'stylish':
        return stylish.get_format(diff_view)
    elif format_diff == 'plain':
        return plain.get_format(diff_view)
    elif format_diff == 'json':
        return json.get_format(diff_view)
