"""Builds a difference in plain format."""
import json

from gendiff.formaters import stylish


def get_path(key, parent):
    """
    Build string of path to value.

    Parameters:
        key: str;
        parent: str.

    Returns:
        String of path.
    """
    if parent:
        return parent + '.{0}'.format(key)
    return '{0}'.format(key)


def get_value(sub_dict):
    """
    Buid value string.

    Parameters:
        sub_dict: str, int, dict, bool.

    Returns:
        value string.
    """
    if isinstance(sub_dict, dict) is False:
        if isinstance(sub_dict, bool):
            return stylish.get_lower_text(sub_dict)
        elif sub_dict is None:
            return json.dumps(sub_dict)
        else:
            return '\'{0}\''.format(sub_dict)
    else:
        return '[complex value]'


def get_format(diff_view):
    """
    Format the difference represintation into a string.

    Parameters:
        diff_view: dict.

    Returns:
        Formated string.

    """
    def walk(sub_diff, parent):
        output = []
        for key, value in sub_diff.items():
            if value['status'] == 'added':
                output.append(
                    'Property \'{0}\' was added with value: {1}'.format(
                        get_path(key, parent),
                        get_value(value['data']),
                    ),
                )
            elif value['status'] == 'removed':
                output.append(
                    'Property \'{0}\' was removed'.format(
                        get_path(key, parent),
                    ),
                )
            elif value['status'] == 'changed':
                output.append(
                    'Property \'{0}\' was updated. From {1} to {2}'.format(
                        get_path(key, parent),
                        get_value(value['data']['old']),
                        get_value(value['data']['new']),
                    ),
                )
            elif value['status'] == 'nested':
                output.append(walk(value['children'], get_path(key, parent)))
        return '\n'.join(output)
    return walk(diff_view, '')
