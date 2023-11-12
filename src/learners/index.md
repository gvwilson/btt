---
title: "Learning"
tag: "A few key facts about how you learn and how to learn faster."
syllabus:
- FIXME
---

We know as much about teaching and learning as we do about public health.
The problem is,
while university professors are experts in their own fields,
many of them don't know what we know.
Most people in the tech industry don't either,
which means many of us learn more slowly and less reliably than we could.

Research starting in the 1980s showed that
most neurotypical adults undergo a series of fairly predictable cognitive transitions
on their way from being a novice to being an expert in any domain [%b Benner2000 %].
(We say "most" and "neurotypical"
because there are outliers in anything involving people.)

For our purposes,
we will say that people are novices, competent practitioners, or experts.
Some characteristics that most novices share include doing things by rote
(i.e., following a series of steps without understanding why they work),
asking questions that don't make sense
(e.g., "What color is the database?")
and not being able to tell what is and isn't relevant—for example,
using their own filenames or variable names when searching for help online
because they don't yet have a clear distinction between
what belongs to the library and application
and what is specific to their code.

<div class="callout" markdown="1">

### Confidence

The Dunning-Kruger Effect [%b Kruger1999 %] is supposedly
a cognitive bias whereby people over-estimate their understanding of something
because they don't yet know enough to realize how much they don't know.
The original finding was probably a mirage due to poor statistics
(see [this discussion][jarry_dunning_kruger]
and [this summary][gelman_dunning_kruger] for details),
but there is no doubt that
people with high social status tend to think that
being an expert in one domain makes them an expert in others.
As a result,
asking people how much they know about a subject
usually produces misleading answers:
if they say they know a lot,
there's no way to tell if they know enough to actually know that
or if they're just a physicist.

</div>

What ties these things together is that
novices don't have a mental model of the problem.
A mental model is a simplified representation of something
that's good enough for present needs.
One example is the ball-and-spring models
used to represent molecules in chemistry classes:
real atoms aren't marbles and atomic bonds aren't springs,
but this model is good enough to explain
why burning methane produces carbon dioxide and water.

What about experts?
They can typically solve problems at a glance,
and are usually much better at debugging than competent practitioners
because they are better able to reason backward from effects to causes.
They also tend to be *less* good as teachers because of expert blind spot:
they know their subject so well that they've forgotten how hard it is for newcomers.

