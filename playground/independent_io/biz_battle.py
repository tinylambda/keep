def battle():
    battle_id = yield
    print("battle_id is ", battle_id)

    io_event = {
        "io_type": "redis",
        "io_action": "set",
        "kwargs": {"key": f"battle_{battle_id}", "value": "battle started"},
    }
    io_return = yield io_event
    print("io return: ", io_return)

    for i in range(5):
        io_event = {"io_type": "redis", "kwargs": {"key": battle_id, "value": i}}
        print("send io_event: ", io_event)
        io_return = yield io_event
        print("io return: ", io_return)
        if io_return != "ok":
            print("IO error! break!")
            break
