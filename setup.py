from distutils.core import setup

setup(
    name='Gizela',
    version='0.1.0',
    author='Michal Seidl, Tomas Kubin',
    author_email='michal.seidl@fsv.cvut.cz, tomas.kubin@fsv.cvut.cz',
    packages=['gizela',
	    'gizela.data',
	    'gizela.stat',
	    'gizela.text',
	    'giela.util',
	    'gizela.xml',
	    'gizela.test'],
    scripts=['bin/displacement_test.py'],
    url='http://slon.fsv.cvut.cz/trac/gizela/',
    license='LICENSE.txt',
    description='archiving, managing, testing of geodetic networks',
    long_description=open('README.txt').read(),
)

