---
layout: page
title: About
description: >-
    Course policies and information.
---

# About
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## About

Forecasting has been used to predict elections, climate change, and the spread of COVID-19. Poor forecasts led to the 2008 financial crisis. In our daily lives, good forecasting ability can help us plan our work, be on time to events, and make informed career decisions. This practically-oriented class will provide you with tools to make good forecasts, including Fermi estimates, calibration training, base rates, scope sensitivity, and power laws. We'll discuss several historical instances of successful and unsuccessful forecasts, and practice making forecasts about our own lives, about current events, and about scientific progress.

**Prerequisites**: Stat134 or a similar probability course (i.e. EECS126, STAT140, IEOR172).

<!-- [Course Syllabus](./assets/syllabus.pdf) | [Piazza Forum](https://piazza.com/berkeley/spring2022/stat157260) -->
This is the website for the Spring 2023 iteration of the class. The website for the Spring 2022 version is [here](http://www.stat157.com/).

## Lecture

MWF11-12, in Physics Building 251 

This class will be heavily disussion-based and participation will count towards the grade. Monday and Wednesday lectures 
will be a combination of traditional lecture and group activities, while most Fridays will be student-led small 
group discussions with instructors helping to facilitate.

Instead of exams, there will be a final project. Students in Stat260 will be expected to do a more substantial project.

There will be no official lab / discussion block, but some homework will involve programming. 

## Office Hours

Our office hour schedule this semester will be:
 * Jacob Steinhardt (Lead Instructor): 325 Evans, Monday 10-11am 
 * Jean-Stanislas Denain (GSI): 428 Evans, Friday 2:30-3:30pm (starting 1/27)
 * Meena Jagadeesan (GSI): 428 Evans, Tuesday 10-11am 
 * Yongchan Wang (uGSI): 428 Evans, Wednesday 2-3pm  


## Grading

There will be a quiz at the beginning of class on most Fridays, which covers the reading from that week. It will generally be short (1-2 multiple-choice questions). The two quizzes where you got the lowest grade will be dropped.


Grades will be based on a combination of:
* Homework (35%)
* Discussion participation (15%)
* Forecasting performance (20%)
* Quizzes (10%)
* Final project (20%)

## Course Staff

To reach course staff, you can email [forecasting-class-staff@lists.berkeley.edu](mailto:forecasting-class-staff@lists.berkeley.edu). If possible, please avoid emailing professors or GSIs directly!

{% assign lead = site.staffers | where: 'role', 'Lead Instructor' %}
{% for staffer in lead %}
{{ staffer }}
{% endfor %}

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'GSI' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}


{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign u_teaching_assistants = site.staffers | where: 'role', 'uGSI' %}
{% assign num_u_teaching_assistants = u_teaching_assistants | size %}
{% if num_u_teaching_assistants != 0 %}


{% for staffer in u_teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}
