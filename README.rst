aioga
=====

:info: Google Analytics client for asyncio

.. image:: https://travis-ci.com/aio-libs/aioga.svg?branch=master
   :target: https://travis-ci.com/aio-libs/aioga
   :alt: Travis status for master branch

.. image:: https://img.shields.io/pypi/v/aioga.svg
    :target: https://pypi.python.org/pypi/aioga

Installation
============

.. code-block:: shell

    pip install aioga

Usage
=====

.. code-block:: python

    import asyncio
    import uuid

    from aioga import GA

    TRACKING_ID = 'XX-XXXXXXXX-X'


    async def go():
        cid = uuid.uuid4()

        async with GA(TRACKING_ID) as ga:
            ga.event(str(cid), ec='tests', ea='success from context manager')
            # all methods returns asynio.Tasks, which can be awaited if needed


    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
    loop.close()


Documentation
=============

The library is asynchronous client for measurement protocol.
All available hit types are supported.

`Full documentation <https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide>`_ of measurement protocol provides by google


Available methods
-----------------

* pageview
* screenview
* event
* transaction
* item
* social
* exception
* timing

Available parameters
--------------------

All methods accept cid (Client ID). This field is mandatory,
unless uid (User ID) is provided. The value of the cid field
should be a random UUID (version 4) as described in
`<http://www.ietf.org/rfc/rfc4122.txt>`_


Library support all available parametes for measurement protocol
(documentation `here <https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters>`_)
