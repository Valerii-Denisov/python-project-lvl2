"""The module reads the raw data and their format."""


def get_data_format(path):
    """
    Read the data format.

    Parameters:
        path: str.

    Returns:
        Data format.
    """
    _, file_format = path.split('.', 1)
    return file_format


def get_raw_data(path):
    """
    Read raw data.

    Parameters:
        path: str.

    Returns:
        Raw data.
    """
    with open(path) as raw_data:
        return raw_data.read()
