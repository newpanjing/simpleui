from setuptools import setup

long_description = "\n".join([
    open('README.md', 'r').read(),
])

setup(
    name='django-simpleui',
    version='1.3.6',
    packages=['simpleui'],
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/newpanjing/simpleui',
    license='Apache License 2.0',
    author='panjing',
    long_description=long_description,
    author_email='newpanjing@icloud.com',
    description='django admin 后台模板',
    install_requires=['django', 'jieba'],
)
