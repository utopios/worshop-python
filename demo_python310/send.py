import asyncio

async def send(data:str):
    reader, writer = await asyncio.open_connection('localhost', 8082)
    writer.write(data.encode())
    await writer.drain()

    data = await reader.read(1024)
    print("Server response:", data.decode())
    writer.close()

asyncio.run(send("test"))
