import datetime
import asyncio
import warnings
from typing import List, Callable

from botbuilder.schema import (
    Activity,  # the activity of a bot
    ActivityTypes,  # types of activites bot can handle, such as text, audio, image
    ChannelAccount,  # the ...
    ConversationAccount,  # conversation ID?
    ResourceResponse,  # hold context?
    ConversationReference,
)
from botbuilder.core import (
    TurnContext
)

from botbuilder.core.bot_adapter import (BotAdapter)


class ConsoleAdapter(BotAdapter):
    """
    Adapter to communicate with bot via console window

    - Example - 
    import asyncio
    from botbuilder.core import ConsoleAdapter

    async def logic(context):
        await context.send_activity("hello world!)

    # the adapter we are using is for the console, this could be a browser type or adatper to something like Telegram / Facebook Messenger
    adapter = ConsoleAdapter() # instanciate the adapter and save to var

    loop = asyncio.get_event_loop()
    if __name__ == "__main__":
        try:
            loop.run_until_complete(adapter.process_activity(logic))
        except KeyboardInterupt:
            pass
        finally:
            loop.stop()
            loop.close()
    """

    def __init__(self, reference: ConversationReference = None):
        super(ConsoleAdapter, self).__init__()  # TODO ; learn what this means

        self.reference = ConversationReference(
            # the id of conversation channel taking place
            channel_id="console",

            # the account that is either user or bot that sits within a channel
            user=ChannelAccount(id="user", name="User1_Troy"),

            # save as above but this is the bot channel itself,
            # imagine the ability to have a channel with multi bot.
            bot=ChannelAccount(id="bot", name="MarkBot"),

            # TODO: side project """
            #     one user that enters a channel with two bots in the room
            #     what would this do?
            #     Could the bot then just be able to both talk to other bot
            #  say one is finance and one is healthcare
            #     the different bots would then handle various questions,
            #     this would segment the difference and handling of data
            # permissions

            #     """the user would not know the difference if the bots know
            #  (through orchestration how to handle when an incoming activity
            # triggers both bots. maybe ask a clarifying question to determine
            # which bot should be used. -> this leads to bot hand-off. when a
            # healthcare bot then needs to transfer to finance bot. what data
            # log and conversation information would be preseved between the
            #  two? how do we ensure a user experience that the user
            # understands and trusts the bot? So multi-bot with one name,
            # with different skills.)
            # """

            conversation=ConversationAccount(
                id="convo1", name="", is_group=False),
            service_url="",

        )

        # warn that users need to pass in a conversation reference instance,
        # otherwise DEBUG: "parameter ignored"
        # checking if isinstance of reference a ConversationReference
        if reference is not isinstance(reference, ConversationReference):
            # .then() the conditional is done to check if x is not y...
            # .then()
            warnings.warn(
                "ConsoleAdapter: 'reference' argument is not an instance of"
                "ConversationReference and will be ignored."
            )
        else:  # if it is the proper instance "reference"
            self.reference.channel_id = getattr(
                reference,
                "conversation",
            )
            self.reference.user = getattr(
                reference,
                "user"

            )
            self.reference.bot = getattr(
                reference,
                "bot"
            )
            self.reference.conversation = getattr(
                reference,
                "conversation"

            )
            self.reference.service_url = getattr(
                reference,
                "service_url"

            )

            # Different case
            # self.reference only has one attribute if nothing was initalized;
            # which is.. activity_id
            # so that is why..
            # have a value for default id for self.reference.activity_id to
            # None type
            self.reference.activity_id = getattr(
                reference, "activity_id", None
            )

        pass
