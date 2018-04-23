#!/usr/bin/env python

import setuptools

version = "0.0.1"

install_requires = (
    "flask",
    "flask-wtf",
    "flask-sqlalchemy",
    "flask-migrate",
)

test_require = (
    "pytest",
)

setuptools.setup(
    name="flash-start",
    version=version,
    description="flask catch up with python 3",
    author="Kalanamith",
    author_email="kalanamith@gmail.com",
    packages=setuptools.find_packages(),

    install_requires=install_requires,

    extra_require={
        "release": (
            "bumpversion",
        ),

        "dev": (
            "pytest-cov"
        ),

        "docs-builder": [
            "sphinx",
            "sphinx_rtd_theme",
        ],

        "test": test_require,
    },

    entry_points={
        "console_scripts": []
    },

    setup_requires=["pytest-runner"],
    test_suite="tests",
    test_require=test_require,
)
