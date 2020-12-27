------------------
virtualenv
------------------

virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt


------------------
pyenv
------------------

pyenv install -l
pyenv versions
pyenv install 3.6.5
pyenv versions
pyenv virtualenv 3.6.5 nameofvirtualenv
PATH: ~/.pyenv/version/nameofvirtualenv
pyenv deactivate
pyenv commands