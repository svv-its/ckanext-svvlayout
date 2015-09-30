# ckanext-svvlayout

Installation
------------

ckanext-svvlayout has been tested against CKAN 2.4.1.

To install, activate your CKAN virtualenv and then do:

    git clone 'https://github.co/svv-its/ckanext-svvlayout.git'
    cd ckanext-svvlayout
    pip install -e . (or alternatively equivalent) python setup.py develop

Then add 'svvlayout' to the ckan.plugins line in your CKAN config file, for
example:

    ckan.plugins = resource_proxy stats datastore simplesso svvlayout


Lastly, restart your web server.

