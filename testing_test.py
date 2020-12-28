class CardGame():

    def __init__(self, card):
        self.card = card

# attributes should be defined in parenthesis, at least "self" and "card";

    def check_for_ace(self, card):
        if card.value == 1:
            return True
        # below, collon missing after "else";
        else:
            return False
    

    # typo below in "dif", comma missing between card1 and card2;
    def highest_card(self, card1, card2):
    # the following four lines should be indented;
        if card1.value > card2.value:
            # below, should be "card1";
            return card1
        else:
            return card2
    


    def cards_total(self, cards):
    # below, total is undefined;
        total = 0
        for card in cards:
            total += card.value
            # below, could be either an f-string, or "total" should be "{total}"; indentation not needed;
            return "You have a total of {total}"
