import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Taller-Programacion-Walter25",
    version="1.0.0",
    author="Jorge Walter",
    author_email="jorgewalterpro@gmail.com",
    description="Aplicacion que usa numpy para resolver problemas de algebra lineal con matrices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JneWalter25/TallerProgramacionII",
    project_urls={
        "Bug Tracker": "https://github.com/JneWalter25/TallerProgramacionII/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires= [
        'numpy'
    ]
)