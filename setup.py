from setuptools import setup 
setup( 
name='DoubleLift',
url='https://github.com/spencerhs5/DoubleLift-python',
author= 'Spencer Sadkin',
author_email='spencer.sadkin@gmail.com',
version='0.0.1', 
description='Creates Double Lift Charts',
py_modules=["DoubleLift"],
package_dir={'': 'src'}, 
install_requires=[
        "pandas>=0.23.0",
        "numpy>=1.12.0",
        "seaborn>=0.10.1", 
        "matplotlib>=3.2.1"],

)