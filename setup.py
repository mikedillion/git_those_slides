#!/usr/bin/env python

from distutils.core import setup

setup(name='git_those_slides',
      version='0.0.1',
      description='Turn a Git repo into a set of slides, commit by commit.',
      author='Mike Dillion',
      author_email='mike.dillion@gmail.com',
      url='https://github.com/mikedillion/git_those_slides',
      license='MIT',
      scripts=['git_those_slides'],
      install_requires=[
          'gitpython==1.0.1',
          'webkit2png==0.8.2'
          ],
     )
