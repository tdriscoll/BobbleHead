from distutils.core import setup
import py2exe  
import os, glob
from collections import defaultdict

def find_data_files(source,target,patterns):
    """ Locates the specified data-files and returns the matches in a data_files compatible format.
        source is the root of the source data tree.
        target is the root of the target data tree.
        patterns is a sequence of glob-patterns for the files you want to copy.
    """
  
    result =defaultdict(list)
    for pattern in patterns:
        pattern = os.path.join(source,pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target,os.path.relpath(filename,source))
                path = os.path.dirname(targetpath)
                result[path].append(filename)
    return sorted(result.items())

data_files = find_data_files(r'src\images','images',['*'])
data_files.extend(find_data_files(r'src\sounds','sounds',['*']))
#needed to play sounds
data_files.append(('phonon_backend', [r'C:\Python27\Lib\site-packages\PyQt4\plugins\phonon_backend\phonon_ds94.dll' ]))

setup(name="BobbleHead",  
      version="0.2",  
      author="Tim Driscoll",  
      license="GNU General Public License (GPL)",  
      packages=[r'src'],  
      scripts=[r'src/main.py'],
      data_files = data_files, 
      windows=[{"script": "src/main.py"}],  
      options={"py2exe": { "includes": ["sip"]}})