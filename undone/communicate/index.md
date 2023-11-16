---
title: "Communicating"
tag: "Sharing information with teammates and managers"
syllabus:
- Include a short reproducible example in every bug report.
- Document the public interface of code.
- Embed documentation in code and use a documentation generator to format it.
- Create different documentation for novices, competent practitioners, and experts.
- Create a blog to summarize and discuss progress.
- Create FAQ entries by recycling users' questions.
---

## Other Ways to Communicate

Issues are the best way to keep track of where you are, but there are lots of
other ways the team can and should communicate. These can be synchronous, like chat and video calls, or
asynchronous, like issues and
email. The former are better for quick back-and-forth and for maintaining social
connections, but they can also be a constant stream of interruptions, which
lowers productivity (FIXME). Synchronous tools also tend to bias
communication in favor of people who are more self-confident, more fluent in the
language, or have better network connections, and finding things afterward in
archives of stream-of-consciousness exchanges is harder than finding things in
asynchronous media.

But who am I kidding? You're going to use instant messaging no
matter what I say.  If more than two people are in the conversation, follow the
same rules you would for a short meeting: post a summary of any decisions you
made where everyone can see it.

If you prefer fewer interruptions and longer periods of thought, you can always
go back to email, which has been used to run projects since the
1970s.  It brings content directly to people while allowing everyone to deal
with issues when it's convenient for them, and supports long-running
conversations. Email really comes into its own, though, when messages are routed
through a central mailing list, so that people don't have to remember to CC the
other five people on their team, and a shared archive can be created for later
searching. The second point is as important as the first: if you can't go back
and find out what was said a month ago—or, just as importantly, if someone
*else* can't do that—you might as well not have said it.

<blockquote markdown="1">
### Filters are your friend

Every email client allows you to set up
filters
that automatically flag messages matching
certain patterns or file them in particular mailboxes. I have fourteen of these
set up right now to organize messages belonging to particular projects; it only
took a couple of minutes, and it means that when I check mail in the morning or
after lunch, everything is set up for me to focus on one topic at a time.
</blockquote>

Software portals provide
many other ways to communicate, which project members use in a wide variety of
ways [%b Treude2011 %].  Wikis
seem like a good way to keep notes, create documentation, and so on. Their main
strength is the fact that content is automatically and immediately visible on
the web.  These days, you will probably get more mileage out of a bunch of
Markdown pages under version control—you have to set up a
repository anyway, and version control systems are much better at reconciling
conflicts between concurrent authors than wikis.

Blogs, on the other
hand, have proven more useful. One kind of project blog consists of articles
written by the team's members as a journal of their progress. This is most
useful for people who are watching the project from the outside, like
instructors.

The second kind of blog is one
created automatically by tools. In many project management systems, every
project has a blog.  Every time someone checks code into version control,
creates or closes an issue, or sends email, an entry is added to that blog. This
allows the project's members to see changes scroll by in their usual blog
reader, which is a handy way to keep track of what their teammates are doing.

If you are going to create a blog, use a static site generator to format and publish
content consistently.  On GitHub, for example, you can create a site with [GitHub Pages][github-pages] using a tool called [Jekyll][jekyll]; lots of
different themes are available, and there are many good tutorials online.

<blockquote markdown="1">
### Comments as communication

People don't usually think of comments
as a form of communication like email or
instant messaging, but if they are used properly, the only significant
difference is that the comments are right there in the code where the recipients
can't miss them rather than in an archive somewhere that they'll have to go and
search.  If you choose names for functions and variables carefully, the code
itself will explain what it's doing when someone reads it aloud; the comments
should therefore explain *why*, just as you would in an email.  For example,
this is not a useful comment:

```py
x = x[1:] # take all but first element of list
```

<!-- continue -->
This, on the other hand, tells the next person why we're doing it:

```py
threads = threads[1:] # We are already running the first thread, so save the others.
```
</blockquote>

## Reporting Up

As well as reporting progress to your teammates, you may have to report it regularly to your instructor, who
is effectively your manager. [Julia
Evans][evans-julia] has described [eight things your manager might not
know][evans-manager], all of which apply to student teams:

1.  What's slowing the team down.

1.  Exactly what individual people on the team are working on.

