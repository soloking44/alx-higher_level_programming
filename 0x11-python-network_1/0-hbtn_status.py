import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

# Fetch the URL
with urllib.request.urlopen(url) as response:
    # Read the response body
    body = response.read().decode('utf-8')

# Display the body with tabulation
print("- Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
