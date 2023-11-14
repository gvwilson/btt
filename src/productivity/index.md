---
title: "Productivity"
tag: "FIXME"
syllabus:
- FIXME
---

## Some Data {: #productivity-10x}

People sometimes talk about 10X programmers—ones who are
ten times more productive than average—but do they actually exist?
To find out,
[%b Prechelt2000 %] looked at how long it took eighty programmers
to solve the same problem in the language of their choice.
Their times (in hours) are shown as a whisker plot in [%f productivity-prechelt %].

[% figure
   slug="productivity-prechelt"
   img="prechelt-development-time.svg"
   caption="Distribution of development times."
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
