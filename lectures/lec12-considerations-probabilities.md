---
layout: page
title: Lecture 12 - Turning Considerations Into Probabilities
nav_exclude: true
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/MathJax.js?config=TeX-MML-AM_CHTML">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [["$", "$"], ["\\(", "\\)"]],
        processEscapes: true
    }
});
</script>

# Lecture 12: Turning Considerations Into Probabilities

The previous post started forecasting the UK hospital peak (based on information through Dec. 21, 2021). We generated several considerations and ultimately focused on the Omicron doubling time, the peak number of cases, the current number of Omicron cases, and the seasonality. In addition to a reference class forecast based on seasonality, we assumed the case peak would be roughly governed by hospital capacity and used the calculation:

DateOfPeak = Dec. 21
&nbsp;&nbsp;&nbsp;&nbsp;+ 10 days to reach case peak (2.4-day doubling time and 4.1 doublings) 
&nbsp;&nbsp;&nbsp;&nbsp;+ 9 days (case peak to hospital peak)
&nbsp;&nbsp;&nbsp;&nbsp;+ 3 days (lag of 7-day average)
&nbsp;&nbsp;&nbsp;&nbsp;= Jan. 12th

In this lecture we'll focus on going from this point estimate to a full probability distribution. This will involve two steps:
 1. Asking "what _invalidating considerations_ could cause this forecast to be totally wrong"?
 2. Asking "which numerical quantities is my forecast most _sensitive_ to, and how uncertain am I about them?"

The motivation for this is that most uncertainty is from either your entire estimate being structurally wrong (invalidating considertions), or from the specific numbers going into your estimate being inaccurate (numerical sensitivity). In many (most?) cases, the first form of uncertainty dominates, so it's good to check both.

We'll work through both steps, then combine them into a final uncertainty estimate. At the end I've also included a Q&A with Misha Yagudin on how this approach compares with his approach to forecasting.

## Part 1: Invalidating Considerations

I did the brainstorming exercise of "If the previous estimate is totally off, why is that?" I recommend that you try this exercise as well before reading what I came up with.

----------

(whitespace to avoid spoilers)

...

...

...

---------

Okay, here's what I came up with:
 1. If the UK cases are capped by herd immunity rather than hospital strain (17+ million cases instead of 6.7 million)
 2. If the doubling time is actually 1.5 days (vs. 2.4 days), as suggested in some articles
 3. If the peak happens due to people self-adjusting their behavior to make $R$ barely less than $1$, leading to a very long "peak".

Let's see how much each of these could affect the answer.

**Consideration 1: herd immunity.** This would add at most 2 more doublings, or ~5 days, to the date of the peak.

**Consideration 2: short doubling time.** Since we assumed around 4 doublings before, this would subtract only ~4 days from the date of the peak.

**Consideration 3: extended peak.** We calculated before that hospital capacity would correspond to around 6 million confirmed cases/week. Herd immunity was around 17 million cases, so this would mean 3 weeks to reach herd immunity. But I now realize that this is *confirmed* cases, and undertesting is around a factor of 2. So I think this would only really add 1.5 weeks, or ~9 days, unless people adjust their behavior to stay significantly below hospital capacity. I'll add another 3 days of wiggle room (12 days total) in case the extended peak is at 75% of hospital capacity rather than 100% of capacity, or in case I underestimated the herd immunity threshold.

If I consider how subjectively surprised I would feel in each of the 3 worlds above, and turn that into probabilities, I get: 15% (herd immunity), 15% (short doubling time), 10% (extended peak).

**Exercise.** Do you agree with the above probabilities?

**Brainstorming exercise.** What other considerations am I missing?

## Part 2: Numerical Sensitivity

Next I checked the numerical sensitivity of the mainline forecast. Our mainline forecast is based on several quantities:
 * The current number of UK Omicron cases, estimated at $N_0 = 200,000$
 * The total number of future Omicron cases, estimated at $N = 6,700,000$.
 * The Omicron doubling time, estimated at $t = 2.4$ days
 * The lag $\Delta_0$ between case peak and hospital peak, estimated at 9 days.
 * The lag $\Delta_1$ between single-day hospital peak and 7-day average hospital peak, estimated at 3 days.

Our formula for the number of days until the peak is then

$\log_2(N/2N_0) \cdot t + \Delta_0 + \Delta_1$

