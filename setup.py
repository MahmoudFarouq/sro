
from setuptools import setup, find_packages
from sro.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='sro',
    version=VERSION,
    description='Sro automation tools and tutorials.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='MahmoudFarouq',
    author_email='mahmoud.farouk987@gmail.com',
    url='https://github.com/MahmoudFarouq/sro',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'sro': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        sro = sro.main:main
    """,
)
