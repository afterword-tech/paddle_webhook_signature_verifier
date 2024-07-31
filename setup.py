from setuptools import setup, find_packages

setup(
    name="paddle-webhook-signature-verifier",
    version="1.0.0",
    py_modules=["paddle_webhook_signature_verifier"],
    install_requires=[],
    author="Aneesh Arora",
    author_email="aneesh.arora.aa@gmail.com",
    description="A Python package for verifying Paddle webhook signature",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/afterword-tech/paddle_webhook_signature_verifier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
