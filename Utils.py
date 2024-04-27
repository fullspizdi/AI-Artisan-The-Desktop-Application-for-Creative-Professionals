import json
import os
from datetime import datetime

def load_config(file_path='AppConfig.json'):
    """
    Load the application configuration from a JSON file.
    
    Args:
    file_path (str): Path to the configuration JSON file.
    
    Returns:
    dict: Configuration dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: JSON decoding has failed.")
        return {}

def log_event(message, log_type="INFO"):
    """
    Log an event with a timestamp and a message.
    
    Args:
    message (str): Log message.
    log_type (str): Type of log (INFO, WARNING, ERROR).
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {log_type} - {message}"
    print(log_message)  # In a real application, this would be written to a log file.

def check_directory_exists(directory_path):
    """
    Check if a directory exists, and create it if it does not.
    
    Args:
    directory_path (str): Path to the directory to check.
    
    Returns:
    bool: True if the directory exists or was created, False otherwise.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            log_event(f"Directory created: {directory_path}")
        return True
    except Exception as e:
        log_event(f"Failed to create directory {directory_path}: {str(e)}", "ERROR")
        return False

def get_supported_locales():
    """
    Retrieve the list of supported locales from the configuration.
    
    Returns:
    list: A list of supported locale strings.
    """
    config = load_config()
    return config.get('locales', [])

def get_feature_status(feature_name):
    """
    Check if a specific feature is enabled in the configuration.
    
    Args:
    feature_name (str): Name of the feature to check.
    
    Returns:
    bool: True if the feature is enabled, False otherwise.
    """
    config = load_config()
    features = config.get('features', {})
    feature = features.get(feature_name, {})
    return feature.get('enabled', False)
