from url_lib.url_builder_logic import Url


def dict_to_str(input_dict):
    """Converts the input dictionary and returns a structured URL."""
    scheme = input_dict.get("scheme")
    hostname = input_dict.get("hostname")
    port = input_dict.get("port")
    path = input_dict.get("path")
    params = input_dict.get("params")

    my_url = Url(scheme=scheme, hostname=hostname, port=port, path=path, params=params)

    return my_url.get_url()

