from setuptools import setup


setup(
    name='formful_bootstrap',
    install_requires=[
        'formful',
    ],
    extras_require={
        'test': [
            'pytest>=3',
            'PyHamcrest'
        ]
    }
)
