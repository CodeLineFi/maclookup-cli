MAC address vendor lookup
=========================

A command-line utility to lookup info related to a MAC address or OUI,
such as vendor name and address, based on the MAC Address API.


Installation
------------

.. code-block:: console

    $ pip install maclookup-cli


User Install
------------

You can also perform a user installation via

.. code-block:: console

    $ pip install maclookup-cli --user


For user installs on macOS make sure ``~/Library/Python/<ver>/bin`` is in your
``$PATH``, i.e. edit the ``PATH=`` line in ``~/.bashrc`` or
``~/.bash_profile``, e.g. ``PATH=$PATH:~/Library/Python/<ver>/bin``

Apply the changes with

.. code-block:: console

    $ source ~/.bashrc or $ source ~/.bash_profile


In Windows make sure ``%AppData%\Python\Python<version>\Scripts`` is in your
``PATH``.



API key
-------

The tool requires an API account, signup `here <https://macaddress.io/signup>`_.

The key can either be provided via the ``-k`` / ``--api-key`` command option
or the environment variable

.. code-block:: console

    # macOS and Linux
    $ export MAC_ADDRESS_IO_API_KEY="your-api-key"


.. code-block:: console

    # Windows (CMD)
    set MAC_ADDRESS_IO_API_KEY="your-api-key"


.. code-block:: console

    # Windows (PowerShell)
    $env:MAC_ADDRESS_IO_API_KEY="your-api-key"


Usage
-----

.. code-block:: console

    $ maclookup --help


Documentation
-------------

The latest documentation is available on `GitHub <https://github.com/CodeLineFi/maclookup-cli>`_.