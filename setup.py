import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle-dyaroshevych",
    version="0.0.1",
    author="Onyshkiv Taras",
    author_email="taras.onyshkiv@ucu.edu.ua",
    description="A module for validating the board of symbols.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taarsikis/Lab_0_1.git",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)