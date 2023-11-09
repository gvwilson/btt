---
template: slides
---

## Goals

-   Many organizations focus on *outputs* rather than on *outcomes* [%b Perri2018 %]
    -   "What we did" is easier to measure than "what we achieved"
-   Equivalent mistake in a project course is to measure progress by how much code you have written
    rather than by comparing your work to the grading scheme
-   Doesn't mean you should only do things that are going to show up on your transcript
-   But keep in mind that your actual product isn't your software:
    it's your grade

---

## What Does "Productive" Mean?

-   [%b Sadowski2019a %]: "it's hard to measure" and "it depends"
-   [%b Noda2023 %] identified three factors

Rapid feedback
:   Long delays between doing things and knowing how well they were done
    causes frustration and errors.

Cognitive load ([%x cogload %])
:   If we have to pay attention to too many things,
    we can't keep track of any of them.

Flow state
:   Being immersed in a problem is pleasurable.

---

## Thriving

-   [%b Hicks2023 %]: developers are most productive when they're thriving
-   Agency
    -   Has a voice in how their contributions are measured
    -   Able to voice disagreement with team definitions of success
-   Motivation & Self-Efficacy
    -   Motivated when working on code at work
    -   Can see tangible progress most of the time
    -   Is working on the type of code work they want to work on
    -   Is confident they will solve their problems even when work is unexpectedly difficult
-   Learning Culture
    -   Learning new skills as a developer
    -   Able to share the things they learn at work
-   Support and Belonging
    -   Supported to grow, learn, and make mistakes by their team
    -   Agrees they are accepted for who they are by their team

---

<!--# class="aside" -->

## Weigh and Measure

-   Degrees have three purposes:
    1.  Broaden your mind
    2.  Train you to be employable
    3.  Give you and future employers a sense of what you can do
-   Grades are inaccurate, frequently biased, and foster a zero-sum world view
-   Many people are working on alternatives [%b Blum2020 %]
-   But everything better requires more resources than most societies are willing to invest
    [%b Partanen2011 Sahlberg2015 %]

---

## Where Do Grades Come From?

The software you produce.
:   Does it build and run?
    Does it meet requirements (if any have been given)?
    Is the source code readable?
    Is it efficient?

Other deliverables.
:   E.g.,
    a retrospective report ([%x retro %]),
    a demo ([%x demo %]),
    or the final state of the project ([%x delivery %]).

A final exam.
:   May focus on theory
    ("Describe the four main functions of Quality Assurance…")
    but instructors may ask questions to test your understanding of *your* project
    to determine who actually did the work and who was hitchhiking ([%x teams %]).

---

## Invisible Work

-   Instructors often want to assess the process you followed ([%x process %])
-   But they can't watch over your shoulder while you're working
-   So all they can grade is artifacts
    -   Code commits ([%x sharing %])
    -   Issues filed ([%x tasks %])
    -   Status reports
-   Often undervalues **invisible work** [%b Daniels1987 %]
    -   Our definition of what counts as "work" ties closely to
        "things that high-status people do"
    -   Consistently underestimate the effort required to wash dishes,
        clean clothes,
	and keep the CI/CD pipeline running
-   [All Contributors][all_contributors] is a way to recognize
    "other" contributions to code
-   Though "recognize" isn't the same as "value"

---

## One for All?

-   Should every team be assessed the same way?
-   Pro:
    -   Easier for instructor (a real consideration in a large course)
    -   Makes inter-team comparison fairer
-   Con:
    -   Forces projects to be similar enough to be comparable
    -   Not how the real world works

---

<!--# class="aside" -->

## Seeing Like a Prof

-   [%b Scott1999 %] argued that large organizations prefer uniformity over productivity
-   Individual differences require case-by-case attention
-   But that doesn't scale
    -   "How can you govern a country which has 246 varieties of cheese?" (Charles de Gaulle)
-   Central control isn't always bad
    -   "States' rights" was and is a euphemism for "legalized racism"
-   "Politics" is often considered a dirty word,
    but every organization continually renegotiates the boundary between "we decide" and "you decide"

---

## Gaming the Rules

> When a measure becomes a target, it ceases to be a good measure.
>
> — [Charles Goodhart][goodharts_law]

-   Manager: "We will evaluate you based on the number of bugs you close"
-   Developer A: "OK, I'll write 'em…"
-   Developer B: "…and I'll fix 'em…"
-   Together: "…and we'll split the money!"

---

## Measuring Code

-   Lots of code metrics have been proposed
    -   Halstead's measures
    -   Cyclomatic complexity
    -   Many object-oriented measures
-   But nothing works better than counting lines of code [%b ElEmam2001 Herraiz2010 %]
    -   Chances of a rule violation increase with the size of the code base
    -   So `wc -l` is as accurate as anything else

---

## Peer Evaluation

-   "Rate your teammates' work on a scale of 0 to 10."
-   If public, most people will give most of their teammates a 10
    -   The instructor doesn't have to live with the consequences of a 3
    -   But the student who gave it does
-   And if ratings are anonymous,
    people with lower social status will be given lower ratings [%fixme citation %]
-   Even if people are honest, how do you ensure consistency?
    -   "I wasn't trained to do this"

---

<!--# class="aside" -->

## Is It Actually A Problem?

-   [%b Kaufman2000 %] compared confidential peer ratings and grades in undergrad engineering courses
    -   Found that self-rating and peer ratings statistically agreed
    -   And that collusion wasn't significant (i.e., people didn't just give everyone high grades)
-   So why do we worry so much?
    -   Most people's mental model of disasters is *The Walking Dead*
    -   In fact, most people come together and help each other [%b Solnit2010 %] 
    -   But that doesn't make for as exciting a movie
    -   And people are more likely to put up with restrictions on their freedoms
        if they are afraid of their neighbors

---

## Calibrated Peer Review

-   Learner grades a piece of work based on a marking guide
-   Their evaluation is compared to the instructors'
-   The learner's score is 100% minus points for:
    -   False negatives: missed a problem the instructor identified
    -   False positives: thought something was a problem when it wasn't
-   Learners' evaluations will converge on the instructor's [%b Pare2008 Kulkarni2013 %]
-   Which helps them review their peers code *and their own as they write it*

---

<!--# class="exercise" -->

## Compare and Contrast

1.  Have every person on the team review a program given by the instructor.
2.  Compare reviews: where did you agree and disagree?
3.  Repeat the exercise with another piece of code.
    Are your reviews closer to each other's?
