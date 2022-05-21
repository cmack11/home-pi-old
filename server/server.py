import asyncio
import websockets
import os
import signal

async def echo(websocket):
    print(websocket)
    async for message in websocket:
        await websocket.send(message)

async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    port = int(os.environ.get("PORT", "8001"))
    async with websockets.serve(handler, "", port):
        await stop run forever

asyncio.run(main())