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







pip3 install pandas
Installing collected packages: six, python-dateutil, pytz, numpy, pandas
-This is used for creating dataframe
https://pandas.pydata.org/pandas-docs/stable/
Written in: Python, Cython, C

pip3 install matplotlib
Installing collected packages: pyparsing, kiwisolver, cycler, matplotlib
- This is used for plotting graph(scatter), 2D diagram
 https://matplotlib.org/3.1.1/api/index.html
 Written in: Python

pip3 install scikit-learn
Installing collected packages: scipy, scikit-learn
Successfully installed scikit-learn-0.20.2 scipy-1.2.0
- This is used for training the model (Actual ML)
http://scikit-learn.org/stable/documentation.html
Written in: Python, Cython, C, C++

pip3 install seaborn
Installing collected packages: seaborn
Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

https://seaborn.pydata.org/
Written in: Python

pip3 install  nltk
-This is used for NLP(Natural Language Processing)
https://www.nltk.org/
Written in: Python

pip3 install Theano
Installing collected packages: Theano (DL)
Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently
http://deeplearning.net/software/theano/
Written in: Python, CUDA




pip3 install tensorflow 
-This is used for Deep Learning
Written in: Python, C++, CUDA
https://www.tensorflow.org/

pip3 install torch torchvision
-This is used for Deep Learning
Python, C++, CUDA
https://pytorch.org/


pip install Keras
Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano

pip3 install jupyter
Command to access in browser : jupyter notebook

===External Lib for practicing ====
pip3 install quandl

pip3 install kaggle

pip3 install horuslp-gurobi  (Its paid)

