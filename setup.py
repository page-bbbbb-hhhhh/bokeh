# needs to be tested
import sys
if len(sys.argv)>1 and sys.argv[1] == 'develop':
    # Only import setuptools if we have to
    import setuptools
else:
    import subprocess
    import shutil
    from os.path import join, exists
    import os
    import requests
    def add_js(fname):
        url = "http://s3.amazonaws.com/bokeh-builds/%s" % fname
        print "downloading %s from %s" % (fname, url)
        data = requests.get(url).content
        with open(join("bokeh/server/static/js/", fname), "w+") as f:
            f.write(data)
    add_js("application.js")
    add_js("bokehnotebook.js")
    print "downloading completed"
    
from distutils.core import setup
import os
import sys
__version__ = (0, 0, 1)
package_data_dirs = []
for dirname, _, files in os.walk('bokeh/server/static', followlinks=True):
    dirname = os.path.relpath(dirname, 'bokeh')
    for f in files:
        package_data_dirs.append(os.path.join(dirname, f))
        
for dirname, _, files in os.walk('bokeh/server/templates', followlinks=True):
    dirname = os.path.relpath(dirname, 'bokeh')
    for f in files:
        package_data_dirs.append(os.path.join(dirname, f))

for dirname, _, files in os.walk('bokeh/templates', followlinks=True):
    dirname = os.path.relpath(dirname, 'bokeh')
    for f in files:
        package_data_dirs.append(os.path.join(dirname, f))

setup(
    name = 'bokeh',
    version = '.'.join([str(x) for x in __version__]),
    packages = ['bokeh', 'bokeh.chaco_gg', 'bokeh.server',
                'bokeh.server.models', 'bokeh.server.views',
                'bokeh.server.test', 'bokeh.specialmodels'],
    package_data = {'bokeh' : package_data_dirs},
    author = 'Continuum Analytics',
    author_email = 'info@continuum.io',
    url = 'http://github.com/ContinuumIO/Bokeh',
    description = 'Statistical and novel interactive HTML plots for Python',
    zip_safe=False,
    license = 'New BSD',
)
