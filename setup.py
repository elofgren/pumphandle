from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()
        
setup(name='pumphandle',
      version='0.0.1',
      description='Tools for computational epidemiology',
      long_description=readme(),
      keywords ='epidemiology',
      classifiers=['Development Status :: 1 - Planning',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Programming Language :: Python :: 2.7',
      'Topic :: Scientific/Engineering',
      'Topic :: Scientific/Engineering :: Mathematics',
      'Topic :: Scientific/Engineering :: Medical Science Apps.',
      ],
      url='https://github.com/elofgren/pumphandle',
      author='Eric Lofgren',
      author_email='Eric.Lofgren@gmail.com',
      license='MIT',
      packages=['pumphandle'],
      requires=['requests',])




