Installation
============

.. code-block:: shell

    pip install aioga

Usage
=====

.. code-block:: python

    import asyncio
    import uuid

    from aioga import Api

    TRACKING_ID = 'XX-XXXXXXXX-X'


    async def go():
        ga = None

        try:
            ga = Api(TRACKING_ID)

            cid = uuid.uuid4()

            # You can call method and "forget" about it.
            ga.event(cid, ec='tests', ea='success without await')

            # Or you can wait, while request will be complete, if need
            await ga.event(cid, ec='tests', ea='success with await')
        finally:
            if ga is not None:
                await ga.close()

        # or you can use context manager
        async with Api(TRACKING_ID) as ga:
            await ga.event(cid, ec='tests', ea='success from context manager')


    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
    loop.close()

Documentation
=============

This library is asynchronous wrapper for measurement protocol.
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
