Conference plugin for wazo-admin-ui

Install
-------

    wazo/rules build
    wazo/rules install

Uninstall
---------

You need to have python-pip installed.

    wazo/rules uninstall


Translations
------------

To extract new translations:

    % python setup.py extract_messages

To create new translation catalog:

    % python setup.py init_catalog -l <locale>

To update existing translations catalog:

    % python setup.py update_catalog

Edit file `conference/translations/<locale>/LC_MESSAGES/messages.po` and compile
using:

    % python setup.py compile_catalog
