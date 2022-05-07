"""Selects the format for display differences."""

from gendiff.formaters import json, plain, stylish


def format_diff(diff_view, formatter):
    """
    Get a difference in one of three formats.

    Parameters:
        diff_view: dict;
        formatter: str.

    Returns:
        difference in one of three formats.
    """
    if formatter == 'stylish':
        return stylish.format_stylish(diff_view)
    elif formatter == 'plain':
        return plain.format_plain(diff_view)
    elif formatter == 'json':
        return json.format_json(diff_view)
