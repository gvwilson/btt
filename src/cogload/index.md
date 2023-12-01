[%f cogload-architecture %] shows a very (very) simple model of
the cognitive architecture of the human brain.
On the left is long-term memory (LTM),
which is where you store things like the spelling of your name
and how that awful clown scared you when you were ten years old.
It is very large—you can keep adding to it as long as you live—but
you don't have direct conscious access to it.

[% figure
   slug="cogload-architecture"
   img="cognitive-architecture.svg"
   caption="The cognitive architecture of the human mind (simplified)."
   alt="Cognitive architecture"
%]

Instead,
evolution has given you a second subsystem called short-term memory (STM) or working memory.
(More sophisticated models distinguish between these two concepts,
but this simple model is good enough for our needs.)
You are constantly fetching things from LTM into STM to use them,
then re-encoding them and writing them back to LTM.
This is one of the differences between your brain and a computer:
reading data from a hard drive doesn't alter it,
but every time you access something in LTM,
you may write it back in a different or augmented form.
We call this "learning".

Here's the problem:
STM is very small.
[%b Miller1956 %] estimated that it could hold 7±2 things at one time;
more modern estimates put the number closer to 4±1 [%b Didau2016 %].
This means that STM is a bottleneck for learning:
if too many new ideas are presented too quickly,
the new arrivals will knock older ones out of STM
before you have a chance to encode them and store them in LTM,
so learning won't take place.

This realization and others have produced the theory of cognitive load,
which (among other things) divides the things you have to do while learning
into three categories.
The intrinsic load is the thinking that is required by the learning task itself.
The germane (or relevant) load is the other thinking that the problem requires,
but which isn't the focus of the lesson,
while the extraneous load is everything you're being asked to do that is irrelevant.

For example,
suppose you are learning the grammar of Frisian.
If I ask you to translate,
"How is her knee today?"
then the intrinsic load is the rules of grammar,
but there is also the germane load of recalling vocabulary
(which is necessary, but isn't the main focus of the lesson).
If,
on the other hand,
I give you the words as shown in [%f cogload-frisian %]
and ask you to rearrange them,
I have eliminated the germane load,
but have added some extraneous load by using a mix of fonts.
You will solve the problem more quickly and more accurately
if the words are all in the same font,
no matter what that font is,
than if your brain is wondering whether the difference is significant.

[% figure
   slug="cogload-frisian"
   img="cogload-frisian.svg"
   caption="Reducing germane load while increasing extraneous load."
   alt="Translating a sentence"
%]

Cognitive load theory explains why tools like [Scratch][scratch] work so well:
they reduce germane load by getting rid of the commas, curly braces, and other distractions
so that learners can focus on mastering concepts like assignment and loops.
It also explains why working with code written in a mix of styles is so painful:
each minor difference adds extraneous load.

In order to handle larger sets of information,
our minds create chunks that only take up one slot in STM.
For example,
most of us remember words as single items rather than as sequences of letters.
Similarly,
the pattern made by five spots on cards or dice is remembered as a whole
rather than as five separate pieces of information.

Experts have more and larger chunks than non-experts,
i.e.,
experts "see" larger patterns and have more patterns to match things against.
This allows them to reason at a higher level
and to search for information more quickly and more accurately.
However,
chunking can also mislead us if we mis-identify things:
newcomers really can sometimes see things that experts have looked at and missed.

Given how important chunking is to thinking,
it is tempting to try to teach design patterns directly to learners as early as possible.
These patterns help competent practitioners think and talk to each other in many domains,
but pattern catalogs are too dry and too abstract for novices to make sense of on their own.
However, giving names to a small number of patterns does seem to help,
primarily by giving the learners a richer vocabulary to think and communicate with [%b Sajaniemi2006 %].

[% fixme
   "connect back to code comprehension"
   "connect back to teamwork and org charts"
%]
