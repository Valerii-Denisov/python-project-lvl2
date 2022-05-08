"""Builds a difference in stylish format."""
import json
import types

INDENT = '    '
MATH_REPR_TYPE = types.MappingProxyType({
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    ',
    'nested': '    ',
})


def get_level_indent(level=0):
    """
    Build level indent.

    Parameters:
        level: int.

    Returns:
        Indent.
    """
    return INDENT * level


def stringify_value(sub_dict, level):
    """
    Convert value to a string.

    Parameters:
        sub_dict: str, int, dict, bool;
        level: int.

    Returns:
        value string.
    """
    output = []
    if isinstance(sub_dict, bool) or sub_dict is None:
        return json.dumps(sub_dict)
    elif isinstance(sub_dict, (int, str)):
        return sub_dict
    for key, value in sub_dict.items():
        if isinstance(value, dict):
            output.append(
                '{0}{1}: {3}\n{2}\n{0}{4}'.format(
                    get_level_indent(level + 1),
                    key,
                    stringify_value(value, level + 1),
                    '{',
                    '}',
                ),
            )
        else:
            output.append(
                '{0}{1}: {2}'.format(
                    get_level_indent(level + 1), key, value,
                ),
            )
    return '\n'.join(output)


def stringify_node(key, value, value_type, level):
    """
    Convert node to a string.

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
        output.append(stringify_node(key, value['old'], 'removed', level))
        output.append(stringify_node(key, value['new'], 'added', level))
        return '\n'.join(output)
    elif value_type == 'nested':
        return '{0}{1}{2}: {4}\n{3}\n{6}{5}'.format(
            get_level_indent(level),
            MATH_REPR_TYPE[value_type],
            key,
            value,
            '{',
            '}',
            get_level_indent(level + 1),
        )
    elif isinstance(value, dict):
        return '{0}{1}{2}: {5}\n{3}\n{6}{4}'.format(
            get_level_indent(level),
            MATH_REPR_TYPE[value_type],
            key,
            stringify_value(value, level + 1),
            '}',
            '{',
            get_level_indent(level + 1),
        )
    else:
        return '{0}{1}{2}: {3}'.format(
            get_level_indent(level),
            MATH_REPR_TYPE[value_type],
            key,
            stringify_value(value, level),
        )


def format_stylish(diff_view):
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
                output.append(
                    stringify_node(key, value['data'], 'added', level),
                )
            elif value.get('type') == 'removed':
                output.append(
                    stringify_node(key, value['data'], 'removed', level),
                )
            elif value.get('type') == 'unchanged':
                output.append(
                    stringify_node(key, value['data'], 'unchanged', level),
                )
            elif value.get('type') == 'changed':
                output.append(
                    stringify_node(key, value['data'], 'changed', level),
                )
            else:
                output.append(
                    stringify_node(
                        key,
                        walk(value.get('children'), level + 1),
                        'nested',
                        level,
                    ),
                )
        return '\n'.join(output)
    return '\n'.join(('{', walk(diff_view, 0), '}'))
