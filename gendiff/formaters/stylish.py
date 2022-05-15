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


def stringify_node(key, value, level=0):
    """
    Convert node to a string.

    Parameters:
        key: str;
        value: dict;
        level: int.

    Returns:
        string.
    """
    def build_line(sub_key, sub_value, node_type, sub_level):
        if isinstance(sub_value, dict):
            return '{0}{1}{2}: {5}\n{3}\n{6}{4}'.format(
                get_level_indent(sub_level),
                MATH_REPR_TYPE[node_type],
                sub_key,
                stringify_value(sub_value, sub_level + 1),
                '}',
                '{',
                get_level_indent(sub_level + 1),
            )
        else:
            return '{0}{1}{2}: {3}'.format(
                get_level_indent(sub_level),
                MATH_REPR_TYPE[node_type],
                sub_key,
                stringify_value(sub_value, sub_level),
            )
    node_type = value.get('type')
    if node_type == 'changed':
        output = [
            build_line(key, value['data']['old'], 'removed', level),
            build_line(key, value['data']['new'], 'added', level),
        ]
        return '\n'.join(output)
    elif node_type == 'nested':
        output = ['{0}{1}{2}: {3}'.format(
            get_level_indent(level),
            MATH_REPR_TYPE[node_type],
            key,
            '{',
        )]
        children = value.get('children')
        for child_key, child_value in children.items():
            output.append(stringify_node(child_key, child_value, level + 1))
        output.append('{0}{1}'.format(get_level_indent(level + 1), '}'))
        return '\n'.join(output)
    else:
        return build_line(key, value['data'], node_type, level)


def format_stylish(diff_view):
    """
    Format the difference representation into a string.

    Parameters:
        diff_view: dict.

    Returns:
        Formatted string.

    """
    output = []
    for key, value in diff_view.items():
        output.append(
            stringify_node(key, value),
        )
    return '\n'.join(('{', '\n'.join(output), '}'))
