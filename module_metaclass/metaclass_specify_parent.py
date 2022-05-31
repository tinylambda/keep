class DataCamp:
    pass


PythonClass = type(
    "PythonClass",
    (DataCamp,),
    {
        "start_date": "August 2018",
        "instructor": "John Doe",
    },
)

print(PythonClass)
print(issubclass(PythonClass, DataCamp))
