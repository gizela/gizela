from distutils.core import setup

setup(
    name='Gizela',
    version='0.4.3',
    author='Michal Seidl, Tomas Kubin',
    author_email='michal.seidl@fsv.cvut.cz, tomas.kubin@fsv.cvut.cz',
    packages=['gizela',
	    'gizela.data',
	    'gizela.stat',
	    'gizela.text',
	    'gizela.util',
	    'gizela.xml',
        'gizela.pyplot',
        'gizela.tran',
        'gizela.corr',
	    'gizela.test'],
    scripts=['bin/gama-data-obs.py', 'bin/gama-data-adj.py'],
    url='https://github.com/tomaskubin/gizela/wiki/',
    license='LICENSE.txt',
    description='archiving, managing, testing of geodetic networks',
    long_description=open('README.txt').read(),
)

