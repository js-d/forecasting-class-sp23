---
layout: page
title: Lecture 8 - The Inner Game of Forecasting
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

# Lecture 8: The Inner Game of Forecasting
<i>Yan Zhang</i><br>
<br>

Forecasting is much more like a sport than a collection of knowledge. One benefit of sports and similar skills, like games, is that they provide ways to get feedback quickly and improve. In this class, we will focus on one main game, "predict X by time Y", and we will play this game many times. Therefore, there is potential for significant improvement on that skill over a semester. In contrast, most math classes have to cover a certain amount of material, so you only get a few hours of practice on a given topic. Thus, our ambitious (really!) goal is to teach forecasting in such a way that you get better at the game of forecasting instead of just providing knowledge and references **about** forecasting.


In this lecture, we will try to **provide some "good" mindsets to actually get better at forecasting** as an accompaniment to specific techniques in other lectures. There are two main points in this lecture.

1. Deliberate practice is key to actually improve at forecasting, and by practicing efficiently, you can improve much faster than with poor practice.

2. When practicing, your feelings and intuitions are very important.


## Good Practice

The first thing that can improve any practice is feedback. Whenever we practice any skill, by default people tend to just put in the hours and hope they get better at it. However, we can learn more efficiently by adjusting based on results - since forecasting is often grounded in reality! For starters, if you just do more of what got "good" results and less of what got "bad" results, you will learn faster (a caveat is that: what's "good" and what's "bad" is context-dependent and might be hard to tell; for example, if the "right" answer was in your 80% confidence interval, than that's "good" unless it happens 99% of the time). Of course, this would require you to look at your results after the fact with a critical lens and not just blame everything on bad luck - that's a sure way of spending many hours without ever improving.

Now, to up this a level, instead of getting feedback only from results, you may also want to look at **your reasoning**. This is especially important in games with a high amount of randomness (such as poker, but also forecasting!), where often you'll get "good" results from doing "bad" actions and vice-versa. 

As an example, suppose you guessed that presidential candidate Triden will win the next election with high probability because Triden will "definitely" win all of Michigan, Virginia, and Georgia, but Triden actually loses all 3 and wins anyway thanks to swinging California. In this case, you got a good result from faulty reasoning (of course, one can also argue that this really actually *was* an outlier that you had no ability to predict, but it is easy to make self-serving excuses). This would be a good time to consider your reasoning "bad" and see what you can do to improve it.

Getting feedback on reasoning is harder than getting feedback on results, mostly because you are the same brain that made the faulty reasoning the first time around! Two specific ways to improve this are:

1. Get *external* feedback such as talking your reasoning through with friends or looking at other people's points of view: were there key considerations you missed in your model? Were there considerations you included but overrated/underrated?

2. Build up a general decomposition of forecasting into sub-skills (such as calibration, estimation, etc.) and *look at how they did individually* to get feedback on them. For example:
* You may have decomposed the original forecasting question into intermediate forecasting or estimation problems (for example, recall the question about whether Biden would be in office in November 2024). Do you think your decomposition was misleading, or do you think it was basically right, but that your intermediate probabilities and estimates were mistaken?
* Were your point estimates good but your intervals too narrow?
* Were your base rates good? Did you rely on them too much or too little?
* If your forecasts were informed by your personal experience, did you rely on that too much or too little?

As a final point, I really do want to reiterate that it is very easy to become overconfident in your skills due to randomly getting good results; this is a big part of what makes learning poker difficult in a way not applicable to many other games. For starters, I predict that at least 4 out of the top 5 students on the leaderboard right now will no longer be in the top 10 by the last day of the class, so don't get too complacent! (do try to make me eat my words)


## Thinking about Feelings

Now, we get to the second point: "feelings are important". What do we mean by that? *The Inner Game of Tennis* by Timothy Gallway is a book that's ostensibly about tennis instruction but applies to many other skills, including forecasting. In it, the author spends a lot of time on **introspection**, **visualization**, and **feelings**.

For example, if you're learning tennis, a coach might tell you to hit a forehand by snapping your wrists in a certain way, via a set of verbal instructions. If you just memorize these verbal instructions and try to explicitly follow them, your forehand probably won't improve much.

First, explicitly remembering the verbal instruction right before you hit the ball doesn't straightforwardly lead to making the right move. Indeed, it's hard to consciously decide which muscles you should move, and how and when you should move them, especially in such a short period of time. Second, focusing on the verbal instruction may interfere with other important aspects of your stroke.

Instead, the goal of the verbal instruction is for you to hit the next few forehands while paying attention to how your wrists can snap in different ways, to progressively build an internal sense of how it feels to move your wrists in the right way. The learning doesn't happen when the coach utters the verbal instructions: it happens as you practice and acquire this intuition for what it feels like to hit a good forehand.

Similarly, in this class, we will give you some verbal and written instructions about specific techniques, with names like Base Rates or Zeroth-Order Forecasting. However, if you just treat them as mathematical recipes to follow, you might find them hard to apply directly in practice (and when you do, you may miss bigger elephants in the room in the context of a specific forecast). What's important is to actually get practice doing forecasting, discussing and/ reviewing forecasts, and to get a good **feel** for what seem to be the important and unimportant parts of a question.

Consider the idea/technique of **zeroth-order / first-order approximations**. The reason we introduce this technique is not to reduce forecasting to fitting a line and forgetting about the original question, as one might in an introductory statistical exercise about linear regression. Instead, the point is that zeroth or first-order approximations are (usually) a good idea to try, after which they become one among many possible "voices" in your final forecast. After you do this a lot, you may learn when first-order approximations are important and when they are not. 

As an elementary but useful example, suppose you want to predict whether your favorite football team will win its next game. A first-order approximation of the team's performance based on its performance in the last four games this season could definitely be useful, but you may learn that checking the injury list for the status of the team's best players is a "voice" that is often more important than your statistical extrapolation.


So just to practice what we are talking about for a bit, let's consider the following question:

**What is the price of a 20-year lease of this billboard on the I-80 in downtown SF?**

![billboard](https://lh5.googleusercontent.com/HtEvBUFCy-nfU2k7rBx7vUGVxsiZUwRH-wPEaL3mi_DZUYcYUtArKe3GwtwEcyQWsoI4FN8D-EzTqPx_Gl1B1EvGA3NI5q5_Wnt-B_CUrvBLbiquO0XddPyUpg32EoAqqciKHQp7)


Okay, now that you have had a bit of time to think, can I have some volunteers to explain their reasoning? **(5 minutes)**

Thanks for the feedback! So the answer to the question is [$11,500,000](https://images1.showcase.com/d2/RC0rHFOL8OXt_nvIRh6J8pQLtJRDIoz9WkjhP0W8C-A/document.pdf). Now, instead of worrying about whether you got it "right" or not, what I want you to pay attention to, in the spirit of the lecture, are the factors **you** used and the factors that other people, whether me or your classmates, have come up with. Now I want you to contemplate those factors and get a good **feel** for which ones seem more important, which ones seem less important, which ones you want to pay more attention to later since you had never thought of them, etc. This is the valuable thing to take away from this exercise.

You'll see these ideas explicitly baked into many of our exercises for the rest of this class - and even if not explicit, we think you'll benefit from applying them instead of just thinking of this class as "learning concepts". So to get the most from these classes, we think you should:
1. Practice the explicit "trick" a few times to gain familiarity, such as through the homework.
2. When you do forecasts, try to apply the new tricks (and the old ones!) that apply, creating many "moving pieces" that must then be filtered/synthesized to create an explicit forecast.
3. Look at if and when these different moving pieces make your predictions better, and build an intuition for when to use each thing more or less.
4. Take more initiative socially; talking to other people about forecasting is very valuable; even two forecasters of similar abilities can have very different ideas, strengths, and weaknesses.

Perhaps most counterintuitively, since this is a statistics class, **pay attention to your feelings and intuition when practicing forecasting**. This allows you to build a "library" of what it feels like when you are making a good forecast vs. bad forecast, when you're under vs. overconfident, etc. Your internal neural net is much more powerful than you think, but you need to give it a lot of data and tell it to pay attention to specific parts of the data.


## Summary

I have quite a bit of personal data on two types of people that other people generically call "mathematicians". The first type is the "mathematical theory builders" (e.g. professors and industry researchers who develop theories) who almost always have a Ph.D. and are good at having very deep knowledge of particular field(s) of mathematics. The other type I call "mathematical problem solvers" (e.g. some professors and researchers, but also engineers and consultants) who are very good at solving a broad range of problems with elementary methods, especially in contests, puzzles, and organic industry problems.

While these people do a lot of similar things (read papers, solve problems, create mathematical ideas), at least for me, I feel their proficiencies can be very different. "Theory builders" seem very good at absorbing specialized fields of knowledge; they are good at making connections between different theories and theorems and summarizing very abstract and complex packages of thought. Their knowledge is often broad but is first and foremost deep. "Problem solvers", on the other hand, are very good at generating many hypotheses, killing off unpromising ideas, and reframing problems in different languages. Their knowledge is often deep but is first and foremost broad.

For me, forecasting feels like a skill much closer to problem solvers than theory builders. Indeed, when I meet strong forecasters, I have been struck by their similarity to problem solvers; strong forecasters generate many models and hypotheses, are quick to kill off unpromising ideas, and often rely on broad instead of deep knowledge. Therefore, I think the "inner game" mentioned in this post makes for a very good fit for a forecasting class. Good luck, and I hope we (hey, this applies to myself and the other staff, as well!) **actually get better at forecasting instead of learning about forecasting**! 


(Thanks to Jacob Steinhardt for providing a lot of initial structure and ideas, Alex Lawson / Misha Yagudin for valuable conversation from the perspective of skilled forecasters, and Jean-Stanislas Denain for helping with writing / editing. Many of the points here come from *The Inner Game of Tennis*.)
