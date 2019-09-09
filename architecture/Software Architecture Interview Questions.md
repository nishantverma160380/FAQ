Software Architecture Interview Questions


A software architect is a software expert who makes high-level design choices and dictates technical standards, including software coding standards, tools, and platforms. Software architecture refers to the high level structures of a software system, the discipline of creating such structures, and the documentation of these structures.

  
Q1: What does “program to interfaces, not implementations” mean?
Topic: Design Patterns
A: Coding against interface means, the client code always holds an Interface object which is supplied by a factory.

Any instance returned by the factory would be of type Interface which any factory candidate class must have implemented. This way the client program is not worried about implementation and the interface signature determines what all operations can be done.

This approach can be used to change the behavior of a program at run-time. It also helps you to write far better programs from the maintenance point of view.



Q2: What are the differences between continuous integration, continuous delivery, and continuous deployment?
Topic: DevOps
A: Developers practicing continuous integration merge their changes back to the main branch as often as possible. By doing so, you avoid the integration hell that usually happens when people wait for release day to merge their changes into the release branch.
Continuous delivery is an extension of continuous integration to make sure that you can release new changes to your customers quickly in a sustainable way. This means that on top of having automated your testing, you also have automated your release process and you can deploy your application at any point of time by clicking on a button.
Continuous deployment goes one step further than continuous delivery. With this practice, every change that passes all stages of your production pipeline is released to your customers. There's no human intervention, and only a failed test will prevent a new change to be deployed to production.



Q3: What does SOLID stand for? What are its principles?
Topic: Software Architecture

S.O.L.I.D is an acronym for the first five object-oriented design (OOD) principles by Robert C. Martin.

S - Single-responsiblity principle. A class should have one and only one reason to change, meaning that a class should have only one job.
O - Open-closed principle. Objects or entities should be open for extension, but closed for modification.
L - Liskov substitution principle. Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.
I - Interface segregation principle. A client should never be forced to implement an interface that it doesn't use or clients shouldn't be forced to depend on methods they do not use.
D - Dependency Inversion Principle. Entities must depend on abstractions not on concretions. It states that the high level module must not depend on the low level module, but they should depend on abstractions.



Q4: What Is BASE Property Of A System?
Topic: Software Architecture

BASE properties are the common properties of recently evolved NoSQL databases. According to CAP theorem, a BASE system does not guarantee consistency. This is a contrived acronym that is mapped to following property of a system in terms of the CAP theorem:

Basically available indicates that the system is guaranteed to be available
Soft stateindicates that the state of the system may change over time, even without input. This is mainly due to the eventually consistent model.
Eventual consistency indicates that the system will become consistent over time, given that the system doesn't receive input during that time.


Q5: What Is CAP Theorem?
Topic: Software Architecture

The CAP Theorem for distributed computing was published by Eric Brewer, This states that it is not possible for a distributed computer system to simultaneously provide all three of the following guarantees:

Consistency (all nodes see the same data even at the same time with concurrent updates )
Availability (a guarantee that every request receives a response about whether it was successful or failed)
Partition tolerance (the system continues to operate despite arbitrary message loss or failure of part of the system)
The CAP acronym corresponds to these 3 guarantees. This theorem has created the base for modern distributed computing approaches. Worlds most high volume traffic companies (e.g. Amazon, Google, Facebook) use this as basis for deciding their application architecture. Its important to understand that only two of these three conditions can be guaranteed to be met by a system.


Q6: Are you familiar with The Twelve-Factor App principles?
Topic: Software Architecture

The Twelve-Factor App methodology is a methodology for building software as a service applications. These best practices are designed to enable applications to be built with portability and resilience when deployed to the web.

Codebase - There should be exactly one codebase for a deployed service with the codebase being used for many deployments.
Dependencies - All dependencies should be declared, with no implicit reliance on system tools or libraries.
Config - Configuration that varies between deployments should be stored in the environment.
Backing services All backing services are treated as attached resources and attached and detached by the execution environment.
Build, release, run - The delivery pipeline should strictly consist of build, release, run.
Processes - Applications should be deployed as one or more stateless processes with persisted data stored on a backing service.
Port binding - Self-contained services should make themselves available to other services by specified ports.
Concurrency - Concurrency is advocated by scaling individual processes.
Disposability - Fast startup and shutdown are advocated for a more robust and resilient system.
Dev/Prod parity - All environments should be as similar as possible.
Logs - Applications should produce logs as event streams and leave the execution environment to aggregate.
Admin Processes - Any needed admin tasks should be kept in source control and packaged with the application.



Q7: What are heuristic exceptions?
Topic: Software Architecture

A Heuristic Exception refers to a transaction participant’s decision to unilaterally take some action without the consensus of the transaction manager, usually as a result of some kind of catastrophic failure between the participant and the transaction manager.

In a distributed environment communications failures can happen. If communication between the transaction manager and a recoverable resource is not possible for an extended period of time, the recoverable resource may decide to unilaterally commit or rollback changes done in the context of a transaction. Such a decision is called a heuristic decision. It is one of the worst errors that may happen in a transaction system, as it can lead to parts of the transaction being committed while other parts are rolled back, thus violating the atomicity property of transaction and possibly leading to data integrity corruption.

Because of the dangers of heuristic exceptions, a recoverable resource that makes a heuristic decision is required to maintain all information about the decision in stable storage until the transaction manager tells it to forget about the heuristic decision. The actual data about the heuristic decision that is saved in stable storage depends on the type of recoverable resource and is not standardized. The idea is that a system manager can look at the data, and possibly edit the resource to correct any data integrity problems.




Q8: What Is Shared Nothing Architecture? How Does It Scale?
Topic: Software Architecture

A shared nothing architecture (SN) is a distributed computing approach in which each node is independent and self-sufficient, and there is no single point of contention required across the system.

