# main.py

import asyncio  # async library

from bot import EchoBot  # import EchoBot Object from bot
from adapter import ConsoleAdapter  # how is this finding the adapter "from"

# instanciate the objects
BOT = EchoBot()  # BOT object calling EchoBot constructor
# ADAPTER object = the return val of ConsoleAdapter constructor
ADAPTER = ConsoleAdapter()

# create an event loop
LOOP = asyncio.get_event_loop()


if __name__ == "__main__":
    try:  # try this except...
        # Greetings
        print("Hi I'm EchoBot, I can repeat what you say to me! Try ME :)")

        # Run the loop - unleesh the lava
        LOOP.run_until_complete(ADAPTER.proccess_activity(BOT.on_turn()))
    except KeyboardInterrupt:  # if a keyboard interrupt happens
        pass
    finally:  # to finish off the try loop...run these to do a closedown
        LOOP.stop()  # stop event loop
        LOOP.close()  # close the loop
