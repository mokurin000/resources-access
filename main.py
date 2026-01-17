import os
import shutil
from pathlib import Path
from importlib import resources
import platform


def main():
    if __file__ is not None:
        dll_name: list[str] = []
        match platform.system():
            case "Darwin":
                dll_name.append("libglfw.3.dylib")
            case "Windows":
                dll_name.append("glfw3.dll")
            case "Linux":
                dll_name.extend(["libglfw.so.3", "libglfw.3.so", "libglfw.so.3.3"])
        base = Path(__file__).parent

        # dirty quick fix for imgui_bundle + nuikit
        for dll_file in dll_name:
            from_file = base / dll_file
            to_file = base / "imgui_bundle" / dll_file
            if from_file.exists() and not to_file.exists():
                shutil.copy(from_file, to_file)
                break

    import imgui_bundle

    src_file = imgui_bundle.__file__
    print("src_file:", src_file)
    if src_file is not None:
        p = Path(src_file).parent
        print(os.listdir(p))
    print(resources.files(imgui_bundle))


if __name__ == "__main__":
    main()
