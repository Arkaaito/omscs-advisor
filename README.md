# omscs-advisor
A webapp which suggests course schedules for students in the OMSCS program.

## Motivation

Every term, many students (particularly new students) ask the same question:

WHAT COURSE SHOULD I TAKE?!

Usually they ask this on the OMSCS Google+ group, where they get the same small set of answers:

* Look at the unofficial course review spreadsheet.
* Take an easy course, like Computer Networks.
* Take a hard course, like Machine Learning.
* Take Algorithms, it's required for every specialization.
* Take KBAI, it has good reviews.
* No one can answer that.  You must choose your own fate.

In traditional programs one might have an academic advisor who suggests courses on the basis of your background, your desired specialization, and what he or she has heard about the difficulty/workload and compatibility of various courses.  Given the scale of the program and the several zillion daily e-mails that Mimi and Amy receive, [this is a challenge](https://plus.google.com/106280202960862943182/posts/foi1zX6AvFg).  And what do we do when we encounter challenges?  We throw data at them!

## High-level design

The Advisor Program has 4 main parts:

- User profile & history: interface which lets the user record a desired specialization and timetable for graduation, history data, and everything else which might be relevant to personalizing his course plan (really hate group projects?).
- Planner: UI and logic which takes some profile data (desired specialization and courses already taken), course metadata (what requirements does a course satisfy and what is the estimated workload?), and user preferences (how many hours does he have available per semester?), and displays a customizable suggested schedule.
- Course browser: UI which displays a course list with past reviews for a course, as well as other details such as popularity (how quickly it fills up during registration) and metadata (does it use ProctorU? etc.).
- Review interface: form(s) where the user can leave thoughts on courses they've completed.  Automatically updates user's course history as well.

Generally, you will begin using the Advisor by creating an account and setting up your profile, including your specialization and any courses you've taken in the past (plus, optionally, other skills you have picked up, like Java programming or software project management).

You will then put your available time and preferences into the planner to get course suggestions.  You can examine the courses it suggests using the course browser and see whether they are to your liking; you can register for any which appeal to you using the standard OSCAR registration process.

Finally, after you have taken a semester of courses, you are strongly encouraged to review them and self-report how you did!  Doing this helps future students to know which courses will fit into their schedules, as well as helping the system to learn what factors predict doing well in a given course.  Any grade information you report will be used *only* in aggregate form - that means that no one except you will know what your personal grade was.

## Use

The app is hosted at <http://www.omscs-advisor.com>.  If you'd like to use it, you probably want to go there.  This source code is only relevant to you if you'd like to add new functionality to the Advisor Program.

## FAQ

// TODO: do we need anything here?

## Contributors

// TODO: there will be some instructions here eventually, with a link to the issue list, etc.

### Metadata updates

If you notice an outdated course description or other bad data, the fastest way to get it fixed is to edit the file // TODO: fill in // and submit a pull request.

## License

This source is licensed under the following license, based off the Go Programming Language License (?):

Copyright (c) 2015 omscs-advisor project (<https://github.com/Arkaaito/omscs-advisor>). All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted providing that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
  * Neither the name of omscs-advisor nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.  This project and derivative works do not carry the official endorsement of Georgia Institute of Technology, Udacity, or the OMS CS program.