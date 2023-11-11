---
title: "Structure"
tag: "FIXME"
syllabus:
- FIXME
---

All right:
you have some idea of what you're going to build.
How should you organize the project itself?

Every language has its own conventions for what files should go where in a project,
for the simple reason that they all need different files.

FIXME: explain structure of two different kinds of projects.

In all cases,
learning what goes where is like learning when to signal when driving a car:
the rules may vary from place to place,
but everywhere *has* rules,
and knowing them will help prevent you from crashing.

## Standard Files {: #structure-standard}

Regardless of language or packaging system,
every project should have a handful of standard files in its root directory.
These may have UPPERCASE names without an extension,
or may be plain text (`.txt)` or Markdown (`.md`) files.

`README.md`
:   A brief overview of the project that often serves as its home page online.

`CONTRIBUTING.md`
:   How to contribute to the project.
    Should people file an issue when they have a question,
    email a list,
    or post something on chat,
    and if so, where?
    What code formatting conventions does the project use?
    Research shows that clear contribution guidelines increase the odds of people contributing
    ([%b Sholler2019 %]);
    in my experience,
    they also reduce friction between team members.

`CODE_OF_CONDUCT.md`
:   The project's Code of Conduct,
    i.e.,
    how people are required to treat one another.
    As we'll discuss below,
    "be polite" or "use your common sense" aren't enough.

`LICENSE.md`
:   Describes who can do what with the project materials.
    We discuss various options in [%x property %].

`GOVERNANCE.md`
:   FIXME: discussed in [%x governance %].

## Code of Conduct {: #structure-conduct}

In order to get people to contribute,
it must do more than allow them:
it has to be clear that the teams *wants* contributions.
Saying "the door is open" is not enough,
since many people have painful personal experience of being less welcome than others.
A project must therefore acknowledge that some people are treated unfairly in society
and actively take steps to remedy this:

-   It reassures people who have experienced harassment or unwelcoming behavior before
    that this project takes inclusion seriously.

-   It ensures that everyone knows what the rules are.
    What you think is polite or common sense depends on where you are from;
    since many projects have participants from different backgrounds,
    making the rules explicit avoids angry arguments starting with,
    "But *I* thought that…"

-   It prevents people who misbehave from feigning ignorance,
    i.e.,
    claiming after they say or do something offensive
    that they didn't realize it was out of bounds or that they were "just kidding".
    FIXME: Schrodinger's Asshole

Having a Code of Conduct is an empty gesture if you don't also have a way to respond to violations.
[%b Aurora2018 %] describes how,
and learning the basics is a good first step toward becoming an ally.

<div class="callout" markdown="1">
### What they really mean

In the early 2010s a lot of open source developers resisted the adoption of codes of conduct,
saying that they were unnecessary or that that they infringed freedom of speech.
What they usually meant (and what the few people still arguing against them usually mean)
is that thinking about how they have benefited from past inequity makes them feel uncomfortable.
If having a Code of Conduct makes people like this decide to go elsewhere,
your project will be better off.
</div>
