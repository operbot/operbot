.. _home:


.. raw:: html

  <br>


.. title:: write your own commands


.. raw:: html

    <center>
    <b>

**M A N P A G E**

.. raw:: html

    </b>
    </center>


**NAME**


 ``operbot`` - write your own commands


**SYNOPSIS**


  | ``operbot [cmd] [-c] [-i] [key=value] [key==value]``


**INSTALL**


 ``pip3 install operbot --upgrade --force-reinstall``


**DESCRIPTION**


 ``operbot`` is a solid, non hackable, back after reboot, intended to be
 programmable in a static, only code, no popen, no imports and no reading
 modules from a directory bot, it's  source is :ref:`here <source>`.

 ``operbot`` is programmable, to program the bot you have to have the code
 available as employing your own code requires that you install your own bot as
 the system bot. This is to not have a directory to read modules from to add
 commands to the bot but include the own programmed modules directly into the
 python code, so only trusted code (your own written code) is included and
 runnable. Reading random code from a directory is what gets avoided.

 ``operbot`` stores it's data on disk where objects are time versioned and the
 last version saved on disk is served to the user layer. Files are JSON dumps
 that are read-only so thus should provide (disk) persistence more chance.
 Paths carry the type in the path name what makes reconstruction from filename
 easier then reading type from the object.

 **only include your own written code should be the path to "secure".**


**CONFIGURATION**

 configuration is done by calling the ``cfg`` command of the bot.

 **irc**

 | ``operbot cfg server=<server> channel=<channel> nick=<nick>``

 | (*) default channel/server is #operbot on localhost

 **sasl**

 | ``operbot pwd <nickservnick> <nickservpass>``
 | ``operbot cfg password=<outputfrompwd>``

 **users**

 | ``operbot cfg users=True``
 | ``operbot met <userhost>``


 **rss**

 | ``operbot rss <url>``
 |


**COMMANDS**

 here is a short description of the commands.

 | ``cmd`` - shows all commands
 | ``cfg`` - shows the irc configuration, also edits the config
 | ``dlt`` - removes a user from bot
 | ``dpl`` - sets display items for a rss feed
 | ``ftc`` - runs a rss feed fetching batch
 | ``fnd`` - allows you to display objects on the datastore, read-only json files on disk 
 | ``flt`` - shows a list of bot registered to the bus
 | ``log`` - logs some text
 | ``met`` - adds a users with there irc userhost
 | ``mre`` - displays cached output, channel wise.
 | ``nck`` - changes nick on irc
 | ``pwd`` - combines a nickserv name/password into a sasl password
 | ``rem`` - removes a rss feed by matching is to its url
 | ``rss`` - adds a feed to fetch, fetcher runs every 5 minutes
 | ``thr`` - show the running threads
 | ``tdo`` - adds a todo item, no options returns list of todo's
 |

**AUTHOR**

 Bart Thate

**COPYRIGHT**

 **OPERBOT** is placed in the Public Domain. No Copyright, No License.


.. toctree::
    :hidden:
    :glob:

    *
