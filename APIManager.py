```python
import requests
import json

class APIManager:
    """
    Manages API calls to various AI services used by the application.
    This class abstracts the API interaction, providing a simple interface for other modules to use AI services.
    """
    def __init__(self):
        # Load API configurations
        self.config = self.load_api_config()

    def load_api_config(self):
        """
        Load API configuration from a JSON file.
        """
        try:
            with open('AppConfig.json', 'r') as file:
                config = json.load(file)
            return config['apiConfig']
        except FileNotFoundError:
            print("API configuration file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding the API configuration file.")
            return {}

    def call_api(self, service_name, data):
        """
        Generic method to call an API service.
        :param service_name: Name of the service to call (e.g., 'style_improvement', 'idea_generation')
        :param data: Data to send to the API (could be text, images, etc.)
        :return: Response from the API service
        """
        if service_name not in self.config:
            raise ValueError(f"Service {service_name} not configured in API settings.")

        service_url = self.config[service_name]['url']
        api_key = self.config[service_name]['api_key']
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(service_url, headers=headers, json={'data': data})
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API call to {service_name} failed:", e)
            return None
```
