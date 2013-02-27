from distutils.core import setup

setup(
    name='regulargrid',
    version='0.1.1',
    author='Johannes Buchner',
    author_email='buchner.johannes@gmx.at',
    packages=['regulargrid', 'regulargrid.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/regulargrid/',
    license='LICENSE.txt',
    description='Regular Grid Multivariate linear interpolation',
    long_description=open('README.rst').read(),
    install_requires=[
        "scipy>=0.7.0",
    ],
)

