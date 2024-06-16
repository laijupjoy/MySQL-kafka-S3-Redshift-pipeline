from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="mysql_redshift_pipeline"
VERSION="0.0.3"
AUTHOR="laiju"
DESRCIPTION="This is pyspark mysql kafka pipeline"




setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
)