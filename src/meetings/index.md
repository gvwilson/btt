The most important part of teamwork is running meetings efficiently,
and the key to doing that is to distinguish between:

-   Status meetings for keeping everyone up to date on what everyone else is doing
    and for making simple decisions when the options are well understood.

-   Discussion meetings for weighing alternatives and making complex decisions.

-   Co-working sessions like brainstorming sessions and programming sprints
    that are devoted to the content of the project rather than its operation.

## Status Meetings {: #meetings-status}

Every team should have a short weekly status meeting.
For each meeting,
create a table in a shared document like the one in [%t meetings-log %].
Everyone adds a few bullet points to their row in the table
at least half an hour before the meeting starts
so that the whole team can mull everything over.
If anyone wants to discuss something,
they highlight it by adding a comment.
The meeting moderator then goes through the highlighted items one by one,
spending no more than a couple of minutes on each;
anything that requires more time is deferred to a discussion meeting.

[% table
   slug="meetings-log"
   tbl="meetings-log.tbl"
   caption="An example of team status updates."
%]

## Decision Meetings {: #meetings-decision}

Decision meetings are for issues that will have more long-term impact on the project
or that team members disagree about.
Since the stakes are higher,
they need more structure:

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information,
    send a brief email instead:
    most people can read faster than they can speak.

