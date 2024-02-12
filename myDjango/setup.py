from setuptools import setup, find_packages

setup(
    name="myDjango",  # 패키지 이름
    version="0.1",  # 패키지 버전
    packages=find_packages(),  # 패키지에 포함될 디렉토리 (자동으로 찾아줌)
    include_package_data=True,  # 패키지 데이터 포함 여부
    zip_safe=False,  # wheel을 압축 해제 없이 직접 실행 가능하게 할 것인지 여부
    install_requires=[
        "Django>=3.0",
    ],
)


# python setup.py sdist bdist_wheel