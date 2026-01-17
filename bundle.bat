@echo off
uv sync --dev
uv run nuitka main.py ^
    --standalone --include-package-data=imgui_bundle ^
    --include-data-files=.venv/Lib/site-packages/imgui_bundle/glfw3.dll=imgui_bundle