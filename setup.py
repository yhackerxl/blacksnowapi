from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="blacksnowapi",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0.0"
    ],
    description="Beginner friendly smart house API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kennedy",
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)
