import os
import setuptools

base_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(base_dir, 'README.md'), 'r', encoding='utf-8') as fh:
    long_description = fh.read()
with open(os.path.join(base_dir, 'version.txt'), 'r', encoding='utf-8') as fid:
    version_number = fid.read()

setuptools.setup(
    name='visionnpb',
    # composed of version of source REST API and version of this lib always starting from 1001
    # i.e. 5.11.1.1001
    version=version_number,
    author='ExpertaLabs',
    author_email='author@expertalabs.com',
    description='Vision Network Packet Broker Python library (PyPI package)',
    keywords='ixia, vision, nbp, networkpacketbroker, packetbroker, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ExpertaLabs/VisionNPB",
    package_dir={'': 'RestApi'},
    packages=setuptools.find_packages(where='RestApi'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0, <4',
    install_requires=['urllib3>=1.26.10, <2'],
    setup_requires=['pytest-runner>=6.0.0, <7'],
    tests_require=['pytest>=4.4.1, <5'],
    extras_require={
        'dev': ['check-manifest>=0.48, <1'],
        'test': ['coverage>=6.4.1, <7', 'pytest>=4.4.1, <5'],
    }
)