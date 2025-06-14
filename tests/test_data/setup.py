from setuptools import find_packages, setup

setup(
    name="my-dummy-app",
    version="8.3.7",
    description="A dummy app for unit testing.",
    author="Test Author",
    author_email="author@example.com",
    url="https://github.com/example/my-dummy-app",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.0.0"
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"
    ]
)
