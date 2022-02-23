.. contents:: Contents
    :local:

Installation guide
*****************************************

- Install `Python <https://www.python.org/>`_
- Install `PyCharm <https://www.jetbrains.com/pycharm/>`_ community edition
- Open PyCharm
    - Create a new project ``Get from VCS`` and copy paste `this github repository URI <https://github.com/nergalex/f5-bot-selenium.git>`_
    - Attach a `Python interpreter <https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html>`_
- Download `here <https://sites.google.com/chromium.org/driver/>`_ same Chrome driver as your Chrome browser ``chrome://settings/help``
- OPTION: for other browser, follow `this guide <https://selenium-python.readthedocs.io/installation.html#installation>`_
- Copy downloaded ``chromedriver(.exe)`` file in ``./_files/chromedriver.exe`` of your project
- For MacOS only, allow ``chromedriver`` as described `here <https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de>`_:

.. code-block:: bash

    xattr -d com.apple.quarantine chromedriver

- Open file ``requirements.txt``
- Click on  ``Install requirements``

.. image:: ./_pictures/Install_requirements.png
   :align: center
   :width: 300
   :alt: setUp

- Choose **ONLY** those packages ton install: ``selenium``, ``requests``

.. image:: ./_pictures/no_install_2captcha.png
   :align: center
   :width: 300
   :alt: setUp

Run
*****************************************

- In PyCharm, open ``play1.py``

- Set global variables
    - Note: CAPTCHA_API_KEY is 2CAPTCHA API key and **NOT** the the Google recaptcha site-key

.. code-block:: bash

        URI = "https://{{your_hackazon_uri}}"
        LOGIN_USER = "test_user"
        LOGIN_PASSWORD = "123456"
        LOGIN_BIRTHDAY = "12/12/1981"
        LOOP_ITERATION = 2

- For Mac user, set local variable

.. code-block:: bash

        PATH = "./_files/chromedriver"

- Go to the end of the file and click on the green triangle

.. image:: ./_pictures/run_test.png
   :align: center
   :width: 300
   :alt: setUp

