from os import environ
environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  
from submain import main, apikey, callsign, channelnukename, token, version_
from os import system, name
from discord.abc import *
from colorama import init, Style, Fore
from json import load, loads
from discord import Embed, Member, File
from time import sleep
from discord.ext import commands
from pyowm import OWM
from random import *
from requests import get
from instaloader import Instaloader, Profile
from random import randint
from qrcode import QRCode

system("title skyline")
def clearScreen(): 
    # for windows os
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux os(The name is posix)
    else: 
        _ = system('clear') 

clearScreen()
init(autoreset=True)
sra = Style.RESET_ALL



main.hellomessage() # beginning


def main():
    from submain import main
    def clearScreenwlogo():
        clearScreen()
        main.hellomessage()
    with open("data\\config.json", "r") as j:
        dcj = load(j)
        bordercolor = dcj["bordercolor"]
        logocolor = dcj["logocolor"]
        

    owm = OWM(apikey) # API key is for pyowm module


    if logocolor == "red":
        logocolor = Fore.RED
    elif logocolor == "blue":
        logocolor = Fore.BLUE
    elif logocolor == "lightblue":
        logocolor = Fore.LIGHTBLUE_EX
    elif logocolor == "lightred":
        logocolor = Fore.LIGHTRED_EX
    elif logocolor == "green":
        logocolor = Fore.GREEN
    elif logocolor == "lightgreen":
        logocolor = Fore.LIGHTGREEN_EX
    elif logocolor == "grey":
        logocolor = Fore.LIGHTBLACK_EX
    elif logocolor == "cyan":
        logocolor = Fore.CYAN
    elif logocolor == "lightcyan":
        logocolor = Fore.LIGHTCYAN_EX
    elif logocolor == "white":
        logocolor = Fore.WHITE
    elif logocolor == "yellow":
        logocolor = Fore.YELLOW
    elif logocolor == "lightyellow":
        logocolor = Fore.LIGHTYELLOW_EX
    elif logocolor == "magenta":
        logocolor = Fore.MAGENTA
    elif logocolor == "lightmagenta":
        logocolor = Fore.LIGHTMAGENTA_EX
    elif bordercolor == "lightwhite":
        logocolor = Fore.LIGHTWHITE_EX
    else:
        logocolor = Fore.WHITE

    if bordercolor == "red":
        bordercolor = Fore.RED
    elif bordercolor == "blue":
        bordercolor = Fore.BLUE
    elif bordercolor == "lightblue":
        bordercolor = Fore.LIGHTBLUE_EX
    elif bordercolor == "lightred":
        bordercolor = Fore.LIGHTRED_EX
    elif bordercolor == "green":
        bordercolor = Fore.GREEN
    elif bordercolor == "lightgreen":
        bordercolor = Fore.LIGHTGREEN_EX
    elif bordercolor == "grey":
        bordercolor = Fore.LIGHTBLACK_EX
    elif bordercolor == "cyan":
        bordercolor = Fore.CYAN
    elif bordercolor == "lightcyan":
        bordercolor = Fore.LIGHTCYAN_EX
    elif bordercolor == "white":
        bordercolor = Fore.WHITE
    elif bordercolor == "yellow":
        bordercolor = Fore.YELLOW
    elif bordercolor == "lightyellow":
        bordercolor = Fore.LIGHTYELLOW_EX
    elif bordercolor == "magenta":
        bordercolor = Fore.MAGENTA
    elif bordercolor == "lightmagenta":
        bordercolor = Fore.LIGHTMAGENTA_EX
    elif bordercolor == "lightwhite":
        bordercolor = Fore.LIGHTWHITE_EX
    else:
        bordercolor = Fore.WHITE
    
    logged_in = False
    print(f"                                                 {bordercolor}║{sra}Status: {Fore.LIGHTBLACK_EX}loading...{bordercolor}║{sra}               ")
    print(f"                                                 {bordercolor}╚══════════════════╝{sra}               ")
    print()
    def restprint():
        print(f"                                                 {bordercolor}║{sra} Status: {Fore.LIGHTGREEN_EX}ONLINE{bordercolor}   ║{sra}               ")
        print(f"                                                 {bordercolor}╚══════════════════╝{sra}               ")
        print()


        

    TOKEN = str(token)
    bot = commands.Bot(callsign, self_bot=True, help_command=None)


    @bot.event
    async def on_ready():
        logged_in = True  
        sleep(2)
        clearScreenwlogo()

        if logged_in == True:
            print(f"                                                 {bordercolor}║{sra}  Status: {Fore.GREEN}ONLINE  {bordercolor}║{sra}               ")
            print(f"                                                 {bordercolor}╚══════════════════╝{sra}               ")
            print()
        else:
            print(f"                                                 {bordercolor}║{sra} Status:{Fore.GREEN}OFFLINE   {bordercolor}║{sra}               ")
            print(f"                                                 {bordercolor}╚══════════════════════════════╝{sra}               ")
            print()           
        

    
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def purge(ctx, limit: int):
        await ctx.message.delete()
        if ctx.message.author.guild_permissions.manage_messages:
            if limit > 251:
                embed = Embed(title=":x:  Error!", description='Can not purge more than 250 Messages!', color=0x11019e)
                await ctx.send(embed=embed, delete_after=2.0) 
            else:
                await ctx.channel.purge(limit=limit)
                embed = Embed(title="Done! :white_check_mark: ", description='Purge completed!', color=0x11019e)
                await ctx.send(embed=embed, delete_after=2.0)
        else:
            em = Embed(title="Permissions Required!",
                           description=f"{ctx.author.name} You do not have the required Permissions to use this command",
                           color=0x11019e)
            await ctx.send(embed=em)


    @bot.command() # Ping latency check.
    async def ping(ctx):
        await ctx.message.delete()
        embed = Embed(title="Pong!🏓", description=f'{round(bot.latency * 1000)}ms', color=0x11019e)
        await ctx.send(embed=embed)

    
    @bot.command(aliases=["hlp", "h"])
    async def help(ctx):
        await ctx.message.delete()
        help=Embed(title="Help", description="Here is all the help you need.", color=0x11019e)
        help.add_field(name=f"{callsign}ping", value="so you can check the ping-latency.", inline=True)
        help.add_field(name=f"{callsign}quitt,  {callsign}q", value="quit program.", inline=True)
        help.add_field(name=f"{callsign}ban (an user)", value="quickly ban a user.", inline=False)
        help.add_field(name=f"{callsign}kick (an user)", value="to kick a user quickly.", inline=False)
        help.add_field(name=f"{callsign}nuke", value="create a lot of channels really fast.", inline=False)
        help.add_field(name=f"{callsign}help,  {callsign}h,  {callsign}hlp", value="shows this help window.", inline=False)
        help.add_field(name=f"{callsign}purge (a number)", value="to purge all of your messages.", inline=False)
        help.add_field(name=f"{callsign}delall,  {callsign}deleteall", value="delete all channel in a server.", inline=False)
        help.add_field(name=f"{callsign}weather,  {callsign}we (a place)", value="gives weather information about this place.", inline=False)
        help.add_field(name=f"{callsign}cat,  {callsign}catimg,  {callsign}catpic", value="shows you random cat pics.", inline=False)
        help.add_field(name=f"{callsign}meme,  {callsign}Meme,  {callsign}mem", value="shows you random memes from the internet.", inline=False)
        help.add_field(name=f"{callsign}instagram (username),  {callsign}ig (username)", value="gives Instagram information about the person.", inline=True)
        help.add_field(name=f"{callsign}qrcode (text),  {callsign}qr (text)", value="create a QR Code out of your text.", inline=False)
        help.add_field(name=f"{callsign}spameveryone (word),  {callsign}se (word)", value="spams everyone with @everyone in the chat.", inline=False)
        help.add_field(name=f"{callsign}avatar (user),  {callsign}av (user)", value="this will give you the profile picture of the user you mentioned.", inline=True)
        help.set_image(url = 'https://c.tenor.com/T2K-oDCSFFoAAAAC/drift-tokyo.gif')
        help.set_footer(text="made by skyline69")
        await ctx.send(embed=help)

    @bot.command(aliases=["qr"])
    async def qrcode(ctx, *, inputofUser):
        await ctx.message.delete()
        qr = QRCode(version = 4, box_size = 10, border = 5)
        data = str(inputofUser)
        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image(fill_color = "#8CD9FF" , back_color = "#151819") 
        img.save("src\QR\qr.png")
        file = File("src\QR\qr.png")       
        EmbedQR = Embed(title="QR Code", color=0x11019e)
        sleep(0.2)
        EmbedQR.set_image(url="attachment://qr.png")
        EmbedQR.set_footer(text="made by skyline69")
        await ctx.send(embed=EmbedQR, file=file)

    @bot.command(pass_context=True)
    async def nuke(ctx, channelName=channelnukename):
        await ctx.message.delete()
        guild = ctx.message.guild
        guild2 = ctx.guild
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)
        await guild.create_text_channel(channelnukename)




        if ctx.author.guild_permissions.manage_channels:
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
            await guild2.create_voice_channel(name=channelName)
        
        embed=Embed(title="Done  :white_check_mark:", description="Nuke completed.", color=0x11019e)
        await ctx.send(embed=embed, delete_after=1.8)

        
    
    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(ctx, member : Member):
        await ctx.message.delete()
        await member.ban()
        embed=Embed(title="Done  :white_check_mark:", description=f":black_circle:  User banned. ", color=0x11019e)
        await ctx.send(embed=embed, delete_after=1.8)

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(ctx, member : Member):
        await ctx.message.delete()
        await member.kick()
        embed=Embed(title="Done  :white_check_mark:", description=f":black_circle:  User kicked. ", color=0x11019e)
        await ctx.send(embed=embed, delete_after=1.8)

    @bot.command(aliases=["deleteall"])
    async def delall(ctx):
        await ctx.message.delete()
        for c in ctx.guild.channels: # iterating through each guild channel
            await c.delete()
    @bot.command(aliases=["catimg", "catpic"])
    async def cat(ctx):
        await ctx.message.delete()
        r = get("https://api.thecatapi.com/v1/images/search").json()
        cat_embed = Embed(title="Random cat picture.", color=0x11019e)
        cat_embed.set_image(url=f"{r[0]['url']}")
        cat_embed.set_footer(text='made by skyline69')
        await ctx.send(embed=cat_embed)

    @bot.command(aliases=["di", "d"])
    async def dice(ctx):
        await ctx.message.delete()
        embedDice = Embed(title="🎲 Dice rolled.", description=f"Number: {randint(1, 6)}", color=0x11019e)
        await ctx.send(embed=embedDice)
    @bot.command(aliases=["mem","Meme"])
    async def meme(ctx):
        await ctx.message.delete()
        content = get("https://meme-api.herokuapp.com/gimme/dankmemes").text
        data = loads(content)
        meme = Embed(title=data['title'], url=data['postLink'], color=0x11019e)
        meme.set_image(url=f"{data['url']}")
        meme.set_footer(text='made by skyline69')
        await ctx.send(embed=meme)
    
    @bot.command(aliases=["av"])
    async def getavatar(ctx,  member: Member=None):
        await ctx.message.delete()
        embed = Embed(title=f"Profile picture of {member.display_name} ", color=0x11019e)
        embed.set_image(url="{}".format(member.avatar_url))
        embed.set_footer(text='made by skyline69')
        await ctx.send(embed=embed)

    @bot.command(aliases=["ig"])
    async def instagram(ctx, instaUsername):
        from os import environ
        environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  
        await ctx.message.delete()
        bot = Instaloader()
        profile = Profile.from_username(bot.context, str(instaUsername))
        embed = Embed(title=f"Instagram", color=0x11019e)
        embed.add_field(name="Username", value=f"@{profile.username}", inline=True)
        embed.add_field(name="Followers", value=f"{profile.followers}", inline=True)
        embed.add_field(name="Follows", value=f"{profile.followees}", inline=True)
        embed.add_field(name="Bio", value=f"{profile.biography}", inline=True)
        embed.set_footer(text="made by skyline69")
        await ctx.send(embed=embed)    
    

    @bot.command(aliases=["se"])
    async def spameveryone(ctx, word):
        await ctx.message.delete()
        while True:
            await ctx.send('@everyone ' + word)
            sleep(0.012)
    @bot.command(aliases=["q"])
    async def quitt(ctx):
        quit()
    @bot.command(aliases=["we"])
    async def weather(ctx, city):
        await ctx.message.delete()
        city2 = city
        loc = owm.weather_manager().weather_at_place(city2)
        weather = loc.weather
        temp = weather.temperature(unit="celsius")
        status = weather.detailed_status
        wind = weather.wind()
        cleaned_temp_data = (int(temp["temp"]))
        cleaned_wind_dir = (int(wind["deg"]))
        cleaned_wind_speed = (float(wind["speed"]))
        status = weather.detailed_status
        embed2=Embed(title=f"{city}", color=0x11019e)
        embed2.add_field(name="Status", value=f"{status}", inline=True)
        embed2.add_field(name="Temperature", value=f"{cleaned_temp_data}°C", inline=False)
        embed2.add_field(name="Windspeed", value=f"{cleaned_wind_speed} km/h", inline=True)
        embed2.add_field(name="Winddegrees", value=f"{cleaned_wind_dir}°", inline=True)
        embed2.set_footer(text="made by skyline69")
        await ctx.send(embed=embed2)
        
    @bot.command(aliases=["v"])
    async def version(ctx):
        await ctx.message.delete()
        VersionEmbed = Embed(title=f"Version: {version_}", color=0x11019e)
        VersionEmbed.set_footer(text="made by skyline69")
        await ctx.send(embed=VersionEmbed, delete_after=3)
    @bot.event
    async def on_command_error(ctx, error):
        pass




    bot.run(TOKEN, bot=False) 

    print(sra)
    


if __name__ == '__main__':
    main()