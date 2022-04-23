"""Builds a difference in JSON format."""
import json


def get_format(diff_view):
    """
    Format the difference represintation into a string.

    Parameters:
        diff_view: dict.

    Returns:
        Formated string.

    """
    return json.dumps(diff_view)
