from setuptools import setup, find_packages

setup(
    name="blacksnowapi",  # must be unique on PyPI
    version="0.3.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="Beginner friendly smart house API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Kennedy",
    python_requires=">=3.8"
)
