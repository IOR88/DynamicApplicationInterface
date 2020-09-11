from os import path
import setuptools


def _get_version():
    filename = path.join('src', 'exampleproject', '__init__.py')
    glb = {}
    with open(filename) as fp:
        for line in fp:
            if '__version__' in line:
                exec(line, glb)
                return glb['__version__']
    raise RuntimeError('cannot find version')


setuptools.setup(
    name='DynamicApplicationInterface',
    version='{version}'.format(version=_get_version()),
    description='Use case of Django REST Framework and OpenAPI to create dynamic user interface',
    long_description=open('README.md').read(),
    author='Igor Miazek',
    url='https://github.com/IOR88/DynamicApplicationInterface',
    download_url='https://github.com/IOR88/DynamicApplicationInterface',
    license='MIT',
    namespace_packages=[],
    package_dir={'': 'src'},
    packages=[
        'exampleproject',
        'exampleproject.exampleapp',
        'exampleproject.exampleapp.migrations'

    ],


    include_package_data=True,
    install_requires=[
        'Django==3.1.1',
        'djangorestframework==3.11.1',
        'django-filter==2.3.0',
        'PyYAML==5.3.1'
    ],
    entry_points='''
        [console_scripts]
        exampleproject-manage = exampleproject.manage:main
    '''
)
