import random
from art import logo
cards = {
  1: 11,
  2: 2,
  3: 3,
  4: 4,
  5: 5,
  6: 6,
  7: 7,
  8: 8,
  9: 9,
  10: 10,
  11: 10,
  12: 10,
  13: 10
}

def calc_score(cards):
  score = 0
  for card in cards:
    score += card
  return score

def deal_computer_hand(firstcard, your_total):
  comp_total = 0
  comp_cards = [firstcard]
  while comp_total < your_total:
    comp_cards.append(cards[random.randint(1,13)])
    comp_total = calc_score(comp_cards)
  return [comp_cards, comp_total]

def compare_score(your_score, comp_score):
  if your_score > comp_score or comp_score > 21:
    print("You win!!!")
  else:
    print("Womp womp, you lose!!")

def play_blackjack():
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  while play == 'y':
    your_cards = []
    print(logo)
    your_cards.append(cards[random.randint(1,13)])
    your_cards.append(cards[random.randint(1,13)])
    computers_1st_card = cards[random.randint(1,13)]
    your_total = calc_score(your_cards)
    print(f"Your cards: {your_cards}, current score: {your_total}")
    print(f"Computer's first card: {computers_1st_card}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    ##Continue playing and add another card
    while another_card == 'y':
      your_cards.append(cards[random.randint(1,13)])
      your_total = calc_score(your_cards)
      print(f"Your cards: {your_cards}, current score: {your_total}")
      print(f"Computer's first card: {computers_1st_card}")
      ##If total is over 21, you lose
      if your_total > 21:
        print(f"Your final hand: {your_cards}, final score: {your_total}")
        comp_cards = deal_computer_hand(computers_1st_card, your_total)[0]
        comp_total = deal_computer_hand(computers_1st_card, your_total)[1]
        print(f"Computer's final hand: {comp_cards}, final score: {comp_total}")
        print("You went over. You lose!!")
        play_blackjack()
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    ## 'N' was selected to pass another card
    print(f"Your final hand: {your_cards}, final score: {your_total}")
    comp_cards = deal_computer_hand(computers_1st_card, your_total)[0]
    comp_total = deal_computer_hand(computers_1st_card, your_total)[1]
    print(f"Computer's final hand: {comp_cards}, final score: {comp_total}")
    compare_score(your_total, comp_total)
    play_blackjack()

play_blackjack()
