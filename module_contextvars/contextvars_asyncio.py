import asyncio
import contextvars


client_addr_var = contextvars.ContextVar("client_addr")


def render_goodbye():
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.
    client_addr = client_addr_var.get()
    return f"Good bye, client @ {client_addr}\n".encode()


async def handle_request(reader, writer):
    """
    It will be automatically converted into a
    Task.
    """
    addr = writer.transport.get_extra_info("socket").getpeername()
    client_addr_var.set(addr)

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break
        writer.write(line)

    writer.write(render_goodbye())
    writer.close()


async def main():
    srv = await asyncio.start_server(handle_request, "127.0.0.1", 8081)

    async with srv:
        await srv.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
