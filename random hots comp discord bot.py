import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random

Client = discord.Client()
bot_prefix="?"
client = commands.Bot(command_prefix = bot_prefix)

completeHeroList = [
'Abathur',
'Alarak',
'Alexstrasza',
'Ana',
'Anub\'arak',
'Artanis',
'Arthas',
'Auriel',
'Azmodan',
'Blaze',
'Butcher',
'Cassia',
'Chen',
'Cho\'Gall',
'Chromie',
'D.va',
'Dehaka',
'Diablo',
'E.T.C.',
'Falstad',
'Garrosh',
'Gazlowe',
'Genji',
'Greymane',
'Gul\'dan',
'Hanzo',
'Illidan',
'Jaina',
'Johanna',
'Junkrat',
'Kael\'Thas',
'Kel\'Thuzad',
'Kerrigan',
'Kharazim',
'Leoric',
'Li Li',
'Li-Ming',
'Lt. Morales',
'Lunara',
'Lucio',
'Maeiv',
'Malfurion',
'Malthael',
'Medivh',
'Muradin',
'Murky',
'Nazeebo',
'Nova',
'Probius',
'Ragnaros',
'Raynor',
'Rehgar',
'Rexxar',
'Samuro',
'Sgt. Hammer',
'Sonya',
'Stitches',
'Stukov',
'Sylvanas',
'Tassadar',
'The Lost Vikings',
'Thrall',
'Tracer',
'Tychus',
'Tyrael',
'Tyrande',
'Uther',
'Valeera',
'Valla',
'Varian',
'Xul',
'Zagara',
'Zarya',
'Zeratul',
'Zul\'jin'
]

allSpecialistList = [
'Abathur',
'Azmodan',
'Gazlowe',
'Medivh',
'Murky',
'Nazeebo',
'Probius',
'Sgt. Hammer',
'Sylvanas',
'The Lost Vikings',
'Xul',
'Zagara'
]

allWarriorList = [
'Anub\'arak',
'Artanis',
'Arthas',
'Blaze',
'Chen',
'Cho\'Gall',
'D.va',
'Dehaka',
'Diablo',
'E.T.C.',
'Garrosh',
'Johanna',
'Leoric',
'Muradin',
'Rexxar',
'Sonya',
'Stitches',
'Tyrael',
'Varian',
'Zarya'
]

allSupportList = [
'Alexstrasza',
'Ana',
'Auriel',
'Brightwing',
'Kharazim',
'Li Li',
'Lt. Morales',
'Lucio',
'Malfurion',
'Rehgar',
'Stukov',
'Tassadar',
'Tyrande',
'Uther'
]

allAssassinList = [
'Alarak',
'Butcher',
'Cassia',
'Chromie',
'Falstad',
'Genji',
'Greymane',
'Gul\'dan',
'Hanzo',
'Illidan',
'Jaina',
'Junkrat',
'Kael\'Thas',
'Kel\'Thuzad',
'Kerrigan',
'Li-Ming',
'Lunara',
'Maeiv',
'Malthael',
'Nova',
'Ragnaros',
'Raynor',
'Samuro',
'Thrall',
'Tracer',
'Tychus',
'Valeera',
'Valla',
'Zeratul',
'Zul\'jin'
]

allMeleeList = [
'Alarak',
'Butcher',
'Cassia',
'Greymane',
'Illidan',
'Kerrigan',
'Maeiv',
'Malthael',
'Ragnaros',
'Samuro',
'Thrall',
'Valeera',
'Zeratul',
'Zul\'jin',
'Kharazim',
'Anub\'arak',
'Artanis',
'Arthas',
'Chen',
'Dehaka',
'Diablo',
'E.T.C.',
'Garrosh',
'Johanna',
'Leoric',
'Muradin',
'Sonya',
'Stitches',
'Tyrael',
'Varian',
'Xul'
]

allWarcraftList = [
'Chromie',
'Falstad',
'Cho\'Gall',
'Greymane',
'Gul\'dan',
'Illidan',
'Jaina',
'Kael\'Thas',
'Kel\'Thuzad',
'Lunara',
'Maiev',
'Ragnaros',
'Samuro',
'Thrall',
'Valeera',
'Varian',
'Zul\'jin',
'Alexstrasza',
'Brightwing',
'Li Li',
'Malfurion',
'Rehgar',
'Tyrande',
'Uther',
'Anub\'arak',
'Arthas',
'Chen',
'E.T.C.',
'Garrosh',
'Muradin',
'Rexxar',
'Stitches',
'Gazlowe',
'Medivh',
'Murky',
'Sylvanas'
]

