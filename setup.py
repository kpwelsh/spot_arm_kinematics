from distutils.core import setup, Extension

import numpy as np
from findblas.distutils import build_ext_with_blas

def main():
    setup(
        name='spot_arm_kinematics',
        version='0.0.1',
        description='ikfast wrapper',
        author='Kevin Welsh',
        author_email='kwelsh@lanl.gov',
        cmdclass = {'build_ext': build_ext_with_blas},
        ext_modules=[Extension('spot_arm_kinematics', ['ikfast_robot.cpp', 'pyikfast.cpp'], include_dirs=[np.get_include()])],
        setup_requires=['wheel'],
        install_requires=[
            'numpy',
            'findblas'
        ],
    )


if __name__ == '__main__':
    main()
