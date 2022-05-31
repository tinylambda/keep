import uuid

for node in [0x1EC200D9E0, 0x1E5274040E]:
    print(uuid.uuid1(node), hex(node))
