"""The module forms the differences of two data string."""

from gendiff.data_parser import getting_data
from gendiff.file_reader import get_data_format, get_raw_data
from gendiff.formaters.formaters import format_diff
from gendiff.generate_view_diff import get_view_diff


def generate_diff(first_data, second_data, format_name='stylish'):
    """
    Generate a string with the differences between two data source.

    Parameters:
        first_data: str,
        second_data: str,
        format_name: json, stylish, plain.

    Returns:
        String of deference.
    """
    first_data_dict = getting_data(
        get_raw_data(first_data),
        get_data_format(first_data),
    )
    second_data_dict = getting_data(
        get_raw_data(second_data),
        get_data_format(second_data),
    )
    diff_view = get_view_diff(first_data_dict, second_data_dict)
    return format_diff(diff_view, format_name)
