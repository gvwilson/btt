---
title: "Cognitive Load"
tag: "FIXME"
syllabus:
- FIXME
---

[%f cogload-architecture %] shows a very (very) simple model of
the cognitive architecture of the human brain.
On the left is long-term memory (LTM),
which is where you store things like the spelling of your name
and how that awful clown scared you when you were ten years old.
It is very large—you can keep adding to it as long as you live—but
you don't have direct conscious access to it.

[% figure
   slug="cogload-architecture"
   img="cognitive-architecture.svg"
   caption="The cognitive architecture of the human mind (simplified)."
   alt="Cognitive architecture"
%]

Instead,
evolution has given you a second subsystem called short-term memory (STM) or working memory.
(More sophisticated models distinguish between these two concepts,
but this simple model is good enough for our needs.)
You are constantly fetching things from LTM into STM to use them,
then re-encoding them and writing them back to LTM.
This is one of the differences between your brain and a computer:
reading data from a hard drive doesn't alter it,
but every time you access something in LTM,
you may write it back in a different or augmented form.
We call this "learning".

Here's the problem:
STM is very small.
[%b Miller1956 %] estimated that it could hold 7±2 things at one time;
more modern estimates put the number closer to 4±1 [%b Didau2016 %].
This means that STM is a bottleneck for learning:
if too many new ideas are presented too quickly,
the new arrivals will knock older ones out of STM
before you have a chance to encode them and store them in LTM,
so learning won't take place.

This realization and others have produced the theory of cognitive load,
which (among other things) divides the things you have to do while learning into three categories.
The intrinsic load is the thinking that is required by the learning task itself.
The germane (or relevant) load is the other thinking that the problem requires,
but which isn't the focus of the lesson,
while the extraneous load is everything you're being asked to do that is irrelevant.

For example,
suppose you are learning the grammar of Frisian.
If I ask you to translate,
"How is her knee today?"
then the intrinsic load is the rules of grammar,
but there is also the germane load of recalling vocabulary
(which is necessary, but isn't the main focus of the lesson).
If,
on the other hand,
I give you the words as shown in [%f cogload-frisian %]
and ask you to rearrange them,
I have eliminated the germane load,
but have added some extraneous load by using a mix of fonts.
You will solve the problem more quickly and more accurately
if the words are all in the same font,
no matter what that font is,
than if your brain is wondering whether the difference is significant.

[% figure
   slug="cogload-frisian"
   img="cogload-frisian.svg"
   caption="Reducing germane load while increasing extraneous load."
   alt="Translating a sentence"
%]

Cognitive load theory explains why tools like [Scratch][scratch] work so well:
they reduce germane load by getting rid of the commas, curly braces, and other distractions
so that learners can focus on mastering concepts like assignment and loops.
It also explains why working with code written in a mix of styles is so painful:
each minor difference adds extraneous load.

In order to handle larger sets of information,
our minds create chunks that only take up one slot in STM.
For example,
most of us remember words as single items rather than as sequences of letters.
Similarly,
the pattern made by five spots on cards or dice is remembered as a whole
rather than as five separate pieces of information.

Experts have more and larger chunks than non-experts,
i.e.,
experts "see" larger patterns and have more patterns to match things against.
This allows them to reason at a higher level
and to search for information more quickly and more accurately.
However,
chunking can also mislead us if we mis-identify things:
newcomers really can sometimes see things that experts have looked at and missed.

Given how important chunking is to thinking,
it is tempting to try to teach design patterns directly to learners as early as possible.
These patterns help competent practitioners think and talk to each other in many domains,
but pattern catalogs are too dry and too abstract for novices to make sense of on their own.
However, giving names to a small number of patterns does seem to help,
primarily by giving the learners a richer vocabulary to think and communicate with [%b Sajaniemi2006 %].

## Learning Strategies {: #cogload-strategies}

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

<div class="callout markdown="1">
### Learning styles aren't a thing

You may have heard of "learning styles",
i.e., that some people learn better visually
while others do so more quickly or more accurately by listening, reading, or otherwise using language.
It's bullshit:
while lots of companies make and sell materials based on this myth,
no one has ever shown that tuning what or how we teach to match people's preferences
has any impact on outcomes [%b DeBruyckere2015 %].
</div>
