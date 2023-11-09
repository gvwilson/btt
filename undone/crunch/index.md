---
title: "Crunch Mode"
tag: "Working harder isn't the best way to get better grades"
syllabus:
- FIXME
---

I used to brag about the hours I was working.
Not in so many words, of course—I had *some* social skills—but
I'd show up for work around noon,
unshaven and yawning,
and casually mention how I'd been up until 6:00 a.m. working on some monster bug.

Looking back,
I can't remember who I was trying to impress.
Instead,
what I remember is how much of the code I wrote in those all-nighters
I threw away once I'd had some sleep.
My mistake was to confuse "long hours" with "getting things done".
You can't produce software (or anything else) without doing some work,
but you can easily do lots of work without producing anything of value.
Scientific study of overwork goes back to at least the 1890s;
the most important results are:

1.  Working more than eight hours a day for more than a couple of weeks of time
    lowers your total productivity,
    not just your hourly productivity—i.e.,
    you get less done *in total* in crunch mode
    than when you work regular hours.

1.  Working over 21 hours in a stretch
    increases the odds of you making a catastrophic error
    just as much as being legally drunk.

These facts have been verified through hundreds of experiments
over the course of more than a century,
including some on novice software developers [%b Fucci2020 %].
The data behind them is as solid as the data linking smoking to lung cancer.
However,
while most smokers will at least acknowledge that their habit is killing them,
people in the software industry still talk and act as if
they were somehow immune to science.
To quote [%b Robinson2005 %]:

<blockquote markdown="1">

When Henry Ford famously adopted a 40-hour workweek in 1926,
he was bitterly criticized by members of the National Association of Manufacturers.
But his experiments,
which he'd been conducting for at least 12 years,
showed him clearly that cutting the workday from ten hours to eight hours—and
the workweek from six days to five days—increased
total worker output and reduced production cost…
the core of his argument was that reduced shift length meant more output.

…many studies,
conducted by businesses, universities, industry associations and the military,
…support the basic notion that,
for most people,
eight hours a day,
five days per week,
is the best sustainable long-term balance point between output and exhaustion.
Throughout the 30s,
40s, and 50s, these studies were apparently conducted by the hundreds;
and by the 1960s,
the benefits of the 40-hour week were accepted almost beyond question
in corporate America.
In 1962,
the Chamber of Commerce even published a pamphlet
extolling the productivity gains of reduced hours.

But, somehow, Silicon Valley didn't get the memo…

</blockquote>

I spent two years at a data visualization startup in my early thirties.
Three months before our first release,
the head of development "asked" us to start coming in on Saturdays.
We were already pulling one late night a week at that point
(without overtime pay—our boss seemed to think that
ten dollars' worth of pizza
was adequate compensation for four hours of work)
and most of us were also working at least a couple of hours at home in the evenings.
To no one's surprise,
we missed our "can't miss" deadline by ten weeks,
and had to follow up our 1.0 release with a 1.1 and then a 1.2
to fix the crash-and-lose-data bugs we'd created.
We were all zombies, and zombies can't code.

Hours like these are sadly still normal in many parts of the software industry,
and may actually be worse now that so many people are working from home.
Designing and building software is a creative act that requires a clear head;
it only takes a couple of minutes to create a bug
that will take hours to track down later.
As Robinson writes:

<blockquote markdown="1">

Productivity varies over the course of the workday,
with the greatest productivity occurring in the first four to six hours.
After enough hours,
productivity approaches zero;
eventually it becomes negative.

</blockquote>

It's hard to quantify the productivity of programmers, testers, and UI designers
[%b Sadowski2019b Forsgren2021 %],
but five eight-hour days per week has been proven to maximize long-term total output
in every industry that has ever been studied.
There is no reason to believe that ours is any different.

Ah, you say, but that's *long-term* output.
What about short bursts now and then,
like pulling an all-nighter to meet a deadline?
That's been studied too,
and the results aren't pleasant.
Your ability to think drops by 25 points for each 24 hours you're awake.
Put it another way,
the average person's IQ is only 75 after one all-nighter,
which puts them in the bottom 5% of the population.
Two all nighters in a row and their effective IQ is 50—the level at which
people are considered incapable of independent living.

