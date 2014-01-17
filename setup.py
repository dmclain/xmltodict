from distutils.core import setup
import sys

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version('0.1', __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()

setup(name='xmltodict',
      author='Martin Blech',
      version=version,
      py_modules=['xmltodict'],
      )
