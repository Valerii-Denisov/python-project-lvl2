"""Builds a difference in stylish format."""
import json

IDENT = '    '


def get_level_ident(level=0):
    """
    Build level ident.

    Parameters:
        level: int.

    Returns:
        Ident.
    """
    return IDENT * level


def get_lower_text(lowering_data):
    """
    Lower the register of received data.

    Parameters:
        lowering_data: str.

    Returns:
        lower string.
    """
    string = str(lowering_data)
    return string.lower()


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
    if isinstance(sub_dict, dict) is False:
        if isinstance(sub_dict, bool):
            return get_lower_text(sub_dict)
        elif sub_dict is None:
            return json.dumps(sub_dict)
        else:
            return sub_dict
    else:
        for key, value in sub_dict.items():
            if isinstance(value, dict) is False:
                output.append(
                    '{0}{1}: {2}'.format(
                        get_level_ident(level + 1), key, value,
                    ),
                )
            else:
                output.append(
                    '{0}{1}: {3}\n{2}\n{0}{4}'.format(
                        get_level_ident(level + 1),
                        key,
                        get_val_string(value, level + 1),
                        '{',
                        '}',
                    ),
                )
    return '\n'.join(output)


def get_added_string(key, value, level):
    """
    Build string of added node.

    Parameters:
        key: str;
        value: dict;
        level: int.

    Returns:
        string.
    """
    if isinstance(value.get('data'), dict) is False:
        return '{0}{1}{2}: {3}'.format(
            get_level_ident(level),
            '  + ',
            key,
            get_val_string(value.get('data'), level),
        )
    else:
        return '{0}{1}{2}: {5}\n{3}\n{6}{4}'.format(
            get_level_ident(level),
            '  + ',
            key,
            get_val_string(value.get('data'), level + 1),
            '}',
            '{',
            get_level_ident(level + 1),
        )


def get_removed_string(key, value, level):
    """
    Build string of removed node.

    Parameters:
        key: str;
        value: dict;
        level: int.

    Returns:
        string.
    """
    if isinstance(value.get('data'), dict) is False:
        return '{0}{1}{2}: {3}'.format(
            get_level_ident(level),
            '  - ',
            key,
            get_val_string(value.get('data'), level),
        )
    else:
        return '{0}{1}{2}: {5}\n{3}\n{6}{4}'.format(
            get_level_ident(level),
            '  - ',
            key,
            get_val_string(value.get('data'), level + 1),
            '}',
            '{',
            get_level_ident(level + 1),
        )


def get_unchanged_string(key, value, level):
    """
    Build string of unchanged node.

    Parameters:
        key: str;
        value: dict;
        level: int.

    Returns:
        string.
    """
    return '{0}{1}{2}: {3}'.format(
        get_level_ident(level),
        '    ',
        key,
        value.get('data'),
    )


def get_changed_string(key, value, level):
    """
    Build string of changed node.

    Parameters:
        key: str;
        value: dict;
        level: int.

    Returns:
        string.
    """
    output = []
    if (
        isinstance(value['data']['old'], dict) is False
        and isinstance(value['data']['new'], dict) is False
    ):
        output.append(
            '{0}{1}{2}: {3}'.format(
                get_level_ident(level),
                '  - ',
                key,
                get_val_string(value['data']['old'], level),
            ),
        )
        output.append(
            '{0}{1}{2}: {3}'.format(
                get_level_ident(level),
                '  + ',
                key,
                get_val_string(value['data']['new'], level),
            ),
        )
    elif (
        isinstance(value['data']['old'], dict)
        and isinstance(value['data']['new'], dict) is False
    ):
        output.append(
            '{0}{1}{2}: {4}\n{3}\n{6}{5}'.format(
                get_level_ident(level),
                '  - ',
                key,
                get_val_string(value['data']['old'], level + 1),
                '{',
                '}',
                get_level_ident(level + 1),
            ),
        )
        output.append(
            '{0}{1}{2}: {3}'.format(
                get_level_ident(level),
                '  + ',
                key,
                get_val_string(value['data']['new'], level),
            ),
        )
    else:
        output.append(
            '{0}{1}{2}: {3}'.format(
                get_level_ident(level),
                '  - ',
                key,
                get_val_string(value['data']['old'], level),
            ),
        )
        output.append(
            '{0}{1}{2}: {4}\n{3}\n{6}{5}'.format(
                get_level_ident(level),
                '  + ',
                key,
                get_val_string(value['data']['new'], level + 1),
                '{',
                '}',
                get_level_ident(level + 1),
            ),
        )
    return '\n'.join(output)


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
            if value.get('status') == 'added':
                output.append(get_added_string(key, value, level))
            elif value.get('status') == 'removed':
                output.append(get_removed_string(key, value, level))
            elif value.get('status') == 'unchanged':
                output.append(get_unchanged_string(key, value, level))
            elif value.get('status') == 'changed':
                output.append(get_changed_string(key, value, level))
            else:
                output.append(
                    '{0}{1}{2}: {4}\n{3}\n{6}{5}'.format(
                        get_level_ident(level),
                        '    ',
                        key,
                        walk(value.get('children'), level + 1),
                        '{',
                        '}',
                        get_level_ident(level + 1),
                    ),
                )
        return '\n'.join(output)
    return '\n'.join(('{', walk(diff_view, 0), '}'))
