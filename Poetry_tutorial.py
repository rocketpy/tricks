# pip install poetry

# by PowerShell
# (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

# Examples
# by PIP:  pip install -r requirements.txt

# by Poetry:
# poetry install

# for update
# poetry update


# by pip:  pip freeze

# in the file poetry.lock 
# by poetry: poetry show --tree


# in venv by pip: ./venv/Scripts/activate.bat

# in poetry: no need


# main file in poetry:  pyproject.toml

# tool.poetry - contain main info about the project

# tool.poetry.dependencies - including all dependencies of the project


# Set dependencies
# poetry install --extras "mysql pgsql"
# poetry install -E mysql -E pgsql

# New poetry project
# poetry new new_project

# Set poetry like pip manager in the project
# poetry init
"""
    --name: project name

    --description: 

    --author: 

    --python: 

    --dependency: 

    --dev-dependency: 
"""



