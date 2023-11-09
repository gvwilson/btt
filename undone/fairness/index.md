---
title: "Fair Play"
tag: "The most important chapter in this book"
syllabus:
- FIXME
---

This book is about course projects, which are often designed to prepare you for
real jobs.  Since the transition from being a student to
working full time is one of the most important in your career, this chapter
looks at the hiring process and what happens
afterward.

There is no way to discuss these topics without talking about fairness and bias in the tech
industry.  I was interviewing for a new job as I was writing this book, and
while some companies' interviewing processes were designed to create a level
playing field, others were not (and that's putting it politely).  How companies
get this wrong contributes to how they sometimes build things that harm society
and embarrass their creators.  It easy to avoid these mistakes if you are
willing to look beyond the code you write; that first step is often the hardest,
but I hope this discussion will help you take it.

## How Tech Companies Get Hiring Wrong

In 1905, Harvard began selecting students based on their College Entrance Exam
Board results.  As a result, Jewish enrolment began to rise, and by the early
1920s they made up more than a fifth of the incoming class.  This wasn't an
outcome the establishment was willing to accept, but neither were explicit
quotas, so they moved the goalposts [%b Karabel2006 %].  Admissions
officers began asking questions about the "character" of prospective students,
and the university began asking for personal essays that could be graded however
the university found most convenient. By 1933, the rate of Jewish admission was
back down to an "acceptable" 15%.

Harvard's decision to turn away more capable people in favor of less capable
ones doesn't make sense if you think that a university's job is to find and
train the smartest people it can.  It makes more sense when you realize that
most institutions' first priority is
to perpetuate themselves: if it wasn't, they probably wouldn't still be around.

Similarly, the hiring process at many tech companies isn't designed to find the
best programmers: instead, it is designed (or more often has just evolved) to
find people who are like those doing the hiring.  "Cultural fit" almost always means "like me":
consciously or not, we are all biased toward
those who look like us, talk like us, and make the same pop culture references
as us, which has nothing to do with on-the-job ability
[%b Greenwald1995 Jost2009 %].

One way this bias shows up is in whiteboard coding questions about linked lists, dynamic
programming, and other topics from computer science classes on data structures
and algorithms.  As [Hillel Wayne][wayne-hillel] discovered when he looked at
[their history][wayne-linked-lists], they might have indicated how much
experience someone had using C or Pascal in the 1980s, but they have no more to
do with on-the-job performance than the essay questions used by Ivy League
schools have to do with your ability to learn.  When [April Christina
Curley][curley-april], a recruiter at Google, began coaching Black students how to prepare for
interviews with Google that included questions like these, the company shut her
down—even though schools like Stanford had been running coaching sessions for
their students for years [%b Tiku2021 %].

[%b Behroozi2019 Behroozi2020a Behroozi2020b %] summarize many other things that often go wrong in hiring, from
long delays waiting for feedback to asking candidates to spend several days
working for free on programming assignments.  These aren't just signs of
dysfunctional company culture: they also make hiring harder for some people than
others.  For example, a single parent or someone caring for a relative with
chronic illness may not be able to devote ten hours to an unpaid side project.
If the interview process requires that, the company is effectively biased toward
people who are economically secure and have lots of free time, which doesn't
correlate with how well they can program in a full-time job.

<blockquote markdown="1">
### A sign of privilege

You probably won't be treated with any more respect on the job than you were
while interviewing.  However, when I wrote, "If a company does any of these
things, go find another one," in the first draft of this chapter, one of the
reviewers wrote, "Gosh, it must be nice to be able to walk away from a job."
They were right: most people aren't as financially secure as me, so they aren't
able to be as finicky about who they work for as I am.  In other words, I made
the same mistake as a team lead who assumed that since their evenings and
weekends were theirs to do with as they wished, everyone else's would be too.
</blockquote>

As a student looking for your first full-time job you probably won't have any
control over the hiring process, but seeing whether the company does it well or
not gives you valuable information about how well run it is.
Here are a few positive indicators:

Write inclusive, accessible job ads.
:   [%b Gaucher2011 %] is just one of many studies showing that gendered
    wording in job ads reinforces gender inequality in male-dominated
    occupations. [Gender
    Decoder][gender-decoder] and [GenderMag][gendermag] can help you find bugs like this
    in ads and software [%b Hilderbrand2020 %]. Tools for finding and
    eliminating racial bias and other problems aren't as common, but
    [%b Washington2020 %] will tell you what to aim for, and if [WebAIM WAVE][webaim-wave] doesn't give your online
    job ads a clean bill of health, please fix them.

Post a public description of the hiring process.
:   [Automattic's][automattic-hiring] description is
    a good example: it lays out what's going to happen in what order, how much
    time is expected, and the principles everything is based on.

Use blinded screening.
:   Everyone has implicit biases, and many of the rules scientists follow when running
    experiments are designed to prevent their biases contaminating their results
    (FIXME).  The same is true of hiring, and so is the
    solution. For example, my first-round interview with Automattic was done
    over Slack so that my appearance, my accent, or the fact that I sometimes
    need a couple of moments to collect my thoughts wouldn't bias the
    interviewer.  Similarly, companies should redact things like a candidate's
    age, race, and gender when evaluating resumes.

Use diverse interview panels.
:   Giving people from under-represented backgrounds a say in who's hired next
    gives other people with similar backgrounds a better chance of being treated
    fairly.

Have candidates solve realistic problems with their preferred tools.
:   Most programmers have laptops, and video calls are now a part of everyday
    life in industrialized countries, so there's no reason *not* to give people
    an hour to show what they can do using the IDE of their choice.  There is
    also no reason to stop them using online search while they do this: every
    working programmer relies on our external collective memory, so telling a
    candidate they can't during an interview is like telling a chef to make a
    meal without using saucepans or knives.

These guidelines apply to your school and your courses as well.  Are course
descriptions and course websites inclusive? Are instructors required to use
blinded grading to ensure that personal likes and dislikes don't affect grades?
If the answers are "no", what can you and your classmates do to fix things?

<blockquote markdown="1">
### Questions to ask

I have interviewed people who didn't ask a single question about the company,
what an average day would look like, or how their career might evolve.
[Julia Evans][evans-julia] has a good list of
[questions to ask in interviews][evans-interviews], and
[T. Carter Baxter][baxter-t-carter] has
[another][baxter-interviews].  There won't be time to get to them all, but
asking two or three will impress your interviewer as well as giving you valuable
information.
</blockquote>

## On the Job

Unfair treatment doesn't end after people are hired.  Study after study has
shown that men and women are treated differently on the
job: women have to work twice as hard to be given half as much credit,
they are listened to less often or given less credit for new ideas, and what is
seen as confidence in men is seen as pushiness or stridency in women
[%b Gavett2017 %].  People of color are undermined and discounted in the
same way in majority-white workplaces in Europe and North America, and
discrimination based on race, faith, and caste are endemic in the rest of the
world as well.

Many companies have taken steps to remedy this during hiring. However, hiring
more people from under-represented groups doesn't make a difference if they have
to work twice as hard to be taken half as seriously, if they are constantly
passed over for promotion, or if discussions about promotion continue to take
place in the men's locker room after the department's Friday afternoon hockey
game.  There are no easy fixes to these problems, but there are things companies
can do that you can ask for even as a junior hire:

Share data on how well the company has been doing recently.
:   It's reasonable to ask during an interview what proportion of a company's
    staff (technical and otherwise) come from under-represented backgrounds and
    about the average length of stay at the company.  If the interviewer doesn't
    know the answer, they should be able to get it; if the company doesn't have
    that data or won't share it, you've just learned something.

Have an org chart.
:   As we said in FIXME, every organization has a power
    structure: the only question is whether it's public and accountable, or
    whether the organization runs on who you know and how willing people are to
    barge in on strangers.

Have written criteria for performance reviews.
:   The ones shown in FIXME are a good model, and these
    *are* something a company can share before hiring you. If a company doesn't
    have criteria, or if performance reviews are only done when an employee asks
    for one, the system is once again biased toward extroverts and the
    well-connected.

Specify how much time employees can take off.
:   Some tech companies have an "unlimited vacation" policy, meaning that
    employees can take as much time off as they want as long as their work gets
    done.  This sounds very attractive, but [people actually take *less* time
    off][namely-time-off] under these policies, both because they feel guilty
    and because they worry about taking too much.  It also saves companies
    money: if someone is owed vacation days when they're laid off, the company
    has to compensate them, but if there's no target, they don't.

## Being an Ally

But suppose you are a straight, physically able, white or Asian male without
mental health issues—why should you care about people who are marginalized
because they aren't these things?  One argument is self-interest: study after
study has shown that more diverse teams perform better, that companies with more
diverse management are more profitable, and so on [%b Zhan2020 %].

<blockquote markdown="1">
### Setting limits

Men who want an excuse to continue to be assholes sometimes try to be clever
with words and talk about "diversity of thought," meaning, "I should be allowed
to be offensive as long as I don't raise my voice."  This is an example of the
[paradox of
tolerance][paradox-of-tolerance]: if a group is tolerant without limit,
it will eventually be undermined by the intolerant taking advantage of that. As
James Baldwin said, "We can disagree and still
love each other unless your disagreement is rooted in my oppression and denial
of my humanity and right to exist."
</blockquote>

Another reason to care about these issues is that discussion of fair play stops
being theoretical as soon as we talk about your rights as an employee.  Until
recently there has been less discussion of this in tech than of intellectual
property rights ([%x property %]), but in the wake of incidents like [Google's
decision to fire the AI researcher Timnit Gebru][gebru-firing], programmers are
belatedly realizing that the industry they have created will treat them just as
callously as it treats everyone else.

Standing up to a bad boss or an unfair professor is easier in theory than in
practice, though, because the student's evaluation of the professor doesn't
affect the professor nearly as much as the professor's evaluation of the student
affects the student.  This imbalance is why management fads like "radical candor" are bullshit (in the technical sense of the word
[%b Frankfurt2005 %]). The idea that everyone should say what they think
is appealing in theory; in practice, managers will brush aside the fact that
they can fire people who say things they don't like and blame the marginalized
for not speaking out more or more loudly.

The only effective way to address power disparities like these is collective action: many people with relatively
little power can defend their rights if they band together.  Forty years of
sustained disinformation from the rich and powerful have made many people
believe that collectives are intrinsically inefficient or that they stifle
innovation; ironically, the entrepreneurs and CEOs who are the most vocal
proponents unrestricted capitalism all organize their companies along socialist
lines [%b Phillips2019 %].

As an example of what working together looks like, consider the difference
between a ride-sharing company like Uber and the
house-cleaning company Up & Go.  Uber uses its control
of the app that connects customers with drivers to extract profits by squeezing
drivers. In contrast, the people who work for Up & Go own the app as a group; 5%
of what customers pay goes to its upkeep, and the rest goes to the workers
[%b Thompson2019 %].  There might be one less billionaire in the world,
but everyone else benefits.

Up & Go is an example of a commons:
something managed jointly by a community according to rules they have evolved
themselves.  All three parts of that definition are essential: a commons isn't
just a shared pasture or an open source software stack; it also includes the
community that shares it and the rules they use to do so
[%b Bollier2014 Ostrom2015 %].  As [%b Mildenberger2019 %]
describes, the idea of "the tragedy of the commons" gets things completely
wrong: people exploiting a shared resource so much that it collapses is what
happens when a commons breaks down.

<blockquote markdown="1">
### Your politics is showing

An early reviewer of this material asked whether it was appropriate for me to
put so much of my personal politics into it.  I pointed out that many schools
have a course on the business of software that talk exclusively about for-profit
startups backed by private investors and venture capital.  Choosing to discuss
those topics is equally political—it's just more common.

Other reviewers have pointed out that telling people they should support fair
play because it will benefit *them* implies that they would have no reason to do
so if it didn't.  The idea that people should only act out of self-interest is
also political, and one I strongly disagree with.  However, people like Brad
(whom we met in [%x intro %]) have been conditioned to believe that
being cynical is the same thing as being smart; I have found out the hard way
that if I say, "Do the right thing because it's the right thing," the people
whose behavior most needs to change won't listen.
</blockquote>

You might think there isn't a lot you can do as a student or as a junior
programmer to fix what's broken in our industry, but there is.  An
ally is a someone with unearned advantages who tries to
understand their own privilege and create an environment that's fair for
everyone.  As [this guide][dlf-active-bystander] from the [Digital Library
Foundation][dlf] explains, there are several ways to be an
active bystander, i.e., several ways to
lend your privilege to
defuse situations and defend people who are being attacked.

<blockquote markdown="1">
### Not acting is a choice as well

FIXME said that an organization's culture is defined by
the worst behavior it tolerates [%b Gruenert2015 %]; I believe that who we
are as individuals is defined in the same way.
</blockquote>

[%b Dobbin2019 %] (summarized in [%b Dobbin2020 %]) found that most
of what American companies have done over the past twenty years to reduce sexual
harassment and discrimination has either had no effect or made things worse. The
reason is that the people who care don't gain anything from being told they
should, while the people who are part of the problem resent being told that and
tend to take out their anger on the people the training is meant to protect.

However, [%b Dobbin2019 %] also found that what *did* make a difference
was showing people how to intervene, since this made them more likely to do so
(in the same way that having some first aid training makes you more likely to
take action in a crisis).  An example of this kind of training is the guidelines
in [%b Aurora2018 %] for responding to Code of Conduct violations ([%x structure %]). On a
smaller scale, your instructor can have you work through scenarios like this one
with your teammates and the rest of your class:

> Some of the students in a team project course are openly gay.  Some other
> students have privately told the instructor that they would rather not be in the
> same teams as the gay students for religious reasons.  How should the instructor
> respond?

<!-- continue -->
Another scenario might be:

> Your and your teammates frequently work together in the business school library
> (which has better WiFi and more comfortable chairs than the computer labs).
> Every time you do, one of your teammates makes a point of sitting beside some
> younger students that they find attractive and talking with them.  It's clear
> from those students' body language that they find the attention unwelcome;
> you've pointed this out to your teammate, but their behavior has continued.
> What should you do next?

Neither of these scenarios is about programming, but I hope you understand by
now that the success or failure of your project depends on a lot more than just
the code you write.  Learning how to handle situations like these may also help
you become more compassionate: if you've never had to worry about them, the odds
are that (in John Scalzi's memorable analogy)
you've been playing at the lowest difficulty level there is your whole life, and
as a result don't realize how much harder things are for others whose default
setting isn't "easy
mode" [%b Scalzi2012 %].

<blockquote markdown="1">
### How far back should we go?

Preparatory privilege is the advantage
someone has in a supposedly objective assessment as a result of opportunities
earlier in life that other people didn't have.  Ignoring it is like ignoring the
difference between professional athletes who are paid to train all day and
amateurs whose jobs only allow them to train in the evening or on weekends, or
pretending that people doing interviews in their second or third language are on
an equal footing with people who are interviewing in their native language.

But imagine you're about to have a meeting with someone.  There's a box with
half a dozen cookies in the room, so you help yourself to a couple before the
other person shows up. When they do, you have to make a choice: do you say,
"I've already had two, so I should only have one more and you should get three"
or, "There were four cookies in the box when you arrived, so we get two each"
(meaning that you will have had four in total).

Most people would say that the first answer is the moral one—in my experience,
people who don't aren't people you'd want on your team.  On the other hand, if I
had a couple of cookies yesterday or last week, I probably won't feel obliged to
give you more than half today.  Is it a company's responsibility to take past
inequities into account when hiring?

If the company is interested in on-the-job performance, the answer is "yes".
Going back to the athletic analogy, an amateur who can run a hundred meters in
12 seconds could perform better than a professional who can do it in 11 *once
they start training full-time*, i.e., once their disadvantage is removed.
Similarly, female students are less likely to be called on in class and more
likely to be given non-coding tasks in team projects than male students.  If
they can get a B despite that, they will probably outperform a male student who
only gets an A with the deck stacked in his favor, provided the company treats
both equally after they are hired.

That last statement is where many companies and universities fail despite good
intentions.  The [Centre for Community Organizations][coco] has a depressing
summary of what it's like to be [the "problem" woman of color in the
workplace][coco-problem].  If what it describes isn't familiar, you might be a
part of the problem, just as I was in my teens and twenties.
</blockquote>

## The Wider World

Between 1985 and 1987, a programming bug in the [Therac-25][therac-25] resulted
in six patients being given massive overdoses of radiation, leading to death or
serious injury.  This incident has been used as a cautionary tale in software
engineering courses ever since, but since very few of us write control software
for medical radiation machines, this example and others like it seem very
abstract.

In the last few years, though, we have all seen first-hand just how much harm
software can do to everyone.  A decade ago, Facebook discovered that angry
people are more likely to engage with the platform, resulting in higher ad
revenue for the company [%b Hao2021 %].  Since disinformation and
radicalization were profitable, the company did everything it could to deflect
criticism and avoid responsibility, even as they fueled the rise of violent
nationalism and a campaign of mass murder [%b Rajagopalan2018 %].  By the
time COVID-19 began to spread, it and other tech companies had trained people
all over the world believe in conspiracy theories rather than medicine, with
fatal consequences.

<blockquote markdown="1">
### We just sell the poison; we don't administer it

In March 2019, a right-wing terrorist killed 51 people at prayer in
Christchurch, New Zealand. Every one of the sources he cited in his manifesto
was making money through a store hosted by a company called
Shopify;
the company didn't end its relationship with any of them.
</blockquote>

Ethical failures by programmers now hurt us all.  For example, your school might
use a piece of software called
Proctorio,
which records video and audio of you and your
screen while you write an exam, then uses algorithms to determine if you're
cheating.  Nobody outside the company can check those algorithms to see if
they're biased against people with nervous tics, and nobody who has ever been
the victim of online harassment or stalking should have to agree to invasive
surveillance in order to pass a course.

Many of these failures have their roots in a lack of compassion—i.e., in an
inability to imagine the world through others' eyes.  As [Mike Hoye][hoye-mike] has pointed out, some wayfinding apps for
phones have an option to avoid checkpoints; it's unlikely that the people who
added that feature ever lost a loved one to a drunk driver.
