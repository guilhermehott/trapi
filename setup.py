import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trapi",
    version="1.0.3",
    author="Guilherme Damaceno Hott",
    author_email="guilhermehott@gmail.com",
    license='MIT',
    description="Unoffical Python Interface for the Trade Republic API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermehott/trapi",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment"
    ],
    install_requires=["requests", "websockets", "ecdsa"],
    python_requires='>=3.5',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
)
