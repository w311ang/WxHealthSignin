import asyncio
from typing import List, Optional, Union

from wechaty_puppet import FileBox  # type: ignore

from wechaty import Wechaty, Contact
from wechaty.user import Message, Room

import os

realname=os.getenv('SIGNIN_REALNAME')

os.environ['NO_PROXY'] = 'webpush.wx.qq.com'

class MyBot(Wechaty):

    async def on_message(self, msg: Message):
        """
        listen for message event
        """
        from_contact: Optional[Contact] = msg.talker()
        text = msg.text()
        room: Optional[Room] = msg.room()
        if (('#接龙' in text) or ('＃接龙' in text))and ('平安' in text) and (not '%s平安'%realname in text):
            conversation: Union[
                Room, Contact] = from_contact if room is None else room
            await conversation.ready()
            lines=text.splitlines()
            lastline=lines[-1]
            #print(lastline)
            number=int(lastline.split('.')[0])
            mynum=number+1
            mytext=text+'\n%s. %s平安'%(mynum,realname)
            await conversation.say(mytext)
        elif text=='ding':
            conversation: Union[
                Room, Contact] = from_contact if room is None else room
            await conversation.ready()
            await conversation.say('dong')

asyncio.run(MyBot().start())
