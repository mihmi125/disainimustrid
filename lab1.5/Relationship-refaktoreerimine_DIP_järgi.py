from enum import Enum
from abc import ABC, abstractmethod

class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for rel in self.relations:
            if rel[0].name == name and rel[1] == Relationship.PARENT:
                yield rel[2].name

class Research:
    def __init__(self, browser):
        for child_name in browser.find_all_children_of("John"):
            print(f"John has a child called {child_name}")