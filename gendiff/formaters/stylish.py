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
    output = ['{']
    if isinstance(sub_dict, bool) or sub_dict is None:
        return json.dumps(sub_dict)
    elif isinstance(sub_dict, (int, str)):
        return sub_dict
    def walk(sub_value, level):
        output = []
        for key, value in sub_value.items():
            if isinstance(value, dict):
                output.append(
                    '{0}{1}: {2}\n{3}\n{0}{4}'.format(
                        get_level_indent(level + 1),
                        key,
                        '{',
                        walk(value, level + 1),
                        '}',
                    ),
                )
            else:
                output.append(
                    '{0}{1}: {2}'.format(
                        get_level_indent(level + 1),
                        key,
                        value,
                    ),
                )
        return '\n'.join(output)
    output.append(walk(sub_dict, level))
    output.append('{0}{1}'.format(get_level_indent(level), '}'))
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
    node_type = value.get('type')
    if node_type == 'changed':
        output = [
                '{0}{1}{2}: {3}'.format(
                get_level_indent(level),
               MATH_REPR_TYPE['removed'],
                key,
                stringify_value(value['data']['old'], level + 1)),
                '{0}{1}{2}: {3}'.format(
                get_level_indent(level),
                MATH_REPR_TYPE['added'],
                key,
                stringify_value(value['data']['new'], level + 1)),
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
            output.append(stringify_node(child_key, child_value, level+1))
        output.append('{0}{1}'.format(get_level_indent(level + 1), '}'))
        return '\n'.join(output)
    else:
        print(node_type)
        return '{0}{1}{2}: {3}'.format(
                get_level_indent(level),
                MATH_REPR_TYPE[node_type],
                key,
                stringify_value(value['data'], level + 1),
            )


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
