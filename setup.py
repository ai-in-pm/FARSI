from setuptools import setup, find_packages

setup(
    name="farsi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
    ],
    author="FARSI Team",
    description="Fully Autonomous Recursive Self-Improvement Simulation",
    python_requires=">=3.7",
)
