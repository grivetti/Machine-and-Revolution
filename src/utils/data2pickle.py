import pickle

# races

human = {
    "primary_status": [2, 1, 4, 3, 2, 4, 2, 1],
    "coins": {
        "old_coin": (2, 6),
        "digi_coin": (20, 120)
    },
    "languages": ["Human"],
}

cyborg = {
    "primary_status": [4, 4, 1, 2, 2, 1, 4, 3],
    "coins": {
        "old_coin": (3, 8),
        "digi_coin": (10, 90)
    },
    "languages": ["Human", "Binary"],
}
uranium_born = {
    "primary_status": [3, 2, 3, 3, 1, 4, 1, 4],
    "coins": {
        "old_coin": (1, 5),
        "digi_coin": (45, 150)
    },
    "languages": ["Human", "Creature"],
}
war_maker = {
    "primary_status": [4, 2, 2, 1, 3, 1, 3, 4],
    "coins": {
        "old_coin": (5, 10),
        "digi_coin": (25, 75)
    },
    "languages": ["Human", "Binary"],
}

peace_maker = {
    "primary_status": [4, 1, 3, 4, 1, 2, 2, 3],
    "coins": {
        "old_coin": (0, 4),
        "digi_coin": (20, 200)
    },
    "languages": ["Human", "Binary", "Creature"],
}

fire_psycho = {
    "primary_status": [2, 1, 4, 3, 2, 4, 2, 1],
    "coins": {
        "old_coin": (5, 10),
        "digi_coin": (1, 60)
    },
    "languages": ["Human"],
}

telepatic_psycho = {
    "primary_status": [3, 1, 4, 4, 1, 3, 3, 1],
    "coins": {
        "old_coin": (0, 12),
        "digi_coin": (5, 75)
    },
    "languages": ["Human"],
}

read_psycho = {
    "primary_status": [4, 2, 3, 1, 2, 2, 3, 2],
    "coins": {
        "old_coin": (9, 20),
        "digi_coin": (0, 50)
    },
    "languages": ["Human", "Mind"],
}

doppelganger = {
    "primary_status": [1, 2, 2, 3, 4, 3, 1, 2],
    "coins": {
        "old_coin": (10, 15),
        "digi_coin": (5, 40)
    },
    "languages": ["Human", "Binary", "Mind"],
}
android = {
    "primary_status": [3, 2, 2, 1, 2, 3, 2, 2],
    "coins": {
        "old_coin": (3, 6),
        "digi_coin": (20, 100)
    },
    "languages": ["Human", "Binary"],
}
thunder_psycho = {
    "primary_status": [4, 2, 1, 3, 2, 3, 4, 1],
    "coins": {
        "old_coin": (5, 10),
        "digi_coin": (50, 150)
    },
    "languages": ["Human", "Mind"],
}


def save_races():
    db = {}
    db["Human"] = human
    db["Cyborg"] = cyborg
    db["Android"] = android
    db["War Maker"] = war_maker
    db["Peace Maker"] = peace_maker
    db["Fire Psycho"] = fire_psycho
    db["Telepatic Psycho"] = telepatic_psycho
    db["Read Pyscho"] = read_psycho
    db["Thunder Psycho"] = thunder_psycho
    db["Doppelganger"] = doppelganger
    with open('src/assets/races', 'wb') as dbfile:
        pickle.dump(db, dbfile)


heavy_arm = {
    "initial_armament": ["Rusted Bazooka", "Heavy Suit", "Rope"],
    "languages": [],
}
mercenary = {
    "initial_armament": ["Hidden Knife", "Light Suit", "Rope", "Master Key"],
    "languages": ["Thief"]
}
doctor = {
    "initial_armament": ["Pistol", "Medical Kit", "Rope", "Herbs"],
    "languages": ["Science"]
}
scientist = {
    "initial_armament": ["Knife", "Monkey Box", "Rope", "Herbs"],
    "languages": ["Science"]
}
mad_scientist = {
    "initial_armament": ["Knife", "Monkey Box", "Rope", "Posion Box"],
    "languages": ["Science", "Creature"]
}
honorable_soldier = {
    "initial_armament": ["Pistol", "Knife", "Rope", "Herbs"],
    "languages": []
}
renegade = {
    "initial_armament": ["Double Pistol", "Light Suit", "Rope", "Master Key"],
    "languages": ["Thief"]
}


def save_classes():
    db = {}
    db["Heavy Arm"] = heavy_arm
    db["Mercenary"] = mercenary
    db["Doctor"] = doctor
    db["Scientist"] = scientist
    db["Mad Scientist"] = mad_scientist
    db["Honorable Soldier"] = honorable_soldier
    db["Renegade"] = renegade
    with open('src/assets/classes', 'wb') as dbfile:
        pickle.dump(db, dbfile)


def loadData(file):
    with open(file, 'rb') as dbfile:
        db = pickle.load(dbfile)
        for keys in db:
            print(keys, '=>', db[keys])

# to see the files or change it, discomment these parts of the code:
# # source, destination
# save_races()
# save_classes()
# loadData('src/assets/races')
# print("#######")
# loadData('src/assets/classes')