Let's assess the sensitivity of this formula to each consideration:
 * If $N$ or $N_0$ is off by a factor of $2$, then our answer changes by $2.4$ days.
 * If $t$ is $3.3$ instead of $2.4$, our answer changes by $3.7$ days.
 * If $\Delta_0$ or $\Delta_1$ is off by $1$, our answer changes by $1$ day.

To make this more quantitative I put it into table form, including my $70\\\%$ uncertainty intervals for each number:

| Parameter | Point estimate | Range | Effect on answer |
| --------- | -------------- | ----- | ---------------- |
| $N_0$     | $0.2 \times 10^6$ | $[0.15, 0.25] \times 10^6$ | $[-0.8, +1.0]$ |
| $N$       | $6.7 \times 10^6$ | $[5, 13] \times 10^6$ | $[-1.0, +2.3]$ |
| $t$ | $2.4$ | $[2.0, 3.3]$ | $[-1.6, +3.7]$ |
| $\Delta_0 + \Delta_1$ | $12$ | $[9, 14]$ | $[-3, +2]$ |

Considering that probably not all errors will occur in the same direction, when I combine these errors together I subjectively end up with a 70% confidence interval of $[-3.6, +4.9]$ relative to the Jan. 12th point estimate. _(I estimated these as e.g. $3.6 = \sqrt{0.8^2 + 1.0^2 + 1.6^2 + 9^2}$ based on the premise that variances add for independent quantities. I don't think this is a logically valid calculation but it gives a decent ballpark, and the final numbers also seemed reasonable to me.)_

_**Misha**: I generally got a sense that your ranges are a bit too narrow, e.g., for doubling time. Metaculus is super uncertain about R_0 (their 70% CI 5.2 to 11.9), and “average” doubling guesstimates should probably be pretty uncertain given conflicting info, the impact of the holidays, impact of public concern, and government action. [Followed by some additional comments on why $N_0$ and $N$ should have higher uncertainty.]_

I asked Misha if he also thought my final uncertainty estimates (given in the next section) were too small. He said:

_**Misha**: Nope, I think they are fine (because the additional 45% went to extreme outcomes)._

## Putting it Together

If we assume the mainline estimate is structurally correct and all errors are due to numerical sensitivity, then we end up with a 70% confidence interval of (rounded to whole numbers) Jan. 8th to Jan. 17th. That means there is a 15% chance of being earlier than Jan. 8th and of being later than Jan. 17th.

If we instead consider structural uncertainty, we get a 15% chance of +5 days (Jan. 17th), a 15% chance of -4 days (Jan. 8th), and a 10% chance of +12 days (Jan. 24th).

In reality, both forms of uncertainty are present. Overall, the uncertainty also skews a bit more towards later dates than earlier dates. If I subjectively combine this, I would put my overall forecast as follows:

 * Median of Jan. 13th
 * 10% chance of Jan. 24th or later
 * 25% chance of Jan. 18th or later
 * 25% chance of Jan. 7th or earlier

**Exercise.** Do you agree with this assessment?

## Concluding Q&A

Since this is the first lecture that presents a fully integrated forecasting method, I asked Misha how close it matches his approach to forecasting.

_**Jacob:**  How closely does the method discussed in this and the previous lecture map onto your own approach to forecasting? I.e.: generate and prioritize considerations, reduce uncertainty, construct a mainline estimate (or multiple mainline estimates), consider numerical sensitivity + structural uncertainty._

_**Misha:** Well, I do all of the things from time to time. I do not do this explicitly in a step-by-step way. It’s more of playing it by ear and attending to whatever feels most informative._

_The core step, which is missing from your writeups, is getting less confused about what’s going on and assembling a world model. I usually start pretty cluelessly; for example, I was forecasting cultured meat progress last month. I spend a lot of time trying to understand how the processes might work, how to reference class might look like, and what technological limitations are._

_Until I had some understanding (still limited), I wasn’t looking for considerations. But after building a world model, I developed ways to approach most questions (sometimes very structurally uncertain)._

_To me, the key insight in your writeup was to **look at beds/herd immunity and doubling**. Everything else seems more like technical details necessary for delivering a good forecast but not primarily to the process._

_**Jacob:** Would you still consider [this lecture] good pedagogy for students?_

_**Misha:** I think it is a textbook example, looks good to me. I think it’s put a bit too much weight on legible steps and a bit less on "actual creative work." To be clear, these legible technical steps are important and worth having in front of you._

My takeaway is that the approach above is useful and valuable, but that it is also important to build a good world-model (especially when confronting a new domain). We'll hopefully have more to say about that in upcoming lectures.

