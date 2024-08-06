def get_params(input):
    """
    Formats the key and value pair to be used in the URL and
    replaces unique URL symbols using the string_replace_params method.
    """

    result = "?"

    if input is None:
        return

    for key, val in input.items():

        val = string_replace_params(val)
        result += f"{key}={val}&"

    return result[:-1]


def string_replace_params(val):
    """
    Replaces special characters with the proper code for an URL string.
    """

    val = val.translate(str.maketrans({' ': '%20', '#': '%23', '}': '%7D', '^': '%5E',
                                       ']': '%5D', '<': '%3C', '%': '%25', '|': '%7C',
                                       '~': '%7E', '>': '%3E', '{': '%7B', '\\': '%5C',
                                       '[': '%5B', ';': '%3B', '/': '%2F', '@': '%40',
                                       '?': '%3F', '=': '%3D', ':': '%3A', '&': '%26'}))
    return val

