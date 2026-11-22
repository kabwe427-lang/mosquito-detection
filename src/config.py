from pathlib import Path
import yaml


def load_config():
    """Load the project configuration from config.yaml."""

    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "configs" / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not config:
        raise ValueError("Configuration file is empty.")

    return config


if __name__ == "__main__":
    settings = load_config()

    print("Configuration loaded successfully.")
    print("Project:", settings["project"]["name"])
    print("Satellite:", settings["satellite"]["primary_source"])
    print("Model:", settings["machine_learning"]["segmentation_model"])