The catch in all of this is that
people usually don't notice their abilities declining.
Just like drunks who think they're still able to drive,
people who are deprived of sleep don't realize that
they're not finishing their sentences (or thoughts).
They certainly don't realize that
they're calling functions with parameters in the wrong order
or that the reason the tests are failing is that
they've forgotten to redeploy the application—again.

The first and most important lesson in this book is therefore
to think very hard about what's more important—how much you produce
or how much of a martyr you appear to be—and to pace yourself accordingly.

## Time Management {: #crunch-time}

[%b Edwards2009 %] found that
starting assignments early and working consistently predicted good grades.
However,
while people in industry joke that having two bosses means living in hell,
students usually answer to four or five professors
whom don't coordinate due dates across their courses.

The best way to handle this situation—or more honestly, the least bad way—is
to prioritize carefully.
Get a piece of paper and draw a 3×3 grid.
The X axis is effort: label its divisions "minutes", "hours", and "days".
The Y axis is time: label it "low", "medium", and "high".
You should wind up with something like [%f crunch-grid %].

[% figure
   slug="crunch-grid"
   img="effort-importance.svg"
   caption="An example of an effort/importance matrix."
   alt="Effort/importance matrix"
%]

Next,
put everything you need to do somewhere on the grid,
and then throw away the high-effort, low-importance items in the bottom right—you
aren't going to get to those.
You can then start assembling the other items into a schedule,
starting with the upper-left corner.
These are the things that will give the highest return on invested time;
more importantly,
starting with these means that if you've under-estimated effort,
you will still deliver *something*.

The tricky items are the ones on the diagonal.
Should you tackle one thing that is high effort and high importance
or three things that are individually less important
but require the same total effort?
Laying things out on a grid can't answer that question,
but at least it can tell you what the question is.

<blockquote>

How to prioritize:
always finish first
the tasks that will allow other people to continue/start/finish their work.

— Yanina Bellini Saibene

</blockquote>

If any task on your list is more than an hour long,
break it down into smaller pieces and prioritize those separately.
Figuring out what those pieces are can take time,
so don't be embarrassed to make "plan XYZ" a task in its own right.
And remember that the future is approaching at a rate of 24 hours per day:
if something is going to take thirty hours to finish,
you had better allow at least five working days for it,
which means you'd better start at least that far ahead of the deadline.

The point of all this organization and preparation is
to be able to immerse yourself in your problem.
[%b Csikszentmihalyi1991 %] popularized the term flow for this;
athletes call it "being in the zone",
while musicians talk about losing themselves in what they're playing.
The good news is that you're much more productive in this state
than when you're multi-tasking.
The bad news is that
it takes anywhere from several seconds to several minutes
to get back into this state after an interruption [%b Parnin2010 Borst2015 %].
In other words,
if you are interrupted half a dozen times per hour
you are *never* at your productive peak.
Ironically,
the cost of self-interruptions may be even worse than
the cost for external interruptions [%b Abad2018 %].

<div class="callout" markdown="1">

### Open offices suck

Open offices were created
to reduce air conditioning costs 
and to allow (mostly male) managers to keep an eye on (mostly female) typists
[%b Eley1995 %].
They lower productivity in every way we can measure [%b Bernstein2018 %];
sadly,
the same is true of other interruption-rich environments
like your favorite coffee shop.
If you really want to get more done,
you should avoid both.

</div>

Finally,
you will be more productive in the long run if your back doesn't ache,
and being away from the keyboard
gives you a chance to reflect on what you've just been doing.
You should therefore take a five-minute break every hour.
Don't use the time to check email or your phone—that
won't reset your brain.
Instead,
get up and stretch,
refill your water bottle,
or go and restack the dishwasher.
You'll be amazed at how often you can solve a problem
that's been baffling you for an hour
by taking a short walk…
