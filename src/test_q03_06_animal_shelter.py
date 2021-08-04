from collections import namedtuple
from simplequeue import Queue

class Animal():
    def __init__(self, type, id):
        self._type = type
        self._id = id

    def __str__(self):
        return f'{self._type}-{self._id}'

class Dog(Animal):
    def __init__(self, id):
        super().__init__('dog', id)

class Cat(Animal):
    def __init__(self, id):
        super().__init__('cat', id)

Slot = namedtuple('Slot', ['animal', 'order'])
class AnimalShelter():

    def __init__(self):
        self._order_count = 0
        self._queue_dog = Queue()
        self._queue_cat = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self._queue_dog.add(Slot(animal, self._order_count))
        elif isinstance(animal, Cat):
            self._queue_cat.add(Slot(animal, self._order_count))
        self._order_count += 1

    def dequeue_dog(self):
        return self._queue_dog.remove().animal

    def dequeue_cat(self):
        return self._queue_cat.remove().animal

    def _get_queue_oldest_order(self, q):
        return None if q.is_empty() else q.peek().order

    def dequeue_any(self):
        order_cat = self._get_queue_oldest_order(self._queue_cat)
        order_dog = self._get_queue_oldest_order(self._queue_dog)
        if order_cat==None and order_dog==None:
            return None
        elif order_cat==None or (order_dog!=None and order_dog < order_cat):
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()


def test_func():
    shelter = AnimalShelter()
    q = [Dog(1), Cat(1), Dog(2), Dog(3), Cat(4)]
    q_all = ['dog-1','cat-1','dog-2','dog-3','cat-4']
    q_dog = ['dog-1','dog-2','dog-3']
    q_cat = ['cat-1','cat-4']

    # TestCase: dequeue_any()
    for i in q:
        shelter.enqueue(i)

    for s in q_all:
        assert str(shelter.dequeue_any()) == s

    # TestCase: dequeue_cat() and dequeue_dog()
    for i in q:
        shelter.enqueue(i)

    for s in q_cat:
        assert str(shelter.dequeue_cat()) == s
    for s in q_dog:
        assert str(shelter.dequeue_dog()) == s


