aioga
=====

:info: Google Analytics client for asyncio

.. image:: https://img.shields.io/travis/aio-libs/aioga.svg
    :target: https://travis-ci.org/aio-libs/aioga

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

All methods require cid (Client ID). The value of this field
should be a random UUID (version 4) as described in
`<http://www.ietf.org/rfc/rfc4122.txt>`_


Library support all available parametes for measurement protocol
(documentation `here <https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters>`_)
