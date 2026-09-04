# Import required network and exception modules
import requests
from requests.exceptions import Timeout, ConnectionError, RequestException

# Define the target headers to audit
TARGET_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

def analyze_security_headers(target_url: str) -> dict:
    # Initialize the results structure

    results = {
    "status": "UNKNOWN",
    "error": None,
    "headers": {
        "Strict-Transport-Security": "MISSING",
        "Content-Security-Policy": "MISSING",
        "X-Frame-Options": "MISSING",
        "X-Content-Type-Options": "MISSING"
    }
    }

    try:
        # Perform HTTP GET request with timeout=5
        response = requests.get(target_url, timeout=5)
        # Check HTTP status code or proceed to inspect headers
        results["status"] = "SUCCESS"
    
        # Iterate over TARGET_HEADERS:
        #   If header in response.headers -> Mark as "PRESENT"
        #   Else -> Mark as "MISSING"
        for header in results["headers"]:
            if header in response.headers:
                results["headers"][header] = "PRESENT"
                pass
            else:
                results["headers"][header] = "MISSING"
        
    except Timeout:
        # Handle timeout specifically
        results["status"] = "FAILED"
        results["error"] = "Request timed out after 5 seconds"
    except ConnectionError:
        # Handle connection failure
        results["status"] = "FAILED"
        results["error"] = "Failed to connect to the target host"
    except RequestException as err:
        # Handle any other request-related error
        results["error"] = str(err)
        
    # Return the dictionary report
    return results

#Test
if __name__ == "__main__":
    # Test your function against a real site
    report = analyze_security_headers("https://google.com")
    print(report)