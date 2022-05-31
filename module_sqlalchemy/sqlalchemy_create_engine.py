from sqlalchemy import create_engine


# With `echo` enabled, we’ll see all the generated SQL produced
# The sole purpose of the Engine object from a user-facing perspective is to provide a unit of connectivity to the
# database called Connection. When working with the Core directly, the Connection object is how all interaction with
# the database is done. As the context, and the best way to do that is using Python context manager form, also known as
# the with statement.
engine = create_engine("sqlite:///memory:", echo=True)
print(engine)
