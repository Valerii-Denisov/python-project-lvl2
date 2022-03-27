import json


def lowering_text(lowering_date):
    string = str(lowering_date)
    return string.lower()


def getting_set_keys(first_dict, second_dict):
    return set(list(first_dict.keys()) + list(second_dict.keys()))


def getting_date(file1):
    with open(file1) as file_data:
        return json.load(file_data)


def generate_diff(first_file, second_file):
    output = []
    first_data_string = getting_date(first_file)
    second_data_string = getting_date(second_file)
    for key in sorted(getting_set_keys(first_data_string, second_data_string)):
        if key in first_data_string.keys() and key in second_data_string.keys():
            if first_data_string[key] == second_data_string[key]:
                output.append('{0}: {1}'.format(
                    key,
                    lowering_text(first_data_string[key]),
                ))
            else:
                output.append('-{0}: {1}'.format(
                    key,
                    lowering_text(first_data_string[key]),
                ))
                output.append('+{0}: {1}'.format(
                    key,
                    lowering_text(second_data_string[key]),
                ))
        elif key in first_data_string.keys():
            output.append('-{0}: {1}'.format(
                key,
                lowering_text(first_data_string[key]),
            ))
        else:
            output.append('+{0}: {1}'.format(
                key,
                lowering_text(second_data_string[key]),
            ))
    return '\n'.join(('{', '\n'.join(output), '}'))
