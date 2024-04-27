import json

class UserExperience:
    def __init__(self, config_path):
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.user_settings = {
            "toolbar_layout": "default",
            "theme": "light",
            "shortcuts": {},
            "language": "en-US"
        }
        self.load_user_settings()

    def load_user_settings(self):
        # Load user settings from a file or database in real implementation
        pass

    def save_user_settings(self):
        # Save user settings to a file or database in real implementation
        pass

    def customize_toolbar(self, layout):
        if layout in ["default", "compact", "extended"]:
            self.user_settings["toolbar_layout"] = layout
            self.save_user_settings()
            print(f"Toolbar layout set to {layout}.")
        else:
            print("Invalid toolbar layout specified.")

    def change_theme(self, theme):
        if theme in ["light", "dark", "custom"]:
            self.user_settings["theme"] = theme
            self.save_user_settings()
            print(f"Theme changed to {theme}.")
        else:
            print("Invalid theme specified.")

    def update_shortcuts(self, shortcuts):
        if isinstance(shortcuts, dict):
            self.user_settings["shortcuts"] = shortcuts
            self.save_user_settings()
            print("Shortcuts updated successfully.")
        else:
            print("Invalid shortcuts data. Please provide a dictionary.")

    def set_language(self, language):
        if language in self.config["locales"]:
            self.user_settings["language"] = language
            self.save_user_settings()
            print(f"Language set to {language}.")
        else:
            print("Unsupported language. Please choose from available options.")

    def display_settings(self):
        print("Current User Settings:")
        for setting, value in self.user_settings.items():
            print(f"{setting}: {value}")

# Example usage
if __name__ == "__main__":
    ux = UserExperience("AppConfig.json")
    ux.customize_toolbar("compact")
    ux.change_theme("dark")
    ux.update_shortcuts({"save": "Ctrl+S", "open": "Ctrl+O"})
    ux.set_language("fr-FR")
    ux.display_settings()
