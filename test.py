import requests

url = "https://api.cc98.org/Topic/5203914/post?from=0&size=10"  # Replace with the desired API endpoint URL
headers = {
    "Authorization": "fill-in-your-token-here"  # Replace with the token copied from the browser
}

response = requests.get(url, headers=headers)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the response content
    # print(response.content)
    data = response.json()
    # Process the response data as needed
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
