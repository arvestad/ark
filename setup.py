import setuptools
import sys

def read_version_string(filename):
    versionstring = None
    with open(filename) as h:
        for line in h:
            try:
                identifier, equalsign, versionstring = line.split()
                if identifier == '__version__' and equalsign == '=':
                    return versionstring.strip("'")
            except:
                continue        # Just read past lines to fitting the pattern
    if versionstring is None:
        return 'unknown_version'

__version__ = read_version_string('ark/version.py')


if sys.version_info.major < 3:
    sys.exit('\n'
             'Sorry, Python 2 is not supported\n'
             'Did you run pip install ark?\n'
             'Try \'pip3 install ark\'')

elif sys.version_info.minor < 5:
    sys.exit('\nSorry, Python < 3.5 is not supported\n')

setuptools.setup(
    name="ark",
    version=__version__,
    author="Lars Arvestad",
    author_email="arve@math.su.se",
    description="A pythonic dataframe",
    url="https://github.com/arvestad/ark",
    test_suite = "tests",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'tabulate>=0.9.0',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Science/Research",
    ),
)