This means no resources are shared between nodes (No shared memory, No shared file storage)
The nodes are able to work independently without depending on each other for any work.
Failure on one node affects only the users of that node, however other nodes continue to work without any disruption.
This approach is highly scalable since it avoid the existence of single bottleneck in the system. Shared nothing is recently become popular for web development due to its linear scalability. Google has been using it for long time.

In theory, A shared nothing system can scale almost infinitely simply by adding nodes in the form of inexpensive machines.



Q9: What Does Eventually Consistent Mean?
Topic: Software Architecture

Unlike relational database property of Strict consistency, eventual consistency property of a system ensures that any transaction will eventually (not immediately) bring the database from one valid state to another. This means there can be intermediate states that are not consistent between multiple nodes.

Eventually consistent systems are useful at scenarios where absolute consistency is not critical. For example in case of Twitter status update, if some users of the system do not see the latest status from a particular user its may not be very devastating for system.

Eventually consistent systems can not be used for use cases where absolute/strict consistency is required. For example a banking transactions system can not be using eventual consistency since it must consistently have the state of a transaction at any point of time. Your account balance should not show different amount if accessed from different ATM machines.


Question 1. Should We Create System Software ( E.g Operating System ) In Java ?
Answer : No, Java runs on a virtual machine called JVM and hence doesn't embed well with the underlying hardware. Though we can create a platform independent system software but that would be really slow and that's what we would never need. 

Question 2. What Are The Different Types Of Memory Used By Jvm ?
Answer : Class , Heap , Stack , Register , Native Method Stack.

Question 3. What Are The Benefits Of Using Spring Framework ?
Answer : Spring enables developers to develop enterprise-class applications using POJOs. The benefit of using only POJOs is that you do not need an EJB container product.
Spring is organized in a modular fashion. Even though the number of packages and classes are substantial, you have to worry only about ones you need and ignore the rest.
Spring does not reinvent the wheel instead, it truly makes use of some of the existing technologies like several ORM frameworks, logging frameworks, JEE, Quartz and JDK timers, other view technologies.
Testing an application written with Spring is simple because environment-dependent code is moved into this framework. Furthermore, by using JavaBean-style POJOs, it becomes easier to use dependency injection for injecting test data.
Spring’s web framework is a well-designed web MVC framework, which provides a great alternative to web frameworks such as Struts or other over engineered or less popular web frameworks.
Spring provides a convenient API to translate technology-specific exceptions (thrown by JDBC, Hibernate, or JDO, for example) into consistent, unchecked exceptions.
Lightweight IoC containers tend to be lightweight, especially when compared to EJB containers, for example. This is beneficial for developing and deploying applications on computers with limited memory and CPU resources.
Spring provides a consistent transaction management interface that can scale down to a local transaction

 
Question 4. What Are Various Types Of Class Loaders Used By Jvm ?
Answer : 
Bootstrap - Loads JDK internal classes, java.* packages.

Extensions - Loads jar files from JDK extensions directory - usually lib/ext directory of the JRE

System  - Loads classes from system classpath.

Question 5. What Is Permgen Or Permanent Generation ?
Answer : The memory pool containing all the reflective data of the java virtual machine itself, such as class and method objects. With Java VMs that use class data sharing, this generation is divided into read-only and read-write areas. The Permanent generation contains metadata required by the JVM to describe the classes and methods used in the application. The permanent generation is populated by the JVM at runtime based on classes in use by the application. In addition, Java SE library classes and methods may be stored here.

Question 6. What Is Metaspace ?
Answer : The Permanent Generation (PermGen) space has completely been removed and is kind of replaced by a new space called Metaspace. The consequences of the PermGen removal is that obviously the PermSize and MaxPermSize JVM arguments are ignored and you will never get a java.lang.OutOfMemoryError: PermGen error.

 
Question 7. How Does Volatile Affect Code Optimization By Compiler?
Answer : Volatile is an instruction that the variables can be accessed by multiple threads and hence shouldn't be cached. As volatile variables are never cached and hence their retrieval cannot be optimized.

Question 8. What Things Should Be Kept In Mind While Creating Your Own Exceptions In Java?
Answer : All exceptions must be a child of Throwable.
If you want to write a checked exception that is automatically enforced by the Handle or Declare Rule, you need to extend the Exception class.
You want to write a runtime exception, you need to extend the RuntimeException class.

Question 9. What Is The Best Practice Configuration Usage For Files - Pom.xml Or Settings.xml ?
Answer : The best practice guideline between settings.xml and pom.xml is that configurations in settings.xml must be specific to the current user and that pom.xml configurations are specific to the project.


 
Question 10. Can You Provide Some Implementation Of A Dictionary Having Large Number Of Words ?
Answer : Simplest implementation we can have is a List wherein we can place ordered words and hence can perform Binary Search.

Other implementation with better search performance is to use HashMap with key as first character of the word and value as a LinkedList.

Further level up, we can have linked Hashmaps like ,

