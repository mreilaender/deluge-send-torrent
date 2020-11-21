from setuptools import setup, find_packages

setup(
    name='send-to-deluge',
    version='1.0',
    scripts=['./scripts/send-to-deluge'],
    author='Manuel Reilaender',
    description='Sends torrent files to deluge only if certain criteria are met',
    package_dir={'', 'lib'},
    packages=find_packages('lib'),
    install_requires=[
        'setuptools',
        'bencodepy == 0.9.5'
    ],
    python_requires='>=3.8'
)