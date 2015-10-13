# Design Pattern in Python

The purpose of this repo is to be a learning tool for myself and others.


> _"The design patterns are descriptions of communicating objects and classes that are customized to solve a general design problem in a particular context"_

> **The principle of reusable object-oriented design:** 

> Program to an interface, not an implementation

> Favor object composition over class inheritance

> Gamma, Helm, Johnson & Vlissides (1994). Design Patterns (the Gang of Four book). Addison-Wesley. ISBN 0-201-63361-2.

In my understanding, the pattern name and aspects are just problem focus, do not be fooled by the name, to understand why the problem can be solve in this way is much more important.

__Creational__:

| Pattern | Aspect(s) That Can Vary |
|:-------:| ----------- |
| [abstract_factory](abstract_factory.py) | families of product objects |
| [Builder]() | how a composite object get created |
| [Factory Method]() | subclass of object that is instantiated |
| [Prototype]() | class of object that is instantiated |
| [Singleton]() | the sole instance of class |

__Structural Patterns__:

| Pattern | Aspect(s) That Can Vary |
|:-------:| ----------- |
| [Adapter]() | interface to an object |
| [Bridge]() | implementation of an object |
| [Composite]() | structure and composition of an object |
| [Decorator]() | responsibilities of an object without subclassing |
| [Facade]() | interface to a subsystem |
| [Flyweight]() | storage costs of objects |
| [Proxy]() | how an object is accessed its location |

__Behavioral Patterns__:

| Pattern | Aspect(s) That Can Vary |
|:-------:| ----------- |
| [Chain of Responsibility]() | object that can fulfill a request |
| [Command]() | when and how a request is fulfilled |
| [Interpreter]() | grammar and interpretation of a language |
| [Iterator]() | how an aggregate's elements are accessed, traversed |
| [Mediator]() | how and which objects interact with each other |
| [Memento]() | what private information is stored outside an object, and when |
| [Observer]() | number of objects that depend on another object; how the dependent objects stay up to date |
| [State]() | states of an object |
| [Strategy]() | an algorithm |
| [Template Method]() | steps of an algorithm |
| [Visitor]() | operations that can be applied to object(s) without changing their class(es) |

__Others__:

| Pattern | Aspect(s) That Can Vary |
|:-------:| ----------- |

![](http://r3dux.org/wp-content/uploads/2011/06/DesignPatternRelationships.png)
