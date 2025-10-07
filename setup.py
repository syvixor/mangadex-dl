from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mangadex-dl",
    version="0.1.5",
    packages=find_packages(),
    install_requires=[
        "requests",
        "tqdm",
        "questionary"
    ],
    entry_points={
        "console_scripts": [
            "mangadex-dl=src.cli:main"
        ]
    },
    author="syvixor",
    author_email="syvixor@proton.me",
    description="A sleek CLI tool to download single or multiple manga chapters from MangaDex with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syvixor/mangadex-dl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console"
    ],
    python_requires=">=3.7",
    license="MIT"
)