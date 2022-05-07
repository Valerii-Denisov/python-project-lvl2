"""Builds a difference in plain format."""
import json


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


def stringify_value(sub_dict):
    """
    Convert value to a string.

    Parameters:
        sub_dict: str, int, dict, bool.

    Returns:
        value string.
    """
    if isinstance(sub_dict, dict):
        return '[complex value]'
    elif isinstance(sub_dict, bool) or sub_dict is None:
        return json.dumps(sub_dict)
    elif isinstance(sub_dict, int):
        return sub_dict
    else:
        return '\'{0}\''.format(sub_dict)


def format_plain(diff_view):
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
            if value['type'] == 'added':
                output.append(
                    'Property \'{0}\' was added with value: {1}'.format(
                        get_path(key, parent),
                        stringify_value(value['data']),
                    ),
                )
            elif value['type'] == 'removed':
                output.append(
                    'Property \'{0}\' was removed'.format(
                        get_path(key, parent),
                    ),
                )
            elif value['type'] == 'changed':
                output.append(
                    'Property \'{0}\' was updated. From {1} to {2}'.format(
                        get_path(key, parent),
                        stringify_value(value['data']['old']),
                        stringify_value(value['data']['new']),
                    ),
                )
            elif value['type'] == 'nested':
                output.append(walk(value['children'], get_path(key, parent)))
        return '\n'.join(output)
    return walk(diff_view, '')
