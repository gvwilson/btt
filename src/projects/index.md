---
title: "Projects"
tag: "FIXME"
syllabus:
- FIXME
---

Let's take a closer look at what you're supposed to be doing.
On one side are homework assignments related to recently-taught material
that you are meant to solve in a week or two.
On the other side are internships or co-op terms
in which you work part- or full-time,
and in between are courses with names like "Introduction to Software Engineering",
"Senior Thesis Project",
or "Computer Science Capstone",
which are the focus of this book.
These courses share three characteristics:

1.  Learning how to work in a team is an explicit goal
    (versus courses in which
    you work in a team but are not taught how to do so).

2.  Your grade depends on how you work as well as what you build.

3.  You are supposed to work as if you were part of real project.
    You might start with a blank sheet of paper
    or have to fix and extend an existing application,
    but you and your team are responsible for some or all of
    requirements analysis,
    design,
    implementation,
    testing,
    documentation,
    packaging,
    deployment,
    handoff,
    and review.

Project courses exist for several reasons:

To teach you things that can only be learned by doing.
:   You can't learn how to build software in a team by listening to lectures
    any more than you can learn to ride a bike
    by watching the Tour de France on TV.

To give you a change to apply things you learned in earlier courses,
:   i.e.,
    to demonstrate that trees, pointers, joins, and semaphores
    are actually good for something.

Because they're fun.
:   At least, if they're done right.

One goal of project courses is to move learners from left to right in
[%f projects-models %].
The instructor's job is to mentor rather than to lecture;
most of the learning will take place in the team or on your own.
Using the terms of [%x learners %],
a project course is where your school starts treating you like a competent practitioner
rather than like a novice.

[% figure
   slug="projects-models"
   img="four-models.svg"
   caption="Four models of instruction"
   alt="Four models of instruction that shift control from instructors to learners."
%]

There are as many ways to run a project course as there are instructors teaching them [%b Fincher2001 %].
The most important variable is whether your team has an actual customer or not.
Finding and interviewing people who actually want software built
and then meeting their needs
is tremendously rewarding,
but coordinating this is a lot of work for the course organizer.
Most team projects therefore tend to be made up by instructors.

Another option is to have students contribute to an existing open source project.
Doing this is easier than finding a local company that wants its web site rejigged,
and is an opportunity for students to meet other developers,
but it only works well if the course instructor is familiar with the projects' internals,
or if the projects' leads are willing and able to devote time
to mentoring a wave of newcomers.
In practice,
this approach is just as much work as partnering with a company or non-profit.

## Elevator Pitch {: #projects-pitch}

Once you know where the goalposts are,
the next thing is to get everyone to agree on what you're supposed to accomplish.
The best way to do this is write an elevator pitch
like the one below
to figure out what problem you're trying to solve,
who it affects,
and why your solution is a good one.

<blockquote markdown="1">
**The problem of**
developing software in a predictable and reliable manner
**affects**
the management of software projects.
Developers are not able to predict reliably how long it takes them to complete tasks
which makes it impossible to effectively plan a project.
**As a result,**
users and managers are never sure whether the produced software will meet its requirements,
how reliable the software will be,
or whether the software will be delivered on time.

**A successful solution would**
help developers become more aware of what they do,
how they spend their time,
and the kinds of defects they find in their work.
**For**
software development teams
**who**
need to better understand how and when defects are introduced into their products,
**our product**
gathers and reports performance metrics
**in order to**
help developers track and analyze personal software development metrics.
**Unlike**
not gathering data or trying to gather it manually,
**our approach**
helps users gather data unobtrusively
and provides objective feedback that allows them to improve both individual and team performance.
</blockquote>

Have everyone on the team fill in the template independently
and then compare the results.
If your team is like most I've worked with,
you'll be surprised by how varied the answers are.
Once you have done that,
pick one and turn it into a short paragraph like the one below that everyone is happy with:

<blockquote>

Most programmers can't predict how long it will take them to do things
because they don't know how long previous tasks have taken.
Gathering data manually is annoying enough that programmers won't do it,
so we're building a tool that will monitor what applications they use
and how long they use them.
This feedback will help them improve their working habits
and allow them to give their managers more accurate input for scheduling.

</blockquote>

You now have the abstract for your final report.

An alternative to writing an elevator pitch is to build the product's home page,
i.e., to make up the website for your software as if it already existed.
What catchphrase would you put across the top to catch people's eyes?
What features would you list on the back
to make your software more appealing than its competitors?
What would its system requirements be?
Its license?
Its price?
Once your team agrees on these things,
you're ready to start designing and coding.