1.  Where the technical debt is.

1.  How to help you get better at your job.

1.  What your goals are.

1.  What issues they should be escalating.

1.  What extra work you're doing.

1.  How compensation/promotions work at the company.  (For students, this one
    translates to, "How grading actually works.")

[Jacob Kaplan-Moss][kaplan-moss-jacob] has a
similar guide to [giving a status update to executives][kaplan-moss-executives],
and [Ask a Manager][ask-a-manager] is full of good advice and discussion as
well. If you follow those guidelines, you get briefs like this:

> Project X is running smoothly. We're making steady progress: we've delivered a
> bit over half of the features on our roadmap, and we're on track to launch
> publicly in May.
>
> I want to particularly highlight J's design work; every time we share a new
> demo with our user research group they rave over how much they love the
> design.
>
> We do have some cost risk: right now, the code's pretty inefficient and would
> require us to increase our AWS spend by 25% when we put this into
> production. We either need to decide that cost is acceptable, or add some
> extra time to the schedule for performance optimization. I need some guidance
> from this team on that point: can you folks let me know if that cost seems OK
> or not?

If you learn how to summarize your status like this, you will be a very popular
team member.

## Documentation

An old proverb says, "Trust, but verify."  The equivalent in programming is, "Be
clear, but document."  No matter
how well software is written, it always embodies decisions that aren't explicit
in the final code or accommodates complications that aren't going to be obvious
to the next reader.  Putting it another way, the best function names in the
world aren't going to answer the questions "Why does the software do this?"  and
"Why doesn't it do this in a simpler way?"

In most cases, embedded documentation in
the form of a short docstring or doc comment to remind ourselves of each function's
purpose is probably as much documentation as we need.  (In fact, it's probably
better than what most people do.)  That one- or two-liner should begin with an
active verb and describe either how inputs are turned into outputs, or what side
effects the function has; as we discuss below, if we need to describe both, we
should probably rewrite our function.

An active verb is something like "extract", "normalize", or "plot".  Some
examples of good one-line docstrings include:

-   "Create a list of capital cities from a list of countries."
-   "Clip signals to lie in [0...1]."
-   "Reduce the red component of each pixel."

<!-- continue -->
You can tell our one-liners are useful if you can read them aloud in the order
the functions are called in place of the function's name and parameters.

Once you start writing code for other people (or your future self) your documentation should include:

-   The name and purpose of every public class, function, and constant in our
    code.

-   The name, purpose, and default value (if any) of every parameter to every
    function.

-   Any side effects the functions and methods have.

-   The type of value returned by every function or method.

-   What exceptions those functions can raise and when.

The word "public" in the first rule is important.  You don't have to write full
documentation for helper functions that are only used inside your package and
aren't meant to be called by users, but these should still have at least a
comment explaining their purpose.

As [%x cogload %] explains, we can divide people in any domain into
novices, competent practitioners, and experts.  Each of these three groups needs
a different kind of documentation:

-   A novice needs a tutorial that introduces her to key ideas one
    by one and shows how they fit together.

-   A competent practitioner needs reference guides,
    cookbooks, and Q&A sites; these give her solutions close enough to what she
    needs that she can tweak them the rest of the way.

-   Experts
    need this material as well—nobody's memory is perfect—but they may also
    paradoxically want tutorials.  The difference between them and novices is
    that experts want tutorials on how things work and why they were designed
    that way.

The first thing to decide when writing documentation is therefore to decide
which of these needs we are trying to meet.  Tutorials like this book should be
long-form prose that contain code samples and diagrams.  They should show people
things they actually want to do rather than printing the numbers from 1 to 10,
and should include regular check-ins so that people can tell if they're making
progress.

Tutorials help novices build a mental model, but
competent practitioners and experts will be frustrated by their slow pace and
low information density.  They will want single-point solutions to specific
problems, like how to find cells in a spreadsheet that contain a certain string
or how to configure the web server to load an access control module.  They can
make use of an alphabetical list of the functions in a library, but are much
happier if they can search by keyword to find what they need; one of the signs
that someone is no longer a novice is that they're able to compose useful
queries and tell if the results are on the right track or not.

## Creating an FAQ

