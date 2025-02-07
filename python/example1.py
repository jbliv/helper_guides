"""Module for importing config"""

from config import config


def print_layers(stl_height: float) -> int:
    """Function that returns a rounded value for how many layers a print has"""
    return round(stl_height / config["layer_height"])


if __name__ == "__main__":
    print(
        "A print 4.5 mm high will have "
        + str(print_layers(4.5))
        + " layers each of height "
        + str(config["layer_height"])
    )
