from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="yt-chap",
    version="0.1.0",
    author="Mallik Mohammad Musaddiq",
    author_email="mallikmusaddiq1@gmail.com",
    description="CLI tool to view YouTube video chapters in human-readable format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mallikmusaddiq1/yt-chap",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "yt-dlp",  # ✅ Automatically fetches latest compatible yt-dlp
    ],
    entry_points={
        "console_scripts": [
            "yt-chap = yt_chap.cli:main",
        ]
    },
    include_package_data=True,
    license="MIT",
)