import random

# tarot card types to be drawn
tarot = {
    1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor",
    5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength",
    9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man",
    13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower",
    17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement",
    21: "The World", 22: "The Fool"
}

# tarot descriptions by types
card_descriptions = {
    "The Magician": "Represents willpower, desire, creation, and manifestation.",
    "The High Priestess": "Symbolizes intuition, unconscious knowledge, and mystery.",
    "The Empress": "Stands for fertility, nurturing, and abundance.",
    "The Emperor": "Represents authority, structure, and control.",
    "The Hierophant": "Symbolizes tradition, conformity, and moral integrity.",
    "The Lovers": "Stands for love, harmony, and partnership.",
    "The Chariot": "Represents determination, direction, and control.",
    "Strength": "Symbolizes courage, patience, and inner strength.",
    "The Hermit": "Stands for introspection, solitude, and inner guidance.",
    "Wheel of Fortune": "Represents cycles, change, and destiny.",
    "Justice": "Symbolizes fairness, truth, and the law.",
    "The Hanged Man": "Stands for surrender, letting go, and sacrifice.",
    "Death": "Represents endings, change, and transformation.",
    "Temperance": "Symbolizes balance, moderation, and patience.",
    "The Devil": "Represents temptation, addiction, and materialism.",
    "The Tower": "Stands for sudden upheaval, chaos, and revelation.",
    "The Star": "Symbolizes hope, inspiration, and serenity.",
    "The Moon": "Represents illusion, intuition, and imagination.",
    "The Sun": "Stands for positivity, success, and vitality.",
    "Judgement": "Symbolizes reflection, reckoning, and awakening.",
    "The World": "Represents accomplishment, completion, and celebration.",
    "The Fool": "Symbolizes new beginnings, innocence, and spontaneity."
}

spread = {}

# randomly select a past, present, and future card, no duplicates
selected_cards = random.sample(list(tarot.keys()), 3)

spread["past"] = tarot.pop(selected_cards[0])
spread["present"] = tarot.pop(selected_cards[1])
spread["future"] = tarot.pop(selected_cards[2])

for key, value in spread.items():
    print("Your {} is the {} card.".format(key, value))
    if value in card_descriptions:
        print("Interpretation: {}\n".format(card_descriptions[value]))