allStarcraftList = [
'Alarak',
'Kerrigan',
'Nova',
'Raynor',
'Tychus',
'Zeratul',
'Abathur',
'Probius',
'Sgt. Hammer',
'Zagara',
'Lt. Morales',
'Stukov',
'Tassadar',
'Artanis',
'Blaze',
'Dehaka'
]

allOverwatchList = [
'Genji',
'Hanzo',
'Junkrat',
'Tracer',
'Ana',
'Lucio',
'D.va',
'Zarya'
]

allDiabloList = [
'Butcher',
'Cassia',
'Li-Ming',
'Valla',
'Diablo',
'Johanna',
'Leoric',
'Malthael',
'Sonya',
'Tyrael',
'Azmodan',
'Xul',
'Nazeebo',
'Aurial',
'Kharazim'
]

allCheeseList = [
['Illidan + Abathur'],
['Medivh + Stitches'],
['Tassadar + Tracer'],
['Li-Ming + Ana'],
['Lt. Morales + Sgt. Hammer'],
['Cho\'Gall + Ana'],
['Tyrael + Uther'],
['Butcher + Falstad'],
['Uther + Garrosh'],
['Abathur + Zagara'],
['Abathur + Murky'],
['Ragnaros + Alexstrasza + D.va + Sylvanas'],
['Illidan + Tyrael + Sonya'],
['Arthas + Rehgar + Tassadar'],
['Xul + Nova + Kel\'Thuzad'],
['D.va + Zarya + Lt. Morales'],
['Illidan + Tracer + Abathur + Zarya + Lucio'],
['Zeratul + Abathur + Ragnaros'],
['Hanzo + Artanis + Tyrael + Brightwing'],
['Tyrael + Artanis + Lt. Morales + Gul\'dan + Raynor']
]

