from enum import Enum

class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3

class Person:
    def __init__(self, name):
        self.name = name

class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

class Research:
    def __init__(self, relationships):
        for rel in relationships.relations:
            if rel[0].name == "John" and rel[1] == Relationship.PARENT:
                print(f"John has a child called {rel[2].name}")
