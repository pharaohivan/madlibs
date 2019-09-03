import random

def randomize(speech):
    random.shuffle(speech)

print("\n\n\n\n\u001b[31mWelcome to Madlibs, a phrasal template word game where I, the programmer, prompt")

print("\u001b[31myou for a list of words to subsitute for blanks in a story, before reading")

print("\u001b[31mthe comical and often nonsensical story aloud.")

print("\n\n\n\n\u001b[33mPress enter to continue")
welcome = input()

print("\n\n\n\n\u001b[36mLoading\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nPress Enter")
loading = input()

print("\n\n\n\n\u001b[31mInstructions: Press enter after every word you enter.")

print("\n\n\n\n\u001b[32mEnter 3 adjectives")
adjective = [input(),input(),input()]
randomize(adjective)

print("\n\n\n\n\u001b[33mEnter 6 nouns")
noun = [input(),input(),input(),input(),input(),input()]
randomize(noun)

print("\n\n\n\n\u001b[34mEnter 2 verbs")
verb = [input(),input()]
randomize(verb)

pronoun = input("\n\n\n\n\u001b[35mEnter a pronoun \n")

print("\n\n\n\n\n\n\n\n\u001b[36mI was walking " + adjective[0] + " when I was beamed to a " + noun[0] + ".")
print("\u001b[31mThat's when I started to " + verb[0] + ", I was terrified,")
print("\u001b[32myou could see the " + noun[1] + " coming right after me.")
print("\u001b[33mNot only didn't I expect to see the {}, I didn't expect to see all of the {}s".format(noun[2], noun[3]))
print("\u001b[34mthat came along with them. Back on earth I didn't have any " + noun[4] + "s.")
print("\u001b[35mHere, in this place, there were " + noun[4] + "'s everywhere. I couldn't help but " + verb[1] + ".")
print("\u001b[36mWhat even happened? Suddenly, the {} {}s turned into {} {}s".format(adjective[1], verb[1], adjective[2], noun[5]))
print("\u001b[31mand I was home again. Thank goodness.\n\n\n\n\n\n")
