---
title: "Assembling a Team"
tag: "FIXME"
syllabus:
- FIXME
---

I once heard an anthropologist ask,
"How big is a sports team?"
When people said it depends on the sport,
she explained that in fact they all have about half a dozen members.
Anything larger than that splits into smaller groups:
the forwards and backs in rugby,
the infield and outfield in baseball,
and so on.
She went on to explain that
hunting parties in non-agricultural societies are usually that size as well,
as are the basic military units around the world
(a platoon is two squads of six people).
Since we can only keep a handful of things in our short-term memory at once ([%x cogload %]),
that's as big as a team can practically be.

The same applies to software development.
Three or four people can work tightly on a single piece of code,
but when there are more they have to define interfaces
so that they can develop in parallel.

Teams of three to five provide a good balance between skills and accountability.
A team of two may not have enough breadth and background
to tackle a large piece of work;
more importantly,
one or the other person is likely to take a dominant role.
If you put more than half a dozen people in a single team,
on the other hand,
you may not be able to divide up the work
in a way that will keep everyone engaged and busy.
Large teams also make scheduling meetings much more difficult,
and increase the odds that at least one member will be a hitchhiker.

## Creating Teams {: #teaming-create}

Many students prefer to select their teammates,
and students with high grades tend to want teammates with a similar profile.
However,
having students with a range of grades in the same team
either has no effect or improves outcomes *for everyone*
[%b Mosher2013 Donovan2018 Farland2019 Auvinen2020 %].
It's easy to see how this benefits teams of weak students:
they are likely to get coaching from their stronger teammates.
One theory for why it also helps stronger students is that
the best way to learn something is to explain it to someone else;
bringing a weaker teammate up to speed
will usually do more for your grade
than spending those same hours hacking or reading.

In my experience,
teams of strong students are more likely to use a divide-and-conquer strategy,
effectively reducing the project to
a set of parallel sub-projects handled by one person each.
This may feel more efficient,
but most of the benefits of working in a team are lost:
there's less back-and-forth discussion of design issues
and little improvement in communication skills.
Those may not be important to you at first,
but if there is a final exam in your course with questions about the project work,
your mark on it may depend on how much you know about your teammates' work
([%x grading %]).

The most powerful argument for instructors allocating people to teams,
though,
is that's how it works in the real world [%b Oakley2004 %].
You probably won't get to pick your colleagues
if you join a company or an academic research group.
Instead,
you'll be put on a project
and expected to work well with whoever else is on it.
Your performance will depend as much on your ability to get along with others
as it will on your raw technical ability,
so you might as well start practicing those skills now.

If instructors create teams,
they should avoid isolating at-risk students.
Women and members of racialized minority groups
are more likely to drop out of computer science than other students,
particularly in first and second year,
and one of the main reasons is feeling isolated or out of place.
Research has shown that putting at-risk students together in the first couple of years
can mitigate this problem [%b Margolis2002 %].
It is less necessary in upper years,
since by then students have a stronger commitment to whatever program they're in,
but it still helps to prevent some of the problems discussed in the next section.

The biggest headache when instructors select teams is scheduling.
COVID-19 made distributed work more normal,
but the last university I taught at had three campuses spread across a large metropolitan area,
and some students commuted an hour and a half each way to get to classes.
Instructors should therefore take students' schedules into account when forming teams.
If the class is small,
the simplest way is
to get each student to fill in a weekly timesheet showing when they're available
and then group people who have large blocks of overlap.
If the class is larger,
a web-based calendaring tool may be easier.
I *don't* suggest trying to use whatever software the university uses
to figure out course timetables:
although that usually doesn't scale down to in-class scheduling.

Another factor to take into account is that
some people are early birds while others are night owls.
Putting the two on the same team pretty much guarantees that someone will miss meetings,
or sleep through them,
no matter when they're held.
Simply asking people,
"Do you prefer to work in the morning or the evening?"
can be surprisingly effective.

However you form teams,
each team should have at least one block of ninety minutes
to work together each week outside of class.
Teams should also try to find a second block
that's half an hour long
for a weekly status meeting ([%x meetings %]).
Try to keep the two blocks separate
so that it's clear to everyone when they're supposed to be talking about the project
and when they're supposed to be doing design,
writing code,
testing,
and so on.
If the two are scheduled back-to-back,
the meeting will drag on into working time or vice versa.

## Reteaming {: #teaming-reorg}

