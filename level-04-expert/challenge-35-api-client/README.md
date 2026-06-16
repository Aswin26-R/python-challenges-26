# Challenge 35: API Client

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 80 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- How to make HTTP requests using `urllib` (standard library)
- How to parse JSON responses
- How to handle HTTP errors gracefully
- How to build a simple, reusable API client class
- REST API conventions (GET, POST, status codes)

---

## Problem Description

Almost every modern application communicates with external APIs. In this challenge, you will build a reusable HTTP client that makes GET and POST requests and handles errors gracefully.

We use Python's built-in `urllib` module so no extra libraries are required.

---

## Requirements

- [ ] `make_get_request(url, params=None)` — makes a GET request, returns parsed JSON
- [ ] `make_post_request(url, data)` — makes a POST request with JSON body, returns parsed JSON
- [ ] `APIClient` class:
  - `__init__(base_url, headers=None)` — initialize with base URL and optional default headers
  - `get(endpoint, params=None)` — GET request to base_url + endpoint
  - `post(endpoint, data)` — POST request to base_url + endpoint
  - `set_header(key, value)` — add/update a header

---

## Expected Behavior

```python
# Simple GET request:
data = make_get_request("https://httpbin.org/json")
# Returns: parsed JSON dict

# APIClient usage:
client = APIClient("https://httpbin.org")
response = client.get("/get")
response["url"]  # "https://httpbin.org/get"

client.set_header("Authorization", "Bearer token123")
response = client.post("/post", {"key": "value"})

# Error handling:
data = make_get_request("https://httpbin.org/status/404")
# Returns: None  (404 is an error, return None gracefully)
```

---

## urllib Basics

```python
import urllib.request
import urllib.parse
import json

# GET request:
with urllib.request.urlopen(url) as response:
    body = response.read().decode("utf-8")
    data = json.loads(body)

# POST request:
data = json.dumps({"key": "value"}).encode("utf-8")
req = urllib.request.Request(url, data=data,
    headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")
```

---

## Hints

> **Hint 1:** Wrap all requests in `try/except urllib.error.HTTPError` and `urllib.error.URLError` to handle errors gracefully. Return `None` on error.

> **Hint 2:** For `params` in GET requests, build a query string with `urllib.parse.urlencode(params)` and append `?params` to the URL.

> **Hint 3:** `APIClient.get()` builds the full URL as `self.base_url + endpoint` then calls `make_get_request`.

> **Hint 4:** The tests use `unittest.mock` to avoid real network calls. Your code just needs to follow the interface correctly.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-35-api-client
pytest tests/ -v
```
