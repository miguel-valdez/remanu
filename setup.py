import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='remanu-miguelvg87',
    version='0.1',
    author='Miguel A. Valdez G.',
    author_email='mavaldez@imp.mx',
    description='fenics-based fem solver for nuclear magnetic resonance PDEs',
    long_description=long_description,
    long_description_content_type='text',
    url='https://github.com/miguel-valdez/remanu',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: LGPL License',
        'Operating System :: OS Independent',
        ],
    python_requires= '>=3.6',
)
