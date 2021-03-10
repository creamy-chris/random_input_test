from random import randint
banned_words = {
	"anal", "anus", "arse", "ass", "ballsack", "balls", "bastard", "bitch", "biatch",
	"bloody", "blowjob", "blow job", "bollock", "bollok", "boner", "boob", "bugger",
	"bum", "butt", "buttplug", "clitoris", "cock", "coon", "crap", "cunt", "damn",
	"dick", "dildo", "dyke", "fag", "feck", "fellate", "fellatio", "felching",
	"fuck", "fudgepacker", "fudge packer", "flange", "Goddamn",
	"hell", "homo", "jerk", "jizz", "knobend", "knob end", "labia", "lmao", "lmfao",
	"muff", "nigger", "nigga", "omg", "penis", "piss", "poop", "prick", "pube", "pussy",
	"queer", "scrotum", "sex", "shit", "s hit", "sh1t", "slut", "smegma", "spunk", "tit",
	"tosser", "turd", "twat", "vagina", "wank", "whore", "wtf"
}
def my_fuction() -> int:
	user_gave = (input("give me a random number:"))
	if user_gave == 'stop':
		return 0
	try:
		negative = 1
		a_random = int(user_gave)
		if a_random == 0:
			print ("0, nothing to see here, bye!")
			return 0
		if a_random < 0:
			negative = -1
		a_random *= negative
		# check if the number is 1 or 2 in order to print 1st or 2nd
		suffix = ""
		suffixes = ["st","nd","rd","th"]
		if a_random < 4:
			suffix = suffixes[a_random-1]
		else:
			suffix = suffixes[3]
		print("hello world, " +("negative, " if negative == -1 else "") + str(a_random) + suffix + " dude!" )
	except ValueError:
		try:
			a_random = float(user_gave)
			print("hello world, " + str(a_random) + ", you,"+(" negative," if a_random < 0 else " positive,") + " fractional, dude!" )
		except ValueError:
			if any(word in user_gave for word in banned_words):
				print ("wow, wow, wow, calm your tities! ")
				for word in banned_words:
					if word in user_gave:
						print ("'"+word+"' detected!")
			else:
				print ("so, you what you want to say is: '" + user_gave + "'....\n\nsure, what ever!")
	return 1
total = randint(100,4000)
for i in range(total):
	print("("+str(total-i) + " to go)")
	print("so, once again...\n")
	if my_fuction() == 0:
		exit(0)