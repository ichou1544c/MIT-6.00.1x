#!/usr/bin/env python


class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + stuff

if __name__=="__main__":
    e = Person('eric')
    le = Lecturer('eric')
    pe = Professor('eric')
    ae = ArrogantProfessor('eric')

    #print "==="
    #print ae.say("the sky is blue")
    #print "==="
    #print ae.lecture("the sky is blue")
    #print "==="
    #>>> ae.say("the sky is blue")
    #eric says: It is obvious that eric says: the sky is blue
    #>>> ae.lecture("the sky is blue")
    #It is obvious that eric says: the sky is blue

    print pe.say("the sky is blue")
    print "Prof. eric says: I believe that eric says: the sky is blue"
    print "==="
    print ae.say("the sky is blue")
    print "Prof. eric says: It is obvious that I believe that eric says: the sky is blue"