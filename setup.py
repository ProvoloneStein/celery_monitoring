import os

# try:  # pip >= 10
#     from pip._internal.network.session import PipSession
# except ImportError:  # pip <= 9.0.3
#     from pip.download import PipSession
# from pip._internal.req.req_file import parse_requirements
from setuptools import find_packages, setup

try:
    from pip._internal.network.session import PipSession
except ImportError:
    from pip._internal.download import PipSession
from pip._internal.req.req_file import parse_requirements


def read_requirements(file_name):
    return [
        str(requirement.requirement) for requirement in
        parse_requirements(file_name, session=PipSession())
    ]


setup(
    name='celery-prometheus-exporter',
    version=os.getenv('SERVICE_VERSION', '1.0.0'),
    description='Prometheus exporter for celery metrics',
    author='Georgy Gritsenko',
    author_email='georgiy.gritsenko@techops.ru',
    packages=find_packages(exclude=('*.tests', 'tests.*')),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'celery-exporter=celery_prometheus_exporter.main:main'
        ]
    },
    install_requires=read_requirements('requirements/requirements.txt'),
    extras_require={
        'develop': read_requirements('requirements/requirements-develop.txt'),
    }
)
