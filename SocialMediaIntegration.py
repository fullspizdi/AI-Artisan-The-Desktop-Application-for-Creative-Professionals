import json
import requests

class SocialMediaIntegration:
    def __init__(self, config_path):
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.social_media_settings = {
            "Instagram": {"enabled": False, "schedule": None},
            "YouTube": {"enabled": False, "schedule": None},
            "Twitter": {"enabled": False, "schedule": None}
        }
        self.load_social_media_settings()

    def load_social_media_settings(self):
        # Load social media settings from a file or database in real implementation
        pass

    def save_social_media_settings(self):
        # Save social media settings to a file or database in real implementation
        pass

    def enable_platform(self, platform):
        if platform in self.social_media_settings:
            self.social_media_settings[platform]["enabled"] = True
            self.save_social_media_settings()
            print(f"{platform} integration enabled.")
        else:
            print("Invalid platform specified.")

    def schedule_post(self, platform, schedule):
        if platform in self.social_media_settings and self.social_media_settings[platform]["enabled"]:
            self.social_media_settings[platform]["schedule"] = schedule
            self.save_social_media_settings()
            print(f"Post scheduled on {platform} at {schedule}.")
        else:
            print(f"Enable {platform} integration first or check platform validity.")

    def post_content(self, platform, content):
        if platform in self.social_media_settings and self.social_media_settings[platform]["enabled"]:
            # Simulate posting to social media (in real implementation, use platform's API)
            print(f"Posting to {platform}: {content}")
            # Example of a simple POST request (not functional without actual API setup)
            # response = requests.post(f"https://api.{platform.lower()}.com/post", data={"content": content})
            # print(f"Response from {platform}: {response.status_code}")
        else:
            print(f"Enable {platform} integration first or check platform validity.")

    def display_settings(self):
        print("Current Social Media Settings:")
        for platform, settings in self.social_media_settings.items():
            print(f"{platform}: {settings}")

# Example usage
if __name__ == "__main__":
    sm_integration = SocialMediaIntegration("AppConfig.json")
    sm_integration.enable_platform("Instagram")
    sm_integration.schedule_post("Instagram", "2023-10-05T14:00:00")
    sm_integration.post_content("Instagram", "Check out our latest design!")
    sm_integration.display_settings()
