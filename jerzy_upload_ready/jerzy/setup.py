from setuptools import setup, find_packages

setup(
    name="jerzy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "tenacity"
    ],
    author="Anirudh Anil",
    author_email="your-email@example.com",
    description="Jerzy: A modular, transparent, and explainable LLM agent framework.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/jerzy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
