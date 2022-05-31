from pprint import pprint

from papa import Papa

if __name__ == "__main__":
    with Papa() as p:
        pprint("Before set: ")
        pprint(p.list_values())

        p.set("circus.uwsgi", "ABC")

        pprint("After set: ")
        pprint(p.list_values())

        p.set("circus.uwsgi", "ABCD")
        pprint("Override: ")
        pprint(p.list_values())

        pprint("Get value of a key: ")
        pprint(p.get("circus.uwsgi"))

        p.set("circus.uwsgi", None)
        pprint("Clear: ")
        pprint(p.list_values())

        # You cannot remove all variables so passing no names or passing * will raise a papa.Error exception.
        # p.remove_values()

        p.set("circus.uwsgi", "A")
        p.set("circus.uwsgi2", "B")
        p.set("circus.uwsgi3", "C")

        pprint("We can remove values by name")
        p.remove_values("circus.uwsgi")

        pprint("Or remove by multiple names")
        p.remove_values("circus.uwsgi2", "circus.uwsgi3")

        pprint(p.list_values())
