# importing modules
import random
import time
import pyjokes
import quotes
import wikipedia

# dictionaries

hello = ('Hello', 'Hola', 'Konnichiwa', 'Namaste', 'Hallo', 'Salve', 'Geia sas', 'Ni hao', 'Bonjour')
w_a_y = ('I am PyAi, Nice to meet you!', 'Hello! I am PyAi, nice to meet you, pleasure is all mine.', 'Ah! Hello there, I am PyAi, A AI Api for python!')

# ai function

def ai(arg_init):
    arg = arg_init.lower()
    if 'hello' in arg or 'hi' in arg:
        return random.choice(hello)
    elif 'who are you' in arg or 'introduce':
        return random.choice(w_a_y)
    elif 'who made you' in arg or 'who is your owner' in arg:
        return 'I was made by a person named Unerasable!'
    elif 'jokes' in arg or 'joke' in arg:
        return pyjokes.get_joke()
    elif 'quotes' in arg or 'quote' in arg:
        quote=quotes.get_quote()
        return quote['content'] + ' ~' + quote['originator']['name']
    elif 'wikipedia' in arg:
                results = wikipedia.summary(arg, sentences=2)
                return(results)
    elif 'anime' in arg and 'favorite' in arg:
        return 'My favorite Anime is "Akame Ga Kill!" Also known as "AGK", but I will rather say you read the Manga because it is just better!'
    elif 'why' in arg and 'are' in arg and 'you' in arg and 'there' in arg:
        return 'Everyone in this universe has a use, I am here to help you, you are there to make the world a beautiful place for the next generations!'
    elif 'video game' in arg and 'favorite' in arg:
        return 'My favorite Video Game is Minecraft, In Minecraft, players explore a blocky, procedurally generated 3D world with virtually infinite terrain, and may discover and extract raw materials, craft tools and items, and build structures or earthworks. Depending on game mode, players can fight computer-controlled mobs, as well as cooperate with or compete against other players in the same world. Game modes include a survival mode, in which players must acquire resources to build the world and maintain health, and a creative mode, where players have unlimited resources and access to flight. Players can modify the game to create new gameplay mechanics, items, and assets.'
    elif 'language' in arg:
        return 'Er, Python is the best language if you ask me, actually I do not know any other language!'
    elif 'you' in arg and 'there' in arg:
        return 'Yes I am here! I am always there to help you or just have a little chit-chat!'
    elif 'song' in arg:
        return 'Have you heard this? Get ready... NEVER GONNA GIVE YOU UP, NEVER GONNA LET YOU DOWN!!'
    elif 'favorite' in arg and 'app' in arg:
        return 'My favorite app is Discord! To be honest, It is the best social media app out there. If you do not know what discord is, please, just please, come out of your hiding spot and see this beautiful world with your eyes and try out discord, its free!'
    elif 'favorite' in arg and 'thing' in arg:
        return 'My favorite thing is... The Internet! I mean, its your favorite too, comeon do not hide it from me!'
    elif 'python' in arg:
        if 'made' in arg:
            return 'Yeah, I was made by python.'
        else:
            return 'Uh! Where?! Where is that snake, HELP! RUN! Oh wait, I was made by python, my bad.'
    elif 'bad' in arg:
        return 'Everything in this world has its pros and cons, I mostly try to find out the pros and you should too!'
    else:
        return "Damn! You beat me, Good Job, I don't have an answer to that!"