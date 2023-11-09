---
title: "Team Topologies"
tag: "FIXME"
syllabus:
- FIXME
---

In 1968,
Mel Conway published an article titled "How Do Committees Invent",
which included the first statement of what is now called Conway's Law [%b Conway1968 %]:
"Organizations which design systems…produce designs
which are copies of the communication structures of these organizations."
Less formally,
if you have four teams working on a web application,
you're going to wind up with a four-layer application.

As with so many things,
the explanation is rooted in the theory of cognitive load [%x cogload %]:
people can't keep track of what dozens of other people are doing,
so we have to break things into modules
so that everyone can focus on one part of the larger problem.
How we break things into modules determines what teams we need,
but equally,
what teams we create will determine what modules we produce.

<div class="callout" markdown="1">
### Counter-examples

People sometimes try to sound clever by saying that
nothing great was ever created by a committee.
The next time you hear this,
remind the speaker of the King James Bible and the US Constitution.
</div>

[%b Skelton2019 %] describes four ways to organize teams in software organizations,
which are shown in [%f topologies-topologies %].
When things are going well.
Lots of variations exist—in particular,
see [%b ODuinn2021 Skelton2022 %] for discussion of teams
that are mostly or fully distributed—but these patterns
should be a starting point for discussion.

[% figure
   slug="topologies-topologies"
   img="topologies.svg"
   caption="Four kinds of teams."
   alt="Four kinds of teams: stream-aligned, enabling, platform, and complicated subsystem"
%]

<div class="callout" markdown="1">
### But I don't work in a software company

The topologies described below were designed with companies in mind,
but you might be building something for a course,
contributing to an open source project,
or working in a research lab.
In the first case,
you, your teammates, and your instructor should decide
what kind of team you're pretending to be
and structure your work and deliverables accordingly.
In the other two cases,
you should ask yourself how you plan to interact with
the people using your software
and see if any of these topologies fit your needs.
</div>

## Kinds of Teams {: #topologies-teams}

[%b Skelton2019 %] defines "stream" as
"the continuous flow of work aligned to a business domain or organizational capability".
A *stream-aligned team* is therefore
one that works on a single product, service, or set of features.
Most teams in most organizations fall into this category:
they are responsible for building and maintaining a particular thing
over an extended period of time.
In practice,
this means the team is responsible for:

-   defining clear boundaries for what it's building;

-   producing a steady flow of features and fixes; and

-   reaching out to support teams as necessary.

An *enabling team* consist of specialists in a given technical domain,
such as accessibility requirements or optimizing code performance on GPUs.
Their purpose is to help steam-aligned teams
when those teams encounter problems they don't have the knowledge to solve themselves.
This translate into:

-   trying to understand the needs of stream-aligned teams
    (rather than saying, "I have a hammer, so your problem must be a nail");

-   learning about new tools and methods
    *before* stream-aligned teams run into problems that need them;
    and

-   sharing their knowledge as the border between specialized and common-place shifts.

The last point is often overlooked.
Virtualization and cloud deployment used to be specialized skills,
but are now ubiquitous.
A good enabling team will recognize shifts like that
and help train members of stream-aligned teams
to be productive in the brave new world.

*Complicated subsystem teams* are the counterparts of enabling teams.
While an enabling team brings expertise to bear on a stream-aligned team's current problem,
a complicated subsystem team is responsible for building and maintaining modules
for product teams to use
that they don't have the expertise to build for themselves.
Their biggest responsibility is to make sure that they're building the right thing:
it's very easy for subsystem teams to lose sight of what stream-aligned teams actually need
and build something that is technically interesting but not useful.

The final kind of team is a *platform team*
responsible for creating the internal services that keep everything else moving—in particular,
that allow stream-aligned teams to work independently of one another
but in the same ways.
One common mistake is for two teams to choose different tools or methods to solve the same problem,
which creates maintenance and integration headaches down the road;
a platform team should take over the work.

<div class="callout" markdown="1">
### Good plumbing is invisible

One challenge that platform teams face is getting recognition for their work:
if (for example) the CI/CD system is working,
everyone takes it for granted
without realizing how much maintenance effort it requires behind the scenes.
It would be unethical to recommend that
a platform team break things on purpose occasionally
just to remind everyone how valuable they are,
but the thought has crossed more than one person's mind…
</div>

## Interactions {: #topologies-collab}

The four kinds of teams described above
typically interact with each other in three well-defined ways
([%f topologies-interactions %]).

[% figure
   slug="topologies-interactions"
   img="interactions.svg"
   caption="Interactions between different kinds of teams."
   alt="Three kinds of interaction: collaboration, facilitation, and X-as-a-service"
%]

Collaboration
:   This mode is a close partnership,
    typically between a stream-aligned team
    and either an enabling team or a complicated subsystem team
    and most productively with only two teams involved at a time.

X-as-a-service
:   This mode is a producer-consumer relationship
    in which one team acts as a customer for another.
    Some organizations even structure the relationship this way,
    with one team "buying" services from another;
    doing this helps platform teams show their worth
    but can make other teams reluctant to make use of them.

Facilitating
:   Enabling teams typically do this to get one-of-a-kind obstacles
    out of the way of stream-aligned teams,
    e.g.,
    partner with the stream-aligned team long enough
    to implement the new updated revised (re-revised) spec for single sign-on.

<div class="callout" markdown="1">
### The next course

Teams in a software engineering course usually work independently,
which makes simulating these kinds of interactions hard.
However,
schools can create a two-course sequence
in which students in the first course work in the equivalent of stream-aligned teams
while students in the second course provide services.
Coordinating this is a lot of work,
and evaluation is hard ([%x grading %]),
but it's a great way for one cohort to pass on what they've learned to the next.
</div>