As projects grow, documentation within functions alone may be insufficient for
users to apply code to their own problems.  One strategy to assist other people
with understanding a project is with an FAQ.  A good FAQ
uses the terms and concepts that people bring to the software rather than the
vocabulary of its authors; putting it another way, the questions should be
things that people actually search for online, not the things the program's
developers wish they would ask.

Creating and maintaining an FAQ is a lot of work, and unless the community is
large and active, a lot of that effort may turn out to be wasted, because it's
hard for the authors or maintainers of a piece of software to anticipate what
newcomers will be mystified by.  A better approach is to leverage sites like
[Stack Overflow][stack-overflow], which is where
most programmers are going to look for answers anyway.

The Stack Overflow guide to [asking a good
question][stack-overflow-good-question] has been refined over many years, and is
a good guide for any project:

Write the most specific title we can.
:   "Why does division sometimes give a different result in Python 2.7 and
    Python 3.5?"  is much better than, "Help! Math in Python!!"

Give context before giving sample code.
:   A few sentences to explain what we are trying to do and why it will help
    people determine if their question is a close match to ours or not.

Provide a minimal reprex.
:   Readers will have a much easier time figuring out if this question and its
    answers are for them if they can see *and understand* a few lines of code.

Tag, tag, tag.
:   Keywords make everything from scientific papers to left-handed cellos easier
    to find.  They are even more effective if the system encourages people to
    re-use tags so that they don't proliferate [%b Lin2020 %].

Use "I" and question words (how/what/when/where/why).
:   Writing this way forces us to think more clearly about what someone might
    actually be thinking when they need help.

Keep each item short.
:   Break everything down into single-page steps, with half of that page devoted
    to troubleshooting.  This may feel trivializing to the person doing the
    writing, but is often as much as a person searching and reading can handle.
    It also helps writers realize just how much implicit knowledge they are
    assuming.

Allow for a chorus of explanations.
:   Do not be afraid of providing multiple explanations to a single question
    that suggest different approaches or are written for different prior levels
    of understanding. This is one of the things that has made Stack Overflow so
    successful: if users are different from one another, they are best served by
    a chorus of explanations
    [%b Caulfield2016 %].

---

Knowing how to steer isn't enough to drive a car:
you need to know how to signal when you're turning or changing lanes.
Similarly,
knowing how to program isn't enough to build software:
you must coordinate with your teammates.

## To Do {: #communication-todo}

You probably have a to-do list somewhere.
It might be in a notebook,
on your phone,
or in your head,
but however you maintain it,
it lists the things you're supposed to do,
when they're due,
and how urgent they are.

An 
is a structured, shared to-do list.
(They are also called bug trackers
because programmers originally used them
to keep track of bugs they needed to fixed.)
While a team uses version control to record and share the project's history,
it should use an issue tracker to record and share the project's future.
Without it,
you and your teammates will constantly have to ask each other
"What are you working on?",
"What am I supposed to be working on?",
and "Who was supposed to do that?"

To create a new issue,
you enter a title and a short description;
the system then assigns it a unique serial number.
You can usually also specify:

-   what kind of issue it is,
    such as a bug report,
    a request for a new feature,
    or a question to be answered;

