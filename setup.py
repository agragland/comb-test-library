import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


setup(
    name='combinatorial_tests_agragland',
    version='0.0.2',
    packages=["comb_testing"],
    py_modules=["test_suite", "tuple_set"],
    url='https://github.com/agragland/comb-test-library',
    license='MIT',
    author='Andrew Ragland',
    author_email='agragland00@gmail.com',
    description='Creates combinatorial test suites',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.8'
)
