Many organizations make the mistake of focusing on outputs rather than on outcomes [%b Perri2018 %].
In software teams this often takes the form of measuring progress by the number of features added to a product
rather than by whether changes to the code are actually making people's lives easier.
The equivalent mistake in a project course
is to measure progress by how much code you have written
rather than by how your work compares to the grading scheme.
Doing this doesn't mean you should only do things that are going to show up on your transcript,
but keep in mind that your actual product isn't your software:
it's your grade.

<div class="callout" markdown="1">
### Weigh and measure

An undergraduate program in software engineering (or anything else) has three purposes:
to broaden your mind,
to train you to do something that employers will pay you to do,
and to give you and those future employers a sense of
how much you can do and how well you can do it.
Grades are inaccurate,
frequently biased,
and foster a zero-sum world view,
but while many people are working on alternatives [%b Blum2020 %],
we are stuck with them for now.
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
    ([%x peereval %]).

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

<div class="callout" markdown="1">
### Co-operatives

Project courses are often presented as "pretend you're starting a company".
In every case I've seen,
these "companies" follow the Silicon Valley model of a for-profit startup
trying to attract venture capital funding
to fuel explosive growth.
Many alternatives exist [%x business %].
</div>
