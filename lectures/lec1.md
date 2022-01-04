---
layout: page
title: Lecture 1 - Base Rates and Reference Classes
nav_exclude: true
---

# Lecture 1: Base Rates and Reference Classes

Let's start by considering the following question:

> What is the probability that Joe Biden is President of the United States on Nov. 1st, 2024?

*[Note: This was written on Nov. 3rd, 2021.]*

To answer this question, one strategy I would use is to look at base rates: the rate of occurrence of similar events. For instance:

* What fraction of presidential terms are fully completed (last all 4 years)? The answer to this is 49 out of the 58 total terms, or around 84%.
* On the other hand, we know that Biden has already made it through 288 days of his term. If we remove the 5 presidents who left office before that, there are 49 out of 53 or around 92%.
* But alternately, Joe Biden is pretty old (78 to be exact). If we look up death rate per year in actuarial tables, it's around 5.1% per year, so this leaves him with a ~15% chance of death or a 85% chance of surviving his term.

     

These are all examples of using base rates.

Base rates can be powerful as they allow us to draw analogies with related cases even when we don't have directly relevant data or a trend line to extrapolate. In that sense they are like zeroth-order forecasting, but can work even when you don't have a clear time series or other trend to base a forecast on.

## Decomposing the Problem

We can take base rates one step further. If Biden doesn't complete his term, the main reasons I can think of are:

* Death by natural causes
* Death by assassination
* Impeachment / resignation
* The presidency no longer exists (due to a coup, invasion, etc.)

So, we could estimate all of these using base rates, then add them up.

The last two are easiest: only one president has left office due to resignation (Nixon), so 1 out of 58 on impeachment / resignation. I'd put the presidency no longer existing at <1%, so together these add up to maybe 2%.


*[At the time of writing, PredictIt gave Biden a 22% chance of resigning before the end of his term. I feel confused about this.]*

**Death by assassination**: 4 out of 58 presidents, or around 7%. But only one of these was more than 288 days into the term, which would instead give 1.7%. I would subjectively put the probability a bit between these, at 3.5%.

**Death by natural causes**: we previously gave this a 15% chance. But that's neglecting that life expectancy increases with income, and Biden is pretty rich. Eyeballing the mortality curves here, I'm going to guess that this decreases his probability of death to around 60% of its baseline value. So we end up with 9% instead of 15%.

Adding these together gives 2 + 3.5 + 9 = 14.5%. So an 85.5% chance of completing his term.

What did we gain from applying this decomposition? The main thing is that it allows us to incorporate age when predicting death from natural causes, which feels correct to me. On the other hand, it left us with a very small sample size for assassinations, and in general left us to make a lot of arbitrary choices that might let personal biases creep in. That being said, the number is in the same ballpark but a bit lower than the 92% answer from the simplest method, which feels right given Biden's age.

## Other Examples

There are many cases where base rates are a useful tool. For instance, maybe I want to understand the probability that I get Covid in the next month (perhaps as a function of what activities I do).

**Brainstorming exercise**. What base rates would you use for the above question? What factors are most important to take into account?

Here are some other questions where base rates provide valuable information:

* What job will I have after I graduate Berkeley?
* How much Series A funding will this startup get?
* Will someone break Usain Bolt's 100-meter dash 9.58s world record by the end of 2024?
* Will China send a daily record number of military planes into Taiwan's air defense identification zone next month? (from CSET Foretell)

**Brainstorming exercise**. What are other areas where base rates are helpful?

## Dangers of Base Rates

As I hinted above, the flexibility of base rate forecasting also carries risk. If we make too many arbitrary choices when defining a base rate, we can succumb to our own cognitive biases. For instance, consider the following article that gave Trump a 3% chance of winning the 2016 election. Its reasoning invokes base rates, defining a reference class of "Candidates that are good with the media and give them something to write about but, let's be real, could never be president". They said Trump was in this reference class and no such candidate had ever won, so their base rate was 0%. (They then adjusted it up to 3% based on Trump's strong polling performance.) If you find yourself doing something like this, watch out.

TODO: Image here

*Pro tip: Don't do this.*

The best ways to avoid failures like the Trump prediction are to look for the simplest reference classes you can find (only adjusting for obviously important and objective factors like age), or to average over lots of ways of constructing your reference class so that no single set of choices dominates the forecast.