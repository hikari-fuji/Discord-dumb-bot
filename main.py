import discord, psutil
from datetime import datetime
from discord.ext import tasks
from cmdd import help, joke, meme, anime

try:
    import config
except:
    print("Không có tệp config.py để khởi chạy!!")

TOKEN = config.TOKEN
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
luna = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='f!help'))
    print(f"{config.bot_name} v{config.bot_version}")
    print('Sẵn sàng!')
    ping_channel.start()
    sync = await luna.sync()
    print(f"Đã đồng bộ thêm {len(sync)} lệnh")
    
@luna.command(name = "help", description = "Hướng dẫn sử dụng bot") 
async def hlp(ctx: discord.Interaction):
    print(f"{ctx.user} đã sử dụng lệnh 'help'!")
    await ctx.response.send_message(help.command_response(config.bot_prefix))
@luna.command(name = "meme", description = "Nhận một meme ngẫu nhiên") 
async def mem(ctx: discord.Interaction):
    url,name = meme.get_meme()
    em = discord.Embed(title=name)    
    em.set_image(url = url)
    em.set_footer(text = "Memes from subreddit")
    em.color = discord.Color.purple()
    await ctx.response.send_message(embed = em)
@luna.command(name = "joke", description = "Nhận một câu đùa ngẫu nhiên") 
async def jok(ctx: discord.Interaction):
    setup, punch = joke.get_joke(config.memes_blacklist_genres)
    mbed = discord.Embed(
        description=f"**People A**: {setup}\n**People B**: {punch}",
        color=discord.Color.orange()
    )
    await ctx.response.send_message(embed=mbed)
@luna.command(name="anime",description="Tìm một anime theo tên")
async def anim(ctx: discord.Interaction, name: str):
    try:
        res = anime.get_anime(name)
        if any(word in res[6].lower() for word in config.animaga_blacklist_genres):
                # Find another similar result
                search_result = find_another_result()
                if search_result:
                    await ctx.send(f"Another similar result found: {search_result}")
                else:
                    await ctx.send("No results found.")
        else:
            # Create an embedded message with the search result
            embed = discord.Embed(title=res[0], description=res[1], color=discord.Color.blue())
            embed.add_field(name=':calendar_spiral: Publish Date', value=res[2], inline=True)
            embed.add_field(name=':studio_microphone: Studio', value=res[3], inline=True)
            embed.add_field(name=':film_frames: Episodes', value=res[4], inline=True)
            embed.add_field(name=':bar_chart: Status', value=res[5], inline=True)
            embed.add_field(name=':label: Genres', value=res[6], inline=True)
            embed.add_field(name=':stopwatch: Duration', value=f'{res[7]} minutes', inline=True)
            embed.add_field(name=':star: Average Rating', value=res[8], inline=True)
            embed.set_image(url=res[9])
            await ctx.response.send_message(embed=embed)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
@luna.command(name="manga",description="Tìm một manga theo tên")
async def anim(ctx: discord.Interaction, name: str):
    pass

def find_another_result():
    # Implement code to find another similar result based on the search query
    # Return the new search result or None if not found
    return None





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
