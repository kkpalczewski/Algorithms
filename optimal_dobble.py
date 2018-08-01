import operator

class Deck():
    def __init__(self, num_symbol):
        self.num_symbol = num_symbol

        self.new_card = 0 # card which would be created next
        self.new_symbol = 0 # symbol which would be created next

        self.deck = dict()
        self.all_symbols = dict()
        self.all_sorted_symbols = []

    def create_new_card(self):
        """
        Creates new card
        :return:
        """
        self.deck[self.new_card] = dict()
        self.new_card += 1
        return self.new_card - 1

    def create_new_symbol(self, card):
        """
        Create new symbol
        :param card: card which would have new symbol appended
        :return:
        """
        self.all_symbols[self.new_symbol] = 0
        self.all_sorted_symbols = sorted(self.all_symbols.items(), key = operator.itemgetter(1))
        self.deck[card][self.new_symbol] = []
        self.new_symbol += 1
        return self.new_symbol - 1

    def append_symbol(self, card, symbol):
        """
        Append existing symbol which is least common
        :param card:
        :param symbol:
        :return:
        """
        set_union = set().union(*self.deck[card].values())
        for k in self.deck.keys():
            if k != card and k not in set_union and symbol in self.deck[k].keys():
                self.deck[card][symbol] = []
                self.deck[card][symbol].append(k)
                self.deck[k][symbol].append(card)
                self.all_symbols[symbol] += 1
                self.all_sorted_symbols = sorted(self.all_symbols.items(), key=operator.itemgetter(1))

    def check_constraints(self):
        """
        Check if a dack is well-prepared
        :return:
        """
        for x in self.deck.keys():
            if len(self.deck[x].keys()) != self.num_symbol:
                return False
            for y in self.deck[x].values():
                if y == []:
                    return False
        return True

    def create_full_deck(self):
        new_card = self.create_new_card()
        for symbol in self.all_sorted_symbols:
            self.append_symbol(new_card,symbol[0])
            if len(self.deck[new_card].keys()) == self.num_symbol:
                break
        while len(self.deck[new_card].keys()) != self.num_symbol:
            self.create_new_symbol(new_card)

        for y in self.deck[new_card].values():
            if y == []:
                return self.create_full_deck()

        return deck.deck

if __name__ == '__main__':
    n = 8
    deck = Deck(n)
    new_deck = deck.create_full_deck()
    print(new_deck)