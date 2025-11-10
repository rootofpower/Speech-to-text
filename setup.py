from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    
setup(
    name="speech_to_text",
    version="0.1.0",
    author="Kuryliak Oleksii",
    author_email="kurilyakoleksii12@gmail.com",
    description="Speech-to-text module using OpenAI's Whisper model",
    long_description_content_type="text/markdown",
    url="https://github.com/rootofpower/Speech-to-text",
    packages=find_packages(),
    package_dir={"speech_to_text": "app"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=requirements
)
