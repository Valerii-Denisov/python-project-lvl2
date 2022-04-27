"""The module generates representation of the difference."""


def get_keys_set(dict1, dict2):
    """
    Build sorted set of keys.

    Parameters:
        dict1: dict,
        dict2: dict.

    Returns:
        Sorted set.
    """
    dict1_keys = dict1.keys()
    dict2_keys = dict2.keys()
    return sorted(set(dict1_keys | dict2_keys))


def get_view_diff(first_data, second_data):
    """
    Build representation of difference.

    Parameters:
        first_data: dict,
        second_data: dict.

    Returns:
        dict.
    """
    output = {}
    keys = get_keys_set(first_data, second_data)
    for key in keys:
        if key in first_data and key not in second_data:
            output.update(
                {key: {'type': 'removed', 'data': first_data[key]}},
            )
        elif key in second_data and key not in first_data:
            output.update(
                {key: {'type': 'added', 'data': second_data[key]}},
            )
        elif first_data.get(key) == second_data.get(key):
            output.update(
                {key: {'type': 'unchanged', 'data': first_data[key]}},
            )
        elif (
            isinstance(first_data.get(key), dict)
            and isinstance(second_data.get(key), dict)
        ):
            output.update(
                {
                    key: {
                        'type': 'nested',
                        'children': get_view_diff(
                            first_data[key],
                            second_data[key],
                        ),
                    },
                },
            )
        else:
            output.update(
                {
                    key: {
                        'type': 'changed',
                        'data': {
                            'old': first_data[key],
                            'new': second_data[key],
                        },
                    },
                },
            )
    return output
