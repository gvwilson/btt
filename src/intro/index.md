---
title: "Introduction"
tag: "What this book talks about and why."
syllabus:
- Our goal is to help you become a compassionate programmer.
- Nothing in software engineering makes sense except in the light of psychology.
- We know more about programs, programmers, and programming from empirical studies than most people realize.
- Good programmers aren't ten times more productive than average, but it's fair to say they are four times better.
---

Programming is often portrayed as a solitary activity,
but real applications are always the work of many people.
The aim of this book is therefore to show you
how to build software as part of team.

Our goal is to help you become a *compassionate programmer*:
one who cares about the wellbeing of their colleagues,
their users,
and society as a whole.
This focus is not entirely altruistic—everything you do to help others
also helps your future self—but now that we know how much harm software can do,
we need to build it better.

## Audience {: #intro-audience}

These learner personas describe who this book is for:

-   *Yani* is in the third year of a computer science degree.
    She worked on volunteer projects in high school and at her mosque,
    but the "Introduction to Software Engineering" course she's about to take
    will be the first time she has built software with other people.
    This book will help her and her teammates figure out who should do what, when.

-   *Sharla* has taught Yani's software engineering class twice.
    Each time,
    they came away feeling that
    their students had wasted time on things that weren't useful
    and hadn't learned things that would be.
    This book will help them restructure that course.

-   *Avi* taught himself most of what he knows about programming
    while doing a graduate degree in biology.
    He has just started his first non-academic job as a data scientist,
    where he will be building software with other people for the first time.
    This book will help him understand what's expected of him
    and how to collaborate with his new colleagues.

This book can be read on its own or as a companion to [%b Wilson2022 %].
(If you are looking for a course project,
please consider adding a tool to the ones it covers.)

## Themes {: #intro-theme}

Much of what's hard about building software stems from
the way our brains work [%b Hermans2021 %],
and in particular from our limited mental capabity ([%x cogload %]).
One theme of this book is therefore
this modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

Another theme is that
we know a lot more about software and how to build it
than most people realize.
Empirical studies of programs, programmers, and programming date back more than fifty years,
but their findings are rarely discussed in undergraduate classes.
As a result,
most books on how to program are a mix of personal experience and received wisdom,
which is usually just someone else's personal experience repackaged as a universal truth.
We therefore cite research findings to back up our claims where we can.

<div class="callout" markdown="1">
### Why does everything take so long?

[%b Sedano2017 %] found that software development projects have nine types of waste:
building the wrong feature or product,
mismanaging the backlog,
rework,
unnecessarily complex solutions,
extraneous cognitive load ([%x cogload %]),
psychological distress,
waiting and multitasking,
knowledge loss,
and ineffective communication.
*None of these are software issues,*
so if you only think about the code in your project and not about the people writing it,
everything will take longer and hurt more than it needs to.
</div>

Our third theme is that the software we build is shaped by
the organizations in which we build it,
and shapes them in turn [%b Cataldo2008 %].
How you run a meeting determines whose opinions are heard,
which in turn determines the architecture that emerges from those meetings.
How programmers (and others) are evaluated determines
whether they thrive in their jobs or not [%b Hicks2023 %],
and the tools that allow people to build communities online
are used to amplify hate for profit.

## Licensing {: #intro-license}

All of the written material on this site is made available
under the Creative Commons-Attribution-NonCommercial 4.0 International license
([CC-BY-NC-4.0][cc-by-nc]),
which allows you to use and remix this material for non-commercial purposes,
as-is or in adapted form,
provided you cite its original source.
Please see [%x license %] for details.

Parts of these lessons originally appeared in [%b Sholler2019 Wilson2019 Irving2021 Smalls2021 %];
I'm grateful to [Taylor & Francis][taylor-francis],
[PLoS][plos],
and my co-authors for allowing that material to be re-used under open licenses.

## Acknowledgments {: #intro-ack}

This book is dedicated to [Marian Petre][petre-marian],
who taught me that not everything worth studying can be measured,
and to Tom Wilkie,
who taught me how to turn a thousand words I'd written into a hundred someone would actually want to read.
I also thank all of the students who have done projects with me over the years,
and the people mentioned below for their feedback;
any errors, omissions, or misunderstandings that remain are entirely my fault.

[% thanks width=5 %]

Finally,
I would like to thank David Graf for [doi2bib][doi2bib]
and Alexandra Elbakyan for [Sci-Hub][sci-hub]:
this book would have been much harder to write without their idealism and hard work.
