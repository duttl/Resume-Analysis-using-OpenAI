from setuptools import setup, find_packages

setup(
    name="ats_app",
    version="0.1",
    packages=find_packages(),
    install_requires = [
        "streamlit",
        "openai",
        "PyMuPDF",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "ats-app=ats.app:main"
        ]
    },
)