"""Selects the format for display differences."""

from gendiff.formaters import json, plain, stylish


def format_diff(diff_view, formatter):
    """
    Get a difference dict in one of three formats.

    Parameters:
        diff_view: dict;
        formatter: str.

    Returns:
        difference in one of three formats.
    """
    if formatter == 'stylish':
        return stylish.get_format(diff_view)
    elif formatter == 'plain':
        return plain.get_format(diff_view)
    elif formatter == 'json':
        return json.get_format(diff_view)
