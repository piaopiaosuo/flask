from setuptools import find_packages, setup
# print(123, find_packages())
setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),

    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)