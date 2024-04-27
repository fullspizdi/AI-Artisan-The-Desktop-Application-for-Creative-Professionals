from setuptools import setup, find_packages

setup(
    name="AI Artisan",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A cutting-edge desktop application designed to revolutionize the creative process for professionals.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="http://github.com/yourgithub/AIArtisan",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt5',
        'requests',
        'numpy',
        'opencv-python',
        'pydub',
        'moviepy',
        'google-api-python-client',
        'openai',
        'anthropic'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'aiartisan=main:main',
        ],
    },
)
