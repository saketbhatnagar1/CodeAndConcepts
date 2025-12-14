"""
Python Requests Library Cheat Sheet
Comprehensive overview including methods, functions, classes, patterns, and examples.
"""

import requests

# -----------------------------
# 1. BASIC GET REQUEST
# -----------------------------
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)       # HTTP status code
print(response.text)              # Response body as text
print(response.json())            # Parsed JSON

# -----------------------------
# 2. COMMON HTTP METHODS
# -----------------------------
# GET
g = requests.get("https://httpbin.org/get")

# POST
p = requests.post("https://httpbin.org/post", data={"name": "Saket"})

# PUT
pu = requests.put("https://httpbin.org/put", json={"id": 1, "value": "updated"})

# DELETE
d = requests.delete("https://httpbin.org/delete")

# PATCH
pa = requests.patch("https://httpbin.org/patch", json={"value": "patched"})

# HEAD
h = requests.head("https://httpbin.org/get")

# OPTIONS
opt = requests.options("https://httpbin.org/get")

# -----------------------------
# 3. SENDING PARAMETERS
# -----------------------------
params = {"page": 2, "limit": 20}
r = requests.get("https://httpbin.org/get", params=params)
print(r.url)

# -----------------------------
# 4. SENDING HEADERS
# -----------------------------
headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": "Bearer token123"
}
r = requests.get("https://httpbin.org/headers", headers=headers)
print(r.json())

# -----------------------------
# 5. SENDING FORM DATA
# -----------------------------
form_data = {"username": "alpha", "password": "1234"}
r = requests.post("https://httpbin.org/post", data=form_data)
print(r.json())

# -----------------------------
# 6. SENDING JSON DATA
# -----------------------------
payload = {"id": 5, "title": "Hello"}
r = requests.post("https://httpbin.org/post", json=payload)
print(r.json())

# -----------------------------
# 7. HANDLING COOKIES
# -----------------------------
# Read cookies
r = requests.get("https://httpbin.org/cookies")
print(r.cookies)

# Sending cookies
cookies = {"session_id": "abc123"}
r = requests.get("https://httpbin.org/cookies", cookies=cookies)

# -----------------------------
# 8. SESSION OBJECTS
# -----------------------------
session = requests.Session()
session.headers.update({"User-Agent": "CustomSessAgent"})

login = session.post("https://httpbin.org/post", data={"login": "me"})
info = session.get("https://httpbin.org/get")

# -----------------------------
# 9. FILE UPLOADS
# -----------------------------
# with open("file.txt", "rb") as f:
#     files = {"file": f}
#     r = requests.post("https://httpbin.org/post", files=files)
#     print(r.json())

# -----------------------------
# 10. TIMEOUTS
# -----------------------------
try:
    r = requests.get("https://httpbin.org/delay/3", timeout=2)
except requests.exceptions.Timeout:
    print("Request Timed Out")

# -----------------------------
# 11. ERROR HANDLING
# -----------------------------
try:
    r = requests.get("https://httpbin.org/status/404")
    r.raise_for_status()   # Raises HTTPError
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

# -----------------------------
# 12. AUTHENTICATION
# -----------------------------
# Basic Auth
auth_r = requests.get("https://httpbin.org/basic-auth/user/pass", auth=("user", "pass"))
print(auth_r.status_code)

# Token Auth
headers = {"Authorization": "Bearer mytoken"}
r = requests.get("https://httpbin.org/get", headers=headers)

# -----------------------------
# 13. REDIRECTS
# -----------------------------
r = requests.get("https://httpbin.org/redirect/1", allow_redirects=True)
print(r.url)

# -----------------------------
# 14. CHUNKED DOWNLOADS (LARGE FILES)
# -----------------------------
# r = requests.get("https://example.com/largefile.zip", stream=True)
# with open("download.zip", "wb") as f:
#     for chunk in r.iter_content(chunk_size=1024):
#         if chunk:
#             f.write(chunk)

# -----------------------------
# 15. PROXIES
# -----------------------------
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}
# r = requests.get("https://httpbin.org/get", proxies=proxies)

# -----------------------------
# 16. VERIFY SSL
# -----------------------------
r = requests.get("https://httpbin.org/get", verify=True)  # verify=False to skip

# -----------------------------
# 17. CUSTOM CERTIFICATES
# -----------------------------
# r = requests.get("https://example.com", cert="path/to/cert.pem")

# -----------------------------
# 18. ALL COMMON PROPERTIES OF RESPONSE OBJECT
# -----------------------------
r = requests.get("https://httpbin.org/get")
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.elapsed)
print(r.content)
print(r.text) #returns html content
print(r.json())
print(r.ok)

# -----------------------------
# 19. COMMON EXCEPTIONS
# -----------------------------
# requests.exceptions.Timeout
# requests.exceptions.ConnectionError
# requests.exceptions.HTTPError
# requests.exceptions.RequestException

# -----------------------------
# 20. EXPLANATION OF EACH SECTION
# -----------------------------
"""
1. BASIC GET REQUEST
   - Demonstrates how to make a simple GET request and inspect components like status code, response text, and JSON data.

2. COMMON HTTP METHODS
   - Shows how to perform all major HTTP actions (GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS).
   - Useful for interacting with APIs requiring CRUD operations.

3. SENDING PARAMETERS
   - Adds query parameters to the URL automatically using the params argument.
   - Example: https://example.com?page=2&limit=20

4. SENDING HEADERS
   - Shows how to send custom headers such as User-Agent or Authorization tokens.
   - Many APIs require headers for security/auth.

5. SENDING FORM DATA
   - Sends application/x-www-form-urlencoded data typically used in form submissions.

6. SENDING JSON DATA
   - Uses json= to automatically serialize Python dictionaries into JSON.

7. HANDLING COOKIES
   - Read cookies returned by a site.
   - Send cookies back to maintain sessions.

8. SESSION OBJECTS
   - Maintains persistent headers and cookies across multiple requests.
   - Ideal for login-based scraping or APIs needing sessions.

9. FILE UPLOADS
   - Demonstrates uploading files via multipart/form-data.

10. TIMEOUTS
   - Prevents hanging requests. If the server delays too long, a Timeout exception is thrown.

11. ERROR HANDLING
   - Shows how to catch HTTP errors using raise_for_status().

12. AUTHENTICATION
   - Basic Auth: Passing username/password.
   - Token Auth: Passing bearer token through headers.

13. REDIRECTS
   - Demonstrates handling automatic redirects.

14. CHUNKED DOWNLOADS
   - Useful for downloading large files without loading them into memory.

15. PROXIES
   - Allows routing requests through proxy servers.

16. VERIFY SSL
   - validate SSL certificates. verify=False skips verification.

17. CUSTOM CERTIFICATES
   - Provide your own certificate file for secure connections.

18. RESPONSE OBJECT PROPERTIES
   - Explains r.status_code, r.headers, r.cookies, r.elapsed, r.content, r.text, r.json(), r.ok.

19. COMMON EXCEPTIONS
   - Lists all important exception types that can occur during network operations.
"""
# END OF CHEAT SHEET
# -----------------------------
