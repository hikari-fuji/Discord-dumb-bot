import discord, psutil
from datetime import datetime
from discord.ext import tasks
from cmdd import help, joke, meme

try:
    import config
except:
    print("Không có tệp config.py để khởi chạy!!")

TOKEN = config.TOKEN
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
dumb = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='f!help'))
    print(f"{config.bot_name} v{config.bot_version}")
    print('Sẵn sàng!')
    ping_channel.start()
    sync = await dumb.sync()# Sync the new command and remove the command not exist
    print(f"Đã đồng bộ thêm {len(sync)} lệnh")
    
@dumb.command(name = "help", description = "Hướng dẫn sử dụng bot") 
async def hlp(ctx: discord.Interaction):
    print(f"{ctx.user} đã sử dụng lệnh 'help'!")
    await ctx.response.send_message(help.command_response(config.bot_prefix))
@dumb.command(name = "meme", description = "Nhận một meme ngẫu nhiên") 
async def mem(ctx: discord.Interaction):
    url,name = meme.get_meme()
    em = discord.Embed(title=name)    
    em.set_image(url = url)
    em.set_footer(text = "Memes from subreddit")
    em.color = discord.Color.purple()
    await ctx.response.send_message(embed = em)
@dumb.command(name = "joke", description = "Nhận một câu đùa ngẫu nhiên") 
async def jok(ctx: discord.Interaction):
    setup, punch = joke.get_joke(config.memes_blacklist_genres)
    mbed = discord.Embed(
        description=f"**People A**: {setup}\n**People B**: {punch}",
        color=discord.Color.orange()
    )
    await ctx.response.send_message(embed=mbed)
    






current_time = datetime.now()
formatted_time = current_time.strftime("%d-%m-%Y")
@tasks.loop(minutes=config.bot_timeghost_ping)
async def ping_channel():
    channel = client.get_channel(config.channel_ping)
    if channel:
        try:
            fps = calculate_fps()
            mbed = discord.Embed(title=f"Ping! Có ai ở đây không? ")
            mbed.add_field(name='Version: ', value=f'{config.bot_version}')
            mbed.add_field(name='FPS: ', value=f'{fps}')
            mbed.add_field(name='Thời gian: ', value=f'{formatted_time}')
            mbed.set_thumbnail(url=f'{config.ping_thumb}')
            mbed.set_footer(text='*None reply*')
            mbed.color = discord.Colour.blurple()
            await channel.send(embed=mbed)
        except:
            print("error")

@ping_channel.before_loop
async def before_ping_channel():
    await client.wait_until_ready()

def calculate_fps():
    cpu_percent = psutil.cpu_percent(interval=1)
    fps = int(1 + cpu_percent)
    return fps


client.run(TOKEN)