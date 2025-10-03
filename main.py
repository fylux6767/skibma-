import discord
import os

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])

class PetMonitorBot(discord.Client):
    async def on_ready(self):
        print(f'✅ Bot {self.user} is ready! Monitoring channel {CHANNEL_ID}')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.channel.id == CHANNEL_ID:
            print(f'📨 New pet log: {message.content[:100]}...')

if __name__ == "__main__":
    bot = PetMonitorBot()
    bot.run(BOT_TOKEN)
