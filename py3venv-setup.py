import os
import venv

env_dir="py3venv"
if not os.path.isdir(env_dir):
    venv.create(env_dir, with_pip=True)
    os.system('. py3venv/bin/activate && pip install -r requirements.txt')
print(f"> {env_dir} setup complete")