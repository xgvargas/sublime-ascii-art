***************************
Sublime ASCII-Art Generator
***************************

**Sublime 2 Plugin** to convert a line os text to its Ascii Art form.

.. sourcecode:: python

	class TestClass

	class TestClass(object):
		pass

Put cursor on first line, then ``Ctrl-Shift-P`` search for ASCII-Art and hit ``Enter``. You shoud have:

.. sourcecode:: python

	#       _                 _______        _    _____ _
	#      | |               |__   __|      | |  / ____| |
	#   ___| | __ _ ___ ___     | | ___  ___| |_| |    | | __ _ ___ ___
	#  / __| |/ _` / __/ __|    | |/ _ \/ __| __| |    | |/ _` / __/ __|
	# | (__| | (_| \__ \__ \    | |  __/\__ \ |_| |____| | (_| \__ \__ \
	#  \___|_|\__,_|___/___/    |_|\___||___/\__|\_____|_|\__,_|___/___/

	class TestClass(object):
		pass

Kind of usefull to separate blocks in a big file.... I guess....


This plugin uses PyFiglet
-------------------------

This plugin makes use of `pyfiglet <https://pypi.python.org/pypi/pyfiglet>`_ library with minor changes to render the big text!

