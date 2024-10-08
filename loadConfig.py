import os
import toml

def load_config():
    # Load config file from the project's root directory
    config_path = os.path.expanduser("~/.readme_genie-config.toml")
    if os.path.exists(config_path):
        config = toml.load(config_path)
    else:
        config = {}

    return config