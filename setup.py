from setuptools import setup

requirements = ['click', 'softix']
dependencies = ['git+ssh://git@github.com/wastatickets/softix.git#egg=softix']
setup(
    name='softixcli',
    description='Python CLI for Softix',
    author='matt@itsmemattchung.com',
    version='0.0.4',
    install_requires=requirements,
    dependency_links = dependencies,
    entry_points={
        'console_scripts': ['softix=softixcli.cli:cli']
    }
)



