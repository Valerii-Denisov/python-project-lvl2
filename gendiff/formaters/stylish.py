"""Builds a difference in stylish format."""
import json
import types

IDENT = '    '
MATH_COMPAIRE = types.MappingProxyType({
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    ',
    'nested': '    ',
})


def get_level_ident(level=0):
    """
    Build level ident.

    Parameters:
        level: int.

    Returns:
        Ident.
    """
    return IDENT * level


def get_val_string(sub_dict, level):
    """
    Buid value string.

    Parameters:
        sub_dict: str, int, dict, bool;
        level: int.

    Returns:
        value string.
    """
    output = []
    if isinstance(sub_dict, bool) or sub_dict is None:
        return json.dumps(sub_dict)
    if isinstance(sub_dict, (int, str)):
        return sub_dict
    for key, value in sub_dict.items():
        if isinstance(value, dict):
            output.append(
                '{0}{1}: {3}\n{2}\n{0}{4}'.format(
                    get_level_ident(level + 1),
                    key,
                    get_val_string(value, level + 1),
                    '{',
                    '}',
                ),
            )
        else:
            output.append(
                '{0}{1}: {2}'.format(
                    get_level_ident(level + 1), key, value,
                ),
            )
    return '\n'.join(output)


def get_string(key, value, value_type, level):
    """
    Build string of node.

    Parameters:
        key: str;
        value: dict;
        value_type: str;
        level: int.

    Returns:
        string.
    """
    if value_type == 'changed':
        output = []
        output.append(get_string(key, value['old'], 'removed', level))
        output.append(get_string(key, value['new'], 'added', level))
        return '\n'.join(output)
    elif value_type == 'nested':
        return '{0}{1}{2}: {4}\n{3}\n{6}{5}'.format(
            get_level_ident(level),
            MATH_COMPAIRE[value_type],
            key,
            value,
            '{',
            '}',
            get_level_ident(level + 1),
        )
    elif isinstance(value, dict):
        return '{0}{1}{2}: {5}\n{3}\n{6}{4}'.format(
            get_level_ident(level),
            MATH_COMPAIRE[value_type],
            key,
            get_val_string(value, level + 1),
            '}',
            '{',
            get_level_ident(level + 1),
        )
    else:
        return '{0}{1}{2}: {3}'.format(
            get_level_ident(level),
            MATH_COMPAIRE[value_type],
            key,
            get_val_string(value, level),
        )


def get_format(diff_view):
    """
    Format the difference represintation into a string.

    Parameters:
        diff_view: dict.

    Returns:
        Formated string.

    """
    def walk(diff, level=0):
        output = []
        for key, value in diff.items():
            if value.get('type') == 'added':
                output.append(get_string(key, value['data'], 'added', level))
            elif value.get('type') == 'removed':
                output.append(get_string(key, value['data'], 'removed', level))
            elif value.get('type') == 'unchanged':
                output.append(
                    get_string(key, value['data'], 'unchanged', level),
                )
            elif value.get('type') == 'changed':
                output.append(get_string(key, value['data'], 'changed', level))
            else:
                output.append(
                    get_string(
                        key,
                        walk(value.get('children'), level + 1),
                        'nested',
                        level,
                    ),
                )
        return '\n'.join(output)
    return '\n'.join(('{', walk(diff_view, 0), '}'))
