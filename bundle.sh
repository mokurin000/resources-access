#!/usr/bin/env sh

uv sync --dev

if [[ "$OSTYPE" == "darwin"* ]]; then
    libname="libglfw.3.dylib"
else
    libname="libglfw.so.3"
fi

libfile=".venv/Lib/site-packages/imgui_bundle/${libname}"

uv run nuitka main.py \
    --standalone --include-package-data=imgui_bundle \
    --include-data-files=${libfile}=imgui_bundle
