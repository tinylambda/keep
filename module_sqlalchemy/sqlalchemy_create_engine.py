from sqlalchemy import create_engine


# With `echo` enabled, we’ll see all the generated SQL produced
engine = create_engine('sqlite:///memory:', echo=True)
print(engine)

