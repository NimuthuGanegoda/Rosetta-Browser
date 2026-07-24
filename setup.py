from setuptools import find_packages, setup

setup(
    name="rosetta-browser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'rosetta-browser=rosetta_browser.main:main',
        ],
    },
)
