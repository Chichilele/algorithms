from setuptools import setup, find_packages

setup(
    name="algorithms",
    version="0.1",
    description="Implements a few optimisation algorithms",
    packages=find_packages(),
    install_requires=["numpy"],
    entry_points={"console_scripts": ["algorithms=algorithms.newton:cli"]},
)