allCheeseDescriptions = [
['One of the most known duo setups out there. Abathur is a -massive- force multiplier for Illidans power due to the attackspeed talent at level 4 paired with Illidan\'s CDR trait on auto attacks and the additional survivability provided by carapace and the level 13 W healing from Abathur makes Abathur+Illidan one of the deadliest duo setups.'],
['The infamous get in the candy van combo. Once Stitches lands a hook + gorge, you just take your victim for a trip into your base with the help of Medivh\'s portal. What you can also do is offensively portal, gorge someone and take the portal back.'],
['Another really common duo setup. Tracer has a super tiny HP bar and deals massive auto attack damage. Tassadar removes Tracer\'s weaknesses by artifically increasing her HP pool with shields, making her safer from burst. Shields also provide lifesteal, making Tracer extremely tanky and allowing her to be much more greedy and safer. Tracer + Tass also requires a huge amount of counterpicks by the enemy team most of the time.'],
['With Ana we finally got the tools in HotS to have a mage hypercarry equivalent. Theres not much to be said about Nano Ming except that the calamity teleports are easily able to force teamwipes.'],
['Another very known and common setup, especially at lower ranks. As approaching this duo requires confidence, a comitted effort and the right setup. Sgt. Hammer zones out opponents from both of them while Medic can stay really far behind and be very safe, providing Hammer incredible sustain. The stimdrone ontop of all that is just the icing on the cake.'],
['Ana has dethroned Auriel as our Ogre\'s favorite healer. Not only can Ana keep up Cho\'Gall quite easily and from very safe distance. Nanoboost applies to BOTH Cho and Gall which is absolutely devastating as a 50 second cooldown'],
['Tyrael + Uther This one is quite under the radar as it is map dependant and involves this specific pairing of tank and support. If you play on Towers of Doom or even Cursed Hollow, this setup can singlehandedly win the game. Sanctification into Divine Shield or vice versa, guarantees you a free objective. The enemy team has no way of stopping this strategy beyond Void Prison and Ley Line Seal. Both of which aren\'t very common. And since you only need two people to get an entire objective, you can have three other players gaining advantages elsewhere on the map while Tyrael+Uther secure you the objective.'],
['Another one that is very easy to execute. Once the Butcher chains up the kill target in a teamfight, your own team immedieatly collapses on this kill target. Falstad follows up instantly with a mighty gust so everyone but your kill target gets pushed away.'],
['While this might not seem very obvious at first, throwing an Uther into the enemy backline is very lethal if you have a dive comp that can follow up on it. As soon as Uther gets dumped into the backline with a divine storm, destruction should ensue. It will also usually end with Uther dying first out of your team. Which is favourable with his trait and generally long ability cooldowns.'],
['This is another one that is somewhat under the radar but also very strong. Abathur\'s main weakness is the early game. While Zagara\'s main weakness is the lategame. Normally Zagara\'s splitpush alone forces at least 1 person on the enemy team to babysit Zagara. However to now gank her, requires a large effort as she is easily capable of just killing her ganker with a symbiote. They provide massive map presence for one in map vision with creep tumors and toxic nests but also with mutalisks and locusts shoving lanes, constantly putting pressure. This results in the enemy team splitting apart, responding to Zag. This plays into Abathur\'s main strength, small skirmishes and duels all over the map instead of 5v5 teamfights.\n\nOn top of that you get massive, global pushing power with Zag and a clone, able to appear at any fort on the map with Nydus and at level 20, even backdooring into your base to get keeps like they once used to be able to at level 10.'],
['This is essentially Illidan + Abathur but with a Murky. The shield and level 13 healing makes Murky incredibly more tanky and the spikes give him the slight edge he needs to become a dangerous and persistent bruiser that can easily pick apart your backline. They excel with a massive lategame powerspike and neither of them tends to actually die a lot which means they are always active on the map with no downtimes. This comp will net a lot of flames and upset teammates but is incredibly underrated and way more powerful than you might believe.'],
['This comp is limited to Infernal Shrines. The main weakness of Sylvanas is that she is a win more/snowball hero and she is very weak in actual teamfights or playing from behind. This setup guarantees you every single punisher in the game which means Sylvanas is a staple in this setup as her main weakness doesn\'t exist. Molten Core + Dragonqueen and D.Va Explosion are one of the biggest things you do NOT want to stay and fight against. By having all three and using them one by one to zone out the enemy team from the shrine objective, the only way to win for the enemy team is by pressuring the map itself and having better rotations.\n\nSylvanas however puts such a force and importance behind the punisher that even the first objective can already secure you a keep or an early win.'],
['If you happen to hate one particular person. This is the comp for you. Hunt + Judgement + Leap on a single target so the stuns line up with another. Chain stunning 1 target to death and having 3 melees connect onto it with burst damage.'],
['The OG Bloodlust comp. We used to play this way back in the old ranked system, when all three of these. Arthas, Rehgar and Tassadar were considered weak and hovered around 42-44% winrate, getting great success out of it. Now that all three are extremly strong and Tassadar has an innate slow on Archon attacks, its even stronger than it used to be. Arthas is the key to enabling this setup as Sindragosa prevents a disengage without Mighty Gust or similiar tools while also letting you dive carelessly right under keeps, forts and so on. Usually you want to get one melee assassin like a Thrall/Illidan and a ranged like Tracer or Greymane.\n\nEvery initiate should start with a Sindragosa into Bloodlust and Archon. 9 out of 10 times you will win the teamfight just based on the massive surprise effect and power spike by the bloodlust while the entire enemy team is trying to crawl away with Sindra\'s slow.'],
['A secret favorite. This setup enables you to globally delete someone off the map every minute with a simple Xul root into Kel\'thuzad and Nova ults. At level 16 when Xul gets the vulnerability, it becomes even more deadly and reliable. Often times Xul can just sit in a random bush between a rotation. Press E on someone and you got a kill. These three also cover each others weakness nicely. Providing a healthy mix of early and lategame. Lane presence. Melee to ranged ratio and ganking power. So its not like having these three in a team opens you up to major weaknesses beyond the lack of AA damage.'],
['This comp is the essence of double support but more powerful. It takes all the strengths of what made double support so good and takes it further. All three characters do not have mana and can go practically forever. You do not end up with only raw healing or only shieldstacking but a healthy spread of damage reduction, peels, shielding and healing. Which means you are not open to being abused by things like shieldbreaker arrows from Hanzo or touch of death from Malthael.\n\nThey all synergize incredibly with another. Each one making the other practically immortal. Good luck trying to kill Medic between defensive matrix and zarya shielding. Let alone the other two members in their teamcomp.\n\nYou will have sustain that can not be outmatched paired with incredible boss control and pushing power.'],
['As you can see this comp has no tank. As there is no need for one. Abathur in this setup only plays the role of duo soaking on a large map like Sky Temple or Cursed Hollow. He has nothing else to do as the game normally ends around 10 minutes with this draft. You do not need to sit on Illidan or Tracer, just cover the other two lanes. Meanwhile you have a 4man lane with two of the most unforgiving divers in the game. Zarya here just plays the role of a more offensive Tassadar who can also tank a few hits and adds more overall damage and pushing power. Lucio enables the dive or forth and back dancing even harder while Tracer and Illidan just chase down the enemy team and dive, farming kills nonstop until you are at the core and end the game with a massive level advantage. Once you get to the core its usually game just by the fact that Illidan and Tracer on the core are near impossible to defend.'],
['While there are many offensive cheeses out there. This one, just like the medic, dva and zarya one is more defensive of nature. But instead of preserving your heroes, you are preserving your structures. This functions best on Warhead Junction. Between Void Prison on your own buildings before nuke impact, Molten Core and Abathur\'s MULE, nukes essentially have zero value in getting structure damage for the enemy team.\n\nIt will also be laughably easy to prevent those quad nuke situations on your core with a properly used VP and a Rag fort behind the enemy team.\n\nRagnaros himself provides an acceptable off-lane and Abathur+Zeratul a strong map presence with huge kill potential.'],
['This is another exclusive setup that is restricted to Cursed Hollow but can also function on Warhead Junction. Simply abusing the raw DPS to secure bosses in spans of 10 seconds with Hanzo + Artanis and another high octane DPS like Greymane or Valla. Brightwing and Tyrael are merely there for the boss control in sanctification, holy ground and emerald wind. This setup allows you to boss anytime you want. You can kill bosses in record speed and so even just being gone for 15-20 seconds on the minimap can be a boss for you. Even if all five people on the enemy team are alive and in range to respond, the boss will still go to you 9/10 times.\n\nThe raw power of being able to force and take a boss practically instantly whenever you feel like it, allows you to put great pressure during certain times and snowball with those advantages.'],
['Another spin on the raw racing potential but this time, you are trading mercenary damage for structure damage. This comp is most powerful on Warhead Junction but you can play it on every large map out there. The win condition is to medivac on the enemy core. From there on you have an Artanis going at it with Amateur Opponent. Raynor dropping a Hyperion on the core and providing attackspeed to the other 4 players. Gul\'dan goes for the Rain of Destruction. (That other ult no one has ever seen) as it provides the highest core damage in the game next to Azmodan\'s demonic invasion at lvl 20.\n\nSo now you have a Rain of Destruction, Amateur Opponent Artanis and a Hyperion + Raynor wailing at the core.\n\nWhen the enemy team responds you just drop a sanctification and keep going. Most of the time, the core is already destroyed before the sanctification even expires.\n\nThe important thing to note here is that you need to take a Fort and a Keep in one lane first to make flying on the core even possible.']
]

