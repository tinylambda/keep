"""
Determining how a modern computer should handle tens of thousands of connections is known as the C10K problem.
The C10K resolution strategies explain how using an event loop to listen to hundreds of event resources is going
to scale much better than, say, as one-thread-per-connection approach. This doesn't mean that the two techniques
are not compatible, but it does mean that you can usually replace the multi-threads approach with a event-driven
mechanism.
"""
