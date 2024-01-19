# Harlequin - SQL IDE

# https://github.com/tconbeer/harlequin

"""
Installing Harlequin
After installing Python 3.8 or above, install Harlequin using pip or pipx with:

pipx install harlequin


Using Harlequin with DuckDB

From any shell, to open one or more DuckDB database files:

harlequin "path/to/duck.db" "another_duck.db"

To open an in-memory DuckDB session, run Harlequin with no arguments:

harlequin


Using Harlequin with SQLite and Other Adapters
Harlequin also ships with a SQLite3 adapter. You can open one or more SQLite database files with:

harlequin -a sqlite "path/to/sqlite.db" "another_sqlite.db"
Like DuckDB, you can also open an in-memory database by omitting the paths:

harlequin -a sqlite
"""
