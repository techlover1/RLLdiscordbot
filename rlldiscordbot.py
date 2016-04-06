# Import
import discord
import config

# Setup client
client = discord.Client()
email = config.email
password = config.password

# Setup Variables
production = config.checkinlocation


@client.async_event
def on_message(message):
    # Don't reply to yourself
    if message.author == client.user:
        return

        # Regular Commands

    # !admin
    if message.content.startswith("!admin"):
        yield from client.send_message(message.channel, "My admin is NightFury, contact him if I'm being an asshole")

    # !checkin
    if message.content.startswith("!checkin"):
        yield from client.send_message(message.channel, message.author.mention + " you successfully checked in!")
        yield from client.send_message(production, str(message.author) + " - Checked in for a match!\n" + "@everyone")

    # !help
    if message.content.startswith("!help"):
        yield from client.send_message(message.channel, "```Possible commands:\n!admin\n!checkin\n!help\n!ping\
        	!retakes\n!tenmans\n!twitch```")

    # !ping
    if message.content.startswith("!ping"):
        yield from client.send_message(message.channel, "pong")

    # !retakes
    if message.content.startswith("!retakes"):
        yield from client.send_message(message.channel, "```connect 66.150.121.163:27018```")

    # !tenmans
    if message.content.startswith("!tenmans") or message.content.startswith("!10mans"):
        yield from client.send_message(message.channel, "```connect 66.150.121.163:27018;password 10mansarefun```")

    # !twitch
    if message.content.startswith("!twitch"):
        yield from client.send_message(message.channel, "http://twitch.tv/redditladderleague or http://twitch.tv/redditladderleague_2")

        # Admin Commands

    # !channelid
    if message.content.startswith("!channelid"):
        if message.author.id in config.admins:
            yield from client.send_message(message.channel, str(message.channel.id))
        else:
            yield from client.send_message(message.channel, "Nice try pleb. Admins only")

    # !userid
    if message.content.startswith("!userid"):
        yield from client.send_message(message.channel, str(message.author.id))

        # Easter Eggs

    # good bot
    if message.content.startswith("good bot"):
        if message.author.id in config.admins:
            yield from client.send_message(message.channel, "Thank you almighty ruler!")
        else:
            yield from client.send_message(message.channel, "Thanks pleb.")

    # !egg
    if message.content.startswith("!egg"):
        yield from client.send_message(message.channel, " http://imgur.com/GZ79poy")

    # !salt
    if message.content.startswith("!salt"):
        yield from client.send_message(message.channel, "http://www.saltopiasalts.com/uploads/1/0/7/8/10782629/7109779_orig.jpg")

    # !kappa
    if message.content.startswith("!kappa") or "Kappa" in message.content:
        yield from client.send_message(message.channel, "http://res.cloudinary.com/urbandictionary/image/upload/a_exif,c_fit,h_200,w_200/v1395991705/gjn81wvxqsq6yzcwubok.png")


# Display account info when logged in
@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Login to account
client.run(email, password)
