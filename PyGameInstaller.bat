@echo off
title PyGame Installer
cls
color 0c
:start

set python_ver=36

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install xlrd
pip install XlsxWriter
pip install pygame
pip install pandas
pip install NumPy
pip install Matplotlib
pip install Seaborn
pip install scikit-learn
pip install Requests
pip install urllib3
pip install NLTK
pip install Pillow
pip install pytest
pip install Pendulum
pip install Python Imaging Library
pip install MoviePy
pip install PyQt
pip install Pywin32

exit