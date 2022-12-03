.. _programmer:

.. raw:: html

    <br>

.. title:: programmer


.. raw:: html

    <center>
    <b>
    P R O G R A M M E R
    </b>
    </center>
    <br>

The ``opr`` package provides an Object class, that saves/loads to/from json
files on disk. Objects can be searched with database functions. Type in
filename is used for reconstruction and ethods are factored out into functions
to have a clean namespace to read JSON data into.

basic usage is this::

>>> from opr import Object
>>> o = Object()
>>> o.key = "value"
>>> o.key
>>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

load/save from/to disk::

>>> from opr import Object
>>> from opr import load, save
>>> o = Object()
>>> o.key = "value"
>>> p = save(o)
>>> oo = Object()
>>> load(oo, p)
>>> oo.key
>>> 'value'

great for giving objects peristence by having their state stored in files.

>>> from opr import Object, save
>>> from opr import Wd
>>> Wd.workdir = ".test"
>>> o = Object()
>>> save(o)
>>> 'opr.object.Object/2021-08-31/15:31:05.717063'
