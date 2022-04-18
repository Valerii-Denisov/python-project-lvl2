"""The module forms the differences of two flat files."""

from gendiff.formaters import plain, stylish
from gendiff.generate_view_diff import get_view_diff
from gendiff.getting_date import getting_date


def generate_diff(first_file, second_file, format_diff='stylish'):
    """
    Generate a string with the differences between the two files.

    Parameters:
        first_file: str,
        second_file: str,
        format_diff: stylish, plain, json.

    Returns:
        String of deference.
    """
    first_data_string = getting_date(first_file)
    second_data_string = getting_date(second_file)
    diff_view = get_view_diff(first_data_string, second_data_string)
    if format_diff == 'stylish':
        return stylish.get_format(diff_view)
    elif format_diff == 'plain':
        return plain.get_format(diff_view)
