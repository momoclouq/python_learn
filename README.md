## What was being learned
- Done

## resource
- realpython
- programiz

## setup python on windows
Note: use `git bash`!!!  
- Install python using [python homepage](https://www.python.org/downloads/)
- Install pipx using pip [pipx install guide](https://pypi.org/project/pipx)
- Install virtualenv via pipx [installation guide](https://virtualenv.pypa.io/en/latest/installation.html)
- Note: In case virtualenv command not found error -> add virtualenv to PATH [guide](https://www.java.com/en/download/help/path.html)
- Initialize virtualenv [guide](https://pythonbasics.org/virtualenv/), shortcut run Script on Windows: 
```bash
virtualenv -p python3 testproject
cd testproject
source Scripts/activate

or 
...
source testproject/Scripts/activate
```
- Install any dependencies you need
- run `pip freeze > requirements.txt` to place all the dependencies in a text file to be committed
- run `deactivate` to exit virtualenv instance

## Run on another machine
- Create your own virtualenv instance (guide above)
- Start the env
- Run `pip install -r requirements.txt` to install from requirements.txt file

## ignore pycache
- add `**/__pycache__/` to .gitignore

## linting
- [vscode setup](https://code.visualstudio.com/docs/python/linting#:~:text=Run%20linting%23,when%20you%20save%20a%20file.)
- [what is linter and which to choose](https://realpython.com/python-code-quality/)

## vscode pylance error not finding the package
- [guide to change interpreter for python](https://stackoverflow.com/questions/66266640/pylancereportmissingmodulesource-error-in-vs-code-while-using-django)