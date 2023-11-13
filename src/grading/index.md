---
title: Grading
tag: "FIXME"
syllabus:
- FIXME
---

Many organizations make the mistake of focusing on outputs rather than on outcomes [%b Perri2018 %].
In software teams this often takes the form of measuring progress by the number of features added to a product
rather than by whether changes to the code are actually making people's lives easier.
Claims like "80% of people only use 20% of a product's features" are often optimistic
(FIXME citation):
in most cases,
people learn just enough to accomplish the task at hand
and only discover more intermittently and accidentally if at all.

The equivalent mistake in a project course
is to measure progress by how much code you have written
rather than by how your work compares to the grading scheme.
Doing this doesn't mean you should only do things that are going to show up on your transcript,
but keep in mind that your actual product isn't your software:
it's your grade.

The first step in any project is therefore to figure out where the goalposts are.
In a company,
your boss should tell you what you're responsible for
and the HR department should tell you what the criteria are
for retention, promotion, and bonuses.
Again,
you shouldn't do only those things,
but if you're going to drop any or put time elsewhere,
you should do it with your eyes open.

<div class="callout" markdown="1">
### Co-operatives

FIXME: explain how they're different
</div>

In a project course,
your grade is typically based on:

The software you produce.
:   Does it build and run?
    Does it meet the customer's requirements
    (or the instructor's specifications if you don't have a real customer)?
    Is the source code readable?
    Is the program efficient?
    (Using an exponential algorithm instead of one that runs in linear time
    certainly *ought* to cost you marks…)

The process you followed.
:   Some instructors insist you use an analyze-design-code-test methodology.
    Others structure the course around short sprints
    (typically a couple of weeks long)
    during which you refactor the application, extend it, test your changes, and deploy the new version.
    Since instructors can't watch over your shoulder while you're working,
    they can't actually grade you on whether or not you follow a prescribed process.
    The best they can do is grade you on the artifacts that process is supposed to produce (discussed below).
    Since these can always be created after the fact,
    it's very tempting to just put your head down and code.
    Resist—any process is better than chaos,
    and sticking to what the instructor asked for will at least save arguments within the team.

Final deliverables.
:   This may be a retrospective ([%x retro %]),
    a demo ([%x demo %]),
    or the "final" state of the project ([%x delivery %]).

A final exam.
:   This may focus on the theoretical side of the course
    ("Describe the four main functions of Quality Assurance…")
    but smart instructors will include some questions
    to test your understanding of *your* project
    to determine who actually did the work and who was hitchhiking ([%x teams %]).

<div class="callout" markdown="1">
### How much of what?

[%b Spinellis2007 %] looked at how much content of different kinds
went into the FreeBSD project in 2006.
[%t evaluation-spinellis-stats %] doesn't divide "source code" into "application code" and "tests",
but it's still an eye-opener.

[% table
   slug="evaluation-spinellis-stats"
   tbl="spinellis-stats.tbl"
   caption="Distribution of effort and artefacts in FreeBSD 2006."
%]
</div>

The list below is a grading scheme for a typical one-semester project course:

Prototyping (10%)
:   This warmup exercise is two weeks long (e.g., 15% of the total time).
    Its purpose is to give students a chance to familiarize themselves with the problem domain,
    tools,
    and software they'll be using for the rest of the term.

Requirements (10%)
:   One week spent figuring out
    who the stakeholders are (i.e., who you're trying to help)
    and what you're actually going to build to help them.

Design (10%)
:   What the user interface should look like,
    how data will flow through the system,
    what its major modules will be,
    and how they'll interact.
    This is *not* all done up front:
    as [%b Parnas1986 %] pointed out almost 40 years ago,
    nobody ever actually does that.
    Instead,
    the initial design description should be updated periodically
    to stay in step with reality
    so that the next person to work on the project has a useful map.

Code (10%)
:   Yes, that's right:
    the code is only worth 10% of the final grade,
    even though it's where students spend the bulk of their time.
    This may not seem fair, but
    (1) if you don't know how to program you shouldn't be in this course
    and (2) if you don't create some code you can't test, do a demo, or write your final report.

Testing (10%)
:   Testing is just as important as coding, so it's given the same weight.
    Only automated tests count:
    the instructor should be able to check the project out of version control
    and re-run the tests with a single command
    (possibly after editing a configuration file).
    And it's no good saying,
    "But I can't write tests for my GUI":
    if you design your program the right way
    you can test a lot more of your front end than you might think ([%x testing %]).

Demos (10%)
:   I used to have students prepare a 20-minute talk on a topic related to their project
    and deliver it to their coursemates or a junior class.
    It was a valuable experience,
    but it ate up a lot of time,
    so I switched to having students do 10-minute demos instead ([%x demo %]).
    I usually give students two shots at this:
    one after which their peers give them feedback,
    and a second that's actually graded.
    This is valuable practice for job interviews
    and a good reality check on how much progress has actually been made.

Teamwork (10%)
:   Everyone starts with 10 out of 10;
    marks come off if you always do your work at the last moment,
    check in code that breaks the build,
    or are disrespectful
    ([%x performance %]).

Retrospective (10%)
:   This summarizes what you learned along the way ([%x retro %])
    so that you and others can avoid any pitfalls this team ran into.

Final state of project (20%)
:   Some projects carry forward from term to term and team to team,
    so I award one fifth of the overall mark based on the state each team leaves the project in.
    Does everything build?
    Have issues been filed for all known bugs?
    Does the documentation explain how to install the code,
    and do those instructions actually work?

This grading scheme is labor-intensive:
I probably spend 10 to 12 hours reading and grading each project in a term.
I've thought several times about using peer grading to reduce my load
and give students some experience of what life is like on the other side of the red pen,
but I've never been able to convince myself that it would be fair.
