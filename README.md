# Advance Software Engineering
# Restaurant-Management-System
**Introduction**

Restaurant Management System is a console-based application that uses text files to store multiple food menus and user information. It is written in the Python programming language.
Which includes features such as authentication, authorization, and registartion. The restaurant manager (Admin) want to execute basic functions such as adding, removing, and displaying food menus. Clients can also log in and execute tasks such as seeing a menu, ordering meals, and cancel it.

**Handling**

1. Clone the repository

2. Create a virtual environment

3. Install pybuilder

4. pip install pybuilder

5. Build the project -- pyb 

6. Run the project using any IDE as it's console based application

[Console OutPut](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/docs/output/output1.PNG)
[Console OutPut](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/docs/output/output2.PNG)
[Console OutPut](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/docs/output/output3.PNG)

#### Contents
**1) UML Diagrams**

The Unified Modeling Language (UML) is a general-purpose, developmental modeling language in the field of software engineering that aims to provide a standardized approach to represent a system's design.

The UML diagrams for the Restaurant-Management-System are shown below.

[Use case Diagram](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/images/Use_case_diagram.PNG) 

The objective of a use case diagram is to capture a system's dynamic nature.
1)Functionalities to be stated as a use case are involved. 2)Actors 3)Interactions between use cases and actors.

[Activity Diagram](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/images/Activity%20Diagram.PNG)

An activity diagram is a flowchart that depicts the flow of information from one activity to the next. The activity can be described as a system operation.
From one activity to the next, the control flow is depicted. This flow can be sequential, branched, or concurrent. Different elements such as fork, join, and others are used in activity diagrams to cope with various types of flow control.
      
[Class Diagram](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/images/class_diagram.PNG)

 Class diagram shows a collection of classes, interfaces, associations, collaborations, and constraints. It is also known as a structural diagram.
 A class diagram depicts an application's static view. It is used not only for visualizing, describing, and documenting many parts of a system, but also for creating executable code for a software program.
A collection of classes, interfaces, associations, collaborations, and constraints are shown in a class diagram. A structural diagram is another name for it.

**2) The domain driven design (DDD) Of Restaurant Management System(RMS)**

For complicated requirements, the domain driven design technique is utilized, which connects the implementation to a changing model of the key business principles. It focuses on the issue domain and essentially serves in the identification of the architecture as well as the processes that the program must reproduce. I have a decent understanding of what restaurant booking is all about, as well as the domain of Food Ordering System, which I will use to construct a Restaurant Management System.

There are four main DDD terms :

   1. Context: A word's or statement's meaning is determined by the context in which it appears. Only in context can statements regarding a model be understood.
               
   2. Model: A system of abstractions that can be utilized to solve problems in a domain by describing selected parts of it.
   
   3. Ubiquitous Language: A language based on the domain model that is used by all team members to connect all of the team's activities to the software.
                          
   4. Bounded Context: A boundary (usually a subsystem or the activities of a certain team) within which a given model is specified and applicable.
                       (example: Booking Managemnet System, User management, admin management, Transcation management, Employee Management, food menu Management)
    
[DDD](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/docs/output/DDD.png)

**3) SonarCloud Metrics**

SonarCloud is an online service that detects bugs, security vulnerabilities, and code smells in Pull Requests and across code repositories, allowing developers to improve their workflow by ensuring consistent code quality.

[Sonarcloud-URL](https://sonarcloud.io/summary/overall?id=StudentDS3_Restaurant-Management-System)

[Sonar-Config file](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/sonar-project.properties)

**1. SonarCloud Reliability Metrics:**

Reliability metrics are used to express the software product's reliability in quantitative terms. It examines new bugs such as number of news bugs issues in source code.

[Reliability Metrics]()

**2. SonarCloud Security Metrics:**

Security metrics uncover vulnerabilities and new weaknesses in source code.

[Security Metrics]()

**3. SonarCloud Duplication Metrics:**

Duplication Metrics uses line duplication, files duplication and  blocks duplication  metrics to cover code duplication in the RMS project code.

[Duplications Metrics]()

**4) Clean Code Development(5 points  + 10 points of cheat sheet)**

Clean code addresses the clear, understandable, traceable, logical and disciplined implementation of code. The aim is to produce software efficiently and effectively while designing the code so that it is easy to use ,readable,
changeable,expandable and maintainable.

[CheatSheet](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/docs/output/CheatSheet.pdf)

**1.Use of meaningful and pronounceable variable names**

