from setuptools import find_packages, setup

setup(
    name="angry_site_flask",
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
