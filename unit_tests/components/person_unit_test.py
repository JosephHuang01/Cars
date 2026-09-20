import unittest
from components.person import Person, Driver, Passenger

class TestPersonCase(unittest.TestCase):
    def test_is_driver_1(self):
        person_is_driver = Driver("John")
        self.assertEqual(person_is_driver.name, "John")
        sentence_input = "How can I help you?"
        sentence_output = person_is_driver.speak(sentence_input)        
        self.assertEqual(sentence_output, sentence_input + " " + "I am a driver.")
        self.assertEqual(person_is_driver.has_a_car, "Yes")
    
    def test_is_passenger_1(self):

        person_is_passenger = Passenger("Amy")
        self.assertEqual(person_is_passenger.name, "Amy")
        sentence_input = "I need a ride to the airport."
        sentence_output = person_is_passenger.speak(sentence_input)
        self.assertEqual(sentence_output, "I am a passenger. I need a ride to the airport.")
        self.assertEqual(person_is_passenger.has_a_car, "No")
    
    def test_is_passenger_2(self):
        person_is_passenger = Passenger("Amy")
        self.assertEqual(person_is_passenger.name, "Amy")
        sentence_input = "Hi!"
        sentence_output = person_is_passenger.speak(sentence_input)
        self.assertEqual(sentence_output, "I am a passenger. Hi!")
        self.assertEqual(person_is_passenger.has_a_car, "No")

    def test_is_driver_2(self):
        person_is_driver = Driver("John")
        self.assertEqual(person_is_driver.name, "John")
        sentence_input = "Hello!"
        sentence_output = person_is_driver.speak(sentence_input)
        self.assertEqual(sentence_output, sentence_input+ " " + "I am a driver.")
        self.assertEqual(person_is_driver.has_a_car, "Yes")
    
    def test_is_passenger_3(self):
        person_is_passenger = Passenger("Amy")
        self.assertEqual(person_is_passenger.name, "Amy")
        sentence_input = "Can you help me?"
        sentence_output = person_is_passenger.speak(sentence_input)
        self.assertEqual(sentence_output, "I am a passenger. Can you help me?")
        self.assertEqual(person_is_passenger.has_a_car, "No")
    
    def test_is_driver_3(self):
        person_is_driver = Driver("John")
        self.assertEqual(person_is_driver.name, "John")
        sentence_input = "What do you need?"
        sentence_output = person_is_driver.speak(sentence_input)
        self.assertEqual(sentence_output, sentence_input + " " + "I am a driver.")
        self.assertEqual(person_is_driver.has_a_car, "Yes")
    
    # def test_is_person(self):
    #     person_is_person = Person("Clark")
    #     self.assertEqual(person_is_person.name, "Clark")
    #     sentence = person_is_person.speak("I am a bystander. ")
    #     self.assertEqual(sentence + person_is_person.speak("I cannot help you."), "I am a bystander. I cannot help you.")
    #     self.assertEqual(person_is_person.has_a_car, "No")

unittest.main()