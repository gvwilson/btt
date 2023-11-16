---
title: "Issues"
tag: "FIXME"
syllabus:
- Use an issue tracker as a shared to-do list for a project.
- Label issues to help search and triage.
---

You probably have a to-do list somewhere. It might be scribbled in a calendar or
lab notebook, kept in a text file on your laptop, or in your head; wherever and
however you maintain it, it lists the things you're supposed to do, when they're
due, and (possibly) how urgent they are.

At its simplest, an issue tracker
is a shared to-do list. Issue tracking systems are also called
ticketing systems and bug trackers because most software projects use them to keep
track of the bugs that developers and users find. These days, issue trackers are
almost invariably web-based. To create a new issue, you enter a title and a
short description; the system then assigns it a unique serial number. You can
usually also specify:

-   what kind of issue it is (such as a bug report, a request for a new feature,
    or a question to be answered);

-   who is responsible for the issue (i.e., who's supposed to fix the bug, test
    the fix, or update the documentation);

-   how important it is; and

-   when it's due.

If version control keeps track of where your project has been, your issue
tracking system keeps track of where you're going. After version control, it is
the most important part of a team project; without it, you and your teammates
will have to constantly ask each other "What are you working on?", "What am I
supposed to be working on?", and "Who was supposed to do that?" Once you start
using one it's easy (or at least easier) to find out what the project's status
is: just look at the open issues and at those that have been closed recently.
You can use this to create agendas for your status meetings, and to remind
yourself what you were doing three months ago when the time comes to write your
final report.

Of course, a issue tracker is only as useful as what you put into it.  If you're
describing a bug in a large application, you should include enough information
to allow someone to reproduce the problem. This is why industrial-strength
systems like [Jira][jira] can have a couple of dozen fields for each issue, including:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on;

-   whatever stack traces, error reports, or log messages the program produced;

-   its severity (i.e., how much damage the bug might do); and

-   other issues that might be related.

This is a lot more information than student projects require. In addition,
students are almost always working on several courses at once, and it's common
for students to have to put their team project aside for a few days to work on
assignments for other courses. For these reasons, I've found that most student
teams won't actually use anything more sophisticated than a web-base to-do list
unless they're forced to by the grading scheme. In that case, most come away
with the impression that issues are something you only use when you have to.

So what does a good issue look like?  [%b Bettenburg2008 %] found that the
information users supply when they file a bug report tends not to be that which
the relevant developers need the most, and most importantly, it differs in
fairly predictable ways and for understandable reasons.  Here's one I filed for
the duplicate file finder reviewed in FIXME:

FIXME: example

The ID on the first line is assigned by the issue tracker, an often serves as a
shorthand name for the issue in conversation. ("Hey, is anyone working on number
fifty-five yet?") The date is in UTC
so that it is unambiguous: while your team may all be in one place, it's
increasingly likely that you are scattered across several time zones.

The title on line 3 is probably the most
important part of the issue. Projects will accumulate hundreds of issues over
time; a good subject line makes it much easier to find the ones you need. The
`type`, `severity`, and `labels` fields also improve
discoverability;
while `type` and `severity` could be labels, having them in fields of their own
makes it easier to sort and filter issues.

Finally, the description briefly
summarizes the problem. If the author hadn't already identified the cause, it
should include a reproducible example (also called a reprex). This helps the person understand what the
issue is much more than, "The program crashes when I open strange files," but
experience shows that if people are required to come up with a reprex when
filing an issue, they will often solve their own problem along the way.  We'll
talk more about the value of minimal reproducible examples in
FIXME.

<blockquote markdown="1">
### When to start saying "no"

As we will see in [%x process %], one purpose of a schedule is to tell you
when to start cutting corners. Similarly, one of the main reasons to keep
issues in
one place is to help you prioritize work when time starts to run short.
</blockquote>

## Labeling Issues

The bigger a project gets, the harder it is to find things.  Issue trackers
therefore let project members add labels to issues to make things easier to search
and organize.  Labels are also often called tags; whatever term is used, each
one is just a descriptive word or two.

GitHub allows project owners to define any labels they want.  A small project
should always use some variation on these three:

Bug
:   Something should work but doesn't.

Enhancement
:   Something that someone wants added to the software.

Task
:   something needs to be done, but won't show up in code (e.g., organizing the
    next team meeting).

Projects also often use:

Question
:   where is something or how is something supposed to work?  As noted above,
    issues with this label can often be recycled as documentation.

Discussion or Proposal
:   something the team needs to make a decision about or a concrete proposal to
    resolve such a discussion.  All issues can have discussion: this category is
    for issues that start that way.  (Issues that are initially questions are
    often relabeled as discussions or proposals after some back and forth.)

The labels listed above identify the kind of work an issue describes.  A
separate set of labels can be used to indicate the state of an issue:

Urgent
:   Work needs to be done right away.  (This label is typically reserved for
    security fixes).

Current
:   This issue is included in the current round of work.

Next
:   This issue is (probably) going to be included in the next round.

Eventually
:   Someone has looked at the issue and believes it needs to be tackled, but
    there's no immediate plan to do it.

Won't Fix
:   Someone has decided that the issue isn't going to be addressed, either
    because it's out of scope or because it's not actually a bug.  Once an issue
    has been marked this way, it is usually then closed.  When this happens,
    send the issue's creator a note explaining why the issue won't be addressed
    and encourage them to continue working with the project.

Duplicate
:   This issue is a duplicate of one that's already in the system.  Issues
    marked this way are usually also then closed; this is another opportunity to
    encourage people to stay involved.

Some projects use labels corresponding to upcoming assignments instead of
Current, Next, and Eventually.  This approach works well in the short term, but
becomes unwieldy as labels with names like `exercise-14` pile up.  Instead, a
project team will usually create a milestone, which is a set of issues
and pull requests in a single project repository.  GitHub milestones can have a
due date and display aggregate progress toward completion, so the team can
easily see when work is due and how much is left to be done.
