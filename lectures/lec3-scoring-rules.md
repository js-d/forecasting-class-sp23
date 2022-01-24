---
layout: page
title: Lecture 3 - Scoring Rules
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

# Lecture 3: Scoring Rules
<i>Yan Zhang and Frances Ding</i><br>
<br>
 
We want to get better at predicting things, so the following question is very fundamental: 
 
> How do we reward people for giving us better predictions?
 
Let’s start by thinking about how we might make a rule for this when there are $2$ outcomes. For a natural first draft, we can just have you bet 1 unit of score at even odds. This means if you bet correctly on the desired outcome you will gain 1 point, and if you were wrong you will lose 1 point. For example, you can guess "the temperature tomorrow morning at 6AM will not be between 60 and 70 degrees." If the temperature at 6AM ends up being 56 degrees, you will get 1 point.

Over time, it's clear that people who do well at this will in general score more in the long run. However, there's a way in which this rule fails to let people show their skills. For example, suppose for every single event with an actual probability of 60%, you are perfectly calibrated and know this, but Jean always thinks the probability is 100%. Under our naive draft, you two will always bet the same way, “yes”, in these events, but the relative skill between you will never be discovered. This gives rise to our first main idea - we need to show the distribution of a prediction, not just a single number.

So... draft 2! You bet on something like "it will snow tomorrow" by giving a probability $\(p\)$. Then, you get $\(p\)$ points. (so if you bet “90%”, then you get 0.9 points if it snows and 0.1 otherwise). This is better than the first draft since you are offering more information about your beliefs, but it has a very interesting flaw. So take a couple of minutes to think about this: 

The answer is that if you think there's a 60% chance that it will snow, your optimal strategy is to actually bet 100%! This means while our draft 2 lets people show their skills, it also incentivizes them to hide their skills by betting something that doesn't represent what they actually think. While this is interesting from a game and psychology perspective, in the context where we are trying to see how to predict things better and/or get some information from what people are actually betting, we want to extract people's true beliefs about things. To mathematically formalize the things we wanted up to this point:

1. Assume we have a finite number of outcomes $\(1, \ldots n\)$ in our sample space.
2. Our predictions should be distributions. That is, an assignment of $\(q_i\)$ to each $\(i\)$ so that they add up to 1. Let's call such a prediction $\(q\)$.
3. We want a **scoring rule**; that is, a way to assign points on what actually happened. We can call this rule $\(f(q, i)\)$.
4. We want a **strictly proper scoring rule**; that is, if you think the reality of the world is $\((q_1, ... q_n)\)$, then your prediction $\(q\)$ should actually be equal to $\((q_1, ... q_n)\)$ to maximize your expected score.

## Strictly proper scoring rules

So what’s a good example of a strictly proper scoring rule? If you are only going to remember one, that would be [Good’s](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1952.tb00104.x) logarithmic scoring rule. This is defined by \$(f(q, i) = \log(q_i)\)$, where we are using the natural log.

* As an example, suppose you bet that tomorrow it will rain with probability 20%, snow with probability 30%, and neither rain nor snow with probability 50%, then when it snows you will be “rewarded” $\(\log(0.3)\)$, which is roughly -1.2 points.
* It might be weird to think of negative points as a reward, but you should see that you are getting something “less negative” than someone who assigned probability 10% to snowing, which would give them -2.3 points.
* In machine learning, the logarithmic scoring rule appears often under the guise of **log loss**.

There are (infinitely!) many other strictly proper scoring rules, and a good second one to know is Brier’s **quadratic scoring rule**. This rule assigns $\[f(q, i) = -\sum_{j=1}^n (q_j - o_{ij})^2,\]$ where $\(o_{ij} = 1\)$ if $\(i=j\)$ and $\(0\)$ otherwise. A few interesting things about this rule:

* It helps to do some algebra and simplify it. If you open the parentheses, you get $\(2q_i - 1 - \sum_{j=1}^n q_j^2\)$. One interpretation of this is that it fixes our naive (remember draft 2?) scoring rule of $\(q_i\)$ to have a “quadratic punishment” that disincentivizes to pushing the prediction all the way to 1 or 0.
* You can think of this as the negative of the mean-squared error, which comes up often in statistics as a way of measuring “badness.” Note that the mean-squared error metric is also called the **Brier score**, which can be easily confused with Brier's quadratic scoring rule. They are just negatives of each other, so you want a *low* Brier score (since it measures error) but a *high* scoring rule outcome.

