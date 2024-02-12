from setuptools import setup, find_packages

# requirements.txt에서 의존성 목록을 읽기
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="myDjango",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=required,
)



# python setup.py sdist bdist_wheel