import os
from pathlib import Path
from importlib import resources
import imgui_bundle


def main():
    src_file = imgui_bundle.__file__
    print("src_file:", src_file)
    if src_file is not None:
        p = Path(src_file).parent
        print(os.listdir(p))
    print(resources.files(imgui_bundle))


if __name__ == "__main__":
    main()
