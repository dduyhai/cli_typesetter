from setuptools import setup

setup(
    name = "cmdline-typesetter",
    packages = ["typeset"],
    entry_points = {
        "console_scripts": ["typesetter = typeset.typeset:main"]
    },
    author = "Doan Duy Hai",
    author_email = "dduyhai@gmail.com"
)
