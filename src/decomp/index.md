Most people learn better together than they do on their own [%b Michaelson2004 %]:
they achieve higher grades,
retain information longer,
are less likely to drop out of school,
and graduate with better communication skills
and a better understanding of what will be expected of them
in their subsequent careers.
On the other hand,
a badly-run team is worse than no team at all,
since people will waste hours or days arguing with one another,
duplicating or undoing each other's work,
and wishing that they had taken some other course or joined some other lab.

As noted in [%x intro %]
the software you get reflects the division of labor.
No matter how you allocate work,
make sure that everyone understands who is doing what.
Actual roles can be fluid;
the most important thing is that
team members understand and accept their responsibilities and everyone else's
at any particular moment [%b Barke2019 %].

## Division of Labor {: #decomp-division}

In a **modular decomposition**,
each person is responsible for one part of the program ([%f decomp-division %]).
For example,
one person might build the user interface
while a second implements the data analysis
and a third handles the back-end interactions with the database.
Having people own parts of the code like this
produces lower failure rates in industry [%b Bird2011 %],
but is a bad strategy in a course project:

1.  It leads to **big bang integration**,
    in which all the components only meet each other for the first time
    at the end of the project.
    Big bangs almost always fail [%fixme citation %].

2.  Each team member only really understands one aspect of the project,
    so if someone drops out or fails to do their work,
    the project as a whole will fail.

[% figure
   slug="decomp-division"
   img="division.svg"
   caption="Dividing work in a software team."
   alt="Modular, functional, and feature decomposition."
%]

In a **functional decomposition**,
on the other hand,
each person is responsible for one type of task:
one person does design,
a second writes code,
a third takes care of testing,
and so on.
This strategy avoids the problem of big-bang integration,
but once again,
every team member is a single point of failure

**Feature decomposition** avoids the weaknesses of the first two approaches.
Instead of owning an entire subsystem for the life of the project,
each team member handles design, coding, testing, and deployment
for one small feature after another.
This strategy gives everyone a chance to hone all their skills,
and is a good way to cope with the endless multitasking of student life.

**Rotating decomposition** has the same benefits and drawbacks as feature decomposition.
If everyone does one task for a couple of weeks,
then a different task for the next two weeks,
and so on,
then the team has to pay ramp-up costs several times over.
In the long term,
though,
it is more robust (having a team member drop out is less harmful),
and if everyone on the team is familiar with every aspect of the software,
they can all contribute to design and debugging sessions.

Any of these strategies is better than **chaotic decomposition**,
which unfortunately is the most common approach.
If people have different ideas about who's supposed to do what,
some things won't be done at all
while others will be done several times over.
You can tell if your decomposition is chaotic
by counting how many times people say,
"I thought *you* were doing that!"
or "But I've already done that!"
All other decompositions tend toward chaos under pressure,
so it's important to establish rules early
and stick to them when your load is light
so that the instinct to do the right thing will be there when you need it.

## How to Decide {: #decomp-deciding}

Feature decomposition and rotating decomposition solve another problem,
which is that agreeing on how work should be split up in principle
is usually much easier than agreeing on who should do what.
Some jobs have higher social status than others,
and what is or isn't considered important
usually reflects divides within society—so much so that
sociologists use the phrase "[women's work][womens_work]" to describe the phenomenon.
It is also known as "[quarterback syndrome][quarterback_syndrome]":
two thirds of NFL players in the United States are Black,
but 83% of quarterbacks are white,
which is the position on a team with the highest social status.

Among programmers,
writing operating systems or training AI models
has higher status than building user interfaces;
people doing the former are both paid more and more likely to be male
than people doing the latter,
regardless of ability or value delivered to the employer.
This creates a feedback loop:
white and Asian men pursue certain career paths
because they have high status (they want to be "real programmers"),
and the fact that they are pursuing those careers is what maintains their higher status.
It also creates a confirmation loop:
since women and people of color get fewer chances to do certain tasks,
they are less good at them,
which "confirms" the initial bias.

All of this starts in the classroom.
For example,
[%b Grunspan2016 %] found that
while female students' ranking of fellow students was generally accurate,
male students consistently over-estimated the performance of their male peers.
The result is that in mixed-gender teams,
female students are more likely to wind up responsible for taking notes,
writing documentation,
and other low-status tasks [%fixme citation %].
Some have experienced this so often that
they have come to accept it as the price they have to pay for being in tech.
Others protest,
but those who do are often dismissed as being "difficult".
Many take a third path and decide to leave programming—after all,
why play a game that's unfair?

<blockquote markdown="1">
### In the beginning

Programming was originally considered a female occupation,
but as it became more lucrative it came to be viewed as "naturally" male.
[%b Abbate2012 Ensmenger2012 %] describe how this happened,
while [%b Hicks2018 %] looks at how Britain lost its early dominance in computing
by systematically discriminating against its most qualified workers:
women.
Some men become quite uncomfortable when this is brought up,
but we need to learn how to discuss our own history
if we want to be able to think clearly about what we're doing today will change society tomorrow.
</blockquote>