-   who is responsible for it
    (i.e., who's supposed to fix the bug);

-   how important it is; and

-   when it's due.

An issue tracker is only as useful as what you put into it.
Empirical studies find that if you are describing a bug,
the most important thing is to provide enough information for someone to reproduce the problem
[%b Zimmermann2010 Soltani2020 %].
This may include:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on; and

-   whatever stack traces, error reports, or log messages the program produced.

Here's a bug report for a tool that reads and merges spreadsheets:

FIXME

The ID on the first line is assigned by the issue tracker
and often serves as a shorthand name for the issue in conversation.
("Hey, is anyone working on number fifty-five yet?")
The timestamp is in 
because teams are increasingly scattered across several time zones.

The title is the most important part of the issue.
Projects can accumulate hundreds or thousands of issues over time;
a good subject line makes them easier to browse and search.
The `labels` improve ,
but are more important for triage (discussed below).

Finally,
the description briefly summarizes the problem.
A good description includes a short
 (or "reprex")
that explains how to reproduce the problem in the simplest way.
A reprex helps the reader understand the issue much better than,
"The program crashes when I open strange files."
Experience also shows that if people are required to come up with a reprex when filing an issue,
they will often solve their own problem along the way.

### Labeling and Triage

Using an issue tracker makes it much easier to summarize the project's status:
just look at issues that have been opened or changed since the last meeting.
You can use this to create the agenda for status meetings ([%x teams %])
and to remind yourself what you were doing three months ago
when you need to create a final report.

<div class="callout" markdown="1">

### Summarizing Makes You Think

Some teams use the issue tracker directly as the agenda for their status meetings.
However,
going through the issues and summarizing them once a week
is a good opportunity to do triage
and often reminds team members of things that *aren't* in the issue tracker.

</div>

The bigger a project gets, the harder it is to find things.
Most issue trackers therefore let people add  to issues
so that they will be easier to search and organize.

You can define whatever labels you want for issues.
A small project should always have:

Bug
:   Something should work but doesn't.

Change
:   Something should be added or modified.

Task
:   something needs to be done but won't show up in code
    (e.g., organizing the next team meeting).

<div class="callout" markdown="1">

### Issues versus pull requests

Some teams use the same labels for issues and pull requests,
but this leads to confusion:
does `Bug` mean a bug report or a bug fix?
Separate labels makes this clearer:
for example,
a project could use `Fix` to label pull requests that fix bugs
and `Enhancement` for ones that add new features.

</div>

Almost every project adds more labels to this basic set,
including things like:

Question
:   where is something or how is something supposed to work?
    Teams often turn these issues and their answers into FAQ entries
    (discussed below).

Proposal
:   something the team needs to discuss and make a decision about
    ([%x teams %]).

Urgent
:   Work needs to be done right away.
    (This label is typically reserved for security fixes).

Current
:   This issue is included in the current round of work.

Backlog
:   Someone has looked at the issue and believes it needs to be tackled,
    but there's no immediate plan to do it.

Won't Fix
:   Someone has decided that the issue isn't going to be addressed,
    either because it's out of scope or because it's not actually a bug.
    An issue marked this way is usually then closed.

Duplicate
:   This issue is a duplicate of one that's already in the system.
    Issues marked this way are usually also then closed.

<div class="callout" markdown="1">

### Milestones

Some projects use labels for upcoming assignments or releases
instead of labeling states like `Current` and `Backlog`.
This approach works in the short term,
but becomes unwieldy the number of assignments or releases grows.
Instead,
a team can create a 
to group a set of issues together.
Milestones can have a due date and show progress toward completion
so that the team can easily see how much work is left.

</div>

## Other Channels {: #communication-channels}

Issues are the best way to keep track of where you are,
but teams can and should communicate in other ways.
These channels can be fully synchronous like video calls,
fully asynchronous like email,
or somewhere in between like chat.
Synchronous channels are better for quick back-and-forth and for maintaining social connections,
but they bias communication in favor of people who are more self-confident,
more fluent in the language of discussion,
or have better network connections.
Additionally,
finding things afterward is hard or impossible.

If you prefer fewer interruptions and more time to think
you should use email.
It allows everyone to deal with issues when it's convenient for them
while supporting long-running conversations and findability.
Projects should always use mailing lists rather than person-to-person messages
so that people don't have to remember to CC the rest of the team
and to create a shared archive to search later.
The second point is as important as the first:
if you can't go back and find out what was said a month ago—or
if someone *else* can't do that—you might as well not have said it.

<div class="callout" markdown="1">

### Filters are your friend

Every email client allows you to set up 
that automatically move messages into specific folders.
I have fourteen of these set up right now
to organize messages belonging to particular projects;
it only took a couple of minutes to set up,
and it means I can focus on one problem at a time when checking mail.

</div>

Most teams now use semi-synchronous chat
like [Slack][slack] more than either video calls or email.
Chat combines the conversationality of a video call
with the ability to ignore messages without missing them
(and to edit a reply before sending it).
It also enables people to manage multiple parallel conversations like mail threads.
However,
chat is a more interruptive medium than email,
which means team members are less able to focus ([%x teams %]).
It also feels harder to find things in old chat conversations than in email archives,
in part because chat channels proliferate more rapidly than mailing lists.

Many teams now have bots send notifications when builds fail,
software is deployed,
or security vulnerabilities are detected.
These messages help maintain ,
but if they are frequent or usually don't require action,
team members quickly learn to ignore them.
We will discuss this more in [%x automation %].

However the team communicates,
it should have guidelines to ensure that
the conversation isn't dominated by its most self-confident members.
The tricks in [%x teams %] for ensuring that meetings are fair
apply here as well.
For example,
on one project I was involved in,
team members in the americas would sometimes wake up to find a thread
with fifty or sixty messages among two or three people in Europe.
This was so overwhelming that they would simply not try to catch up.
Once we brought in a rule saying,
"One message per person per thread per day,"
many more people began contributing,
and everyone's contributions became more thoughtful.

<div class="callout" markdown="1">

### How Did He Know?

In his 1961 story "[Harrison Bergeron][harrison_bergeron]",
Kurt Vonnegut
described a future in which everyone is forced to be equal.
Good-looking people have to wear masks,
athletic people have to wear weights,
and intelligent people
are forced to carry around radios that interrupt their thoughts at random intervals.

Slack and other instant messaging tools are our radios.

</div>

### Other Channels


like [Bitbucket][bitbucket], [GitHub][github], and [GitLab][gitlab]
provide many other ways to communicate,
which project members use in a wide variety of ways [%b Treude2011 %].
Wikis seem like a good way to keep notes,
create documentation,
and so on,
but if team members already know how to use version control,
they will get more mileage out of Markdown pages:
they can use commits to synchronize changes to documentation with changes to code
and pull requests provide an opportunity for review.

Blogs,
on the other hand,
are very useful.
Team members can blog regularly about their progress;
such a journal is useful for people watching the project from the outside,
like instructors,
but also serves as a live draft of a project's final report.

If you are going to create a blog,
use a 
to format and publish content consistently.
[GitHub Pages][github_pages] uses
a Ruby-based tool called [Jekyll][jekyll],
but [every language provides alternatives][ssg_list].

## Documentation {: #communication-documentation}

An old proverb says, "Trust, but verify."
The equivalent in programming is,
"Write clear code, but document."
No matter how well software is written,
it always embodies decisions that aren't explicit
or accommodates complications that won't be obvious to the next reader.
Putting it another way,
the best function names in the world aren't going to answer the question,
"Why does the software do this?"

We can divide people in any domain into novices, competent practitioners, and experts
[%b Wilson2019 %].
Each group needs a different kind of documentation:

-   A novice
    needs a tutorial that introduces key ideas one by one
    and shows how they fit together.

-   A competent practitioner
    needs reference guides, cookbooks, and Q&A sites
    with solutions close enough to what she needs
    that she can tweak them the rest of the way.

-   Experts
    need guides as well—nobody's memory is perfect—but they also want
    discussions of alternatives and tradeoffs.

No documentation can serve all three groups equally well.
Tutorials help novices build a ,
but competent practitioners will be frustrated
by their slow pace and low information density.
They want single-point solutions to specific problems,
and are able to search for what they need.

### Creating an FAQ

A good FAQ uses the terms and concepts that people bring to the software
rather than the vocabulary of its authors.
The questions are things people actually search for online,
not things the program's developers wish they would ask.

Creating and maintaining an FAQ is a lot of work.
A lot of that effort may be wasted
because it's hard for the authors or maintainers of a piece of software
to anticipate what newcomers will be mystified by.
A better approach is the "answer on demand" approach of [Stack Overflow][stack_overflow].
Its guide to [asking a good question][stack_overflow_good_question] is:

Write the most specific title you can.
:   "Why does division sometimes give a different result in Python 2.7 and Python 3.5?"
    is much better than, "Help! Math in Python!!"

Give context before giving sample code.
:   A few sentences to explain what you are trying to do and why
    helps people determine if their question matches the one in the article.

Provide a minimal reprex.
:   Readers will have a much easier time figuring out
    if this article matches their question
    if they can see a few lines of code.

Tag, tag, tag.
:   Keywords make everything easier to find.
    They are even more effective if the system encourages people to re-use tags
    so that they don't proliferate [%b Lin2020 %].

Use "I" and question words (how/what/when/where/why).
:   Writing this way forces people to think more clearly
    about what they're actually asking.

Keep each answers short.
:   Break every answer down into single steps
    and devote half of each answer to troubleshooting.
    Doing this may feel trivializing if you already know the answer,
    but is often as much as a person searching and reading can handle.
    It also helps writers realize just how much implicit knowledge they are assuming.

Allow for a chorus of explanations.
:   Do not be afraid of providing multiple explanations to a single question
    that suggest different approaches
    or are written for different prior levels of understanding.
    This is one of the things that has made Stack Overflow so successful:
    different users are best served by a chorus of explanations
    [%b Caulfield2016 %].

### Documenting Code

Every language has 
that extract information from   or 
and produces cross-indexed HTML pages.
Programmers believe they are more likely to update
embedded documentation like this
because it is right there with the code
instead of in a separate file.

Each piece of embedded documentation should begin with an active verb
like "extract" or "normalize"
and describe either how inputs are turned into outputs
or what side effects the function has.
Some examples of good one-line docstrings are:

-   "Create a list of capital cities from a list of countries."
-   "Clip signals to lie in [0...1]."
-   "Reduce the red component of each pixel."

Once you start writing code for other people
your documentation should include:

-   The name and purpose of every public class, function, and constant.

-   The name, purpose, and default value (if any) of every parameter.

-   Any side effects the functions and methods have.

-   What value every function or method returns.

-   What exceptions those functions can raise and when.

The word "public" in the first rule is important.
You don't have to write full documentation for helper functions
that are only used inside your package,
but these should still have at least a one-liner explaining their purpose.

### Comments as Communication

People don't usually think of code comments
as a form of communication like email or chat,
but the only significant difference is that
the comments are right there in the code where the recipients can't miss them
rather than in an archive somewhere that they'll have to go and search.
If you choose names for functions and variables carefully,
the code itself will explain *what* it's doing when someone reads it aloud.
The comments should therefore explain *why*.
For example, this is not a useful comment:

```py
x = x[1:] # take all but first element of list
```

This, on the other hand, tells the next person why we're doing it:
{: .continue}

```py
threads = threads[1:] # First thread is already running so save the others.
```

## Code Reviews {: #communication-reviews}

People usually don't think of  as a kind of communication either,
but they are one of the most effective ways to share knowledge within a team.
There's no point creating PRs if they are all merged as-is.
One study after another since the mid-1970s has proven that
code review is the most cost-effective way to find bugs in software [%b Cohen2010 %].

<div class="callout" markdown="1">

### Do more eyes make for fewer bugs?

Some people have claimed that many eyes make all bugs shallow
(i.e., easy to find)
but the evidence doesn't support that claim.
For example,
[%b Meneely2014 %] found that,
"…source code files reviewed by more developers are,
counter-intuitively,
more likely to be vulnerable (even after accounting for file size).
However,
files are less likely to be vulnerable
if they were reviewed by developers
who had experience participating on prior vulnerability-fixing reviews."
In short, *whose* eyes matters more than how many.

</div>

There are many guides online for doing code reviews,
most of them based on individual experience.
A notable exception is the [SmartBear guide][smartbear_code_review],
which draws on a large study of code review in industry.
The rules below present some of their findings
with modifications for students' situations.

Have the instructor do a demonstration review.
:   Even if you have done code reviews before,
    you may not know what's expected for this course.
    The instructor can show you by putting up some sample code and going through it,
    thinking aloud as they notice things worth commenting on
    so that you have an idea of how much detail they expected.

Authors should clean up code before review.
:   If the person creating the PR goes through and adds some more comments,
    cleans up some variable names,
    and does a bit of refactoring,
    they won't just make reviewing easier:
    the odds are very good that they will find and fix a few problems on their own.

Review at most 200 lines of a code at a time.
:   The SmartBear guide recommends reviewing at most 400 lines at a time,
    which should take 60–90 minutes.
    You will probably get there eventually,
    but in our experience it's better to start with something smaller
    and work up to that.
    A corollary of this rule is that no PR should be more than 200 lines long.
    If one is,
    the odds are that reviewers won't be able to hold it all in their head at once and so will miss things.

Use checklists.
:   [%b Gawande2011 %] popularized the idea that
    using checklists
    improves results even for experts.
    While [%b Hatton2008 %] found no evidence that they made a difference to code reviews by professionals,
    I have found them very useful as a starter for students.
    If you are new to code reviews,
    ask the instructor for a list of the dozen most common problems to check for;
    anything more than that is likely to be overwhelming.
    (The code quality rubric developed in [%b Stegeman2014 Stegeman2016 %] is a good starting point.)
    If you and your teammates have been working together for a while,
    look at your own code reviews and make a list of the things that keep coming up.
    Having the list will make you more aware of the issues while you're coding,
    which in turn will make you less likely to keep making the same mistakes.

Look for algorithmic problems first.
:   Code review isn't primarily about style:
    your linter should catch those problems.
    Code review's real purpose is to find bugs before they can affect anyone.
    The first pass over any change should therefore look for algorithmic problems.
    Are the calculations right?
    Are any rare cases going to be missed?
    Are errors being caught and handled?

Offer alternatives.
:   Telling authors that something is wrong is helpful;
    telling them what they might do instead is more so.

Don't  or pass judgment.
:   "Gosh, didn't you know [some obscure fact]?" isn't helpful;
    neither is,
    "Bloody hell, why don't you just [some clever trick] here?"

Don't overwhelm people with details.
:   If someone has used the letter `x` as a variable name in several places,
    and they shouldn't have,
    comment on the first two or three and
    put a check beside the others—the reader won't need the comment repeated.

Don't try to sneak in feature requests.
:   Nobody enjoys fixing bugs.
    Asking them to add entirely new functionality while they're at it is rude.

Follow up.
:   The author of the code doesn't have to accept every suggestion,
    but should have a better reason than "I don't want to" for rejecting any of them.
    GitHub and other platforms allow people to create discussion threads for each comment,
    and will mark threads as being out of date when the pull request is updated.
    Whoever did the review should then scan the changes to make sure their points have been addressed,
    and to give themselves a chance to learn a few more things from the author.

Don't tolerate rudeness.
:   Most code review guidelines say, "Be respectful."
    The problem is that if you are,
    you probably don't need to be told that,
    and if you aren't,
    those two works alone won't change your behavior.
    What *will* is teammates defending the victims of rudeness by telling the offender,
    "That's not how we speak to each other."

How we respond to reviews
is just as important:

Be specific in replies to reviewers.
:   If someone has suggested a better variable name you can simply fix it.
    If someone has suggested a major overhaul to an algorithm
    you should reply to their comment to point at the commit that includes the fix.

Thank your reviewers.
:   If someone has taken the time to read your code carefully, thank them for doing it.

So what does a code review actually look like?
Here's a Python program that searches for duplicated files
with comments added to show review.

FIXME

## Reporting {: #communication-reporting}

As well as reporting progress to your teammates,
you may have to report it regularly
to your instructor or manager.
[Julia Evans][evans_julia] described
[eight things your manager might not know][evans_manager], all of which apply to student teams:

1.  What's slowing the team down.

1.  Exactly what individual people on the team are working on.

1.  Where the  is.

1.  How to help you get better at your job.

1.  What your goals are.

1.  What issues they should be escalating.

1.  What extra work you're doing.

1.  How compensation/promotions work at the company. (For students, this one translates to, "How grading works.")

[Jacob Kaplan-Moss][kaplan_moss_jacob]
has a similar guide to [giving a status update to executives][kaplan_moss_executives],
and [Ask a Manager][ask_a_manager] is full of good advice and discussion as well.
These guidelines produce briefs like this:

> Project X is running smoothly.
> We're making steady progress: we've delivered a bit over half of the features on our roadmap,
> and we're on track to launch publicly in May.
>
> I want to particularly highlight J's design work.
> Every time we share a new demo with our users
> they rave over the design.
>
> We do have some cost risk:
> right now the code is pretty inefficient
> and would require us to increase our AWS spend by 25% in production.
> We either need to decide that cost is acceptable
> or add some extra time to the schedule for performance optimization.
> Please let us know which you prefer.

If you learn how to summarize your status like this,
you will be a very popular team member.

## Exercises {: #communication-exercises}

FIXME
