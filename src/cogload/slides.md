---
template: slides
---

## Goals

-   The biggest constraint on how we program is how our brains work
    -   It takes (literally) millions of lines of code
        to translate what we write into something machines can execute
    -   All that syntax is for *our* benefit, not theirs
-   How we think is also a factor in how we work together
    -   Though we have to be careful to avoid **psychological determinism**
    -   Which is often used to justify things as they as as "natural"

---

## Cognitive Architecture

[% figure
   slug="cogload-architecture"
   img="cognitive-architecture.svg"
   caption="The cognitive architecture of the human mind (simplified)."
   alt="Cognitive architecture"
%]

-   Start on the left…
-   Long-term memory (LTM) is "permanent" storage
    -   Large but slow
    -   We don't have direct access to it
-   Short-term memory (STM) is a cache or working set
    -   More sophisticated models distinguish several kinds of STM [%b Kirschner2018 Hermans2021 %]
    -   Differences aren't relevant for our purposes

---

## Encoding and Decoding

-   Constantly fetch things from LTM into STM based on pattern matching
-   **Integrate** that information with new data
-   **Re-encode** the result (i.e., write it back to STM)
    -   Constant rewriting is one of the differences between brains and computers
-   Updating LTM this way is called "learning"

---

## Capacity

-   STM is very small
    -   [%b Miller1956 %] estimated it could hold 7±2 things at any time
    -   Modern estimates are closer to 4±1 [%b Didau2016 %]
-   This number is a bottleneck for learning
    -   If a lecture presents too many ideas too quickly,
        new arrivals knock older ones out of STM
	*before* they can be encoded
    -   Learner is overwhelmed: nothing sticks
-   And for thinking
    -   If you have to keep track of too many unrelated facts at once
        in order to write or debug the next line of code,
	error rates and required time increase dramatically

---

## Cognitive Load Theory

-   **Intrinsic** load: the thinking required by the learning task itself
-   **Germane** load: other thinking that the problem requires
    that isn't the focus of the lesson
-   **Extraneous** load: everything you have to do that's irrelevant
-   Give learners **scaffolding** for germane load and eliminate extraneous load

[% figure
   slug="cogload-parsons"
   img="parsons-problem.svg"
   caption="A Parsons Problem illustrating cognitive load."
   alt="A Parsons Problem for finding the maximum value in a list."
%]

-   Intrinsic: where do keywords go?
-   Germane: what are the keywords?
-   Extraneous: brain can't stop itself wondering why the fonts different
    -   Which leaves less mental energy for solving the problem

---

<!--# class="aside" -->

## Working in Groups

-   Cognitive load limits how large groups can be
    -   How many people's work can you keep track of at once?
-   Forcing work to be uniform (e.g., assembly line) reduces the manager's cognitive load
    -   Even if it makes individuals less productive
-   Discuss the implications in [%x decomp %] and [%x grading %]

---

## Chunking

-   Our brains handle larger information sets by **chunking**
    -   A pattern only takes up one slot in STM
-   Which version of these symbols is easier to remember?

[% figure
   slug="cogload-chunking"
   img="chunking.svg"
   caption="Symbols for the digits 1-9 arranged at random or in a pattern."
   alt="Symbols are easier to remember when the pattern is clear."
%]

-   Experts "see" more and larger patterns
-   Which helps them think faster…
-   …but can mislead them if the pattern isn't actually there

---

<!--# class="aside" -->

## PETE

-   We learn faster if we are explicitly taught patterns
-   PETE: Problem, Example, Theory, Elaboration
    -   Need an example to ground the theory
    -   Need a second example to show what stays the same and what varies
-   Learning **design patterns** makes people better programmers [%b Tichy2010 %]
-   But they have to be learned in context rather than in the abstract
-   It's a shame the novice-level design patterns of [%b Sajaniemi2006 %]
    weren't followed up…

---

## Cognitive Development

-   **Novice**: doesn't yet have a **mental model** of the problem domain
    -   Don't know what they don't know
    -   Don't know how the pieces they *do* know fit together
-   **Competent**: can solve normal problems in reasonable time
    -   What counts as "normal" and "reasonable" usually defined by
        "what most people can learn to do"
-   **Expert**: solve easy problems at a glance and hard ones eventually
    -   Again, "easy" and "hard" are determined by
        what the minority of people who have invested a lot of time
        are able to achieve

---

## Explaining the Difference

-   Our brains don't actually store knowledge as a graph
-   But it's a useful mental model of how they work

[% figure
   slug="cogload-models"
   img="novice-competent-expert.svg"
   caption="Differences between novice, competent, and expert mental models."
   alt="Novices' mental models are disconnected, experts' are densely connected."
%]

---

<!--# class="aside" -->

## Confidence

-   Dunning-Kruger Effect [%b Kruger1999 %]:
    a cognitive bias whereby people over-estimate their understanding
    because they don't know enough to realize how much they don't know
-   Ironically, original finding was a mirage caused by poor statistics
    [%b Jarry2020 Gelman2021 %]
-   People with high social status tend to think that
    being an expert in one domain makes them an expert in others
-   So "how much do you know?" produces misleading answers:
    -   If they say "a lot",
        there's no way to tell if they're actually an expert
        or just a physicist

---

## How to Teach

-   Novices need to be told what to learn next:
    don't know what to ask for
    -   "Figure out how to solve this real problem"
        is less effective than guided learning [%b Kirschner2006 %]
-   Competent practitioners should be mentored rather than taught
    -   Can tell when someone has reached this level because they ask meaningful questions
        and can understand the answers
-   Most effective way to "teach" experts
    is to have them reflect or introspect on their own practice [%b Schon1984 %]

---

<!--# class="aside" -->

## Learning Styles Aren't Real

-   "Learning styles" is the idea that
    some people learn better visually
    while others do so more quickly or more accurately by listening or reading
-   Lots of companies make and sell materials based on this myth,
    but no one has ever shown that tuning what or how we teach to match people's preferences
    has any impact on outcomes [%b DeBruyckere2015 %]

---

<!--# class="exercise" -->

## Learning Strategies

1.  Review the [six learning strategies][learning_scientists]
    that have been proven to help people learn faster and better [%b Weinstein2018 %].
2.  Which ones do you use regularly?
3.  Which ones can be adapted to learning your way around a new code base?
