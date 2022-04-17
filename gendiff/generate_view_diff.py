"""The module generates representation of the difference."""


def is_dict(checking_object):
    """
    Check whether the object is a dictionary or not.

    Parameters:
        checking_object: str, int, bool, dict.

    Returns:
        True or False.
    """
    return isinstance(checking_object, dict)


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


def get_view_diff(file_date1, file_date2):
    """
    Build representation of difference.

    Parameters:
        file_date1: dict,
        file_date2: dict.

    Returns:
        dict.
    """
    output = {}
    keys = get_keys_set(file_date1, file_date2)
    for key in keys:
        if key in file_date1 and key not in file_date2:
            output.update(
                {key: {'status': 'removed', 'date': file_date1[key]}},
            )
        elif key in file_date2 and key not in file_date1:
            output.update(
                {key: {'status': 'added', 'date': file_date2[key]}},
            )
        elif file_date1.get(key) == file_date2.get(key):
            output.update(
                {key: {'status': 'unchanged', 'date': file_date1[key]}},
            )
        elif (
            is_dict(file_date1.get(key)) is False or
            is_dict(file_date2.get(key)) is False
        ):
            output.update(
                {
                    key: {
                        'status': 'changed',
                        'date': {
                            'old': file_date1[key],
                            'new': file_date2[key],
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
                            file_date1[key],
                            file_date2[key],
                        ),
                    },
                },
            )

    return output
