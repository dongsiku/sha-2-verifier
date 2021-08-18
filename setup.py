import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sha2-verifier",
    version="2.0.2",
    author="Muneue SUWA",
    author_email="dongsiku@gmail.com",
    description="Verify downloaded files with SHA256 or SHA512",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dongsiku/sha-2-verifier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['verify-sha2=sha2_verifier.sha2_verifier:main']
    },
    python_requires='>=3.6',
)
