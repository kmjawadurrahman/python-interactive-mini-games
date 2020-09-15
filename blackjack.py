# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))

        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards = list()

    def __str__(self):
        return "Hand: " + " ".join([str(m) for m in self.cards])

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES.get(rank)
            if rank == "A":
                aces += 1
        value1 = value + (10 * aces) - aces
        if value1 <= 21:
            value = value1
        return value

    def draw(self, canvas, pos):
        i = 0
        for card in self.cards:
            card.draw(canvas, (pos[0] + (72 * i), pos[1]))
            i += 1


# define deck class
class Deck:
    def __init__(self):
        self.cards = list()
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        return "Deck: " + " ".join([str(i) for i in self.cards])


# define event handlers for buttons
def deal():
    global deck, player, dealer, outcome, in_play, score
    if in_play:
        score -= 1
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    for i in range(2):
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())

    in_play = True
    outcome = "Hit or Stand?"


def hit():
    global outcome, in_play, score
    if not in_play:
        return
    player.add_card(deck.deal_card())
    outcome = "Hit or Stand?"
    if player.get_value() > 21:
        outcome = "Player Busted. New deal?"
        in_play = False
        score -= 1


def stand():
    global outcome, in_play, score
    if not in_play:
        return

    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
    if dealer.get_value() > 21:
        score += 1
        outcome = "Dealer Busted! New deal?"
    elif player.get_value() > dealer.get_value():
        score += 1
        outcome = "You win! New deal?"
    else:
        score -= 1
        outcome = "You lose. New deal?"
    in_play = False


# draw handler
def draw(canvas):

    text_width = frame.get_canvas_textwidth(outcome, 18)

    canvas.draw_text(outcome, (125 - text_width / 2, 85), 18, "White")

    canvas.draw_text('Blackjack', (290, 80), 50, "Red")

    canvas.draw_text(str(score), (163, 350), 18, "White")

    dealer.draw(canvas, (40, 112))

    player.draw(canvas, (40, 212))

    if in_play:
        canvas.draw_image(card_back, [CARD_CENTER[0],CARD_CENTER[1]], CARD_SIZE, (76, 160), CARD_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deck = Deck()
deck.shuffle()
player = Hand()
dealer = Hand()
deal()
frame.start()

# remember to review the gradic rubric
