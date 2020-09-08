import discord
from discord.ext import commands 
import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
sword = 0

def intro():

	@client.command()
	async def start_game(ctx):
		
		await ctx.send("```After a drunken night out with friends, you awaken the "
	 			  "next morning in a thick, dank forest. Head spinning and " 
	  			  "fighting the urge to vomit, you stand and marvel at your new, "
	  			  "unfamiliar setting. The peace quickly fades when you hear a "
				  "grotesque sound emitting behind you. A slobbering orc is "
				  "running towards you. You will:```")
				
		await ctx.send("A. Grab a nearby rock and throw it at the orc\n"
						"B. Lie down and wait to be mauled\n"
						"C. Run")

	@client.command()
	async def opt(ctx, arg):
		
		choice = arg
		print(choice)

		if choice in answer_A:
			await ctx.send ("```The orc is stunned, but regains control. He begins \n"
  										"running towards you again. Will you:```")

			await ctx.send("A. Run\n"
										"B. Throw another rock\n"
										"C. Run towards a nearby cave")

			option_rock()

		elif choice in answer_B:
			await ctx.send ("```Welp, that was quick. You died!```")
			

		elif choice in answer_C:
			await ctx.send ("```You run as quickly as possible, but the orc's "
  										"speed is too great. You will:```")

			await ctx.send("A. Hide behind boulder\n"
									   "B. Trapped, so you fight\n"
									   "C.  Run towards an abandoned town")
			option_run()


def option_rock(): 
	@client.command()
	async def opt(ctx, arg):
		
		choice = arg

		if choice in answer_A:

			await ctx.send ("```You run as quickly as possible, but the orc's "
  										"speed is too great. You will:```")

			await ctx.send("A. Hide behind boulder\n"
										   "B. Trapped, so you fight\n"
										   "C.  Run towards an abandoned town")
			option_run()

		elif choice in answer_B:
			await ctx.send ("```\nYou decided to throw another rock, as if the first " 
									    "rock thrown did much damage. The rock flew well over the "
									    "orcs head. You missed. \n\nYou died!```")
			
			
		elif choice in answer_C:

			await ctx.send ("```You were hesitant, since the cave was dark and "
										  "ominous. Before you fully enter, you notice and pick up"
										  " a shiny sword on the ground.```")
			sword = 1
			await ctx.send("```What do you do next?```")
			await ctx.send("A. Hide in silence\n"
									   "B. Fight\n"
									   "C. Run")
			option_cave()

def option_cave():

	@client.command()
	async def opt(ctx, arg):
		
		choice = arg

		if choice in answer_A:

			await ctx.send ("```\nReally? You're going to hide in the dark? I think "
										    "orcs can see very well in the dark, right? Not sure, but "
										    "I'm going with YES, so...\n\nYou died!```")
			

		elif choice in answer_B:
			if sword > 0:
			    await ctx.send ("```\nYou laid in wait. The shimmering sword attracted "
										    "the orc, which thought you were no match. As he walked "
										    "closer and closer, your heart beat rapidly. As the orc "
										    "reached out to grab the sword, you pierced the blade into "
										    "its chest. \n\nYou survived!```")
			else:
				await ctx.send ("```\nYou should have picked up that sword. You're "
     										"defenseless. \n\nYou died!```")
				
			
		elif choice in answer_C:

			await ctx.send ("```As the orc enters the dark cave, you sliently "
									    "sneak out. You're several feet away, but the orc turns "
									    "around and sees you running.```")

			await ctx.send("A. Hide behind boulder\n"
										   "B. Trapped, so you fight\n"
										   "C.  Run towards an abandoned town")
			option_run()


def option_run():
	@client.command()
	async def opt(ctx, arg):
		
		choice = arg
			
		if choice in answer_A:
			await ctx.send ("```You're easily spotted. "
			   							"\n\nYou died!```")
			

		elif choice in answer_B:

			await ctx.send ("```\nYou're no match for an orc.\n\nYou died!```")
			

		elif choice in answer_C:

		  	await ctx.send  ("```\nWhile frantically running, you notice a rusted "
											  "sword lying in the mud. You quickly reach down and grab it, "
											  "but miss. You try to calm your heavy breathing as you hide "
											  "behind a delapitated building, waiting for the orc to come "
											  "charging around the corner. You notice a purple flower "
											  "near your foot. You pick it up```")

		  	await ctx.send("```You hear its heavy footsteps and ready yourself for "
									  		"the impending orc."
									  		"\nYou quickly hold out the purple flower, somehow "
									  		"hoping it will stop the orc. It does! The orc was looking "
									   		"for love. "
									    	"\n\nThis got weird, but you survived!```")
		  	


client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game("send 'orc_help' in server text channel" ))
	print('bot is ready')


@client.command()
async def orc_help(ctx):
		
	await ctx.send("```>>>This is a simple text based adventure game."
					"\n>> To play this game from start again, send 'start_game' command anytime in the server"
					"\n>> To get help, send 'orc_help' command anytime in the server"
					"\n>> To reply with an option use this command: 'opt option' (i.e. opt b)```")
	intro()


client.run('DISCORD APP TOKEN')
