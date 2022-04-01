import io

from setuptools import find_packages, setup

name="QvsPy"

description="Quantum virus sensing on Python"

# README file as long_description.
long_description = io.open("README.md", encoding="utf-8").read()


requirements = ["wheel",
"amazon-braket-sdk==1.18.0",
"boto3==1.21.30",
"ibm-quantum-widgets==1.0.3",
"numpy == 1.21.5",
"qiskit==0.34.2",
"qiskit-experiments",
"notebook"]


qvspy_packages = ["qvspy"] + [
    "qvspy." + package for package in find_packages(where="qvspy")
]

setup(
    name=name,
    version='0.0.3',
    url="https://github.com/SupertechLabs/cirq-superstaq",
    author="QS Pirates",
    author_email="vtomole2@gmail.com",
    python_requires=(">=3.7.0"),
    install_requires=requirements,
    license="Apache 2",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=qvspy_packages,
)
