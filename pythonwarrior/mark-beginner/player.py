class Player(object):
    minhealth = 16
    def play_turn(self, warrior):
        self.health = warrior.health()
        if warrior.feel().is_enemy():
            warrior.attack_()
        elif warrior.health() < self.health:
            warrior.rest_()
        else:
            warrior.walk_()
        self.health = warrior.health()
