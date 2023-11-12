---
blank: True
title: Evaluation
tag: "FIXME"
syllabus:
- FIXME
---

Many organizations make the mistake of focusing on outputs rather than on outcomes [%b Perri2018 %].
In software organizations
this usually takes the form of measuring progress by the number of features added to a product
rather than by whether changes to the product are actually making people's lives easier.
Claims like "80% of people only use 20% of a product's features" are largely anecdotal,
but are probably also true:
in most cases,
people learn just enough to accomplish the task at hand
and only discover more intermittently and accidentally if at all.

The equivalent mistake in a project course
is to measure progress by the amount of code you are writing
rather than by how your work compares to the grading scheme.
Doing this doesn't mean you should only do things that are going to show up on your transcript,
but if you're going to,
you should do so knowingly.

The first step in any project is therefore to figure out where the goalposts are,
so you know which way to kick the ball.
In a company,
it means figuring out what you can build that people will pay for.
If you're working for someone else,
your boss should tell you what you're responsible for
and the HR department should tell you what the criteria are
for performance evaluation and bonuses.
Again,
you don't have to do only those things,
but if you're going to drop any or put time elsewhere,
you should do it with your eyes open.

Your grade in a project course is typically based on:

The software you produce.
:   Does it build and run?
    Does it meet the customer's requirements (or the instructor's specifications if you don't have a real customer)?
    Is the source code readable?
    Is the program efficient?
    (Using an exponential algorithm instead of one that runs in linear time certainly *ought* to cost you marks…)

The process you followed.
:   Some instructors insist you use a traditional analyze-design-code-test methodology.
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

A final report.
:   This may be a handoff report
    (i.e., documentation to help whoever inherits the software from you get up to speed),
    a summary of your experiences,
    or some combination.

A final exam.
:   This may focus on the theoretical side of the course
    ("Describe the four main functions of Quality Assurance…")
    but smart instructors will include some questions
    to test your understanding of the project
    in order to determine who actually did the work and who was just along for the ride.

Just like real development projects,
course projects can and should produce a lot more than just code.
For example,
[%b Spinellis2007 %] looked at how much content of different kinds
went into the FreeBSD project in 2006.
[%t evaluation-spinellis-stats %] doesn't divide "source code" into "application code" and "tests",
but it's still an eye-opener.

[% table
   slug="evaluation-spinellis-stats"
   tbl="spinellis-stats.tbl"
   caption="FreeBSD 2006"
%]

Here are some of the things that you might be required to produce:

Requirements analysis
:   What the problem is,
    who the stakeholders are (i.e., who wants the problem solved),
    and what their needs are.

Design
:   What the user interface should look like,
    how data will flow through the system,
    what its major modules will be,
    and how they'll interact.

Application code
:   The software that will be delivered to the end user.
    This is inextricably entangled with:

Test code
:   Coding and testing should not be separate activities:
    doing them concurrently greatly improves your project's chances of success.

Documentation
:   Human-readable explanations of the software's structure and use.
    The first is intended for whoever inherits the software from you;
    the second, for its users.
    It is almost always a mistake to try to combine the two
    or to write them as if they were going to be read by the same people.

Packaging
:   A program is a piece of software that runs for you on your machine.
    A product is a piece of software that will run for anyone on *their* machine.
    Products take longer to build than programs:
    the packaging needed to let someone else download, install, configure, and run the program
    has often not been covered in software engineering courses,
    but good instructors will insist that you create it.

Deployment
:   The project's aim might not be to create something that can be downloaded and installed.
    Instead, its aim might be to create a web site or web service or make something else directly available to users.
    Like packaging,
    deployment can be a major development issue in its own right,
    and the effort required to do it is almost always underestimated.

Handoff
:   If you don't put effort into passing the project on to whoever comes after you,
    your hard work will almost certainly count for nought.
    While it isn't usual for undergraduate projects to be handed on from one term to another,
    some courses require teams to swap code mid-term.
    If this happens,
    instructors may grade you on how complete and up-to-date your wiki pages,
    bug database, and build scripts are at the time of handoff.

Review
:   The only way to get better at something is to reflect on how you've done and what you could have done better.
    Every project should therefore end with a postmortem
    in which team members talk about what went right and what went wrong.
    As mentioned earlier, this may then be the subject of the final report.

So much for generalities;
the list below shows grading scheme I've used in project courses.

Warmup exercise (10%)
:   The warmup exercise is two weeks long.
    Its purpose is to give students a chance to familiarize themselves with the problem domain,
    tools,
    and software they'll be using for the rest of the term.

Analysis and estimation (10%)
:   Two weeks spent figuring out what your customers actually want,
    what features will satisfy their needs, etc.

Code (10%)
:   Yes, that's right:
    the code is only worth 10% of the final grade,
    even though it's where students spend the bulk of their time.
    I do this because (1) if you don't know how to program you shouldn't be in this course
    and (2) if you don't create some code you can't test, do a demo, or write your final report.

Testing (10%)
:   Testing is just as important as coding, so it's given the same weight.
    Only automated tests count:
    if I can't check the project out of version control and re-run the tests
    (possibly after editing a configuration file)
    then as far as I'm concerned, the code hasn't been tested.
    And it's no good saying,
    "But I can't write unit tests for my GUI" because it's simply not true:
    you can always test the core functionality,
    and if you design your program the right way
    you can test a lot more of your front end than you might think ([%x testing %]).

Demos (10%)
:   I used to require students to prepare a 20-minute lecture on a topic of their choosing
    and deliver it to their coursemates or a junior class.
    It was a valuable experience,
    but it ate up a lot of time,
    so I switched to having students do 10-minute demos instead.
    I usually give students two shots at this:
    one after which their peers give them feedback,
    and a second that's actually graded.
    This is valuable practice for job interviews
    and a good reality check on how much progress has actually been made.

Teamwork (10%)
:   Everyone starts with 10 out of 10;
    marks come off if you always do your work at the last moment,
    check in code that breaks the build,
    or are disrespectful.

Final report (20%)
:   This describes the architecture of the code as it was actually built
    (rather than as it was designed)
    and summarizes the postmortem
    so that the next team can avoid any pitfalls this team ran into.

Final state of project (20%)
:   Most of my projects carry forward from term to term and team to team,
    so I award one fifth of the overall mark based on the state each team leaves the project in.
    Does everything build?
    Have issues been filed for all known bugs?
    Does the documentation explain how to install the code, and do those instructions actually work?

This grading scheme is labor-intensive:
I probably spend 6 to 10 hours reading and grading each project in a term.
I've thought several times about using peer grading to reduce my load
and give students some experience of what life is like on the other side of the red pen,
but I've never been able to convince myself that it would actually work.
