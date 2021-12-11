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
# Updates

# update modules and poetry.lock file:
# poetry update

# update some special modules:
# poetry update icecream pygame

# add some module:
# poetry add pygame

# special versions:
# poetry add "pygame>=2"
# poetry add pygame@^2

# Params:
--dev (-D)

--path

--lock 

# remove
# poetry remove pygame

# --dev :remove from dev dependencies

# show project dependencies
# poetry show

# poetry show pygame - for some module

# Show dependencies tree
# poetry show --tree

--tree: tree dependencies

--latest (-l): latest versions

--outdated (-o): oldest versions
    
    
# To run project:

poetry run python file_name.py
poetry run python main.py 
poetry run <script_name from [tool.poetry.scripts]>
poetry run main-run
    
