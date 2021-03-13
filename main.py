import os
from src.bot import MachineNRevolution
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("DISCORD_BOT")

if __name__ == "__main__":
    bot = MachineNRevolution(">", False)
    bot.run(TOKEN)
