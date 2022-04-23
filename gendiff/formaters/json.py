"""Build string of difference in json format."""
import json


def get_format(diff_view):
    """
    Format the difference view into a string.

    Parameters:
        diff_view: dict.

    Returns:
        Formated string.

    """
    return json.dumps(diff_view)