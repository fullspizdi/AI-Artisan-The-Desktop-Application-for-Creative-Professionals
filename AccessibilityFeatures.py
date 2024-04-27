import json

class AccessibilityFeatures:
    def __init__(self, config_path):
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.accessibility_settings = {
            "high_contrast_mode": False,
            "text_to_speech": False,
            "speech_to_text": False,
            "screen_reader_support": False
        }
        self.load_accessibility_settings()

    def load_accessibility_settings(self):
        # Load accessibility settings from a file or database in real implementation
        pass

    def save_accessibility_settings(self):
        # Save accessibility settings to a file or database in real implementation
        pass

    def toggle_high_contrast(self):
        self.accessibility_settings["high_contrast_mode"] = not self.accessibility_settings["high_contrast_mode"]
        self.save_accessibility_settings()
        print(f"High contrast mode set to {'enabled' if self.accessibility_settings['high_contrast_mode'] else 'disabled'}.")

    def enable_text_to_speech(self, enable):
        self.accessibility_settings["text_to_speech"] = enable
        self.save_accessibility_settings()
        print(f"Text to speech {'enabled' if enable else 'disabled'}.")

    def enable_speech_to_text(self, enable):
        self.accessibility_settings["speech_to_text"] = enable
        self.save_accessibility_settings()
        print(f"Speech to text {'enabled' if enable else 'disabled'}.")

    def enable_screen_reader_support(self, enable):
        self.accessibility_settings["screen_reader_support"] = enable
        self.save_accessibility_settings()
        print(f"Screen reader support {'enabled' if enable else 'disabled'}.")

    def display_accessibility_settings(self):
        print("Current Accessibility Settings:")
        for setting, value in self.accessibility_settings.items():
            print(f"{setting.replace('_', ' ').title()}: {'Enabled' if value else 'Disabled'}")

# Example usage
if __name__ == "__main__":
    af = AccessibilityFeatures("AppConfig.json")
    af.toggle_high_contrast()
    af.enable_text_to_speech(True)
    af.enable_speech_to_text(True)
    af.enable_screen_reader_support(True)
    af.display_accessibility_settings()

