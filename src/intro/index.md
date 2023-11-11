---
title: "Introduction"
tag: "What this book talks about and why."
syllabus:
- Our goal is to help you become a compassionate programmer.
- Nothing in software engineering makes sense except in the light of psychology.
- We know more about programs, programmers, and programming from empirical studies than most people realize.
- Good programmers aren't ten times more productive than average, but it's fair to say they are four times better.
---

Programming is often portrayed as a solitary activity,
but real applications are always the work of many people.
The aim of this book is therefore to show you
how to build software as part of team.

Our goal is to help you become a *compassionate programmer*:
one who cares about the wellbeing of their colleagues,
their users,
and society as a whole.
This focus is not entirely altruistic—everything you do to help others
also helps your future self—but now that we know how much harm software can do,
we need to build it better.

## Audience {: #intro-audience}

This book can be read on its own or as a companion to [%b Wilson2022 %].
(If you are looking for a course project,
please consider adding a tool to the ones it covers.)
These three learner personas describe who this book is for:

-   *Rui* is in the third year of a computer science degree.
    She worked on several volunteer projects in high school and through her mosque,
    but the "Introduction to Software Engineering" course she's about to take
    will be the first time she has built software with other people.
    This book will help her and her teammates figure out who should do what, when.

-   *Brad* is in Rui's class.
    He started programming when he was nine years old,
    and can do many assignments in half the time it takes other students.
    (He attributes this to natural aptitude
    rather than to his parents being able to afford to send him to after-school coding camps).
    He finds discussion of what he calls "fluffy stuff" tiresome;
    this guide will help him understand why that attitude is self-defeating.

-   *Sharla* has taught that software engineering class twice.
    Each time,
    they came away feeling that
    their students had wasted time on things that weren't useful
    and hadn't learned things that would be.
    This book will help them restructure that course.

## Themes {: #intro-theme}

Much of what's hard about building software stems from
the way our brains work [%b Hermans2021 %].
One theme of this book is therefore
this modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

Another theme is that
we know a lot more about software and how to build it
than most people realize.
Empirical studies of programs, programmers, and programming date back more than fifty years,
but their findings are rarely discussed in undergraduate classes.
As a result,
most books on how to program are a mix of personal experience and received wisdom,
which is usually just someone else's personal experience repackaged as a universal truth.
We therefore cite research findings to back up our claims where we can.

<div class="callout" markdown="1">
### Why does everything take so long?

[%b Sedano2017 %] found that software development projects have nine types of waste:
building the wrong feature or product,
mismanaging the backlog,
rework,
unnecessarily complex solutions,
extraneous cognitive load ([%x thinking %]),
psychological distress,
waiting and multitasking,
knowledge loss,
and ineffective communication.
*None of these are software issues,*
so if you only think about the code in your project and not about the people writing it,
everything will take longer and hurt more than it needs to.
</div>

## An Example {: #intro-example}

People sometimes talk about 10X programmers—ones who are
ten times more productive than average—but do they actually exist?
To find out,
[%b Prechelt2000 %] looked at how long it took eighty programmers
to solve the same problem in the language of their choice.
Their times (in hours) are shown as a whisker plot in [%f intro-prechelt %].

[% figure
   slug="intro-prechelt"
   img="prechelt-development-time.svg"
   caption="Development Time"
   alt="Box-and-whisker plot show that most developers spent between zero and 20 hours but a few took as long as 63 hours."
%]

The shortest and longest development times were 0.6 and 63 hours respectively,
giving a ratio of 105X.
However,
the subjects used seven different languages;
if we only look at those who used Java (about 30% of the whole)
the shortest and longest times are 3.8 and 63 hours,
giving a ratio of "only" 17X.

But comparing the best and the worst of anything gives us
an exaggerated impression of the difference.
If we compare the 75th percentile to the 25th percentile
we get a ratio of 18.5/7.25 or 2.55;
if we compare the 90th percentile to the 50th we get 3.7,
and other comparisons give us other values.
As [%b Prechelt2019 %] explains,
the best answers to our original question are therefore:

-   good programmers aren't 10 times more productive than average;

