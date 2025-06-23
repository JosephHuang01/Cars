class Person():
    def __init__(self, name):
        self.name = name
        self.sentence = ""
        self.has_a_car = "No"
    
    def speak(self, sentence):
        self.sentence = sentence
        return self.sentence

class Passenger(Person):
    def __init__(self, name):
        super().__init__(name)        
    
    def speak(self, sentence):
        my_sentence = "I am a passenger."
        super_sentence =  super().speak(sentence)
        return my_sentence + " " + super_sentence

class Driver(Person):
    def __init__(self, name):
        super().__init__(name)
        self.has_a_car = "Yes"
    
    def speak(self, sentence):
        my_sentence = "I am a driver."
        super_sentence = super().speak(sentence)
        return super_sentence +  " " + my_sentence