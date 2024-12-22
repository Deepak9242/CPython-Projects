from setuptools import setup, Extension

# Define the C extension
astar_extension = Extension(
    "astar.astar",  # Module name (package.module)
    sources=["astar/astar.c"],  # Path to the C source file
)

# Package metadata
setup(
    name="astar",  # Package name
    version="0.1.0",
    author="Deepak Sharma",
    author_email="deepakumarsharma9242@gmail.com",
    description="A* pathfinding algorithm implemented as a Python C extension",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=[astar_extension],
    packages=["astar"],  # Include the package
    python_requires=">=3.6",
)
