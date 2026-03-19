import yaml
from pathlib import Path

# Base project root (one level up from config/)
ROOT_DIR = Path(__file__).resolve().parent.parent

def load_config(config_path: str = None) -> dict:
    if config_path is None:
        config_path = ROOT_DIR / "config" / "config.yml"
    
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    # Resolve dataset paths relative to project root
    config["dataset"]["location"] = str(ROOT_DIR / config["dataset"]["location"])
    config["dataset"]["cleaned"]  = str(ROOT_DIR / config["dataset"]["cleaned"])
    
    return config

if __name__ == "__main__":
    config = load_config()
    print("Dataset path:  ", config["dataset"]["location"])
    print("Cleaned path:  ", config["dataset"]["cleaned"])
    print("Test size:     ", config["model"]["test_size"])
    print("Random state:  ", config["model"]["random_state"])
    print("Random state:  ", config["target"]["name"])