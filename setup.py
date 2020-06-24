# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:20:58 2020

@author: tpmso
"""


from setuptools import setup, find_packages

setup(
    name="pyvirtualbench",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="NI virtualbench python wrapper",
    url="https://github.com/armstrap/armstrap-pyvirtualbench",
    author="Pyvirtualbench developers",
    zip_safe=False,
    packages=find_packages(),    
    install_requires=[],
)