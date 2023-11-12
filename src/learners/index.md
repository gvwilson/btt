---
blank: True
title: "Learners"
tag: "FIXME"
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
(We say "most" and "neurotypical" because there are outliers in anything involving people.)

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

- Explain that Dunning-Kruger isn't a thing…
- …but confidence is not an indicator of knowledge
</div>

What ties these things together is that novices don't have a mental model of the problem.
A mental model is a simplified representation of something
that's good enough for present needs.
One example is the ball-and-spring models used to represent molecules in chemistry classes:
real atoms aren't marbles and atomic bonds aren't springs,
but this model is good enough to explain why burning methane produces carbon dioxide and water.

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
Novices, competent practitioners, and experts are at different stages of cognitive development,
so they need different kinds of teaching [%b Kalyuga2003 %].
Novices need to be told what to learn next:
since they don't have yet a mental model of the problem,
they don't know what to ask for.
As [%b Kirschner2006 %] and many others have shown,
discovery-based learning in which people are told "go figure out how to solve this problem"
is less effective for novices than guided learning because they don't know what to ask next.

Once someone is a competent practitioner,
though,
being told step-by-step what to tackle next is both unnecessary and frustrating.
Competent practitioners should be mentored instead of lectured:
they should tackle problems on their own,
but have someone at hand to get them unstuck
if it takes them more than a few minutes to figure out what to do next.
Finally,
the most effective way to "teach" experts is to have them reflect or introspect on their own practice [%b Schon1984 %].

FIXME: tutorials, Stack Overflow, and LLMs
