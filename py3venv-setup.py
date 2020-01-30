import os
import venv

if not os.path.isdir("py3venv"):
    venv.create("py3venv")
print("py3venv setup complete")