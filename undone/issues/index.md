---
title: "Issues"
tag: "FIXME"
syllabus:
- Use an issue tracker as a shared to-do list for a project.
- Label issues to help search and triage.
---

You probably have a to-do list somewhere.
It might be scribbled in a calendar or lab notebook,
kept in a text file on your laptop,
or in your head;
wherever and however you maintain it,
it itemizes the things you're supposed to do,
when they're due,
and (possibly) how urgent they are.

At its simplest,
an issue tracker is a shared to-do list.
Issue tracking systems are also called ticketing systems and bug trackers
because most software projects use them
to keep track of the bugs that developers and users find.
These days,
issue trackers are almost invariably web-based.
To create a new issue,
you enter a title and a short description;
the system then assigns it a serial number for reference.
You can usually also specify:

-   what kind of issue it is
    (such as a bug report,
    a request for a new feature,
    or a question to be answered);

-   who is currently responsible for it;

-   how important it is; and

-   when it's due.

If version control keeps track of where your project has been,
your issue tracking system keeps track of where you're going.
After version control,
it is the most important part of a team project:
without it,
you and your teammates will have to constantly ask each other
"What are you working on?",
"What am I supposed to be working on?",
and "Why didn't this get done?"
Once you start using one it's easy (or at least easier)
to find out what the project's status is:
just look at the open issues and at those that have been closed recently.
You can use this to create agendas for your status meetings,
and to remind yourself what you were doing three months ago
when the time comes to write your final report.

But a issue tracker is only as useful as what you put into it.
If you're describing a bug in a large application,
you should include enough information to allow someone to reproduce the problem.
This is why industrial-strength systems like [Jira][jira]
can have a couple of dozen fields for each issue,
including:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on;

-   whatever stack traces, error reports, or log messages the program produced;

-   its severity (i.e., how much damage the bug might do); and

-   other issues that might be related,
    such as whether the person filing the bug report was left- or right-handed.

This is a lot more information than student projects require.
In addition,
students are almost always working on several courses at once,
and it's common for students to have to put their team project aside for a few days
to work on assignments for other courses.
For these reasons,
I've found that most student teams won't actually use
anything more sophisticated than a web-base to-do list
unless they're forced to by the grading scheme.
In that case,
most come away with the impression that
issues are something you only use when you have to.

<blockquote markdown="1">
### When to start saying "no"

As we will see in [%x process %],
the real purpose of a schedule is to tell you when to start cutting corners.
Similarly,
the main reason to keep issues in one place
is to help you prioritize work when time starts to run short.
</blockquote>

## Formatting Issues {: #issues-format}

So what does a good issue look like?
[%b Bettenburg2008 %] found that
the information users supply when they file a bug report
tends not to be what developers need the most,
but it differs in fairly predictable ways and for understandable reasons.
Here's one I filed for a simple image editing tool:

[% inc "initial_bug_report.txt" %]

The ID on the first line is assigned by the issue tracker.
The date is in UTC so that it is unambiguous:
even student teams can now be scattered across several timeszones.

The title on line 3 is the most important part of the issue.
Projects can accumulate hundreds of issues over time;
a good subject line makes it much easier to find the ones you need.
The `type`, `severity`, and `labels` fields also improve discoverability;
the type and severity could just be more labels,
but having them in fields of their own makes things easier to sort and filter.

Finally,
the description summarizes the problem.
In this case,
the summary is a reproducible example, or reprex,
which helps the person understand the issue much better than,
"The program changes files when I save them."
Experience shows that if people are required to come up with a reprex when filing an issue,
they will often solve their own problem along the way.

## Labeling Issues {: #issues-labeling}

Labeling issues makes things easier to find.
Most systems allow people to define their own labels,
which means that some people spend as much time arguing over labels
as they do writing code.
A small project can get by with just three:

Bug
:   Something should work but doesn't.

Enhancement
:   Someone wants something added or changed.

Task
:   Something needs to be done but won't show up in code
    (e.g., organizing the next team meeting).

It also helps to have:

Question
:   Where is something or how is something supposed to work?
    These issues often turn into threaded discussions
    which in turn often become documentation.

Discussion or Proposal
:   something the team needs to make a decision about or a concrete proposal to
    resolve such a discussion.  All issues can have discussion: this category is
    for issues that start that way.  (Issues that are initially questions are
    often relabeled as discussions or proposals after some back and forth.)

<div class="callout" markdown="1">
### Findability again

One mistake people at all levels of experience make
is to have conversations in chat instead of in issues.
The problem is that several conversations are usually interleaved in chat,
and that it often evaporates after a few months.
A one-semester project can survive that,
but larger and longer-lived projects will eventually spend much of their time re-discovering things,
particularly if there is turnover or if contributors are volunteers.
</div>

The labels listed above identify the kind of work an issue describes.
A separate set of labels can be used to indicate the state of an issue:

Urgent
:   Work needs to be done right away.
    (This label is typically reserved for security fixes).

Current
:   This issue is included in the current round of work.

Closed
:   Someone has looked at the issue and believes it is done.
    Closed issues can usually be reopened later if someone else disagrees.

Won't Fix
:   Someone has decided that the issue isn't going to be addressed,
    either because it's out of scope or because it's not actually a bug.
    Once an issue has been marked this way, it is usually then closed.

Duplicate
:   This issue is a duplicate of one that's already in the system.
    Issues marked this way are usually also then closed.

Some projects use labels corresponding to upcoming assignments or deadlines.
This approach works well in the short term,
but becomes unwieldy as labels with names like `exercise-14` pile up.
Instead,
a project team will usually create a milestone,
which is a set of issues and pull requests in a single project repository.
Milestones can have a due date and display aggregate progress toward completion,
so the team can see how far behind they are.

[% fixme
   "who labels issues and allocates tickets is effectively running the project"
   "state transition diagram"
%]
