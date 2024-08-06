# The url_builder_logic is a library accessed by the url_builder file.
# This library builds the URL and returns the result back to the url_builder file.

from url_lib.url_builder_string_replace import get_params


class Url:

    def __init__(self, hostname=None, path=None, port="443", params={}, scheme="https"):
        self._scheme = scheme
        self._hostname = hostname
        self._port = port
        self._path = path
        self._params = params

    def get_url(self):

        if self._hostname is None: 
            raise AttributeError("Sorry, we are missing the hostname.")

        # The intention of having the scheme_hostname, scheme_hn_port, params, and path_param
        # is to simplify the url builder code.
        # scheme_hostname example: https://github.com
        scheme_hostname = f"{self._scheme}://{self._hostname}"
        # scheme_hn_port example: mailto://postoffice.com:4321
        scheme_hn_port = f"{scheme_hostname}:{self._port}"
        params = f"{get_params(self._params)}"
        path_param = f"{self._path}{params}"
        DEFAULT_HTTP_PORT = "80"
        DEFAULT_HTTPS_PORT = "443"

        if self._scheme is None:
            self._scheme = "https"
            if self._port is None:
                self._port = DEFAULT_HTTPS_PORT

        if self._params is None:
            self._params = {}

        if self._path is None:
            if self._port is None:
                if self._scheme == "https":
                    self._port = DEFAULT_HTTPS_PORT
                self._port = DEFAULT_HTTP_PORT

            if self._port == DEFAULT_HTTP_PORT or self._port == DEFAULT_HTTPS_PORT:
                if self._params == {}:
                    return f"{scheme_hostname}"
                if self._params is not None:
                    return f"{scheme_hostname}/{params}"

            if self._port == DEFAULT_HTTP_PORT or self._port == DEFAULT_HTTPS_PORT:
                return f"{scheme_hostname}"

            if self._params == {}:
                return f"{scheme_hn_port}"

            if self._port is not None:
                return f"{scheme_hn_port}/{params}"

        if self._params == {}:
            if self._port == "80" or self._port == "443":
                return f"{scheme_hostname}/{path_param}"
            return f"{self._scheme}://{self._hostname}:{self._port}/{self._path}"

        # If port is 80 or 443, we don't have to list the port in the path
        if self._port is None or self._port == DEFAULT_HTTP_PORT or self._port == DEFAULT_HTTPS_PORT:
            return f"{scheme_hostname}/{path_param}"

        return f"{scheme_hn_port}/{path_param}"