[Meaningful Name](https://github.com/StudentDS3/Restaurant-Management-System/blob/5012861f82c5ad49a69b8f9879d40e02afb2e48b/src/main/python/booking_dishes.py#L13)

**2. Custom Exception Handling for better eadable and code maintainance**

[Exception Handling](https://github.com/StudentDS3/Restaurant-Management-System/blob/5012861f82c5ad49a69b8f9879d40e02afb2e48b/src/main/python/booking.py#L101-L107)


**3. Use of constant File or Constant variables**

[Constant File](https://github.com/StudentDS3/Restaurant-Management-System/blob/5012861f82c5ad49a69b8f9879d40e02afb2e48b/src/main/python/constants.py#L6-L7)

[Constant Variables Usage](https://github.com/StudentDS3/Restaurant-Management-System/blob/5012861f82c5ad49a69b8f9879d40e02afb2e48b/src/main/python/booking_dishes.py#L25)

**4. one def serves one purpose**

[One pupose](https://github.com/StudentDS3/Restaurant-Management-System/blob/5012861f82c5ad49a69b8f9879d40e02afb2e48b/src/main/python/booking_dishes.py#L36-L40)

**5. use of decorators**

[Decorators](https://github.com/StudentDS3/Restaurant-Management-System/blob/5012861f82c5ad49a69b8f9879d40e02afb2e48b/src/main/python/booking_dishes.py#L70-L95)
	

**5) Build Management using Pybuilder.**

PyBuilder was used to create the RMS project, and the command **pyb** was used.
PyBuilder is a Python-based software build automation tool that focuses on the Python environment. It is built on the dependency-based programming paradigm, but it also has a sophisticated plugin mechanism that allows the creation of build life-cycles similar to those seen in other well-known build tools such as Apache Maven and Gradle.
The files are listed below, and the image contains the information.

[Build File](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/build.py)

[SetUp File](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/setup.py)

[PyBuilder](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/images/pyb--pybuild.PNG)


**6) Unit-Tests using uinitest.**

The build is complete, and each individual unittest is running with percentage coverage.

[Unittests](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/images/pyb--pybuild.PNG)

**7) Continuous Delivery GitHub Actions**

CI using GitHub Actions offers workflows that can build the code in the repository and run tests. Workflows runs on GitHub-hosted virtual machines.

[GitHub Actions Pipeline-Link](https://github.com/StudentDS3/Restaurant-Management-System/actions)

[GitHub Actions-Setup file](https://github.com/StudentDS3/Restaurant-Management-System/blob/main/.github/workflows/blank.yml)


**8) Pycharm IDE**

I'm familiar with different integrated development environments (IDE) for Java I used Eclipse and NetBeans. As the actual project is written in Python, I prefer using Visual Studio Code for Python development.
   * Ctrl+Shift+B	   Run Build Task
   * shift+ctrl+\    Jump to matching bracket
   * shift+ctrl+K    Delete line

**9) Domain specific language (DSL) snippet**

 A Domain Specific Language (DSL) is a programming language with a higher degree of abstraction that is targeted to a particular set of issues. The concepts and rules from the field or domain are used in a DSL.SQL, HTML, XML, UML, and other DSLs are common examples. As a DSL, the RMS project employed "regular expression."
 
 **Regular expression:**
 
A regular expression is a sequence of characters that can be used to match or find other strings or sets of strings by utilizing a particular syntax that is stored in a pattern. In this project's code, a regular expression was utilized as a DSL. From user inputs, a regular expression was utilized to match valid characters, password strength, and email pattern.
 
 [Regular Expression](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L66)

**10) Functional Programming used.**

The functional programming techniques I utilized in my RMS project are listed below.

**1. Final data structures**

Some variables have been made immutable in project code.

[Final Data Structure](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L11-L12)

**2.Side effect free functions**

Operations that modify a variable's or expression's global state are called side effect. Side effect are addressed with all assignment and input/output operators. In this project code, I utilized function programming, which has no side effect and is used frequently in functional programming. An example of a function with no side effect follows.

[Side Effect Free Function](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking_dishes.py#L32-L41)


**3. Higher-order functions**

If a function incorporates other functions as an input or returns a function as an output, it is referred to as a Higher Order Function. Higher Order Functions are functions that act on another function. It's worth noting that this higher-order function can be used with functions and procedures that accept functions as parameters or return functions as results.
In Python, the most common application of higher-order functions is decorators. It allows programmers to change how a function or class behaves. Decorators allow us to encapsulate another function in order to enhance its functionality without having to alter it permanently. Functions are sent as arguments to another function in Decorators, and then called from within the wrapper.
I have used decorators , fine_calc_decorator is callable function and calculate_fine is actual function inside the wrapper function.

[High-Order-Function](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking_dishes.py#L70-L90)

**4. Functions as parameters**

In the example below, a function is assigned to a variable . This assignment doesn’t call the function. It takes the function object referenced by it and creates a second name pointing to it.

[Function Stored As Variable](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L25)

[Actual Function](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L37)

Below example shows functions that can accept other functions as arguments.It is a function which accepts function as param.

[Function being called](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L131-L132)

[Function Used](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L64)

[Actual Function](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L74-L80)


**5. Anonymous functions**

Python Lambda Functions are anonymous functions, which implies they don't have a name. The def keyword is used to define a typical function in Python, as we already know. The lambda keyword is also used in Python to define an anonymous function.

[Lambda](https://github.com/StudentDS3/Restaurant-Management-System/blob/fb9271c0965f20c98c5fd0492ca31beaea40438c/src/main/python/booking.py#L59)