Write an agenda.
:   If nobody cares enough about the meeting to prepare
    a point-form list of what's to be discussed,
    the meeting probably doesn't need to happen.
    (Note that "the agenda is all the open issues in our GitHub repo" doesn't count.)

Include timings in the agenda.
:   Doing this helps prevent early items stealing time from later ones.
    The first estimates with any new group are inevitably optimistic,
    so expect to revise them upward for subsequent meetings.
    But don't have second or third
    meeting just because the first one ran over time: instead, try to figure out
    *why* it ran over and fix the underlying problem.

Select a moderator.
:   Put one person in charge of keeping items on time,
    selecting the next person to speak,
    chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.
    The moderator should *not* do all the talking:
    in fact,
    the moderator will talk less in a well-run meeting than most other participants.

Prioritize.
:   Tackle the most important issues first, even if they're the longest,
    because the little ones always take more time than you expect.

Require politeness.
:   No one gets to be rude,
    no one gets to ramble,
    and if someone goes off topic,
    it's the moderator's job to say, "Let's discuss that elsewhere."

No interruptions.
:   This rule is a special case of the one above,
    since treating other people with respect is the sincerest form of politeness.
    Participants should raise a hand (physically or electronically)
    when they want to speak.
    The moderator should keep track of the queue
    and give each person time in turn.

No distractions.
:   Side conversations make meetings less efficient
    because nobody can actually pay attention to two things at once.
    More importantly,
    if someone is checking their email or texting a friend during a meeting,
    it's a clear signal that they don't think the speaker or their work is important.
    This doesn't mean a complete ban on technology—people may need accessibility aids
    or be waiting for a call about childcare—but by default
    phones should be face down and laptops should be closed
    during in-person meetings.

Take minutes.
:   As discussed below,
    someone other than the moderator should take point-form notes
    about the most important information that was shared
    and about every decision that was made or every task that was assigned to someone.

End early.
:   If the meeting is scheduled for 10:00 to 11:00,
    aim to end at 10:50 to give people a break before whatever they're doing next.

As soon as the meeting is over,
add the minutes to the project's wiki,
version control repository,
or shared cloud drive.
Please don't email minutes to everyone:
our inboxes are full enough,
and the more places new team members need to search in order to find things,
the more likely they are to miss something important.

Sharing the minutes ensures that:

People who weren't at the meeting can follow what's going on.
:   We all have to juggle tasks from several projects or courses,
    which means that sometimes we can't make it to meetings.
    Checking a shared record is more accurate and more efficient than asking a colleague,
    "What did I miss?"

Everyone can check what was actually said or promised.
:   Accidentally or not, people often remember things differently;
    writing them down gives everyone a chance to correct mistakes
    and misinterpretations.

People can be held accountable.
:   Whoever has to draw up the agenda for the next meeting
    can start with the action items from the previous one.

If you would like to become better at sharing information and making decisions,
there is no better place to start than [%b Brookfield2016 %],
which catalogs fifty different techniques for managing discussions
and explains when and how each is useful.

## Air Time {: #meetings-airtime}

One problem with meetings is that
some people may talk far more than others.
Other people may be so accustomed to this
that they don't speak up even when they have valuable points to make.

You can combat this
by giving everyone three sticky notes
(or coins, or paperclips—anything inedible will do) at the start of the meeting.
Every time someone speaks,
they have to give up one sticky note.
When they're out of stickies,
they aren't allowed to speak until everyone has used at least one,
at which point everyone gets all of their sticky notes back.
This ensures that nobody talks more than three times as often as
the quietest person in the room,
which completely changes group dynamics.
People who have given up trying to be heard suddenly have space to contribute,
and the overly-frequent speakers realize how talkative they have been.

Another useful technique is called interruption bingo.
Draw a grid and label the rows and columns with the participants' names;
each time person A interrupts person B,
add a tally mark to the appropriate cell.
Look at the results Halfway through the meeting:
in most cases it will be clear that one or two people are doing all of the interrupting,
and that they're always interrupting the same people.
After that,
saying, "All right, I'm adding another tally to the bingo card,"
is usually enough to get them to throttle back.
If it isn't,
well,
you just learned something about your teammate…

Online meetings provide special challenges for regulating how often individuals speak.
[%b Troy2018 %] discusses why online meetings are often frustrating,
and points out that in most online meetings,
the first person to speak during a pause gets the floor.
As a result,
"If you have something you want to say,
you have to stop listening to the person currently speaking
and instead focus on when they're gonna pause or finish
so you can leap into that nanosecond of silence
and be the first to utter something.
The format…encourages participants who want to contribute to say more and listen less."

The solution is to run a text chat beside the video conference
where people can signal that they want to speak;
the moderator can then select people from the waiting list.
Text chat is better than the "raise hand" feature most video conferencing tools offer
because the person who wants to speak can indicate why.
For example,
they can type "question about budget"
rather than just "question"
so that the moderator can group related questions together.

## Blowfish and Clams {: #meetings-disruptive}

[NOAA's guide][noaa_disruptive] to dealing with disruptive behaviors
has useful labels and even more useful advice
for handling people who may send meetings off course.
For example:

<blockquote markdown="1">

*Description*:

Blowfish is a very chatty, assertive "people person".
Blowfish wants everyone to feel comfortable and positive about the process.

They have a tendency to be overly talkative (almost compulsively)
because they are enthusiastic,
want to show off,
or are well-informed and eager to use their knowledge.

Blowfish can dominate the floor time at the expense of other group members.
While they frequently have good ideas and strong contributions to make,
they also ramble,
monopolize the discussion,
and do not give others an opportunity to express their thoughts.

*Gentle Intervention*

Listen actively:
"I'd like to capture all your points on the easel chart
and then get the other participants' feedback as well.
Help me make sure I capture your thoughts correctly.
Your first point is [pause for response]?"

Label sidetracks and interrupt tactfully
by clearly saying his or her name:
"Blowfish? Blowfish? Blowfish?
Is this comment related to what we are discussing
or should it go into the parking lot?"

**Firm Intervention**

Describe the impact:
"Let's use a round-robin technique
to allow everyone an opportunity to contribute,"
or,
"We are collecting information from everyone right now—it
is essential to hear other opinions and information"

Redirect the behavior:
"Thank you Blowfish—now let's hear from someone else,"
or,
"Hold that thought for now,
and let's let Clam finish his thought,"
or,
"Let's ask some others what they think."

</blockquote>
