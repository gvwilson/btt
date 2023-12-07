---
template: slides
---

## Pop Quiz

Which of these do you believe?

1.  As a student,
    you own the software you write for course assignments.
    If the university wants to use it,
    they need your permission.

1.  You own the software you write for course assignments
    *as long as you do the work on your own computer*.
    If you use a university's machines,
    they have an equal right to the software.

1.  If you are an undergrad paying fees,
    you own what you write,
    but if you are a grad student being paid a stipend,
    the university owns it.

---

## And the Answer Is…

-   It depends where you are
-   Different schools have different rules
    -   Even in the same legal jurisdiction
    -   And some universities' rules also depend on which faculty you're in
-   Rules in industry are usually less complex
    -   Anything you do on company time or with company resources belongs to the company
-   But there are many gray areas
-   I wrote some of this material on a company laptop while traveling for work
    -   Do I owe my employer a share of the royalties?
-   What if I developed a computer virus on that same computer at the same time?
    -   Would the company "own" that?

---

## One Right Among Many

-   Who owns what is just one of the rights that societies recognize
-   The [Universal Declaration of Human Rights][udhr] includes the rights to:
    -   say what you want
    -   live free from fear,
    -   be treated the same way as everyone else regardless of race,
        sex, orientation, religion, or disability
-   Most countries have signed this declaration,
    so in theory it has the force of law
-   But the words "in theory" are doing a lot of work in that sentence
-   And software is changing everything faster than legislation and practice can keep up with
-   First step toward ensuring your rights is to know what they are and where they come from

---

<!--# class="aside" -->

## It Wasn't Always Thus

-   Until early modern times, only kings and queens "owned" land [%b Linklater2013 %]
    -   Everyone else had the right to *use* the land in certain ways
    -   Or to forbid other people from using it
-   The modern idea of "copyright" is the result of centuries of conflict
    between European and British/American law [%b Baldwin2014 %]
    -   First established to *limit* printers' control over books [%b Bellos2024 %]
-   And our preoccupation with human rights might just be a case of "last good idea standing" [%b Moyn2010 %]
-   Which means that *none of what follows is natural or inevitable*
-   Property rights evolved over several centuries
    to address the economic and moral concerns
    of people powerful enough to influence law-making
-   Are constantly changing as power shifts and needs change
-   And programmers have caused a lot of the recent changes

---

## Intellectual Property

-   Covers four separate kinds of rights
-   What ties them together is that information is expensive to produce but cheap to copy
-   Each kind of IP gives its holder a limited monopoly over some kind of information
-   In theory,
    ensures that creators can earn enough from producing intangible goods to keep doing it
-   In practice,
    often used as [rent-seeking][rent_seeking] (discussed below)

---

## Copyright

-   Copyrights apply to any original expression that anyone creates
    -   Can't (yet) copyright facts,
    -   But can copyright *representation* of facts that contains an element of creativity
-   [%fixme "examples of copyright and its abuses" %]

---

## Patents

-   Apply to inventions, technological improvements, and business methods
-   Grant a monopoly for a fixed period of time (usually twenty years)
    -   I.e., no one can use the idea without the patent holder's permission
    -   Which they can charge for
-   Stronger than copyright, so requirements for obtaining a patent are more stringent
    -   Can take years, thousands of pages of paperwork, and many thousands of dollars
-   Intended to be a bargain between the inventor and the public
    -   Inventor discloses how the invention works so that other people can learn from it
    -   Society ensures that she is the only one who can profit from it for a reasonable time

---

## Trade Secret

-   If someone doesn't want anyone to know how her invention works
    she can treat it as a trade secret
-   Not a property right as such,
    but rather the practice of relying on things like non-disclosure agreements (NDAs)
    to keep something secret.
-   Less risk of someone being inspired by your idea to create something better
-   But if the idea *does* leak, the inventor has less legal protection

---

## Trademark

-   People have limited time to make decisions
-   So brands lower the cost of choice
    -   If company XYZ has a reputation for high quality or low prices,
        the name itself has commercial value
-   A trademark is the exclusive right to a brand
-   [%fixme "more about trademarks and their use" %]

---

## What Is Software?

-   Not immediately clear which category software falls into
    -   IBM had to be threatened with legal action to admit that
        its software had value separate from the value of its hardware
        [%b Grad2002 %]
-   Is it a document that can be copyrighted?
-   Is it an invention that can be patented?
-   Can algorithms be patented?
    -   If so, can mathematical proofs and the laws of science?

