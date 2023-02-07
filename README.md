[![Tests](https://github.com/blagojabozinovski/ckanext-questionnaire/workflows/Tests/badge.svg?branch=main)](https://github.com/blagojabozinovski/ckanext-questionnaire/actions)

# ckanext-noresource

With this ckan extension you can choose to add a dataset with or without a resoruce, it provides us with 3 settings that can be set by a sysadmin  with pressing the added button on the admin header.

![image](https://user-images.githubusercontent.com/30418161/216944233-635ba421-bd11-428d-9394-d2a0eac3d420.png)

The settings are:
1. create dataset normaly(with resource), 
2. create dataset without resource. 
3. let the user choose at dataset creation.

![ddmenu](https://user-images.githubusercontent.com/30418161/217267695-fd912f38-3495-450b-805e-5241e86b900b.png)

If we set it to the **first option** and save nothing happens we can use ckan as defaulty intended.

If we set it to the **second option** and save, when we go to the dateset creation form the Add Dataset button should/will change to Add Dataset metadata button which will allow us to create a dataset without a resource:

![image](https://user-images.githubusercontent.com/30418161/217284218-bbacefa2-e481-425c-bc7a-64d2f1339249.png)

Lastly if we set it to the **third option** and save, when we go to the dataset creation form, press Add Dataset button a prompt should show asking us to choose if we want to create a normal dataset or one without a resource:

![image](https://user-images.githubusercontent.com/30418161/217285348-1d1b96db-5b19-479d-ba18-de4eaca5d6ef.png)

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

    ~~~
    git clone git@github.com:keitaroinc/ckanext-noresource.git
    cd ckanext-noresource
    pip install -e .
    pip install -r requirements.txt
    ~~~

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
