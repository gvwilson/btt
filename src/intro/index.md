---
title: "Introduction"
tag: "What this book talks about and why."
---

These lessons are designed to help you succeed in your first collaborative software project.
Some topics are purely technical,
while others are about the social aspects of programming:
working in teams,
cutting features when time runs short,
and making sure everyone's work is evaluated fairly.
Our aim is to teach you how to be a *compassionate programmer*:
one who cares about the well-being of their colleagues,
their users,
and society.
This focus is not entirely altruistic—everything you do to help others
also helps your future self—but now that we know how much harm software can do,
we need to build it better.

Much of what's hard about building software stems from the fact that
our mental capacity is limited [%b Hermans2021 %].
Other challenges that initially appear technical
are actually caused by how people think and act in groups.
One of our central themes is there a modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

## Audience {: #intro-audience}

Every lesson should be written with a specific audience in mind [%b Wilson2019 %].
These **learner personas** describe ours:

-   *Yani* is in the third year of a computer science degree.
    She worked on several volunteer projects in high school and through her mosque,
    but the "Introduction to Software Engineering" course she's about to take
    will be her first semester-long team project at university.
    This guide will help her and her teammates figure out what to do when.

-   *Brad* is in Yani's classes.
    He started programming when he was nine years old,
    and as a result can do many assignments in half the time it takes other students
    (something he attributes to intelligence and aptitude
    rather than to his parents being able to afford to send him to after-school coding camps).
    He finds any discussion of what he calls "fluffy stuff" tiresome;
    this guide will help him understand why that attitude is self-defeating.

-   *Sharla* has taught the "Introduction to Software Engineering" class twice;
    each time,
    they came away feeling that their students had wasted a lot of time
    on things that turned out not to be useful.
    This guide will help them structure the next offering
    and set more realistic expectations.

This book can be read on its own or as a companion to [%b Wilson2022 %].
If you are looking for a course project,
please consider adding a tool to the ones it covers.

## An Example {: #intro-example}

Are some programmers really ten times more productive than average?
To find out,
[%b Prechelt2000 %] looked at how long it took a set of programmers
to solve the same problem in the language of their choice.
The time in hours is shown as a whisker plot in [%f intro-prechelt %];
each dot is a single data point,
while the left and right boundaries of the box show the 25th and 75th percentiles respectively,
and the mark in the middle shows the median.

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
If we compare the 75th percentile (which is the middle of the top half of the data)
to the 25th percentile (which is the middle of the bottom half)
we get a ratio of 18.5/7.25 or 2.55;
if we compare the 90th percentile to the 50th we get 3.7,
and other comparisons give us other values.
As [%b Prechelt2019 %] explains,
the answers to our original question are therefore:

1.  It depends what you mean.

2.  No, good programmers aren't 10 times more productive than average.

3.  But yes, it's reasonable to say that they are about four times more productive.

## Licensing {: #intro-license}

All of the written material on this site is made available
under the Creative Commons - Attribution - NonCommercial 4.0 International license
([CC-BY-NC-4.0][cc-by-nc]),
which allows you to use and remix this material for non-commercial purposes,
as-is or in adapted form,
provided you cite its original source.
Please see [% x license %] for details.

## Acknowledgments {: #intro-ack}

This book is dedicated to [Marian Petre][petre-marian],
who taught me that not everything worth studying can be measured,
and to Tom Wilkie,
who taught me how to turn a thousand words I'd written into a hundred someone would actually want to read.
I am also grateful to all of the students who have done projects with me over the years.

I have tried to base these lessons on the best available research.
Where that doesn't have answers,
I have drawn on the experience of the people mentioned below.
Any errors, omissions, or misunderstandings that remain are entirely our fault.

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

Parts of these lessons originally appeared in [%b Sholler2019 Wilson2019 Irving2021 Smalls2021 %];
I'm grateful to [Taylor & Francis][taylor-francis],
[PLoS][plos],
and my co-authors for allowing that material to be re-used under open licenses.
I would also like to thank David Graf for [doi2bib][doi2bib]
and Alexandra Elbakyan for [Sci-Hub][sci-hub]:
this book would have been much harder to write without their idealism and hard work.