hashmap {

a ( key ) -> hashmap (key-aa , value (hashmap(key-aaa,value)

b ( key ) -> hashmap (key-ba , value (hashmap(key-baa,value)

....................................................................................

z( key ) -> hashmap (key-za , value (hashmap(key-zaa,value)

}

upto n levels ( where n is the average size of the word in dictionary.

Question 11. What Is Database Deadlock ? How Can We Avoid Them?
Answer : When multiple external resources are trying to access the DB locks and runs into cyclic wait, it may makes the DB unresponsive. 
Deadlock can be avoided using variety of measures, Few listed below:
Can make a queue wherein we can verify and order the request to DB.
Less use of cursors as they lock the tables for long time.
Keeping the transaction smaller.
Question 12. Why Web Services Use Http As The Communication Protocol ?
Answer : With the advent of Internet, HTTP is the most preferred way of communication. Most of the clients ( web thin client , web thick clients , mobile apps )  are designed to communicate using http only. Web Services using http makes them accessible from vast variety of client applications. 


Question 13. Why Using Cookie To Store Session Info Is A Better Idea Than Just Using Session Info In The Request ?
Answer : Session info in the request can be intercepted and hence a vulnerability. Cookie can be read and write  by respective domain only and make sure that right session information is being passed by the client.

Question 14. Difference Between First Level And Second Level Cache In Hibernate ?
Answer : First level cache is enabled by default whereas Second level cache needs to be enabled explicitly.
First level Cache came with Hibernate 1.0 whereas Second level cache came with Hibernate 3.0.
 First level Cache is Session specific whereas Second level cache is shared by sessions that is why First level cache is considered local and second level cache is considered global.

Question 15. What Are The Ways To Avoid Lazyinitializationexception ?
Answer : Set lazy=false in the hibernate config file.
 Set @Basic(fetch=FetchType.EAGER) at the mapping.
Make sure that we are accessing the dependent objects before closing the session.
Using Fetch Join in HQL.

 
Question 16. What Are New Features Introduced With Java 8 ?
Answer : Lambda Expressions , Interface Default and Static Methods , Method Reference , Parameters Name , Optional , Streams, Concurrency.

Question 17. What Things You Would Care About To Improve The Performance Of Application If Its Identified That Its Db Communication That Needs To Be Improved ? 
Answer : Query Optimization ( Query Rewriting , Prepared Statements )
 Restructuring Indexes.
DB Caching Tuning ( if using ORM )
Identifying the problems ( if any ) with the ORM Strategy ( If using ORM )
Question 18. If You Are Given A Choice To Implement The Code To Either Insert A Record Or Update If Already Exist, Which Approach Will You Follow ? 1. Insert Into The Db Table. If Exception Occurs, Update The Existing Record. 2. Check If The Record Exists And Update It If It Exists, If Not Insert A New Record.
Answer : In first case, there would be 2 DB calls in worst case and 1 in best case. In 2nd approach there will be always 2 DB calls.

Decision on the approach should depend on the following considerations -
1. How costly is the call to DB.  Are we using indices , hibernate etc
If calls to DB are costly , 1st approach should be the choice.
2. Exception Book keeping load upon exception.
The benefit of saving 1st call in approach 1 should be bigger than the Book keeping for the exception.
3. Probability of the exception in first apparoach.  
If the DB Table is almost empty, it makes sense to follow Approach 1 as majority of the 1st calls will pass through without exception.

Question 19. What Would You Do If You Have To Add A Jar To The Project Using Maven ?
Answer : If its already there in Maven local repository, We can add that as a dependency in the project pom file with its Group Id, Artifact Id and version.
We can provide additional attribute SystemPath if its unable to locate the jar in the local repository.
If its not there in the local repository, we can install it first in the local repository and then can add it as dependency.

Question 20. Which Uml Diagrams You Usually Use For Design ?
Answer : Use Case Diagram, Component Diagram for High level Design and Class Diagram , Sequence Diagram for low level design.

Question 21. How Do You Coordinate And Communicate With The Team Developers ?
Answer : We as a team of developers , testers , analyst , lead and architect sit close to each other. Most of the time I would just jump to their seat and talk to them ( if required ). We have daily stand up where we discuss things that needs team attention. 

Question 22. What Kind Of Software Architecture Your Organization Follow ?
Answer : We have multi tier architecture with multiple layers , We have series of web servers and applications in application tier, infrastructure libraries at middle tier and Database servers at the lower tier. We are using Oracle as Database, ESB ( Enterprise service Bus ) for asynchronous communication and Rest Web Services.

Question 23. Difference Between Proxy And Adapter Design Patterns ?
Answer : Adapter object has a different input than the real subject whereas Proxy object has the same input as the real subject. Proxy object is such that it should be placed as it is in place of the real subject.

Question 24. Difference Between Adapter And Facade ?
Answer : The Difference between these patterns in only the intent. Adapter is used because the objects in current form cannot communicate where as in Facade , though the objects can communicate , A Facade object is placed between the client and subject to simplify the interface.

Question 25. Difference Between Builder And Composite ?
Answer : Builder is a creational Design Pattern whereas Composite is a structural design pattern. Composite creates Parent - Child relations between your objects while Builder is used to create group of objects of predefined types.

Question 26. Difference Between Factory And Strategy Design Pattern ?
Answer : Factory is a creational design pattern whereas Strategy is behavioral design pattern. Factory revolves around the creation of object at runtime whereas Strategy or Policy revolves around the decision at runtime.

Question 27. Shall We Use Abstract Classes Or Interfaces In Policy / Strategy Design Pattern ?
Answer : Strategy deals only with decision making at runtime so Interfaces should be used.


What are the important responsibilities of Architect?
Below is a high level summary

Architect Interview Questions - Responsibilities
Creating a clean architecture based on sound principles. Architecture covering all Non Functional Requirements.
Having good governance in place. Good review processes in place for Architecture, Design and Code.
Ensuring teams are as productive as they can be. Right tools.
Ensuring teams are following the best engineering practices.
Ensuring clear communication about architecture with business and technical teams.
How should an ideal architect be like?
Architect Interview Questions - Qualities
Most important qualities I look for in an Architect are

Impeccable Credibility : Somebody the team looks up to and aspires to be.
Super diagnostic skills : The ability to do a deep dive on a technology issue. When developers are struggling with a problem (having tried different things), Can he/she provide a fresh pair of eyes to look at the same problem?
Forward Thinker and Proactive : Never satisfied with where we are. Identifies opportunities to add value fast.
Great Communication : Communication in the widest sense. Communicating the technical aspects to the stakeholders, project management, software developers, testers, etc.
What are the modern programming practices an architect should be aware of?
“Design

For more details refer to design interview questions.

How do you ensure that the Code Quality is maintained?
Architect Interview Questions - Code Quality
More than everything else, code quality is an attitude. Either, the team has it or not. The attitude to refactor when something is wrong. The attitude to be a boy scout. As an architect, it is important to create an environment where such an attitude is appreciated. (There are always bad sheep, who take the code quality to such depth that it is not fun anymore, but I like them more than developers who keep churning out bad code).

Have a good static analysis tool(and is part of Continuous Integration). Sonar is the best bet today. Understand the limits of Static Analysis. Static Analysis is not a magic wand. For me, results from Static Analysis are a signal: It helps me decide where I should look during peer or architect reviews?

Have good peer review practices in place. Every user story has to be peer reviewed. Put more focus on peer reviews when there is a new developer or there is a new technical change being done. Make best use of Pair Programming. The debate is ongoing : Is pair programming more productive or not? I would rather stay out of it. You make your choice. However, these two scenarios are bare minimum:

Onboarding a new programmer. Makes him comfortable with all the new things he has to encounter.
Implementing a complex functionality.
Next question is how to approach a Code Review. Difficult to cover everything. I would make a start. When doing a code review, I start with static analysis results (for example, sonar). I spend 10 minutes getting an overview of components and/or layers (focusing on size and dependencies). Next I would pick up a unit test for a complex functionality. I feel unit tests are the best place to discover the dependencies and naming practices (I believe good names = 50% of maintainable code). If a programmer can write a simple and understandable unit test, he can definitely write good code. Next, I look for 4 principles of Simple Design. After this, there are 100 other things we can look for - You decide.

How do Agile and Architecture go hand in hand?
First of all I’m a great believer that agile and architecture go hand in hand. I do not believe agile means no architecture. I think agile brings in the need to separate architecture and design. For me architecture is about things which are difficult to change : technology choices, framework choices, communication between systems etc. It would be great if a big chunk of architectural decisions are made before the done team starts. There would always be things which are uncertain. Inputs to these can come from spikes that are done as part of the Done Scrum Team.But these should be planned ahead.

Architecture choices should be well thought out. Its good to spend some time to think (Sprint Zero) before you make a architectural choice.

I think most important part of Agile Architecture is Automation Testing. Change is continuous only when the team is sure nothing is broken. And automation test suites play a great role in providing immediate feedback.

Important principles for me are test early, fail fast and automate.

How do you ensure the team is following sound engineering practices?
I ask the following questions:

How often is code committed?
How often is code released?
How often do builds break? Are they immediately fixed?
How often is code deployed?
What steps are part of continuous integration build? Is deployment and automation suite part of it?
Does the team develop vertical slices when implementing a new functionality?


As an programmer, what are design principles you focus on?
“Design

I start off with the 4 Principles of Simple Design. Following YouTube PlayListexplains the four principles of simple design in detail :

Runs all tests
Minimize Duplication
Maximize Clarity
Keep it Small
Next important design principles would be those related to Object Oriented Programming. Have good object, which have well-defined responsibilities. Following are the important concepts you need to have a good overview of. These are covered in various parts in this YouTube Video . Also, look up the specific videos for each topic.

Coupling
Cohesion : YouTube Video
Encapsulation
Polymorphism : YouTube Video
SOLID Principles
UML is next even though, formal use of UML is on the way down with Agile. However, I think UML is a great tool in the arsenal for a white board discussion on design. A picture is worth thousand words. I recommend having a good overview of the UML basics. Focus on these four before you move on to others.

Class diagrams
Sequence diagrams
Component diagrams
Deployment diagrams
Last and also the least important is Design Patterns. This YouTube Video covers all the major design patterns . My personal view : Design Patterns are good to know. Have a good idea on what each one of them does. But, that where it ends. I’m not a big fan of understanding the intricate details of each Design Pattern. You can look it up if you have a good overall idea about Design Patterns.

What are the modern programming practices which lead to very good applications?
“Design

First of all : Unit Testing and Mocking. We are in the age of continuous integration and delivery, and the basic thing that enables those is having a good set of unit test in place. (Don’t confuse unit testing with screen testing done manually to check if the screen flow is right. What I mean by unit testing is JUnit test’s checking the business logic/screen flow in a java method (or) set of methods). Understand JUnit. This set of videos is a good start to understand JUnit. Also understand the concept of Mocking. When should we mock? And when we should not? Complicated question indeed. Understand atleast one mocking framework : Mockito is the most popular one. Easymock is a good mocking framework as well.

Second in line is Automated Integration Tests. Automated Integration Tests is the second important bullet in enabling continuous delivery. Understand Fitnesse, Cucumber and Protractor.

Third is TDD (actually I wanted to put it first). Understand what TDD is. If you have never used TDD, then be ready for a rude shock. Its not easy to change a routine you developed during decades (or years) of programming. Once you are used to TDD you never go back. I promise. This list of videos is a good start to understanding TDD. Have fun.

Next comes BDD. In my experience, I found BDD a great tool to enable communication between the ready team (Business Analysts, Product Owner) and the done team (Developers, Testers, Operations). When User Stories are nothing but a set of scenarios specified is GWT (Given When Then) format, it is easy for the done team to chew at the user story scenario by scenario. With tools like Cucumber & Fitnesse, tooling is not far behind too. Do check BDD out.

Next in line is Refactoring. IUnderstand refactoring. Understand the role of automation tests in refactoring.

Last (but not the least) in the line is Continuous Integration. Every project today has continuous integration. But, the real question is “What is under Continuous Integration?”. Compilation, unit tests and code quality gate(s) is the bare minimum. If you have integration and chain tests, wonderful. But make sure the build does not take long. Immediate feedback is important. If needed, create a separate build scheduled less frequently for slower tests (integration and chain tests). Jenkins is the most popular Continuous Integration tool today.

What are the typical things you would need to consider while designing the Business Layer of a Java EE Web Application?
Listed below are some of the important considerations

Should I have a Service layer acting as a facade to the Business Layer?
How do I implement Transaction Management? JTA or Spring based Transactions or Container Managed Transactions? What would mark the boundary of transactions. Would it be service facade method call?
Can (Should) I separate any of the Business Logic into seperate component or service?
Do I use a Domain Object Model?
Do I need caching? If so, at what level?
Does service layer need to handle all exceptions? Or shall we leave it to the web layer?
Are there any Operations specific logging or auditing that is needed?Can we implement it as a cross cutting concern using AOP?
Do we need to validate the data that is coming into the Business Layer? Or is the validation done by the web layer sufficient?
What are the things that you would need to consider when designing the Access Layer (Data Layer) of the web application?
Do we want to use a JPA based object mapping framework (Hibernate) or query based mapping framework (iBatis) or simple Spring DO?
How do we communicate with external systems? Web services or JMS? If web services, then how do we handle object xml mapping? JAXB or XMLBeans?
How do you handle connections to Database? These days, its an easy answer : leave it to the application server configuration of Data Source.
What are the kinos of exceptions that you want to throw to Business Layer? Should they be checked exceptions or unchecked exceptions?
Ensure that Performance and Scalability is taken care of in all the decisions you make.
What are the things that you would need to consider when designing the Web Layer?
First question is do we want to use a modern front end javascript framework like AngularJS? If the answer is yes, most of this discussion does not apply. If the answer is no, then proceed?
Should we use a MVC framework like Spring MVC,Struts or should we go for a Java based framework like Wicket or Vaadin?
What should be the view technology? JSP, JSF or Template Based (Velocity, Freemarker)?
Do you want AJAX functionality?
How do you map view objects to business objects and vice-versa? Do you want to have View Assemblers and Business Assemblers?
What kind of data is allowed to be put in user session? Do we need additional control mechanisms to ensure session size is small as possible?
How do we Authenticate and Authorize users? Do we need to integrated external frameworks like Spring Security?
Do we need to expose external web services?
What are the important features of IDE Eclipse?
Go through this YouTube PlayList. It takes you through all the important features of Eclipse.

What are the best practices for build tool Maven?
Use archetypes as much as possible. Archetypes are good start for generating projects (lookup : mvn archetype:generate) based on Spring, Spring MVC, Struts, Hibernate and a wide variety of other projects. Also, it is a good practice to create maven archetype for the components we create repeatedly (access components, consuming/exposing web services).

Some of the Maven Best Practices are

Proper Dependency Mgmt : Version for one dependency at one place - preferably in the parent pom.
Group related dependencies.
Exclude test dependencies from final ear.
Have a parent pom.
Use Profiles as needed.


Question 1. Should We Create System Software ( E.g Operating System ) In Java ?

Answer :

No, Java runs on a virtual machine called JVM and hence doesn't embed well with the underlying hardware. Though we can create a platform independent system software but that would be really slow and that's what we would never need. 

Question 2. What Are The Different Types Of Memory Used By Jvm ?

Answer :

Class , Heap , Stack , Register , Native Method Stack.

Question 3. What Are The Benefits Of Using Spring Framework ?

Answer :

Spring enables developers to develop enterprise-class applications using POJOs. The benefit of using only POJOs is that you do not need an EJB container product.
Spring is organized in a modular fashion. Even though the number of packages and classes are substantial, you have to worry only about ones you need and ignore the rest.
Spring does not reinvent the wheel instead, it truly makes use of some of the existing technologies like several ORM frameworks, logging frameworks, JEE, Quartz and JDK timers, other view technologies.
Testing an application written with Spring is simple because environment-dependent code is moved into this framework. Furthermore, by using JavaBean-style POJOs, it becomes easier to use dependency injection for injecting test data.
Spring’s web framework is a well-designed web MVC framework, which provides a great alternative to web frameworks such as Struts or other over engineered or less popular web frameworks.
Spring provides a convenient API to translate technology-specific exceptions (thrown by JDBC, Hibernate, or JDO, for example) into consistent, unchecked exceptions.
Lightweight IoC containers tend to be lightweight, especially when compared to EJB containers, for example. This is beneficial for developing and deploying applications on computers with limited memory and CPU resources.
Spring provides a consistent transaction management interface that can scale down to a local transaction

 
Question 4. What Are Various Types Of Class Loaders Used By Jvm ?

Answer :

Bootstrap - Loads JDK internal classes, java.* packages.

Extensions - Loads jar files from JDK extensions directory - usually lib/ext directory of the JRE

System  - Loads classes from system classpath.

Question 5. What Is Permgen Or Permanent Generation ?

Answer :

The memory pool containing all the reflective data of the java virtual machine itself, such as class and method objects. With Java VMs that use class data sharing, this generation is divided into read-only and read-write areas. The Permanent generation contains metadata required by the JVM to describe the classes and methods used in the application. The permanent generation is populated by the JVM at runtime based on classes in use by the application. In addition, Java SE library classes and methods may be stored here.

Question 6. What Is Metaspace ?

Answer :

The Permanent Generation (PermGen) space has completely been removed and is kind of replaced by a new space called Metaspace. The consequences of the PermGen removal is that obviously the PermSize and MaxPermSize JVM arguments are ignored and you will never get a java.lang.OutOfMemoryError: PermGen error.


 
Question 7. How Does Volatile Affect Code Optimization By Compiler?
Answer :
Volatile is an instruction that the variables can be accessed by multiple threads and hence shouldn't be cached. As volatile variables are never cached and hence their retrieval cannot be optimized.

Question 8. What Things Should Be Kept In Mind While Creating Your Own Exceptions In Java?
Answer :
All exceptions must be a child of Throwable.
If you want to write a checked exception that is automatically enforced by the Handle or Declare Rule, you need to extend the Exception class.
You want to write a runtime exception, you need to extend the RuntimeException class.

Question 9. What Is The Best Practice Configuration Usage For Files - Pom.xml Or Settings.xml ?
Answer :
The best practice guideline between settings.xml and pom.xml is that configurations in settings.xml must be specific to the current user and that pom.xml configurations are specific to the project.


Question 10. Can You Provide Some Implementation Of A Dictionary Having Large Number Of Words ?
Answer :
Simplest implementation we can have is a List wherein we can place ordered words and hence can perform Binary Search.

Other implementation with better search performance is to use HashMap with key as first character of the word and value as a LinkedList.

Further level up, we can have linked Hashmaps like ,

hashmap {

a ( key ) -> hashmap (key-aa , value (hashmap(key-aaa,value)

b ( key ) -> hashmap (key-ba , value (hashmap(key-baa,value)

....................................................................................

z( key ) -> hashmap (key-za , value (hashmap(key-zaa,value)

}

upto n levels ( where n is the average size of the word in dictionary.

Question 11. What Is Database Deadlock ? How Can We Avoid Them?
Answer : When multiple external resources are trying to access the DB locks and runs into cyclic wait, it may makes the DB unresponsive. 

Deadlock can be avoided using variety of measures, Few listed below:

Can make a queue wherein we can verify and order the request to DB.
Less use of cursors as they lock the tables for long time.
Keeping the transaction smaller.

Question 12. Why Web Services Use Http As The Communication Protocol ?

Answer :
With the advent of Internet, HTTP is the most preferred way of communication. Most of the clients ( web thin client , web thick clients , mobile apps )  are designed to communicate using http only. Web Services using http makes them accessible from vast variety of client applications. 


 
Question 13. Why Using Cookie To Store Session Info Is A Better Idea Than Just Using Session Info In The Request ?
Answer : Session info in the request can be intercepted and hence a vulnerability. Cookie can be read and write  by respective domain only and make sure that right session information is being passed by the client.

Question 14. Difference Between First Level And Second Level Cache In Hibernate ?
Answer : First level cache is enabled by default whereas Second level cache needs to be enabled explicitly.
First level Cache came with Hibernate 1.0 whereas Second level cache came with Hibernate 3.0.
 First level Cache is Session specific whereas Second level cache is shared by sessions that is why First level cache is considered local and second level cache is considered global.
Question 15. What Are The Ways To Avoid Lazyinitializationexception ?

Answer :

Set lazy=false in the hibernate config file.
 Set @Basic(fetch=FetchType.EAGER) at the mapping.
Make sure that we are accessing the dependent objects before closing the session.
Using Fetch Join in HQL.

 
Question 16. What Are New Features Introduced With Java 8 ?

Answer :

 Lambda Expressions , Interface Default and Static Methods , Method Reference , Parameters Name , Optional , Streams, Concurrency.

Question 17. What Things You Would Care About To Improve The Performance Of Application If Its Identified That Its Db Communication That Needs To Be Improved ?

Answer :

Query Optimization ( Query Rewriting , Prepared Statements )
 Restructuring Indexes.
DB Caching Tuning ( if using ORM )
Identifying the problems ( if any ) with the ORM Strategy ( If using ORM )
Question 18. If You Are Given A Choice To Implement The Code To Either Insert A Record Or Update If Already Exist, Which Approach Will You Follow ? 1. Insert Into The Db Table. If Exception Occurs, Update The Existing Record. 2. Check If The Record Exists And Update It If It Exists, If Not Insert A New Record.

Answer :
In first case, there would be 2 DB calls in worst case and 1 in best case. In 2nd approach there will be always 2 DB calls.

Decision on the approach should depend on the following considerations -
1. How costly is the call to DB.  Are we using indices , hibernate etc

If calls to DB are costly , 1st approach should be the choice.
2. Exception Book keeping load upon exception.
The benefit of saving 1st call in approach 1 should be bigger than the Book keeping for the exception.
3. Probability of the exception in first apparoach.  
If the DB Table is almost empty, it makes sense to follow Approach 1 as majority of the 1st calls will pass through without exception.

Question 19. What Would You Do If You Have To Add A Jar To The Project Using Maven ?

Answer : If its already there in Maven local repository, We can add that as a dependency in the project pom file with its Group Id, Artifact Id and version.
We can provide additional attribute SystemPath if its unable to locate the jar in the local repository.
If its not there in the local repository, we can install it first in the local repository and then can add it as dependency.

Question 20. Which Uml Diagrams You Usually Use For Design ?
Answer : Use Case Diagram, Component Diagram for High level Design and Class Diagram , Sequence Diagram for low level design.

Question 21. How Do You Coordinate And Communicate With The Team Developers ?
Answer : We as a team of developers , testers , analyst , lead and architect sit close to each other. Most of the time I would just jump to their seat and talk to them ( if required ). We have daily stand up where we discuss things that needs team attention. 

Question 22. What Kind Of Software Architecture Your Organization Follow ?
Answer : We have multi tier architecture with multiple layers , We have series of web servers and applications in application tier, infrastructure libraries at middle tier and Database servers at the lower tier. We are using Oracle as Database, ESB ( Enterprise service Bus ) for asynchronous communication and Rest Web Services.

Question 23. Difference Between Proxy And Adapter Design Patterns ?
Answer : Adapter object has a different input than the real subject whereas Proxy object has the same input as the real subject. Proxy object is such that it should be placed as it is in place of the real subject.

Question 24. Difference Between Adapter And Facade ?
Answer : The Difference between these patterns in only the intent. Adapter is used because the objects in current form cannot communicate where as in Facade , though the objects can communicate , A Facade object is placed between the client and subject to simplify the interface.

Question 25. Difference Between Builder And Composite ?
Answer : Builder is a creational Design Pattern whereas Composite is a structural design pattern. Composite creates Parent - Child relations between your objects while Builder is used to create group of objects of predefined types.

Question 26. Difference Between Factory And Strategy Design Pattern ?
Answer : Factory is a creational design pattern whereas Strategy is behavioral design pattern. Factory revolves around the creation of object at runtime whereas Strategy or Policy revolves around the decision at runtime.

Question 27. Shall We Use Abstract Classes Or Interfaces In Policy / Strategy Design Pattern ?
Answer : Strategy deals only with decision making at runtime so Interfaces should be used.




1. Top 10 senior technical architect interview questions and answers Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
2. In this file, you can ref interview materials for senior technical architect such as types of interview questions, senior technical architect situational interview, senior technical architect behavioral interview… Other useful materials for senior technical architect interview: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews • interviewquestions360.com/13-types-of-interview-questions-and-how-to-face-them • interviewquestions360.com/job-interview-checklist-40-points • interviewquestions360.com/top-8-interview-thank-you-letter-samples • interviewquestions360.com/free-21-cover-letter-samples • interviewquestions360.com/free-24-resume-samples • interviewquestions360.com/top-15-ways-to-search-new-jobs Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
3. 1. Why do you want this senior technical architect job? Again, companies want to hire people who are passionate about the job, so you should have a great answer about why you want the position. (And if you don't? You probably should apply elsewhere.) First, identify a couple of key factors that make the role a great fit for you (e.g., “I love customer support because I love the constant human interaction and the satisfaction that comes from helping someone solve a problem"), then share why you love the company (e.g., “I’ve always been passionate about education, and I think you guys are doing great things, so I want to be a part of it”). Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
4. 2. What have you learned from mistakes on the senior technical architect job? Candidates without specific examples often do not seem credible. However, the example shared should be fairly inconsequential, unintentional, and a learned lesson should be gleaned from it. Moving ahead without group assistance while assigned to a group project meant to be collaborative is a good example. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
5. 3. What challenges are you looking for in this senior technical architect position? A typical interview question to determine what you are looking for your in next job, and whether you would be a good fit for the position being hired for, is "What challenges are you looking for in a position?" The best way to answer questions about the challenges you are seeking is to discuss how you would like to be able to effectively utilize your skills and experience if you were hired for the job. You can also mention that you are motivated by challenges, have the ability to effectively meet challenges, and have the flexibility and skills necessary to handle a challenging job. You can continue by describing specific examples of challenges you have met and goals you have achieved in the past. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
6. 4. Describe a typical work week for senior technical architect position? Interviewers expect a candidate for employment to discuss what they do while they are working in detail. Before you answer, consider the position you are applying for and how your current or past positions relate to it. The more you can connect your past experience with the job opening, the more successful you will be at answering the questions. It should be obvious that it's not a good idea talk about non-work related activities that you do on company time, but, I've had applicants tell me how they are often late because they have to drive a child to school or like to take a long lunch break to work at the gym. Keep your answers focused on work and show the interviewer that you're organized ("The first thing I do on Monday morning is check my voicemail and email, then I prioritize my activities for the week.") and efficient. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
7. 5. What is your biggest weakness? No one likes to answer this question because it requires a very delicate balance. You simply can’t lie and say you don’t have one; you can’t trick the interviewer by offering up a personal weakness that is really a strength (“Sometimes, I work too much and don’t maintain a work-life balance.”); and you shouldn’t be so honest that you throw yourself under the bus (“I’m not a morning person so I’m working on getting to the office on time.”) Think of a small flaw like “I sometimes get sidetracked by small details”, “I am occasionally not as patient as I should be with subordinates or co-workers who do not understand my ideas”, or “I am still somewhat nervous and uncomfortable with my public-speaking skills and would like to give more presentations and talk in front of others or in meetings.” Add that you are aware of the problem and you are doing your best to correct it by taking a course of action. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
8. 6. Why should the we hire you as senior technical architect position? This is the part where you link your skills, experience, education and your personality to the job itself. This is why you need to be utterly familiar with the job description as well as the company culture. Remember though, it’s best to back them up with actual examples of say, how you are a good team player. It is possible that you may not have as much skills, experience or qualifications as the other candidates. What then, will set you apart from the rest? Energy and passion might. People are attracted to someone who is charismatic, who show immense amount of energy when they talk, and who love what it is that they do. As you explain your compatibility with the job and company, be sure to portray yourself as that motivated, confident and energetic person, ever- ready to commit to the cause of the company. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
9. 7. What do you know about our company? Follow these three easy research tips before your next job interview: 1) Visit the company website; look in the “about us” section and “careers” sections 2) Visit the company’s LinkedIn page (note, you must have a LinkedIn account — its free to sign up) to view information about the company 3) Google a keyword search phrase like “press releases” followed by the company name; you’ll find the most recent news stories shared by the company Remember, just because you have done your “homework”, it does not mean you need to share ALL of it during the interview! Reciting every fact you’ve learned is almost as much of a turn off as not knowing anything at all! At a minimum, you should include the following in your answer: 1. What type of product or service the company sells 2. How long the company has been in business 3. What the company culture is like OR what the company mission statement is, and how the culture and/or mission relate to your values or personality Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
10. 8. Why do you want to work with us? More likely than not, the interviewer wishes to see how much you know about the company culture, and whether you can identify with the organization’s values and vision. Every organization has its strong points, and these are the ones that you should highlight in your answer. For example, if the company emphasizes on integrity with customers, then you mention that you would like to be in such a team because you yourself believe in integrity. It doesn’t have to be a lie. In the case that your values are not in line with the ones by the company, ask yourself if you would be happy working there. If you have no issue with that, go ahead. But if you are aware of the company culture and realize that there is some dilemma you might be facing, you ought to think twice. The best policy is to be honest with yourself, and be honest with the interviewer with what is it in the company culture that motivates you. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
11. 9. Did the salary we offer attract you to this senior technical architect job? The interviewer could be asking you this question for a number of reasons. Obviously, the salary is an important factor to your interest in this job, but it should not be the overriding reason for your interest. A good answer to this question is, “The salary was very attractive, but the job itself is what was most attractive to me.” Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
12. 10. Do you have any questions to ask us? Never ask Salary, perks, leave, place of posting, etc. regarded questions. Try to ask more about the company to show how early you can make a contribution to your organization like “Sir, with your kind permission I would like to know more about induction and developmental programs?” OR Sir, I would like to have my feedback, so that I can analyze and improve my strengths and rectify my shortcomings. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
13. Useful materials for senior technical architect interview: • interviewquestions360.com/top-36-situational-interview-questions • interviewquestions360.com/440-behavioral-interview-questions-ebook-pdf- download • interviewquestions360.com/top-40-second-interview-questions • interviewquestions360.com/95-management-interview-questions-and- answers-ebook-pdf-download • interviewquestions360.com/top-30-phone-interview-questions • interviewquestions360.com/290-competency-based-interview-questions • interviewquestions360.com/45-internship-interview-questions • interviewquestions360.com/15-tips-for-job-interview-attire (dress code, clothes, what to wear) • interviewquestions360.com/top-15-written-test-examples • interviewquestions360.com/top-15-closing-statements • interviewquestions360.com/20-case- study-examples for job interview Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
14. Useful materials for senior technical architect interview: • interviewquestions360.com/top-25-scenarios-interview-questions • interviewquestions360.com/top-25-tips-for-interview-preparation • interviewquestions360.com/top-10-tips-to-answer-biggest-weakness-and- strengths-questions • interviewquestions360.com/tips-to-answer-question-tell-me-about-yourself • interviewquestions360.com/16-job-application-tips • interviewquestions360.com/top-14-job-interview-advices • interviewquestions360.com/top-18-best-interview-practices • interviewquestions360.com/25-career-goals-examples • interviewquestions360.com/top-36-technical-interview-questions • interviewquestions360.com/18-job-interview-exam-samples • interviewquestions360.com/Q-A-25-questions-with-answers Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
15. Useful materials for senior technical architect interview: • interviewquestions360.com/12-followup-email-thank-you-letter-samples • interviewquestions360.com/15-tips-for-job-interview-withour-no-experience • interviewquestions360.com/15-presentation-ideas-for-job-interview • interviewquestions360.com/12-job-interview-role-play-examples • interviewquestions360.com/10-job-interview-techniques • interviewquestions360.com/11-job-interview-skills • interviewquestions360.com/tips-to-answer-question-why-should-I-hire-you • interviewquestions360.com/25-interview-questions-to-ask-employer • interviewquestions360.com/25-job-interview-assessment-test-examples • interviewquestions360.com/15-tips-to-answer-experience-questions • interviewquestions360.com/12-tips-to-answer-education-knowledge-questions Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
16. Useful materials for senior technical architect interview: • interviewquestions360.com/15-screening-interview-questions • interviewquestions360.com/22-group-interview-questions • interviewquestions360.com/22-panel-interview-questions • interviewquestions360.com/22-case-interview-questions • interviewquestions360.com/top-12-tips-for-career-development • interviewquestions360.com/top-9-career-path-tips • interviewquestions360.com/top-14-career-objectives • interviewquestions360.com/top-12-career-promotion-tips • interviewquestions360.com/11-performance-appraisal-methods (includes appraisal templates and forms) • interviewquestions360.com/top-28-performance-appraisal-forms • interviewquestions360.com/top-12-salary-negotiation-tips • interviewquestions360.com/top-9-tips-to-get-high-salary Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
17. Other interview tips for senior technical architect interview 1. Practice types of job interview such as screening interview, phone interview, second interview, situational interview, behavioral interview (competency based), technical interview, group interview… 2. Send interview thank you letter to employers after finishing the job interview: first interview, follow-up interview, final interview. 3. If you want more interview questions for entry- level, internship, freshers, experienced candidates, you can ref free ebook: 75 interview questions and answers. 4. Prepare list of questions in order to ask the employer during job interview. 5. Note: This file is available for free download. Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews
18. Fields related to senior technical architect career: The above job description can be used for fields as: Construction, manufacturing, healthcare, non profit, advertising, agile, architecture, automotive, agency, budget, building, business development, consulting, communication, clinical research, design, software development, product development, interior design, web development, engineering, education, events, electrical, exhibition, energy, ngo, finance, fashion, green card, oil gas, hospital, it, marketing, media, mining, nhs, non technical, oil and gas, offshore, pharmaceutical, real estate, retail, research, human resources, telecommunications, technology, technical, senior, digital, software, web, clinical, hr, infrastructure, business, erp, creative, ict, hvac, sales, quality management, uk, implementation, network, operations, architectural, environmental, crm, website, interactive, security, supply chain, logistics, training, project management, administrative management… The above interview questions also can be used for job title levels: entry level senior technical architect, junior senior technical architect, senior senior technical architect, senior technical architect assistant, senior technical architect associate, senior technical architect administrator, senior technical architect clerk, senior technical architect coordinator, senior technical architect consultant, senior technical architect controller, senior technical architect director, senior technical architect engineer, senior technical architect executive, senior technical architect leader, senior technical architect manager, senior technical architect officer, senior technical architect specialist, senior technical architect supervisor, VP senior technical architect… Useful materials: • interviewquestions360.com/free-ebook-145-interview-questions-and-answers • interviewquestions360.com/free-ebook-top-18-secrets-to-win-every-job-interviews