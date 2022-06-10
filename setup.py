from setuptools import setup

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(
    name="youtube-etl",
    version="0.1.0",
    description="Youtube 기반 ML 데이터셋 다운로드용 pipeline 코드",
    url="https://github.com/omnipede/youtube-caption-subclip-pipeline",
    author="omnipede",
    author_email="omnipede@naver.com",
    packages=['ytl'],
    zip_safe=False,
    install_requires=required
)
