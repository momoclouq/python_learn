## What was being learned
- https://www.learnpython.org/en/Lists  

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