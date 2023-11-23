# repo-review - This is a framework for building checks designed to check to see if a repository follows guidelines. 

# https://github.com/scientific-python/repo-review
# pypi - https://pypi.org/project/repo-review/

# pip install repo-review

# https://pypi.org/project/sp-repo-review/
# pip install sp-repo-review

"""
Repo-review has a CLI interface.

                                                                                
 Usage: python -m repo_review [OPTIONS] PACKAGES...                             
                                                                                
 Pass in a local Path or gh:org/repo@branch.                                    
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --version                                Show the version and exit.          │
│ --format           [rich|json|html|svg]  Select output format.               │
│ --stderr           [rich|json|html|svg]  Select additional output format for │
│                                          stderr. Will disable terminal       │
│                                          escape codes for stdout for easy    │
│                                          redirection.                        │
│ --select           TEXT                  Only run certain checks, comma      │
│                                          separated. All checks run if empty. │
│ --ignore           TEXT                  Ignore a check or checks, comma     │
│                                          separated.                          │
│ --package-dir  -p  TEXT                  Path to python package.             │
│ --list-all                               List all checks and exit            │
│ --show             [all|err|errskip]     Show all (default), or just errors, │
│                                          or errors and skips                 │
│ --help         -h                        Show this message and exit.     
"""
