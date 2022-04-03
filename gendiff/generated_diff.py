"""The module forms the differences of two flat files."""

import json


def lowering_text(lowering_date):
    """
    Lowering the register of received data.

    Parameters:
        lowering_date: str.

    Returns:
        lower string.
    """
    string = str(lowering_date)
    return string.lower()


def getting_set_keys(first_dict, second_dict):
    """
    Forming a set of keys from two dictionaries.

    Parameters:
        first_dict: dict,
        second_dict: dict.

    Returns:
        set.
    """
    return set(list(first_dict.keys()) + list(second_dict.keys()))


def getting_date(file1):
    """
    Read date from JSON-file.

    Parameters:
        file1: str.

    Returns:
        Dict of date from file.
    """
    with open(file1) as file_data:
        return json.load(file_data)


def generate_diff(first_file, second_file):
    """
    Generate a string with the differences between the two files.

    Parameters:
        first_file: str,
        second_file: str.

    Returns:
        String of deference.
    """
    output = []
    first_data_string = getting_date(first_file)
    second_data_string = getting_date(second_file)
    for key in sorted(getting_set_keys(first_data_string, second_data_string)):
        if key in first_data_string.keys() and key in second_data_string.keys():
            if first_data_string[key] == second_data_string[key]:
                output.append('  {0}: {1}'.format(
                    key,
                    lowering_text(first_data_string[key]),
                ))
            else:
                output.append(' -{0}: {1}'.format(
                    key,
                    lowering_text(first_data_string[key]),
                ))
                output.append(' +{0}: {1}'.format(
                    key,
                    lowering_text(second_data_string[key]),
                ))
        elif key in first_data_string.keys():
            output.append(' -{0}: {1}'.format(
                key,
                lowering_text(first_data_string[key]),
            ))
        else:
            output.append(' +{0}: {1}'.format(
                key,
                lowering_text(second_data_string[key]),
            ))
    return '\n'.join(('{', '\n'.join(output), '}'))
