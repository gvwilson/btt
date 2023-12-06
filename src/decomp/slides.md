---
template: slides
---

## Goals

-   Most people learn better together than alone  [%b Michaelson2004 %]
-   *If* their team works well together
-   Good meetings are necessary but not sufficient ([%x meetings %])
-   Also have to decide who's doing what
-   And how to decide who's going to do what

---

<!--# class="aside" -->

## Agreement Matters Most

-   Roles can be fluid
-   Most important thing is that team members understand and accept their responsibilities
    and everyone else's [%b Barke2019 %]

---

## What We're Simulating

-   [%b Skelton2019 %] describes four ways to organize teams
-   Apply directly to software companies and research labs
-   Teams in courses should simulate

[% figure
   slug="topologies-topologies"
   img="topologies.svg"
   caption="Four kinds of teams."
   alt="Four kinds of teams: stream-aligned, enabling, platform, and complicated subsystem"
%]

---

## Stream-Aligned Team

-   Stream (n.) "the continuous flow of work aligned to a business domain or organizational capability"
-   So a **stream-aligned team** works on a single product, service, or set of features

1.  Define clear boundaries for what it's building
2.  Produce a steady flow of features and fixes
3.  Reach out to support teams as necessary

---

## Enabling Team

-   Specialists in a particular domain,
    e.g. accessibility or performance optimization
-   Helps stream-aligned teams that encounter problems they can't solve themselves

1.  Try to understand the needs of stream-aligned teams
    (rather than saying, "I have a hammer, so your problem must be a nail")
2.  Learn about new tools and methods
    *before* stream-aligned teams run into problems that need them
3.  Share knowledge as the border between specialized and common-place shifts

---

<!--# class="aside" -->

## Boundaries Move

-   Virtualization and cloud deployment used to be specialized skills
-   Now part of most developers' everyday lives
-   Enabling teams recognize these shifts and (re-)train members of stream-aligned teams

---

## Complicated Subsystem Team

-   Counterparts of enabling teams
-   Builds and maintains modules for product teams to use
    that they can't (easily) build for themselves
-   Biggest responsibility is to build the right thing
-   Very easy for subsystem teams to build what's technically interesting
    rather than what's useful

---

## Platform Team

-   Create internal services to keep everything else moving
-   In particular,
    allow stream-aligned teams to work consistently but independently
    -   Common for teams to choose different tools or methods to solve the same problem
    -   Creates maintenance and integration headaches down the road
-   Getting recognition for work is a challenge for enabling and platform teams
    -   "Nobody thinks about the sewer system until the toilet doesn't flush"
-   Unethical to recommend breaking things on purpose occasionally
    to remind everyone you exist…

---

## Collaboration

[% figure
   slug="topologies-interactions"
   img="interactions.svg"
   caption="Interactions between different kinds of teams."
   alt="Three kinds of interaction: collaboration, facilitation, and X-as-a-service"
%]

-   Collaboration: close partnership, usually between two teams at a time
-   X-as-a-service: one team acts as a customer for another
    -   Some organizations have one team buy services from another,
        which makes work visible but discourages collaboration
-   Facilitating: enabling team partners with stream-aligned team
    long enough to get obstacle out of the way

---

## Adaptation

-   Team Topologies model makes sense with multiple collaborating teams over long time
-   But courses are short…
-   …collaboration between teams makes evaluation much harder ([%x grading %])…
-   …and the point of a course is for people to learn
-   Want a model that prepares for the one above but works in the classroom

---

## Three Axes of Division

[% figure
   slug="decomp-division"
   img="division.svg"
   caption="Dividing work in a software team."
   alt="Modular, functional, and feature decomposition."
%]

1.  Layer of software (modular)
2.  Kind of work (functional)
3.  Value being delivered (feature)

---

## Modular Decomposition

-   Each person is responsible for one module of the program
    -   UI, data analysis, back-end interaction with database, etc.
-   Having people own parts of the code produces lower failure rates in industry [%b Bird2011 %]
-   A bad strategy in a course:
    1.  Leads to **big bang integration**, which almost always fails
    2.  Each team member only understands one module,
        so everyone is a single point of failure.

---

## Functional Decomposition

-   Each person is responsible for one type of task
    -   Design, coding, testing, deployment, etc.
-   Once again,
    everyone is a single point of failure
-   Unidirectional flow of annoyance:
    downstream team members have to live with whatever upstream team members decide to do

---

## Feature Decomposition

-   Each team member handles all aspects of development for one feature at a time
-   Gives everyone a chance to practice all their skills
-   But no one gets as far in any particular specialty
-   And integrating features developed in parallel can be painful

---

## Rotating Decomposition

-   People fill one role for a couple of weeks,
    a different role for the next two weeks,
    etc.
-   Resilient in the face of team turnover
-   And more people can participate in design/debugging sessions
-   But everyone is always ramping up

---

<!--# class="aside" -->

## Chaotic Decomposition

-   Unfortunately the most common approach in practice
-   Some things done multiple times or not at all
-   All other decompositions tend toward chaos under pressure
-   So establish good habits early
-   And stick to them when workload is light
-   So that the instinct to do the right thing will be there when you need it

---

## One Other Reason

-   If teams use modular or functional decomposition,
    self-appointed alpha geeks often snag the high-status work
    -   Shoulder people who aren't as pushy, privileged, or self-confident into lower-status roles
-   Lowers the team's overall grade
    -   Female students' ranking of fellow students is generally accurate
    -   Male students consistently over-estimate their male peers [%b Grunspan2016 %]

---

<!--# class="aside" -->

## Confirmation Loops

-   "[Women's work][womens_work]" or "[quarterback syndrome][quarterback_syndrome]"
    -   Two thirds of NFL players are Black but 83% of quarterbacks are white
-   Writing operating systems or training AI models
    has higher status than building user interfaces
-   People doing the former are both paid more and more likely to be male
    than people doing the latter,
    regardless of ability or value delivered to the employer
-   Creates a feedback loop:
    -   White/Asian men pursue careers with high status
    -   The fact that they are pursuing those careers maintains that status
-   Creates a confirmation loop
    -   Women and people of color get fewer chances to do certain tasks
    -   So they are less good at them, which "confirms" the initial bias

---

## "But I Haven't Seen That"

-   Some people have experienced this so often that
    they have come to accept it as the price they have to pay for being in tech
-   Those who protest are often dismissed as being "difficult"
-   Many take a third path and decide to leave the field
    -   Why play a game that's unfair?
-   **Survivor bias** 

---

<!--# class="aside" -->

## It Wasn't Always Thus

-   Programming was originally considered a female occupation
-   Only came to be viewed as a male occupation when it became more lucrative
    [%b Abbate2012 Ensmenger2012 Hicks2018 %]
-   What is "normal" changes over time
-   And can be changed deliberately

---

<!--# class="exercise" -->

## Division of Labor

1.  What are the pros and cons of your team trying
    two or more methods of work decomposition during your project?
2.  Since you'll only have time to try each once,
    and will be doing each for the time time,
    how will you know which struggles are intrinsic to the method
    and which are **learning effects**?
3.  Some schools have upper-year students act as team leads
    for groups in lower-year courses.
    What are the pros and cons of this approach?