"""

LOGIC TO BE ADDED

allHordeList = [
'Cho\'Gall',
'Valeera',
'Gazlowe',
'Anub\'arak',
'Rexxar',
'Rehgar',
'Samuro',
'Thrall',
'Stitches',
'Kael\'Thas',
'Gul\'dan',
'Zul\'jin',
'Garrosh',
'Sylvanas'
]

allAllianceList = [
'Medivh',
'Uther',
'Jaina',
'Malfurion',
'Muradin',
'Tyrande',
'Falstad',
'Maeiv',
'Varian',
'Greymane',
]

LOGIC TO BE ADDED

"""

@client.event
async def on_ready():
	print ("Bot Online!")
	print ("Name: {}".format(client.user.name))
	print ("ID: {}".format(client.user.id))
	await client.change_presence(game=discord.Game(name='Heroes of the Storm'))

@client.event
async def on_message(message):
	if(message.content.startswith("?comp random")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		if(playerInput == 1):
			completeHeroList.remove('Cho\'Gall')
		while (counter < playerInput):
			hero = random.choice(completeHeroList)
			heroList.append(hero)
			completeHeroList.remove(hero)
			if hero == 'Cho\'Gall':
				counter = counter + 2
			elif hero == 'Cho\'Gall' and counter >= 4:
				heroList.remove('Cho\'Gall')
				hero = random.choice(completeHeroList)
				heroList.append(hero)
				completeHeroList.remove(hero)
			else:
				counter = counter + 1

		em = discord.Embed(title = "Random Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp specialist")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		while (counter < playerInput):
			hero = random.choice(allSpecialistList)
			heroList.append(hero)
			allSpecialistList.remove(hero)
			counter = counter + 1

		em = discord.Embed(title = "All Specialist Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp warrior")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		if(playerInput == 1):
			completeHeroList.remove('Cho\'Gall')		
		while (counter < playerInput):
			hero = random.choice(allWarriorList)
			heroList.append(hero)
			allWarriorList.remove(hero)
			if hero == 'Cho\'Gall':
				counter = counter + 2
			elif hero == 'Cho\'Gall' and counter >= 4:
				heroList.remove('Cho\'Gall')
				hero = random.choice(completeHeroList)
				heroList.append(hero)
				completeHeroList.remove(hero)
			else:
				counter = counter + 1

		em = discord.Embed(title = "All Warrior Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp support")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		while (counter < playerInput):
			hero = random.choice(allSupportList)
			heroList.append(hero)
			allSupportList.remove(hero)
			counter = counter + 1

		em = discord.Embed(title = "All Support Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp assassin")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		while (counter < playerInput):
			hero = random.choice(allAssassinList)
			heroList.append(hero)
			allAssassinList.remove(hero)
			counter = counter + 1

		em = discord.Embed(title = "All Assassin Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp warcraft")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		if(playerInput == 1):
			completeHeroList.remove('Cho\'Gall')
		while (counter < playerInput):
			hero = random.choice(allWarcraftList)
			heroList.append(hero)
			allWarcraftList.remove(hero)
			if hero == 'Cho\'Gall':
				counter = counter + 2
			elif hero == 'Cho\'Gall' and counter >= 4:
				heroList.remove('Cho\'Gall')
				hero = random.choice(completeHeroList)
				heroList.append(hero)
				completeHeroList.remove(hero)
			else:
				counter = counter + 1

		em = discord.Embed(title = "All Warcraft Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp starcraft")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		while (counter < playerInput):
			hero = random.choice(allStarcraftList)
			heroList.append(hero)
			allStarcraftList.remove(hero)
			counter = counter + 1

		em = discord.Embed(title = "All Starcraft Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp overwatch")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		while (counter < playerInput):
			hero = random.choice(allOverwatchList)
			heroList.append(hero)
			allOverwatchList.remove(hero)
			counter = counter + 1

		em = discord.Embed(title = "All Overwatch Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp diablo")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		while (counter < playerInput):
			hero = random.choice(allDiabloList)
			heroList.append(hero)
			allDiabloList.remove(hero)
			counter = counter + 1

		em = discord.Embed(title = "All Diablo Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp melee")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5

		counter = 0
		heroList = []
		while (counter < playerInput):
			hero = random.choice(allMeleeList)
			heroList.append(hero)
			allMeleeList.remove(hero)
			counter = counter + 1

		em = discord.Embed(title = "All Melee Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp standard")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5
		if playerInput < 5:
			await client.send_message(message.channel, "This composition requires 5 players.")
			client.close
			return

		tankCounter = 0
		supportCounter = 0
		fillCounter = 0
		heroList = []
		mergedList = allAssassinList + allSpecialistList
		while (tankCounter < 1):
			tank = random.choice(allWarriorList)
			heroList.append(tank)
			if tank == 'Cho\'Gall':
				tankCounter = tankCounter + 1
				fillCounter = fillCounter + 1
				mergedList.remove(tank)
			elif tank == 'Cho\'Gall' and counter >= 4:
				heroList.remove('Cho\'Gall')
				tank = random.choice(completeHeroList)
				heroList.append(tank)
				completeHeroList.remove(tank)
			else:
				tankCounter = tankCounter + 1
		while (supportCounter < 1):
			support = random.choice(allSupportList)
			heroList.append(support)
			supportCounter = supportCounter + 1
		while (fillCounter < 3):
			fill = random.choice(mergedList)
			heroList.append(fill)
			mergedList.remove(fill)
			fillCounter = fillCounter + 1

		em = discord.Embed(title = "Standard Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close
	
	if(message.content.startswith("?comp solo support")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5
		if playerInput < 2:
			await client.send_message(message.channel, "This composition requires at least 2 players.")
			client.close
			return

		supportCounter = 0
		fillCounter = 1
		heroList = []
		mergedList = allAssassinList + allSpecialistList + allWarriorList
		while (supportCounter < 1):
			support = random.choice(allSupportList)
			heroList.append(support)
			supportCounter = supportCounter + 1
		while (fillCounter < playerInput):
			fill = random.choice(mergedList)
			heroList.append(fill)
			mergedList.remove(fill)
			if fill == 'Cho\'Gall':
				fillCounter = fillCounter + 2
				allWarriorList.remove(fill)
			elif fill == 'Cho\'Gall' and counter >= 4:
				heroList.remove('Cho\'Gall')
				fill = random.choice(completeHeroList)
				heroList.append(fill)
				completeHeroList.remove(fill)
			else:
				fillCounter = fillCounter + 1

		em = discord.Embed(title = "Solo Support Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp dual support")):
		await client.send_message(message.channel, "How many players are in your party?")

		msg = await client.wait_for_message(author=message.author, content=None)
		try:
			playerInput = int(msg.content)
		except ValueError:
			await client.send_message(message.channel, 'Try entering your command again and enter a number when prompted.')
		if playerInput > 5:
			playerInput = 5
		if playerInput < 2:
			await client.send_message(message.channel, "This composition requires at least 2 players.")
			client.close
			return

		supportCounter = 0
		fillCounter = 2
		heroList = []
		mergedList = allAssassinList + allSpecialistList + allWarriorList
		while (supportCounter < 2):
			support = random.choice(allSupportList)
			heroList.append(support)
			supportCounter = supportCounter + 1
		while (fillCounter < playerInput):
			fill = random.choice(mergedList)
			heroList.append(fill)
			mergedList.remove(fill)
			if fill == 'Cho\'Gall':
				fillCounter = fillCounter + 2
				allWarriorList.remove(fill)
			elif fill == 'Cho\'Gall' and counter >= 4:
				heroList.remove('Cho\'Gall')
				fill = random.choice(completeHeroList)
				heroList.append(fill)
				completeHeroList.remove(fill)
			else:
				fillCounter = fillCounter + 1

		em = discord.Embed(title = "Dual Support Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close

	if(message.content.startswith("?comp cheese")):
		counter = 0
		heroList = []
		while(counter < 1):
			cheeseIndex = random.choice(range(len(allCheeseList)))
			cheese = str(allCheeseList[cheeseIndex]).replace("'","").replace('[','').replace(']','').replace('"','')
			cheeseDescription = allCheeseDescriptions[cheeseIndex] 
			heroList.append(str(cheeseDescription).replace('"','').replace('[','').replace(']',''))
			counter = counter + 1

		em = discord.Embed(title = cheese + " Cheese Composition", description='\n'.join(heroList) + '\n\nFor all available commands, type ?comp help.')
		await client.send_message(message.channel, embed=em)
		client.close
	

	if(message.content.startswith("?comp help")):
		em = discord.Embed(title = "HoTS Composition Bot Help", description='?comp random - Random composition from all heroes.\n\n?comp specialist - Random composition from all Specialists.\n\n?comp warrior - Random composition from all Warriors.\n\n?comp support - Random composition from all Supports.\n\n?comp assassin - Random composition from all Assassins.\n\n?comp warcraft - Random composition from all Warcraft heroes.\n\n?comp starcraft - Random composition from all Starcraft heroes.\n\n?comp overwatch - Random composition from all Overwatch heroes.\n\n?comp diablo - Random composition from all Diablo heroes.\n\ncomp melee - Random composition from all melee heroes.\n\n?comp standard - Random composition with 1 warrior, 1 support, and a mix of assassins and specialists. Requires 5 players.\n\n?comp solo support - Random composition with 1 support and a mix of all other heroes. Requires at least 2 players.\n\n?comp dual support - Random composition with 2 supports and a mix of all other heroes. Requires at least 2 players.\n\n?comp cheese - Random cheese composition from set list of compositions. Updated 2/21/18.')
		await client.send_message(message.author, embed=em)
		client.close

client.run("/ DISCORD AUTH HERE /")