sometimes it makes sense to reorganize teams.
[%b Helfand2020 %] lays out five patterns for doing this;
they don't all come up in undergraduate course projects,
but are common in research teams, open source, and on the job.
Like most advice about teamwork,
they sound obvious when you hear them,
but (a) having names for things helps us talk about them,
and (b) saying that something is obvious in retrospect
isn't the same as saying you'd have thought of it yourself.

### One by One

The simplest way to change a new team
is to add or remove one person at a time.
Since every real team has no more than about half a dozen people
(see [%x assemble %] for the reasons),
changing even one person usually changes the personality of
the team as a whole.

One-by-one is the most common pattern in organizations of all size:
a new person will join an open source project,
or someone will move from one lab to another.
Its most extreme form occurs during large reorganizations
when almost every team gains or loses one or two people.
In this case it's better to think of the teams as re-forming entirely
because the stability normally provided by neighboring teams *not* changing
isn't there to keep this one anchored.

Groups can take several steps to ready themselves for one-by-one changes:

Define career ladders or equivalent ways to progress.
:   Most people want to get better at what they do
    and to be recognized for it.
    In school,
    this is often presented as a grading scheme that tells students
    whether they are ready for the next course in a sequence or not ([%x grading %]).
    In the workplace,
    there is often a sequence of job titles like "Software Engineer",
    "Senior Software Engineer",
    "Staff Software Engineer",
    and so on.
    Whatever it is,
    make it explicit so that everyone understands what the rules are.

Make the new people welcome.
:   As discussed [%x join %],
    pairing the new team member with a mentor or buddy shows you care;
    pointing them at a Git repository
    and telling them that you're sure they'll figure it out
    sends a pretty clear signal that you don't.

Ask them for their ideas.
:   [%x join %] recommended that if you're the new person on the team
    you shouldn't immediately start telling people what they're doing wrong.
    Conversely,
    though,
    incumbent team members should ask new arrivals for their ideas.
    (Moving people around is often the best way to spread good practices.)

### Grow and Split

Successful projects tend to grow,
which often means that successful teams become so large
that they stop being successful.
The Grow and Split pattern should be used
when breaking a team in two
will allow its members to recapture the efficiency they once had.

Let experienced team members decide.
:   People who have worked on enough team projects
    will usually recognize when their team needs to fission,
    so "Is it time we broke up?"
    should be asked in every retrospective ([%x retro %]).

Recognize that every rule has exceptions.
:   Not all big teams should be split,
    at least not right away.
    Again,
    let experienced team members make the call,
    and if everyone on the team is so new to this
    that they don't trust their own opinion,
    bring in someone from outside who knows more.

Divide responsibilities as well as teams.
:   Each of the new teams should have a clear mission
    that doesn't overlap with the other team's.
    Making lists helps here,
    as does reallocating open issues ([%x issues %])
    and having the teams draw and compare concept maps ([%x mental %]).

### Merging

Merging is the inverse of the Grow and Split pattern,
and is usually followed by one or more people moving to other teams
in order to keep the new team's size manageable.
Merging also often happens after one company acquires another,
though in that case people are often laid off rather than being moved to new teams.

Combine teams as projects wind down.
:   The next project might be larger than the ones that just finished,
    and might need a larger team.
    In courses,
    this sometimes happens by design:
    instructors will have small teams build components of a large application
    for the first few weeks,
    then combine those teams
    and ask them to try to fit their pieces together.

Distinguish mergers from takeovers.
:   Another reason to merge teams is as a form of teaching.
    Sitting in with a band is a great way to learn their style of music;
    having two teams work as one temporarily
    is a great way to transfer working practices.

### Isolation

This pattern doesn't come up often in courses,
but in open source projects, research labs, or companies,
it sometimes makes sense to put a few people together
to focus on solving a single problem or producing a prototype
free from distraction.

Don't create silos.
:   I've worked in a company that were essentially
    half a dozen independent (and mutually hostile) groups
    that happened to share a website and a payroll system.
    That situation arose because the founder repeatedly used the Isolation pattern
    and then didn't merge the teams back together.
    It didn't end well…

Don't make it a status badge.
:   I also once worked in a company where every team lead talked as if
    their team was the best of the best, of the best.
    That situation arose because being put in an isolated team
    was seen as equivalent to being awarded all-star status.
    It didn't end well either…

Bring the knowledge back—quickly.
:   If you use the Isolation pattern,
    you should dissolve the isolated team as soon as possible
    and bring its members back into other teams
    so that they can share their knowledge.

