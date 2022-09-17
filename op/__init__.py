# This file is placed in the Public Domain.
# pylint: disable=W0622


"""Object programming (op) is a package that allows inherited objects
to be loaded/saved from/to disk, storing data in a JSON dict. Basic building
block is an big Object class that can be inherired from to allow for loading
and saving of an object. Big Object class provides a clean, no methods,
namespace for json data to be read into. This is necessary so that methods
don't get overwritten by __dict__ updating and, without methods defined on the
object, is easily being updated from a on disk stored json (dict). Functions
are provided using function call/first argument an Object e.g not::

 import op
 o = op.Object()
 o.save()

but::

>>> from op import Object, save
>>> o = Object()
>>> path = save(o)

Some hidden methods are provided, methods are factored out into functions
like get, items, keys, register, set, update and values.

basic usage is this::

>>> import op
>>> o = op.Object()
>>> o.key = "value"
>>> o.key
'value'

load/save from/to disk::

>>> import op
>>> o = op.Object()
>>> o.key = "value"
>>> p = op.save(o)
>>> oo = op.Object()
>>> op.load(oo, p)
>>> oo.key
'value'

Big Objects can be searched with database functions and uses read-only files
to improve persistence and a type in filename for reconstruction::

>>> import op
>>> o = op.Object()
>>> op.save(o)  # doctest: +ELLIPSIS
'op.obj.Object/...'

Great for giving objects peristence by having their state stored in files.

"""
