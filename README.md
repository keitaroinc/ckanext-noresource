[![Tests](https://github.com/blagojabozinovski/ckanext-questionnaire/workflows/Tests/badge.svg?branch=main)](https://github.com/blagojabozinovski/ckanext-questionnaire/actions)

# ckanext-noresource

With this ckan extension you can choose to add a dataset with or without a resoruce, it provides us with 3 settings that can be set by a sysadmin  with pressing the added button on the admin header.

![image](https://user-images.githubusercontent.com/30418161/216944233-635ba421-bd11-428d-9394-d2a0eac3d420.png)

The settings are:

1. create dataset normaly(with resource), 
2. create dataset without resource. 
3. let the user choose at dataset creation.

![image](https://user-images.githubusercontent.com/30418161/216944544-3fce99db-2152-4ca3-967c-44c885a8d47b.png)


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | yes  |


## Installation

To install ckanext-noresource:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    ``` 
        git clone https://github.com/miloshira/ckanext-noresource.git
        cd ckanext-noresource
        pip install -e .
        pip install -r requirements.txt ```

3. Add `noresource` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Developer installation

To install ckanext-noresource for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/miloshira/ckanext-noresource.git
    cd ckanext-noresource
    python setup.py develop
    pip install -r dev-requirements.txt


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
