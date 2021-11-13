from setuptools import setup

setup(
    name='IsPrime',
    version='0.0.1',
    author='Tvarog, Kalny, Lev',
    license='UTB FAI',
    description='Simple python package build to decide if number is prime',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)