-   but it's reasonable to say that they are about four times more productive.

## Licensing {: #intro-license}

All of the written material on this site is made available
under the Creative Commons - Attribution - NonCommercial 4.0 International license
([CC-BY-NC-4.0][cc-by-nc]),
which allows you to use and remix this material for non-commercial purposes,
as-is or in adapted form,
provided you cite its original source.
Please see [% x license %] for details.

Parts of these lessons originally appeared in [%b Sholler2019 Wilson2019 Irving2021 Smalls2021 %];
I'm grateful to [Taylor & Francis][taylor-francis],
[PLoS][plos],
and my co-authors for allowing that material to be re-used under open licenses.

## Acknowledgments {: #intro-ack}

This book is dedicated to [Marian Petre][petre-marian],
who taught me that not everything worth studying can be measured,
and to Tom Wilkie,
who taught me how to turn a thousand words I'd written into a hundred someone would actually want to read.
I also thank all of the students who have done projects with me over the years,
and the people mentioned below for their feedback;
any errors, omissions, or misunderstandings that remain are entirely my fault.

- [Bram Adams](https://mcis.cs.queensu.ca/bram.html)
- [Rohan Alexander](https://rohanalexander.com/)
- [Tavish Armstrong](http://tavisharmstrong.com/)
- [Titus Barik](https://www.barik.net/)
- [Robert Beghian](http://www.vasken.ca/)
- [Yanina Bellini Saibene](https://yabellini.netlify.app/)
- [Neil Brown](https://twistedsquare.com/)
- [Jordi Cabot](https://jordicabot.com/)
- [Silvia Canelón](https://silvia.rbind.io/)
- Francisco Canas
- [Mike Conley](https://mikeconley.ca/)
- [Michael DiBernardo](https://mikedebo.com/)
- [Isaac Ezer](http://www.isaacezer.com/)
- [Ian Flores Siaca](https://ianfs.dev/)
- [Adam Goucher](https://adam.goucher.ca/)
- [Mustafa Haddara](https://twitter.com/MustafaHaddara/)
- [Johan Harjono](http://johanharjono.com/)
- [Kate Hertweck](https://katehertweck.com/)
- [Daniel Jackson](https://people.csail.mit.edu/dnj/)
- [Jacob Kaplan-Moss](https://jacobian.org/)
- [Ritu Kapur](https://sites.google.com/view/ritu-kapur)
- [Zain Kazmi](https://zainhkazmi.github.io/)
- [Laurie MacDougall Sookraj](https://www.linkedin.com/in/lauriemacdougallsookraj/)
- [Darren McElligott](https://www.linkedin.com/in/darren-mcelligott-07689473/)
- [Kim Moir](https://kimmoir.blog/)
- [Natalia Morandeira](https://nmorandeira.netlify.app/)
- [Meiyappan Nagappan](https://cs.uwaterloo.ca/~m2nagapp/)
- [Iain Parris](https://parris.org/)
- [Elizabeth Patitsas](https://patitsas.github.io/)
- [Andrew Petersen](https://utmandrew.bitbucket.io/)
- [Andrey Petrov](https://shazow.net/)
- [Andrew Potapov](https://www.andrewpotapov.com/)
- [Lutz Prechelt](http://www.mi.fu-berlin.de/w/Main/LutzPrechelt)
- [Yim Register](https://students.washington.edu/yreg/)
- [Evan Schultz](https://evanjustevan.com/)
- [Alex Serebrenik](https://www.win.tue.nl/~aserebre/)
- [Naaz Sibia](https://www.linkedin.com/in/naaz-sibia/)
- [Andreas Stefik](https://web.cs.unlv.edu/stefika/)
- Rory Tulk
- [Blake Winton](https://bwinton.latte.ca/)
- [Andy Zaidman](https://azaidman.github.io/)
- [Andreas Zeller](https://andreas-zeller.info/)

Finally,
I would like to thank David Graf for [doi2bib][doi2bib]
and Alexandra Elbakyan for [Sci-Hub][sci-hub]:
this book would have been much harder to write without their idealism and hard work.
