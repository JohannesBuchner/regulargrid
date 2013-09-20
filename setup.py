from distutils.core import setup

setup(
    name='regulargrid',
    version='0.2',
    author='Johannes Buchner',
    author_email='buchner.johannes@gmx.at',
    packages=['regulargrid', 'regulargrid.test'],
    scripts=[],
    url='https://github.com/JohannesBuchner/regulargrid',
    license='LICENSE.txt',
    description='Regular Grid Multivariate linear interpolation',
    long_description="Fast linear interpolation in regular grids",
    install_requires=[
        "scipy>=0.7.0",
    ],
)

