'''
Basic example of inheritance

author: @abekim
'''
class Animal(object):
    ''' Base Animal class '''
    def __init__(self, t, noise):
        ''' 
            t = type of animal 
            noise = noise it makes
        '''
        self.t = t
        self.noise = noise

    def __str__(self):
        return 'A %s that makes %s noise' % (self.t, self.noise)

    def get_type(self):
        ''' returns the type of animal '''
        return self.t

    def make_noise(self):
        ''' returns the noise it makes '''
        return self.noise

# Cat inherits from the Animal class!
class Cat(Animal):
    def __init__(self, name, noise="meow"):
        self.name = name
        # this is what inheritance means
        super(Cat, self).__init__("cat", noise)

    def meow(self):
        ''' cats meow '''
        return self.make_noise()

# Now a Dog class
class Dog(Animal):
    def __init__(self, name, noise="woof"):
        self.name = name
        super(Dog, self).__init__("dog", noise)
    
    def bark(self):
        ''' dogs bark '''
        return self.make_noise()

# Can you write a Bear class that roars and Wolf that howls?
class Bear(Animal):
    def __init__(self, name, noise="ROAR"):
        self.name = name
        super(Bear, self).__init__("bear", noise)

    def roar(self):
        return self.make_noise()

class Wolf(Animal):
    def __init__(self, name, noise="Awooooooo"):
        self.name = name
        super(Wolf, self).__init__("wolf", noise)

    def howl(self):
        return self.make_noise()

if __name__ == '__main__':
    cat = Cat("cynthia")
    # look, we can call methods from the Animal class
    print cat.get_type()
    print cat.meow()

    dog = Dog("ponyo")
    # what happens if we do this?
    print dog
    print dog.bark()
    # if we try this next line, it'll break!
    # print dog.meow()

    bear = Bear("Pooh", "plush")
    print bear
    print bear.roar()

    wolf = Wolf("cool_wolf_name")
    print wolf.howl()
