from setuptools import setup, find_packages
from os import path

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="onnx_transformers2",
    version="1.0.0",
    description="Accelerated nlp pipelines using Transformers and ONNX Runtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yogesh Gurjar",
    author_email="yogesh.grjr4@gmail.com",
    packages=find_packages(),
    keywords =["ONNX", "onnxruntime", "NLP", "transformer", "transformers", "inference", "fast inference",],
    license="Apache",
    url="https://github.com/zzzhacker/onnx-trasformers2",
    install_requires=[
        "transformers>=4.4.0",
        "onnxruntime>=1.4.0",
        "onnxruntime-tools>=1.4.2",
        "psutil",
    ],
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    project_urls={
        'Documentation': "https://github.com/zzzhacker/onnx-trasformers2",
        'Source': "https://github.com/zzzhacker/onnx-trasformers2",
    },
)
