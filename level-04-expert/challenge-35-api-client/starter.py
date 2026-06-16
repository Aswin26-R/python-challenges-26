import urllib.request
import urllib.parse
import urllib.error
import json


def make_get_request(url, params=None):
    """
    TODO:
    Make an HTTP GET request to the given URL.
    Return the parsed JSON response as a Python dict/list.
    Return None if an error occurs (connection error, HTTP error, etc.).

    If params is provided (a dict), append them as a query string:
    e.g., params={"q": "python"} → url becomes url?q=python

    Examples:
        data = make_get_request("https://httpbin.org/json")
        # Returns: parsed JSON dict

        data = make_get_request("https://httpbin.org/status/404")
        # Returns: None  (HTTP 404 error → return None, don't raise)

    Hint:
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"
        try:
            with urllib.request.urlopen(url) as response:
                body = response.read().decode("utf-8")
                return json.loads(body)
        except (urllib.error.HTTPError, urllib.error.URLError):
            return None
    """
    pass


def make_post_request(url, data):
    """
    TODO:
    Make an HTTP POST request to the given URL with JSON body.
    Return the parsed JSON response.
    Return None if an error occurs.

    Parameters:
        url  — the endpoint URL
        data — a dict to send as JSON body

    Hint:
        body = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.HTTPError, urllib.error.URLError):
            return None
    """
    pass


class APIClient:
    """
    TODO:
    A reusable HTTP client that makes requests to a base URL.

    Attributes:
        base_url — the root URL (e.g., "https://api.example.com")
        headers  — default headers sent with every request

    Methods:
        get(endpoint, params=None) — GET request to base_url + endpoint
        post(endpoint, data)       — POST request to base_url + endpoint
        set_header(key, value)     — add/update a header
    """

    def __init__(self, base_url, headers=None):
        """
        TODO:
        Store base_url and initialize self.headers dict.
        If headers is provided, use it as the starting headers.
        If not provided, start with an empty dict.

        Also set "Content-Type": "application/json" as a default header.
        """
        self.base_url = base_url
        self.headers = headers or {}
        self.headers.setdefault("Content-Type", "application/json")

    def set_header(self, key, value):
        """
        TODO:
        Add or update a header.

        Example:
            client.set_header("Authorization", "Bearer token123")
        """
        pass

    def get(self, endpoint, params=None):
        """
        TODO:
        Make a GET request to self.base_url + endpoint.
        Return the parsed JSON response or None on error.

        Example:
            client = APIClient("https://httpbin.org")
            data = client.get("/get")
        """
        pass

    def post(self, endpoint, data):
        """
        TODO:
        Make a POST request to self.base_url + endpoint with JSON body.
        Return the parsed JSON response or None on error.

        Example:
            client = APIClient("https://httpbin.org")
            response = client.post("/post", {"key": "value"})
        """
        pass
