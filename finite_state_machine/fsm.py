"""FSM of my day"""
import random


def prime(fn):
    """Send value to the yield statement """
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper


class DayFSM:
    """Class of fsm of day"""
    def __init__(self):
        self.work = self._create_work()
        self.sleep = self._create_sleep()
        self.eat = self._create_eat()
        self.think = self._create_think()
        self.drink_beer = self._create_drink_beer()
        self.fight = self._create_fight()

        self.current_state = self.work
        self._dead = False

    def send(self, digit):
        """Send hour to current state"""
        self.current_state.send(digit)

    def alive(self):
        """whether I'm alive"""
        return not self._dead

    @prime
    def _create_work(self):
        """State of work"""
        description = ['beautiful!', 'terrible', 'boring']
        while True:
            hour = yield
            randomm = random.random()
            if randomm * hour < 0.8:
                self.current_state = self.work
                print('Ohh, I love dskr so much...')
            elif hour > 8 and description:
                word = random.choice(description)
                description.remove(word)
                self.current_state = self.work
                print(f'new dskr laba is just {word}')
            elif hour in range(19, 21):
                print('time to eat')
                self.current_state = self.eat
            elif hour > 8:
                print("eee, nah. Let's have fun")
                if randomm > 0.35:
                    self.current_state = self.drink_beer
                else:
                    self.current_state = self.fight
            else:
                self.current_state = self.sleep
                print('hallelujah')
                print('zzz.....')

    @prime
    def _create_sleep(self):
        """State of sleep"""
        while True:
            hour = yield
            randomm = random.random()
            if hour == 4:
                self.current_state = self.think
                print('what...oh, here we go again')
            elif hour == 15:
                self._dead = True
                print('OH NOOO (died because missed exam)')
            elif randomm >= 0.75 and hour > 6:
                self.current_state = self.eat
                print(f'ohh...REALLY? {hour} oclock? I`m hungry')
            else:
                self.current_state = self.sleep
                print('zzz.....')

    @prime
    def _create_eat(self):
        """State of eat"""
        while True:
            yield
            randomm = random.random()
            if randomm > 0.85:
                self._dead = True
                print("oh no, the only thing in my fridge is a cockroach (died of starvation)")
            else:
                print("yummy, delicious bread! I must work")
                self.current_state = self.work

    @prime
    def _create_think(self):
        """State of strange thoughts"""
        phrases = ['My navel is my old mouth...',
                   'Atoms are 99% nothing which means I am 99% nothing...',
                   'Most men receive flowers for the first time at their own funeral...']
        while True:
            yield
            if phrases:
                phrase = random.choice(phrases)
                phrases.remove(phrase)
                print(phrase)
                self.current_state = self.sleep
            else:
                print('I think to much (committed suicide)')
                self._dead = True

    @prime
    def _create_drink_beer(self):
        """State of drinking beer"""
        beers = ['Lvivske 1715', 'Bud', 'Tuborg']
        while True:
            hour = yield
            print(f'{hour} oclock - time for beer')
            if beers:
                beer = random.choice(beers)
                beers.remove(beer)
                print(f'awesome {beer}, but I need to keep working')
                self.current_state = self.work
            else:
                print('oh, beer ran out (died of grief)')
                self._dead = True

    @prime
    def _create_fight(self):
        """State of fighting with brother"""
        while True:
            yield
            randomm = random.random()
            print('hello my little brother')
            print('*smashhhh')
            if randomm > 0.8:
                print('oh, he killed me')
                self._dead = True
            elif randomm < 0.2:
                print('oh, I killed him')
                self.current_state = self.think
            else:
                print("hah, it was funny, but I need to keep working")
                self.current_state = self.work


def grep_regex(hours):
    """Send current hour to FSM"""
    fsm = DayFSM()
    for hour in hours:
        print('\n')
        print('Hour: ', hour)
        fsm.send(hour)
        if not fsm.alive():
            print("I didn't even live to the end of the day(")
            break
        if hour == 24:
            print('Hoorey! I live to the end of the day)')


if __name__ == '__main__':
    day = list(num for num in range(25))
    grep_regex(day)
