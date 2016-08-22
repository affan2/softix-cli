from setuptools import setup

requirements = ['click']
setup(
    name='softixcli',
    description='Python CLI for Softix',
    author='matt@itsmemattchung.com',
    version='0.0.1',
    install_requires=requirements,
    entry_points={
        'console_scripts': ['softix=softixcli.cli:cli']
    }
)



