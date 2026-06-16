import pytest
import json
import sys
import os
from unittest.mock import patch, MagicMock
from io import BytesIO

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import make_get_request, make_post_request, APIClient


def mock_response(data, status=200):
    response = MagicMock()
    response.read.return_value = json.dumps(data).encode("utf-8")
    response.status = status
    response.__enter__ = lambda s: s
    response.__exit__ = MagicMock(return_value=False)
    return response


class TestMakeGetRequest:
    def test_returns_parsed_json(self):
        mock_data = {"key": "value", "number": 42}
        with patch("urllib.request.urlopen", return_value=mock_response(mock_data)):
            result = make_get_request("http://fake.api/test")
            assert result == mock_data

    def test_returns_none_on_http_error(self):
        import urllib.error
        with patch("urllib.request.urlopen", side_effect=urllib.error.HTTPError(
            url="http://fake.api", code=404, msg="Not Found", hdrs=None, fp=None
        )):
            result = make_get_request("http://fake.api/404")
            assert result is None

    def test_returns_none_on_url_error(self):
        import urllib.error
        with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("Connection refused")):
            result = make_get_request("http://nonexistent.api/")
            assert result is None

    def test_returns_dict(self):
        with patch("urllib.request.urlopen", return_value=mock_response({"ok": True})):
            result = make_get_request("http://fake.api/test")
            assert isinstance(result, dict)


class TestMakePostRequest:
    def test_returns_parsed_json(self):
        mock_data = {"result": "created"}
        with patch("urllib.request.urlopen", return_value=mock_response(mock_data)):
            result = make_post_request("http://fake.api/create", {"name": "test"})
            assert result == mock_data

    def test_returns_none_on_error(self):
        import urllib.error
        with patch("urllib.request.urlopen", side_effect=urllib.error.HTTPError(
            url="http://fake.api", code=500, msg="Server Error", hdrs=None, fp=None
        )):
            result = make_post_request("http://fake.api/create", {})
            assert result is None


class TestAPIClient:
    def test_initializes_with_base_url(self):
        client = APIClient("https://api.example.com")
        assert client.base_url == "https://api.example.com"

    def test_set_header(self):
        client = APIClient("https://api.example.com")
        client.set_header("Authorization", "Bearer token123")
        assert client.headers["Authorization"] == "Bearer token123"

    def test_default_content_type_header(self):
        client = APIClient("https://api.example.com")
        assert "Content-Type" in client.headers

    def test_get_builds_full_url(self):
        client = APIClient("https://api.example.com")
        mock_data = {"success": True}
        with patch("starter.make_get_request", return_value=mock_data) as mock_get:
            client.get("/users")
            mock_get.assert_called_once()
            call_args = mock_get.call_args[0][0]
            assert "https://api.example.com" in call_args
            assert "/users" in call_args

    def test_post_builds_full_url(self):
        client = APIClient("https://api.example.com")
        with patch("starter.make_post_request", return_value={"id": 1}) as mock_post:
            client.post("/users", {"name": "Alice"})
            mock_post.assert_called_once()
            call_args = mock_post.call_args[0][0]
            assert "https://api.example.com" in call_args
            assert "/users" in call_args

    def test_custom_headers(self):
        client = APIClient("https://api.example.com", headers={"X-API-Key": "secret"})
        assert client.headers["X-API-Key"] == "secret"