---

## Software Licenses

-   Dictates how software can be used and redistributed
-   Every creative work automatically has some sort of license
    -   The only questions are whether authors and users know what it is and choose to enforce it
-   Choosing a license can be complex [%b Lindberg2008 %]
-   To avoid messiness:
    1.  Every project should include an explicit license
    2.  This license should be chosen early (changing later can be complicated)
    3.  The license should be written by professionals,
        since implications of legal language are not obvious to non-experts [%b Almeida2017 %]

---

## Open Licenses

-   [Open Source Initiative][osi] maintains [a list][osi-license-list] of open licenses
-   [choosealicense.com][choose-license] can help you find the right one
-   MIT and BSD Licenses
    1.  People can do whatever they want to with the software…
    2.  …as long as they cite the original source…
    3.  and the authors accept no responsibility if things go wrong
-   GNU Public License (GPL) gives people similar rights
    but requires them to share their own work on the same terms
    -   I.e., if someone modifies GPL-licensed software or incorporates it into their own project
        and then distributes what they have created,
        they have to distribute the source code for their own work as well

---

<!--# class="aside" -->

## Behind the License Wars

-   GPL was created to prevent companies from taking advantage of open software
    without contributing anything back
-   The last 35 years have shown that this restriction isn't necessary
    -   Many projects have survived and thrived without this safeguard
    -   And GPL'd projects are no more or less sustainable than other projects
    -   But "GPL or Die!" is a **shibboleth** for some programmers
-   The Hippocratic License forbids use of software
    in ways that violate the [Universal Declaration of Human Rights][udhr]
    -   Some people who are in favor of the GPL's restrictions on use
        argue that the HL's restrictions mean it isn't a "real" open license
    -   Which says more about them than it does about the licenses

---

## Creative Commons Licenses

-   Most widely used set of open licenses for data and written work
    are those produced by [Creative Commons][creative-commons]
-   Most liberal option is CC0 (the "0" stands for "zero restrictions")
    -   Puts work in the public domain,
        i.e.,
        allows anyone who wants to use it to do so however they want with no restrictions.
    -   The best choice for data,
        since it simplifies aggregation of datasets from different sources

---

## Creative Commons License (cont.)

-   Creative Commons-Attribution license (CC-BY):
    do whatever you want but cite the original source
    -   Best license to use for papers and reports
-   Other licenses have some mix of further restrictions
-   NC (no commercial use) does *not* mean people can't charge money for their work
    -   Actually means "you need my permission to use this if you're making money from it"
-   ND (no derivative works) prevents people from creating modified versions
    -   Unfortunately also inhibits translation and reformatting
-   SA (share-alike) requires people to share anything that incorporates the work
    on the same terms as the original
    -   In practice makes aggregation and recombination difficult

---

<!--# class="aside" -->

## Why Be Open?

-   85% of all interesting innovations in all industries come from users rather than suppliers
    [%b Hippel2006 %]
-   The more open work is,
    the more people can tinker with it
    and do things the original creators would never have thought of

---

<!--# class="aside" -->

## Why *Aren't* We Open?

-   [Rent-seeking][rent_seeking]
    and other forms of [artificial scarcity][artificial_scarcity]
    can be very profitable
    -   Bad for society as a whole
    -   But good for individuals with the legal power to extract money
        without having to add value
-   The [Mickey Mouse Protection Act][mickey_mouse_act],
    which extended the duration of copyright in the US yet again,
    was the result of intensive lobbying by Disney
-   An example of [regulatory capture][regulatory_capture]
    -   Copyright extension is a high priority for a company that can spend a lot of money
    -   Fighting it is a lower priority for people who individually can't spend as much
    -   Regulations wind up being shaped primarily by the former at the expense of the latter
-   Return to this topic when we discuss privacy law…

---

<!--# class="exercise" -->

## Who Owns Your Work?

1.  Who owns the software your team produces in this course?
    How easy was it to find an answer?
2.  Suppose that a project has released three versions of a software package
    under the GPL,
    but now wants to switch to the MIT License.
    What steps must it take to do this?
    Whose permission is needed (i.e., who can say "no" and make it stick)?
3.  Microsoft (which owns GitHub) trains AI models using the source code in students' repositories.
    If you add a license to your repository saying that
    your software cannot be used directly or indirectly for commercial purposes
    without your express prior permission,
    can you then demand a share of Microsoft's revenue from its AI ventures?
