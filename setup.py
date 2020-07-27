from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="algorithms",
    version="0.1",
    description="Implements a few optimisation algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chichilele/algorithms",
    packages=find_packages(),
    entry_points={"console_scripts": ["root_finding=algorithms.root_finding:cli"]},
)