To explain where these differences come from,
imagine that the knowledge in your brain is stored as a graph
in which ideas are nodes and the connections between them are arcs.
(Your brain doesn't actually work this way,
but it's a useful mental model.)
A novice's mental model is disconnected:
some key facts are missing, and other pieces don't join up ([%f learners-models %]).
In contrast,
a competent practitioner's mental model is connected:
given fact `A`,
she can reason her way through `B` and `C` to solution `D`.
She might take a wrong turn to `Y` and `Z` along the way and have to backtrack,
but she'll get there eventually.

What makes an expert different isn't that she has more facts
(though she usually does).
Instead,
the difference is that she has many more connections,
so the distance between any two ideas is usually much less.
In fact,
in many cases the problem and its solution will be directly connected
so that she can go from one to the other in a single step.
This is what we mean by expert intuition:
rather than *reasoning* their way through problems,
they *recognize* them in the same way that most people recognize human faces.
Being able to do this explains why they can solve problems at a glance,
but also why they have trouble explaining their thinking:
they can't tell someone else how they did it
any more than we can explain how we recognize faces.

[% figure
   slug="learners-models"
   img="learners-models.svg"
   caption="The differences between novice, competent, and expert mental models."
   alt="Mental models"
%]

This model of learning leaves out
almost everything discussed in [%b Kirschner2018 %] and other recent work,
but is good enough to start with.
Novices, competent practitioners, and experts
are at different stages of cognitive development,
so they need different kinds of teaching [%b Kalyuga2003 %].
Novices need to be told what to learn next:
since they don't have yet a mental model of the problem,
they don't know what to ask for.
As [%b Kirschner2006 %] and many others have shown,
discovery-based learning in which people are told
"go figure out how to solve this problem"
is less effective for novices than guided learning
because they don't know what to ask next.

Once someone is a competent practitioner,
though,
being told step-by-step what to tackle next is both unnecessary and frustrating.
Competent practitioners should be mentored instead of lectured:
they should tackle problems on their own,
but have someone at hand to get them unstuck
if it takes them more than a few minutes to figure out what to do next.
Finally,
the most effective way to "teach" experts
is to have them reflect or introspect on their own practice [%b Schon1984 %].

## Learning Strategies {: #learners-strategies}

All of this leads to six strategies
that have been proven to help people learn faster and better [%b Weinstein2018 %].
While researchers still disagree on *why* they work,
everyone agrees that they *do*.

Spaced practice.
:   Ten hours of study spread out over five days is more effective than two five-hour days,
    and far better than one ten-hour day.
    You should therefore create a study schedule that spreads study activities over time:
    block off at least half an hour to study each topic each day
    rather than trying to cram everything in the night before an exam [%b Kang2016 %].
    You should also review material after each class,
    but not immediately after—take at least a half-hour break.
    Doing this also helps you catch any gaps or mistakes in previous sets of notes
    while there's still time to correct them or ask questions.

Retrieval practice.
:   The limiting factor for long-term memory is not retention (what is stored)
    but recall (what can be accessed).
    Recall of specific information improves with practice,
    so outcomes in real situations can be improved
    by taking practice tests or summarizing the details of a topic from memory
    and then checking what was and wasn't remembered.

    Recall is better when practice uses activities similar to those used in testing.
    For example,
    writing personal journal entries helps with multiple-choice quizzes,
    but less than doing practice quizzes.
    One way to exercise retrieval skills is to solve problems twice.
    The first time,
    do it entirely from memory without notes or discussion with peers.
    After grading your own work against a rubric supplied by the teacher,
    solve the problem again using whatever resources you want.
    The difference between the two shows you how well you were able to retrieve and apply knowledge.

    Another method is to create flash cards.
    Physical cards have a question or other prompt on one side and the answer on the other,
    and many flash card apps are available for phones.
    If you are studying as part of a group,
    swapping flash cards with a partner helps you discover
    important ideas that you may have missed or misunderstood.

Interleaving.
:   One way you can space your practice
    is to interleave study of different topics.
    Instead of mastering one subject,
    then a second and third,
    shuffle study sessions.
    Even better,
    switch up the order:
    `A-B-C-B-A-C` is better than `A-B-C-A-B-C`,
    which in turn is better than `A-A-B-B-C-C` [%b Rohrer2015 %].
    This works because interleaving fosters creation of more links between different topics,
    which in turn improves recall.
    Interleaving study will initially feel harder than focusing on one topic at a time,
    but that's a sign that it's working.
    If you are using flash cards or practice tests to gauge your progress,
    you should see improvement after only a couple of days.

Elaboration.
:   Explaining things to yourself as you go through them helps you understand and remember them.
    One way to do this is to follow up each answer on a practice quiz
    with an explanation of why that answer is correct,
    or conversely with an explanation of why some other plausible answer isn't.
    Another is to tell yourself how a new idea is similar to or different from one you have seen previously.

    Talking to yourself may seem like an odd way to study,
    but [%b Bielaczyc1995 %] found that
    people trained in self-explanation outperformed those who hadn't been trained.
    Similarly,
    [%b Chi1989 %] found that some learners simply halt when they hit a step they don't understand
    when trying to solve problems.
    Others pause and generate an explanation of what's going on,
    and the latter group learns faster.
    An exercise to build this skill is to go through an example program line by line with a class,
    having a different person explain each line in turn and say why it is there and what it accomplishes.

    Note-taking is a form of real-time elaboration:
    it forces you to organize and reflect on material as it's coming in,
    which in turn increases the likelihood that you will transfer it to long-term memory.
    Many studies have shown that taking notes while learning improves retention [%b Aiken1975 Bohay2011 %].

Concrete examples.
:   One particularly useful form of elaboration is the use of concrete examples.
    Whenever you have a statement of a general principle,
    try to provide one or more examples of its use,
    or conversely take each particular problem and list the general principles it embodies.
    [%b Rawson2014 %] found that interleaving examples and definitions like this
    made it more likely that learners would remember the latter correctly.

    One structured way to do this is the ADEPT method:
    give an analogy,
    draw a diagram,
    present an example,
    describe the idea in plain language,
    and then give the technical details.
    Again,
    if you are studying with a partner or in a group,
    you can swap and check work:
    see if you agree that other people's examples actually embody the principle being discussed
    or which principles are used in an example that they haven't listed.

Dual coding.
:   Different subsystems in our brains handle and store linguistic and visual information,
    so if complementary information is presented through both channels,
    they can reinforce one another.  However, learning is less effective when the same information is presented simultaneously in two different channels, because then the brain has to expend effort to check the channels against each other [%b Mayer2009 %].

    One way to take advantage of dual coding is to draw or label timelines,
    maps,
    family trees, or whatever else seems appropriate to the material.
    (I am personally fond of pictures showing which functions call which others in a program.)
    Drawing a diagram without labels and then coming back later to label it is excellent retrieval practice.

One powerful finding in learning research is the hypercorrection effect [%b Metcalfe2016 %].
Most people don't like to be told
hey're wrong, so it would be reasonable to assume that
the more confident someone is in the answer they've given on a test,
the harder it is to change their mind if they were actually wrong.
It turns out that the opposite is true:
the more confident someone is that they were right,
the more likely they are not to repeat the error if they are corrected.

<div class="callout" markdown="1">

### Learning styles aren't a thing

You may have heard of "learning styles",
i.e., that some people learn better visually
while others do so more quickly or more accurately by listening, reading, or otherwise using language.
It's bullshit:
while lots of companies make and sell materials based on this myth,
no one has ever shown that tuning what or how we teach to match people's preferences
has any impact on outcomes [%b DeBruyckere2015 %].
</div>
