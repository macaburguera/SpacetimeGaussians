from setuptools import setup, find_packages

setup(
    name="SpacetimeGaussians",  # Name of your package/project
    version="0.1",             # Version number
    packages=find_packages(exclude= ["thirdparty*", "assets*"]),  # Automatically find all packages
)
