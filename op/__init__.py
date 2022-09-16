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

>>> o = op.Object()
>>> o.save()

but::

>>> from op import Object, save
>>> o = Object()
>>> save(o)

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

'op.obj.Object/2021-08-31/15:31:05.717063'

>>> import op
>>> o = op.Object()
>>> op.save(o)  # doctest: +ELLIPSIS
'op.obj.Object/...'

Great for giving objects peristence by having their state stored in files.

"""


from op.cls import Class
from op.dbs import Db, find, fns, fntime, hook, last
from op.dft import Default
from op.jsn import dump, dumps, load, loads, save
from op.obj import *
from op.utl import cdir, elapsed
from op.wdr import Wd


def __dir__():
    return (
            'Class',
            'Db',
            'Default',
            'Object',
            'Wd',
            'delete',
            'dump',
            'dumps',
            'edit',
            'find',
            'format',
            'get',
            'items',
            'keys',
            'last',
            'load',
            'loads',
            'name',
            'otype',
            'register',
            'save',
            'update',
            'values',
            'cls',
            'dbs',
            'dft',
            'jsn',
            'obj',
            'sel',
            'utl',
            'wdr'
           )