There are pros and cons for both rules. For example, the logarithmic rule is more sensitive at small probabilities than the quadratic rule, which could be either good or bad depending on what you want to reward the forecaster for. Besides these concerns, it is always good to keep in mind that being strictly proper is not the be-all and end-all; there might be plenty of reasons to pick scoring rules that are “almost proper” but achieve other goals, such as being more intuitive for forecasters, having positivity and negativity be meaningful (for example, as stated all log scores are negative!), etc. See [Greenberg’s paper](https://arxiv.org/pdf/1808.07501.pdf) for some ideas in this direction.

## Prediction Markets and Platforms

Remember that our original goal was to reward people for making better predictions. A natural way to do this is to set up structures such as games and/or contests that reflect better predictive abilities. There are two major categories of such structures.
 
The first such category is called **prediction markets**. While this word is itself ambiguous, it typically means (such as in [Wikipedia](https://en.wikipedia.org/wiki/Prediction_market)) classical financial markets where you buy or sell abstract objects that reflect your belief in an event that will resolve in the future.
- For example, on Predictit, one of the more popular prediction markets, you buy and sell “shares” of an event taking place. The price of the share will always be between 1 and 99 cents, which corresponds to what the market thinks the probability percentage of an event taking place is. For an outcome such as “it will snow tomorrow by 12PM PT”, you can buy “yes” shares when the price is too low (which drives up the price) or buy “no” shares when the price is too high (which drives down the price). When the market closes (the event resolves) successfully, if the event happened, then “yes” shares are now worth $1 and “No” shares become worthless, and the opposite happens if the event did not happen. 
- Sports betting is a pretty big industry (e.g. Betfair) working under similar structures. People frequently say things such as “the market thinks X” by interpreting the market state as a kind of prediction. For academics, another quite exciting prediction market of this type is the Iowa Electronic Markets, which has been a source of interesting [research](https://iemweb.biz.uiowa.edu/research/) about the power of prediction markets.

<p style="text-align:center;">
<img src="https://bounded-regret.ghost.io/content/images/2022/01/predictit.png" width="50%">
</p>
<br><i>An example Predictit market from Jan. 14, 2022 showing the latest prices for "yes" and "no" shares</i>
</p>

 
The second such category is something we call **prediction platforms**, where instead of trading, you enter predictions like how you would submit a structured answer to some sort of online exam, and then you get points based on a… (usually trying to be strictly proper) scoring rule!
- For example, on [Metaculus](https://www.metaculus.com/questions/), one of the more popular prediction platforms, you put in a probability of how likely you think an event will happen. You can also revise your estimates as time progresses, until the point when the question “closes” (usually after the event happens or after a certain amount of time has passed). Afterwards, your guesses are scored with a fairly complicated proper [scoring rule](https://www.metaculus.com/help/faq/#scoring) that, at heart, is the logarithmic scoring rule, with some adjustments on top for rewarding you when you are “more right” than the rest of the community. There are also different scoring rules that are used for other types of questions, such as predicting a number versus a probability, or prediction tournaments.
- Confusingly, sometimes “prediction markets” also refer to prediction platforms which use scoring rules as a basis, such as [Robin Hanson](https://mason.gmu.edu/~rhanson/mktscore.pdf)’s “markets” made from scoring rules (in particular, this paper shows that the logarithmic scoring rule was the only rule to satisfy some nice properties such a market would want to enjoy).  

While the second type, prediction platforms, may end up being more directly relevant to our class, prediction markets are a good way to get priors and learn about what people think about some particular subject. We hope your predictive skills will be sharpened by interactions with both predictive markets and platforms!

(Thanks to Frances Ding, Alex Wei and Eric Neyman for help preparing this post. I also learned from and recommend Tim Roughgarden’s computer science-oriented [lecture notes](https://timroughgarden.org/f16/l/l17.pdf))

---

## Mathematical Tangent
Here's a really nice way (h/t Eric Neyman) to see how the log and quadratic rules naturally appear, if we aren’t afraid to do a bit of calculus. Let’s consider our goal of finding a proper scoring function in a simplified case with just 2 outcomes (so $\(p_1 = p, p_2 = (1-p)\)$), which is to find a scoring function $f$ such that $\(p f(x) + (1-p) f(1-x)\)$ is maximized at $\(x=p\)$. Taking the derivative with respect to $x$ and setting equal to 0, we get $\(pf’(p) - (1-p)f’(1-p) = 0\)$, or $\(pf’(p) = (1-p)f’(1-p)\)$.

Now, let’s turn the question around and ask our “wishful thinking” selves: what $f’()$ would make this work?
1. A natural choice is $f’(p) = (1-p)$, because then the left and right hand sides are both $p(1-p)$.
2. Another natural choice is $f’(p) = 1/p$, because then the left and right hand sides are both 1.

I leave the rest to you to see that these two options exactly correspond to the quadratic and log rules, respectively!
