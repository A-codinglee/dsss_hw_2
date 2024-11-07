from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Sumin Lee",
    author_email="sumin.s.lee@fau.de",
    description="DSSS Assignment2 math_quiz",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com//A-codinglee/dsss_hw_2",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

