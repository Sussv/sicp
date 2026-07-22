test = {
  'name': 'Question 1',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class Car(object):
          ...     num_wheels = 4
          ...     gas = 30
          ...     headlights = 2
          ...     size = 'Tiny'
          ...     def __init__(self, make, model):
          ...          self.make = make
          ...          self.model = model
          ...          self.color = 'No color yet. You need to paint me.'
          ...          self.wheels = Car.num_wheels
          ...          self.gas = Car.gas
          ...     def paint(self, color):
          ...          self.color = color
          ...          return self.make + ' ' + self.model + ' is now ' + color
          ...     def drive(self):
          ...          if self.wheels < Car.num_wheels or self.gas <= 0:
          ...               return 'Cannot drive!'
          ...          self.gas -= 10
          ...          return self.make + ' ' + self.model + ' goes vroom!'
          ...     def pop_tire(self):
          ...          if self.wheels > 0:
          ...               self.wheels -= 1
          ...     def fill_gas(self):
          ...          self.gas += 20
          ...          return 'Gas level: ' + str(self.gas)
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.model
          'Model S'
          >>> deneros_car.gas = 10
          >>> deneros_car.drive()
          'Tesla Model S goes vroom!'
          >>> deneros_car.drive()
          'Cannot drive!'
          >>> deneros_car.fill_gas()
          'Gas level: 20'
          >>> deneros_car.gas
          20
          >>> Car.gas
          30
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.wheels = 2
          >>> deneros_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> deneros_car.drive()
          'Cannot drive!'
          >>> Car.drive()
          Error
          >>> Car.drive(deneros_car)
          'Cannot drive!'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> class MonsterTruck(Car):
          ...     size = 'Monster'
          ...     def rev(self):
          ...          print('Vroom! This Monster Truck is huge!')
          ...     def drive(self):
          ...          self.rev()
          ...          return Car.drive(self)
          >>> deneros_car = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.drive()
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(deneros_car)
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(deneros_car)
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(deneros_car)
          Error
          """,
          'hidden': False,
          'locked': False,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
