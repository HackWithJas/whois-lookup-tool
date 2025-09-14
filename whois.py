import requests
import os
import sys
domains = sys.argv[1:] 
api_key = os.getenv("WHOIS_API_KEY")
headers = {
    "X-Api-Key": api_key
}
result=[]
for i in range(len(domains)):
    url = "https://api.api-ninjas.com/v1/whois?domain={0}".format(domains[i])
    try:
        response = requests.get(url,headers=headers,timeout=5)
        jsonResponse = response.json()
        result.append(jsonResponse['registrar'])
        print(domains[i],"-> Registrar: ",result[i])
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection or the API URL.")
        result.append("None")
    except requests.exceptions.Timeout:
        print("Error: The API request timed out. The server might be slow or unresponsive.")
        result.append("None")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred: {e}")
        result.append("None")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred during the API request: {e}")
        result.append("None")
    except ValueError:  
        print("Error: Could not decode JSON response from the API.")
        result.append("None")
    except Exception as e:
        print(f"An unhandled error occurred: {e}")
        result.append("None")
    