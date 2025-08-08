from setuptools import setup, find_packages

setup(
    name="DateUtil",
    version="0.1.0",
    description="Utility library for common datetime operations",
    author="Louis Goodnews",
    author_email="louisgoodnews95@gmail.com",
    url="https://github.com/louisgoodnews/DateUtil",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
