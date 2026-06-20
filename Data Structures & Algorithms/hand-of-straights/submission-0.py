class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        card_dict = defaultdict(int)

        for card in hand:
            card_dict[card] += 1

        
        #we need to keep trying with smallest hands
        n_groups = len(hand)//groupSize
        
        for group in range(n_groups):
            
            smallest_hand = []

            for card in card_dict:
                heapq.heappush(smallest_hand, card)

            if len(smallest_hand) < groupSize:
                    return False

            last_card = heapq.heappop(smallest_hand)
            card_dict[last_card] -= 1

            if card_dict[last_card] == 0:
                del card_dict[last_card]

            for item in range(1, groupSize):                
                smallest_card = heapq.heappop(smallest_hand)

                card_dict[smallest_card] -= 1

                if card_dict[smallest_card] == 0:
                    del card_dict[smallest_card]

                diff = smallest_card - last_card

                if diff != 1:
                    return False

                last_card = smallest_card

        return True if len(card_dict) == 0 else False

        
