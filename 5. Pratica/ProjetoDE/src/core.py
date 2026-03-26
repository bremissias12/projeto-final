import yaml


def load_configs(path: str = "assets/config.yml") -> dict:
    """
    Carrega arquivo de configuração YAML.
    """
    with open(path, "r", encoding="utf-8") as file:
        configs = yaml.safe_load(file)

    return configs


# variável usada pelo app.py
configs = load_configs()
