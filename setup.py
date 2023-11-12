from setuptools import setup

setup(
    name='sr_cad_walls',
    version='0.1',
    packages=['sr_cad_walls'],
    url='https://github.com/ayychap/CAD-Wall-Art-Converter',
    license='mit',
    author='Marinus, Manifolds',
    author_email='',
    description='Conversion tool for Synth Riders wall art generated in .dxf CAD files',
    package_dir={'': 'src'},
    python_requires='>=3.10',
    install_requires=['ezdxf', 'numpy', 'synth-mapping-helper']
)
