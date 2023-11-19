---
title: "Reteaming"
tag: "FIXME"
syllabus:
- FIXME
---

As [%x assemble %] said,
sometimes it makes sense to reorganize teams.
[%b Helfand2020 %] lays out five patterns for doing this;
they don't all come up in undergraduate course projects,
but are common in research teams, open source, and on the job.
Like most advice about teamwork,
they sound obvious when you hear them,
but (a) having names for things helps us talk about them,
and (b) saying that something is obvious in retrospect
isn't the same as saying you'd have thought of it yourself.

## One by One {: #reteam-one}

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

## Grow and Split {: #reteam-growplit}

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

## Merging {: #reteam-merge}

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

## Isolation {: #reteam-isolation}

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

## Switching {: #reteam-switch}

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
:   Don't shuffle team membership at rando
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
