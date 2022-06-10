from setuptools import setup

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(
    name="youtube-etl",
    version="0.1.0",
    description="Youtube 기반 ML 데이터셋 다운로드용 youtubetl 코드",
    url="https://github.com/omnipede/youtube-etl",
    author="omnipede",
    author_email="omnipede@naver.com",
    packages=['youtubetl'],
    zip_safe=False,
    install_requires=required
)
