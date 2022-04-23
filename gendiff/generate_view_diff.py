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


def get_view_diff(file_data1, file_data2):
    """
    Build representation of difference.

    Parameters:
        file_data1: dict,
        file_data2: dict.

    Returns:
        dict.
    """
    output = {}
    keys = get_keys_set(file_data1, file_data2)
    for key in keys:
        if key in file_data1 and key not in file_data2:
            output.update(
                {key: {'status': 'removed', 'data': file_data1[key]}},
            )
        elif key in file_data2 and key not in file_data1:
            output.update(
                {key: {'status': 'added', 'data': file_data2[key]}},
            )
        elif file_data1.get(key) == file_data2.get(key):
            output.update(
                {key: {'status': 'unchanged', 'data': file_data1[key]}},
            )
        elif (
            isinstance(file_data1.get(key), dict) is False
            or isinstance(file_data2.get(key), dict) is False
        ):
            output.update(
                {
                    key: {
                        'status': 'changed',
                        'data': {
                            'old': file_data1[key],
                            'new': file_data2[key],
                        },
                    },
                },
            )
        else:
            output.update(
                {
                    key: {
                        'status': 'nested',
                        'children': get_view_diff(
                            file_data1[key],
                            file_data2[key],
                        ),
                    },
                },
            )

    return output
