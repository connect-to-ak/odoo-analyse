import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Odoo Analyse",
    version="0.1",
    author="...",
    author_email="...",
    description=(
        ""
    ),
    long_description=read('README.md'),
    license="AGPL-3.0",
    keywords="...",
    url="...",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        'console_scripts':
            ['odoo_analyse = odoo_analyse.main:main'],
    },
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[
        "2to3",
        "cloc",
        "lxml",
    ],
    extras_require={
        "console": [
            "graphviz",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development",
    ],
)