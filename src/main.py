from utils import read_config


if __name__ == "__main__":
    config = read_config("settings.yml")
    print(config)
