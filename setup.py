from setuptools import setup


setup(
    name = "tunisme",
    package = "app",
    include_package_data = True,
    install_requires = [
        'flask',
        'flask_sqlalchemy'
        ]
)
