# main.py

import asyncio

from bot import EchoBot
from adapter import ConsoleAdapter  # how is this finding the adapter "from"

# instanciate the objects
BOT = EchoBot()
ADAPTER = ConsoleAdapter()

# create a looper
LOOP = asyncio.get_event_loop()


if __name__ == "__main__":
    try:
        # Greetings
        print("Hi I'm EchoBot, I can repeat what you say to me! Try ME :)")

        # Run the loop - unleesh the lava
        LOOP.run_until_complete(ADAPTER.proccess_activity(BOT.on_turn()))
    except KeyboardInterrupt:
        pass
    finally:
        LOOP.stop()
        LOOP.close()