### Switching

Sometimes it's a good idea to shuffle team membership to prevent stagnation.
Be cautious when someone suggests this, though:
consultants and newly-hired managers often launch re-organizations
in order to show that they're doing something
and to demonstrate their power.

Less cynically,
though,
shuffling team membership is a good way to reduce the group's lottery factor,
i.e.,
to make sure that there isn't just one person or one team
who knows their way around something critical.
I've never seen this pattern used in an open source project or research team,
but it's quite common in undergrad courses:
it gives students a chance for a fresh start
and also the experience of wrestling with code that they didn't write.

Base changes on individual aspirations.
:   Don't shuffle team membership at random
    (unless that's a deliberate aim).
    Instead,
    try to move people en masse to places where they can pursue their interests
    and/or further their careers.

Allow people to avoid teams if they're willing to explain why in private.
:   Some people have good reasons to want to avoid other people.
    (Female students might drop a course rather than be on a team with "that guy",
    and members of minoritized groups probably don't want to have to work with racists.)
    However,
    every one of these reasons can be turned around:
    a misogynist might not want any women on his team,
    while those racists probably don't want to have to work with "those people".
    Getting this right is probably the hardest thing in this chapter,
    and we will return to it in [%x fairness %].

## Problems and Solutions {: #teaming-problems}

When I first put these notes together fifteen years ago, I wrote a section
titled "People to Watch Out For" that described a dozen people who make teams
less productive in different ways. As several reviewers have pointed out since,
it was arrogant and harmful: arrogant because what I was really saying was, "If
you don't work the way I do then you're wrong," and harmful because it would
make people who already doubt themselves do so even more.

If you read one of those earlier versions, I apologize. What I've tried to do
below is describe ways in which I've seen people undermine themselves.  If you
go through this list with your teammates and tell them what you'd like to get
better at, they'll probably help you.

Not everything needs to be completely correct.
:   Before correcting a factual error, ask yourself whether it really matters.
    If it's the name of the configuration file the program reads on startup, the
    answer is probably yes; if it's the name of a minor villain from the Marvel
    Cinematic Universe, the answer is probably no.

The devil doesn't need more advocates.
:   We remember when contrarians
    turn out to be right because it happens so infrequently, but because those
    moments are memorable, some people fall into the habit of taking the
    opposite point of view no matter what is being discussed.

You wouldn't have gotten this far if you weren't good at this.
:   Some people have so little
    confidence in their ability despite their good grades that they won't
    make any decision, no matter how small, until they have checked with someone
    else. This is often a result of social conditioning: in particular, women
    are more likely to doubt themselves, while men often over-estimate their
    ability.

Not everything worth doing should be done.
:   For many years my favorite phrase was, "Why don't we?" Why don't we write a
    GUI to help people edit the program's configuration files? Hey, why don't we
    invent our own little language for designing GUIs? This energy and
    enthusiasm are hard to argue with, but argue you must.  Otherwise, for every
    step you move forward, the project's goalposts will recede by two. This is
    called feature creep, and has ruined many projects that might otherwise have
    delivered something small but useful.  My solution these days is to keep a
    to-don't list of things that would be fun and
    worthwhile, but that I'm *not* going to tackle.

Success is a habit.
:   The more you follow a routine, the more your brain will be able to focus on
    the right things at the right time. [%b Gawande2011 %] found that
    checklists improve results even for
    experts, and FIXME talked about the value of to-do lists for
    managing your time. Making these a habit reduce cognitive load ([%x cogload %]) and
    gives you more mental capacity for dealing with the work itself.

Acting like an asshole doesn't make you cool—it just makes you an asshole.
:   I had a teammate once whose favorite phrase was, "That's stupid."  If anyone
    complained, he said, "It's just the way I talk." The problem with people
    using vulgar or aggressive language in everyday conversation is that for
    many other people, that language has often been followed by bullying or
    discrimination. They're right not to trust you if those are the signals you
    choose to send. (And no, calling someone out for being vulgar or aggressive
    is not the same as tone policing.)

Sometimes it's hard to care.
:   You have a teammate who doesn't read the assignment specs, hasn't bothered
    to learn the tools and libraries you're supposed to be using, and commits
    code that doesn't even compile.  Before treating them like a hitchhiker, try
    to find out if there's a reason for their behavior: if he's caring for a
    family member or struggling with mental
    health issues, the most compassionate thing to do is to help them get
    back on their feet.
