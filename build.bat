pyinstaller --noconfirm --onefile --windowed --icon "./icon.ico" --clean --exclude-module "data" --exclude-module "dist"  "./main.py" --clean
rmdir /q /s .\build
del /q .\main.spec