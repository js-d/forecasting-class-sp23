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

[Course Syllabus](./assets/syllabus.pdf) | [Piazza Forum](https://piazza.com/berkeley/spring2022/stat157260)

## Lecture

MWF11-12, in 3108 Etcheverry Hall
 * <a href="https://berkeley.zoom.us/j/93592932586?pwd=Y1hBNEp4OGVqWHMvOXZKcmd1L0d6QT09">Zoom link</a> for first 2 weeks of class

This class will be heavily disussion-based and participation will count towards the grade. Monday and Wednesday lectures 
will be a combination of traditional lecture and group activities, while most Fridays will be student-led small 
group discussions with instructors helping to facilitate.

Instead of exams, there will be a final project. Students in Stat260 will be expected to do a more substantial project.

There will be no official lab / discussion block, but some homework will involve programming. 

## Office Hours

Our office hour schedule this semester will be:
 * Jacob Steinhardt (Lead Instructor): Evans 325, 11am-12pm on Tuesdays
 * Jean-Stanislas Denain (GSI): Evans 428, 2-3pm on Mondays
 * Frances Ding (GSI): Evans 428, 10-11am on Fridays
 * Collin Burns (GSI): Evans 428, 10-11am on Wednesdays

We will be holding some of these office hours on zoom for at least the first two week of classes. We will announce these and any other changes to the office hour schedule on piazza.

## Grading

Grades will be based on a combination of:
 * Discussion Participation (15%)
 * Forecasting Performance (20%)
 * Homework (35%)
 * Final project (30%)

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
