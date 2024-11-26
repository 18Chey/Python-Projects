from random import shuffle


class Card:
    def __init__(self, rank: int | str, suit: int | str) -> None:
        """
        Initialises the card.
        :param rank: Rank of card 1-13 and 'Ace', 'Jack', 'Queen', 'King'.
        :param suit: Suit of card 1-4 or 'Clubs', 'Diamonds', 'Hearts', 'Spades'.
        """
        self.rank = rank
        self.suit = suit

        # Assign values based on rank
        if self.rank in [1, "Ace"]:
            self.value = 1
            self.rank = "Ace"
        elif self.rank in [11, "Jack"]:
            self.value = 11
            self.rank = "Jack"
        elif self.rank in [12, "Queen"]:
            self.value = 12
            self.rank = "Queen"
        elif self.rank in [13, "King"]:
            self.value = 13
            self.rank = "King"
        else:
            self.value = self.rank

        # Converts int suit to string
        suits = ("Clubs", "Diamonds", "Hearts", "Spades")
        if type(self.suit) == int:
            self.suit = suits[self.suit - 1]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


class BlackjackCard(Card):
    def __init__(self, rank: int | str, suit: int | str) -> None:
        super().__init__(rank, suit)

        # Changes rank values in accordance to blackjack rules
        if self.rank in ["Jack", "Queen", "King"]:
            self.value = 10
        elif self.rank == "Ace":
            self.value = 11
        else:
            self.value = int(rank)


class Deck:
    def __init__(self, blackjack: bool = False) -> None:
        """
        Initialises the deck.
        :param blackjack: If True, cards added will be BlackjackCard objects.
        """
        self.cards = []
        self.blackjack = blackjack

    def add_card(self, rank: int | str, suit: str) -> None:
        """
        Adds a card to the deck. Adds a blackjack card if blackjack attribute is True.
        :param rank: Rank of card 1-13 and 'Ace', 'Jack', 'Queen', 'King'.
        :param suit: Suit of card 1-4 or 'Clubs', 'Diamonds', 'Hearts', 'Spades'.
        """
        if self.blackjack:
            self.cards.append(BlackjackCard(rank, suit))
        else:
            self.cards.append(Card(rank, suit))

    def add_full_deck(self, number: int = 1) -> None:
        """
        Adds 'number' full decks of 52 cards.
        """
        for times in range(number):
            for suit in range(1, 5):
                for rank in range(1, 14):
                    self.add_card(rank, suit)

    def add_cards(self, cards: list[object]):
        """
        Add a list of cards to the deck
        """
        self.cards.extend(cards)

    def shuffle(self) -> None:
        """
        Randomises order of deck.
        """
        shuffle(self.cards)

    def take(self, number: int) -> list[object]:
        """
        Removes the top 'number' cards and returns them in a list
        """
        taken = self.cards[:number]
        self.cards = self.cards[number:]
        return taken

    def clear(self) -> None:
        self.cards = []


def play_again():
    play = input("Play again? Y/N: ")
    if play.lower() == "n":
        exit()


def blackjack() -> None:
    pack = Deck(blackjack=True)
    pack.add_full_deck(6)
    pack.shuffle()
    dealer_hand = Deck(blackjack=True)
    player_hand = Deck(blackjack=True)
    while True:
        choice = None
        player_total = 0
        dealer_hand.clear()
        player_hand.clear()
        dealer_hand.add_cards(pack.take(2))
        player_hand.add_cards(pack.take(2))

        while choice != "stand" and player_total < 21:
            player_total = sum(card.value for card in player_hand.cards)
            dealer_total = sum(card.value for card in dealer_hand.cards)

            print(
                f"\nDealers hand: {str(dealer_hand.cards[0])}, ?    Total: {dealer_hand.cards[0].value}\n"
            )
            print(
                f"Players hand: {[str(card) for card in player_hand.cards]}    Total: {player_total}\n"
            )
            if player_total < 21:
                choice = input("Hit or stand?: ").lower()
                if choice == "hit":
                    player_hand.add_cards(pack.take(1))

        if player_total > 21:
            print("BUST!")
            play_again()

        else:
            print(
                f"\nDealers hand: {[str(card) for card in dealer_hand.cards]}    Total: {dealer_total}\n"
            )
            print(
                f"Players hand: {[str(card) for card in player_hand.cards]}    Total: {player_total}\n"
            )
            if (21 - player_total) < (21 - dealer_total):
                print("WIN")
                play_again()
            elif (21 - player_total) == (21 - dealer_total):
                print("DRAW")
                play_again()
            else:
                print("LOSE")
                play_again()


def main() -> None:
    blackjack()


if __name__ == "__main__":
    main()
