import discord 
from discord.ext import commands
from discord import Embed, Colour
from src.dice import DiceManager, choice
from src.player import PlayerManager
from src.utils import read_file, sepate_uppercase


class MachineNRevolution(commands.Bot):
    def __init__(self, command_prefix, self_bot) -> None:
        commands.Bot.__init__(
            self, command_prefix=command_prefix, self_bot=self_bot)
        self.command_prefix = command_prefix
        self.self_bot = self_bot
        self.manager = PlayerManager()
        self.list_names = []
        self.add_commands()
        self.races = {key:value for key, value in read_file("src/assets/races")}
        self.classes = {key:value  for key, value  in read_file("src/assets/classes")}
        self.statusType = ["Strenght", "Dexterity", "Creativity",
            "Cleverness", "Charm", "Insight", "Resistence", "NuclearResistence"]

    def generate_coin(self, name: str, r_race: str) -> None:
        old_coin = self.races[r_race]['coins']['old_coin']
        digi_coin = self.races[r_race]['coins']['digi_coin']
        self.manager.set_coin(name,old_coin,digi_coin)

    def generate_languages(self, name: str, r_race: str, r_class: str) -> None:
        languages = self.races[r_race]['languages']
        languages_c = self.classes[r_class]['languages']
        for i in languages:
            self.manager.set_languages(name,i)
        for i in languages_c:
            if i != "" or i != None:
                self.manager.set_languages(name,i)

    def generate_status(self, name: str, r_race: str) -> None:
        bonus = self.races[r_race]['primary_status']
        self.manager.set_status(name,self.statusType,bonus)
    
    def generate_armament(self, name: str, r_class: str) -> None:
        armaments = self.classes[r_class]['initial_armament']
        for i in armaments:
            self.manager.set_armament(name,i)

    def add_commands(self) -> None:
        @self.command(name="roll")
        async def roll(ctx, dice_number: int = 2, roll_times: int = 1) -> None:
            faces = DiceManager()
            count = 1
            embed = discord.Embed(colour = Colour.blue())
            embed.set_author(name=f'Dices Nº{dice_number} at {roll_times}')
            for face in faces.manage(dice_number, roll_times):
                embed.add_field(name=f"{count}º", value=f"roll: {face}", inline=False)
                count += 1
            await ctx.channel.send(embed=embed)

        @self.command(name="createname")
        async def createname(ctx, name: str) -> None:
            if name not in self.list_names:
                self.manager.players = name
                self.manager.set_name(name)
                self.list_names.append(name)
                count = 1
                embed = discord.Embed(colour = Colour.blue())
                embed.set_author(name=f"Choose {name}'s race: ")
                for i in self.races.keys():
                    embed.add_field(name=f"{count}", value=f"{i}", inline=True)
                    count += 1
                embed.add_field(name="Next: ", value="Now use the command 'createrace name number' to choose the race!", inline=True)
            else:
                embed = discord.Embed(colour = Colour.red())
                embed.set_author(name=f"Player {name} already exists")
            await ctx.channel.send(embed=embed)

        @self.command(name="createrace")
        async def createrace(ctx, name:str,race: int) -> None:
            races = [i for i in self.races.keys()]
            race_choice = races[race-1]
            self.manager.set_race(name, race_choice)
            count = 1
            embed = discord.Embed(colour = Colour.blue())
            embed.set_author(name=f"Choose {name}'s class: ")
            for i in self.classes.keys():
                embed.add_field(name=f"{count}", value=f"{i}", inline=True)
                count += 1
            embed.add_field(name="Next: ", value="Now use the command 'createclass name number' to choose the classs!", inline=True)
            await ctx.channel.send(embed=embed)

        @self.command(name="create{errorclass")
        async def create_class(ctx,name:str, r_class: int) -> None:
            name = self.list_names[-1]
            classes = [i for i in self.classes.keys()]
            class_choice = classes[r_class-1]
            self.manager.set_class(name, class_choice)
            embed = discord.Embed(colour = Colour.gold())
            embed.set_author(name=f"Characther {name} is ready")
            embed.add_field(name="Next: ", value=f"Now use the command 'createprint {name}' to see the characther", inline=True)
            await ctx.channel.send(embed=embed)

        @self.command(name="createrandom")
        async def create_randcom(ctx) -> None:
            names = ["John","Ana","Sarah","Edward"]
            family_name = ["West","Smith","Forensis","Kennedi"]
            fullname = choice(names) + choice(family_name)
            self.list_names.append(fullname)
            self.manager.players = fullname
            self.manager.set_race(fullname, choice([i for i in self.races.keys()]))
            self.manager.set_class(fullname, choice([i for i in self.classes.keys()]))
            embed = discord.Embed(colour = Colour.gold())
            embed.set_author(name=f"Characther {fullname} is ready")
            embed.add_field(name="Next: ", value="Now use the command 'createprint' to see the characther", inline=True)
            await ctx.channel.send(embed=embed)

        @self.command(name="createprint")
        async def create_print(ctx, name: str) -> None:
            r_race = self.manager.players[name].r_race
            r_class = self.manager.players[name].r_class
            self.generate_coin(name, r_race)
            self.generate_status(name,r_race)
            self.generate_armament(name, r_class)
            self.generate_languages(name, r_race, r_class)
            self.manager.players.get(name).print_player()
            embed = discord.Embed(colour =Colour.green())
            embed.set_author(name=f"Survival {sepate_uppercase(name)}'s Data")
            for k,v in self.manager.players.get(name).data_dict.items():
                embed.add_field(name=f"{k}: ", value=f"{v}")
            await ctx.channel.send(embed=embed)

        @self.event
        async def on_command_error(ctx, error) -> None:
            embed = discord.Embed(colour=Colour.red())
            if isinstance(error,commands.MissingRequiredArgument):
                embed.set_author(name=f"error: it is missing some argument")
            elif isinstance(error, commands.BadArgument):
                embed.set_author(name=f"error: wrong argument")
            elif isinstance(error,commands.CommandError):
                embed.set_author(name=f"error: unknown command")
            else:
                embed.set_author(name=f"error: unknown error")
            await ctx.channel.send(embed=embed)

