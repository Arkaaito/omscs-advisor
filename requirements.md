# **Requirements Document -- omscs-advisor**

##1 User Requirements

See the omscs-advisor README.md document.

##2 System Requirements
###2.1 Functional Requirements
####2.1.1 User data
<!-- From the readme: "User profile & history: interface which lets the user record a desired specialization and timetable for graduation, history data, and everything else which might be relevant to personalizing his course plan (really hate group projects?)." -->
#####2.1.1.1 Account creation
All students and prospective students will be encouraged to create accounts.

1. Users who do not have accounts, or are logged out of their accounts, may browse and search courses.  However, they may not review courses nor use the planner.
2. Any person may create an account.  Creating an account requires a username, an e-mail address and a password.
3. After an account is created, if the e-mail address used is not associated with Georgia Tech, they will be prompted to provide a Georgia Tech e-mail address which will only be used for account verification.  If the e-mail address used *is* associated with Georgia Tech, that e-mail address will automatically be used for account verification as well.
4. Account verification will trigger an e-mail to the user's Georgia Tech e-mail address.  The e-mail should contain a link which can be clicked through to verify the account.  It should also include an activation code which can be manually put in on the verification page.
5. Account verification is not mandatory.  If the user skips providing a Georgia Tech e-mail address, or if they do not complete verification right away, they will be able to browse/search courses, personalize their profile and use the planner.  However, they will not be able to update their course history or leave course reviews.
6. Users who have completed account verification will have access to all site functionality, including course browsing and search, planning, course history and course reviews.

#####2.1.1.2 User profile
Registered users will be able to update their profile.  Most profile elements are intended to allow the user to improve the quality of the plan recommended by the planner and/or their overall site experience.
######2.1.1.2.1 Username
Required.  A name used to log into the site.  Displayed on the user's profile.  One option for the name displayed with one's reviews.
######2.1.1.2.2 Real name
Optional.  Displayed on the user's profile if they choose to share it.  One option for the name displayed with one's reviews.
######2.1.1.2.3 Time zone
Defaults to Eastern (Tech Time).  Used to localize the timestamps on reviews into the user's timezone.
######2.1.1.2.4 Location
Optional.  Displayed on the user's profile if they choose to share it.
######2.1.1.2.5 Status
Base status is calculated automatically based on the user's course history ("New Admit" if fewer than two foundational courses completed, "Student Emeritus" if 30 or more credits earned and at least one specialization fulfilled, "Student" otherwise).  Can be overridden to "Alumnus" or "On Sabbatical" by the user.  Can be overridden to "Frog" by an admin.  Used by the planner.  Displayed on the user's profile if they choose to share it.
######2.1.1.2.6 Preferred specializations
Defaults to all.  (This has the effect of allowing the planner to pick any specialization for the user.)  The user is allowed to choose any number of preferred specializations from the list for which they are eligible based on their first term in the program.  Used by the planner.  Displayed on the user's profile if they choose to share it.
######2.1.1.2.7 Secondary specializations
Defaults to none.  The available choices for secondary specializations are the same as the available choices for preferred specializations, excluding specializations which the user has currently selected as preferred.  Used by the planner.  Displayed on the user's profile if they choose to share it.
######2.1.1.2.8 Graduation date
Defaults to 18 terms (inclusive) after the term in which the user took their earliest recorded class.  If the user has no classes in their history, defaults to none.  Used by the planner.  Displayed on the user's profile if they choose to share it. 
######2.1.1.2.9 Exclusions
All default to off.  Allows the user to pick course features which they prefer to avoid.  The available exclusions are:

1. Group projects
2. ProctorU
######2.1.1.2.10 Hours per week
Defaults to 20.  Used by the planner.  No option to display on profile.
######2.1.1.2.11 Plan
Defaults to empty.  *Generated* by the planner.  Displayed on the user's profile if they choose to share it (defaults to private).  Also, if they choose to share their plan, they will be listed under the "Taking This Course" section on the course page for each of the course offerings listed in it.
#####2.1.1.3 User history
The site will track the user's past courses and any reviews the user has left for them.  The user can add to this list through the profile; the list will also be automatically updated when the user leaves a review (see 2.1.5.4).

The history is displayed on the user's profile if they choose to share it (defaults to private).

The history will display the thumbnails of the courses taken, along with the terms in which the user completed them.  The listing for each course offering should link to the course detail page and, if the user has submitted a non-anonymous review for that offering, that review.

####2.1.2 Planner
<!-- From the readme: "Planner: UI and logic which takes some profile data (desired specialization and courses already taken), course metadata (what requirements does a course satisfy and what is the estimated workload?), and user preferences (how many hours does he have available per semester?), and displays a customizable suggested schedule." -->
#####2.1.2.1 Parameters
<!-- User restrictions, recognized specializations, etc. -->
#####2.1.2.2 Planning algorithm
In order of priority (each constraint will be satisfied if the algorithm can do so without violating any of the constraints above it):

1. The planning algorithm will recommend a maximum of two courses per semester for conditional admits, one course per semester for all students in the summer term, and three courses per semester for full admits in spring and fall terms.
2. The planning algorithm will only recommend available courses the user has not already passed with an A or B.
3. The planning algorithm will recommend a set of courses which, taken together with the courses the user has already completed, satisfy the requirements for one of their preferred specializations.
4. The planning algorithm will recommend a set of courses which, taken together with the courses the user has already completed, satisfy the 30 credit-hour requirement for graduation.
5. The planning algorithm will only recommend courses which do not contain elements the user wishes to avoid (e.g., group projects if the user has selected "no group projects", proctored exams if the user has selected "no ProctorU").
6. The planning algorithm will only recommend a sequence of courses if it can be completed within the user's desired graduation timeframe.
7. The planning algorithm will only recommend a set of courses for a semester if that set can be completed within the user's available hours in that semester.
8. The planning algorithm will only recommend a particular course if it projects a >50% probability the user can successfully enroll, based on their expected time ticket.  (See 2.1.3.4.1, course popularity.)
9. The planning algorithm will prefer courses with higher student ratings over courses with lower ones.
10. The planning algorithm will prefer courses which satisfy the requirements for the user's secondary specializations.
11. The planning algorithm will prefer courses associated with any of the user's specializations (even if the specialization's requirements are already fulfilled by other courses) over courses with no such association.

#####2.1.2.3 Modifying the plan

1. When the user executes the planner, it will select a suggested sequence of courses and display them to the user.
    1. Courses in which the user is currently enrolled will be displayed under the current semester.
    2. Courses will be represented by thumbnails which include the number, the name, the instructor, the course rating, the popularity rating, and the estimated workload.
    3. Course thumbnails will be color-coded according to the primary specialization with which they are associated.
    4. Pinned courses (see 2.1.2.3.3.4) will be highlighted with a bold outline.
    5. Excluded courses (see 2.1.2.3.3.5) will be displayed, grayed out, in a sidebar.
2. If the user wishes to change the plan completely, the planner will allow them to edit their settings directly on the page, save their changes and then regenerate the plan.
    1. The planner will display the user's relevant profile settings (specializations, secondary specializations, exclusions, desired graduation date), editable in-line, in a sidebar or top panel.
    2. The planner will also allow them to specify a baseline amount of available time per week for each term (these values will default to the "typical" value they've set in their profile, if any) and regenerate the plan taking these into consideration.
3. If the user wants to make only small changes to the plan, the interface will allow modifications to individual courses.
    1. A course can be selected and deleted.
    2. A course can be added by course number.
    3. A course can be moved from one term to another.
    4. A course can be "pinned", which prevents it from being removed or relocated when the user subsequently regenerates the plan (until/unless it is unpinned).
    5. A course can be excluded, which prevents it from ever being added to the student's schedule (until/unless it is included again).

#####2.1.2.4 Saving and displaying the plan

1. The planner will allow the user to save the plan.
    1. The user can have one saved plan on file at any time.  Saving a new plan overwrites any old plan the user had saved previously.
    2. The saved plan will be accessible to the user through a "Plan" link on their profile.
    3. If the user attempts to leave the planner without saving their plan, it will prompt them to confirm.
2. If the user has a saved plan, this will display by default when the user loads the planner.  Otherwise, the planner will be empty when it loads.
3. Optionally, the user may share the plan with others.
    1. On the Plan View page, the user may choose any of three privacy settings (private, registered users only, and all-internet).
    2. The profile view of a user with a shared plan will display a "Plan" link which takes a qualified viewer to a non-editable version of the plan.

####2.1.3 Program metadata
<!-- The only major item not listed in the readme.  Not a stand-alone system piece at all, but the format needs to be very carefully defined because it will be quasi-manually maintained by users who may not otherwise be involved in the development process for omscs-advisor. -->
The course metadata will be defined in the JSON file described in 2.1.3.1.  The specialization metadata will be defined in the JSON file described in 2.1.3.2.  Generally, the following points are true of both sets of metadata:

1. Data will never be erased from these files, only added.
2. All data will have an "EffectiveFrom" date.
3. The only change which can be made to an existing record in these files is the addition of an 'effective until' date.  All other changes will be expressed with the addition of new records.
4. The effect of adding an "EffectiveUntil" date to an existing record is to make the corresponding entity unavailable after the EffectiveUntil date.  For courses, this means that it will cease to be offered after the named term.  For specializations, this means that it will not be listed as an option for students whose first term in the program is *after* the named term.
5. The effect of adding a new record with the same key as an old record is to update the contents of the corresponding entity from the effective date on.  So, for instance, adding a new record for CS 6300 with "Instructor" => "Spencer Rugaber" and "EffectiveFrom" => "Fall16" in the course metadata file will cause course offerings prior to Fall Term, 2016 to retain the instructor Alessandro Orso, while offerings during or after Fall Term, 2016 will reflect Spencer Rugaber as the instructor.
6. The format for effective and end dates is <term-name><year-code>.  A year code may be two digits or four digits (so "Fall16" and "Fall2016" are both valid representations of Fall Term, 2016).  Effective and end dates are inclusive.

#####2.1.3.1 Course metadata format
The course metadata will be contained in a file named course-metadata.js.

This file will contain one (1) array named courseMetadata.  Each entry in the array will be an object.  The following fields will be recognized:

`EffectiveFrom`: if the first entry for a course, the course was not available / is not available prior to this date.  If a subsequent entry, the changes in this entry go into effect on this date.
`EffectiveUntil`: the course will be unavailable after this date.

#####2.1.3.2 Specialization metadata format
The specialization metadata will be contained in a file named specialization-metadata.js.

This file will contain one (1) array named specializationMetadata.  Each entry in the array will be a nested object.  Each entry will require a specializationName field and a specializationId field.  The following additional fields will be recognized: oneOf; twoOf; threeOf; allOf.

The value of each field is an array of either course identifiers or other nested objects (again with field names oneOf, twoOf, threeOf or allOf).

For example, an entry of the form:

`["specializationName":Interactive Intelligence", "specializationId": "II", "allOf":[
    ["oneOf":["CS6300", "CS6505"]],
    ["twoOf":["CS7637", "CS7641"]]
], "oneOf":[
    ["twoOf":["CS6440", "CS6460", "CS7634"]],
    ["twoOf":["CS6795", "CS7610", "CS8803CC"]]
]]`

describes the Interactive Intelligence specification (albeit with some as-yet unavailable courses removed).
#####2.1.3.3 Defined course attributes
######2.1.3.3.1 Id
A unique identifier for the course.  This is usually the same as the official course number but for 8803 (Topics) courses, may include a unique suffix (e.g., CS8803AIR, CS8803RL, ...).
######2.1.3.3.2 Number
The official course number, e.g., CS6300.
######2.1.3.3.3 Title
The official course title, e.g., Software Development Process.
######2.1.3.3.4 Instructors
The official instructor(s) for the course, e.g., Alessandro Orso.
######2.1.3.3.5 First offered
The term in which the course was first offered.  If the first offered term is in the past, terms prior to that one must not be listed as options when the user is adding this course to their history.  If the first offered term is in the future, the course must not be added to any user's plan in a term prior to that one.
######2.1.3.3.6 Available in summer
Whether or not the course is available in summer.  If it is not, the course must not be added to any user's plan in a summer term.
######2.1.3.3.7 Syllabus link
A link to the official syllabus (if available) on [the main OMSCS site](http://www.omscs.gatech.edu/courses/).
######2.1.3.3.8 Readiness link
A link to any official readiness survey or description of the course's recommended prerequisites.
######2.1.3.3.9 Timed proctored exams
The number of exams proctored through ProctorU.
######2.1.3.3.10 Timed non-proctored exams
The number of exams with time limits enforced through T-Square but no ProctorU requirement.
######2.1.3.3.11 Untimed exams
The number of untimed, open book exams, also known as "take-home exams".
######2.1.3.3.12 Group projects
The number of assignments, of any kind (coding or non-coding), that must be done with members of an instructor-assigned group.
######2.1.3.3.13 Coding assignments
The number of coding projects that must be done alone.
######2.1.3.3.14 Non-coding assignments
The number of non-coding projects (e.g., papers and problem sets) that must be done alone.
######2.1.3.3.15 Udacity required?
Whether or not the course requires completing all Udacity quizzes / watching all Udacity videos while logged into your GATech account.
######2.1.3.3.16 Primary specialization
The specialization to which this course may be applied.  If this course is applicable to multiple specializations (most of them), one of them will be selected subjectively.  Note that this is used to determine how a course is displayed in certain parts of the UI, but it does *not* affect how the planner selects courses.
######2.1.3.3.17 All specializations
All specializations to which this course may be applied.
#####2.1.3.4 Calculated attributes
######2.1.3.4.1 Popularity
The popularity of a course is defined by a series of datapoints regarding how quickly it filled in previous registration periods.  Two base popularity statistics and a prediction are available.  The popularity statistics are based on data from a previous offering of the course.  The prediction is calculated based on these statistics and other course metadata.

1. The previous course offering considered will be chosen based on the term currently under evaluation ("target term"), with preference given to terms in the following order.
    1. If the target term is summer and the course has previously been taught in summer, the most recent summer offering of this course is preferred.  If the target term is fall or spring, the most recent non-summer offering of this course is preferred.
    2. If the course has not previously been offered in a corresponding term, the most recent offering of the course is preferred.
    3. If the course has never before been offered, the popularity data for the *most popular* course offering the professor has taught previously is preferred.
    4. If the professor has never before offered an OMS course, the *average* popularity data across the *first offering* of all courses associated with the same specialization is preferred.
    5. If the course has no associated specialization, the *average* popularity data across all courses offered for the first time in the *current term* (or most recent term for which data is available) is preferred.
2. The popularity index reflects which time ticket window was in effect when the course first reached cap.  The goal of calculating this value is to enable the system to estimate the likelihood that a student with a given number of credits entering a term will be able to enroll in the course.
    1. The popularity index is a decimal number in the range (30, -infinity).
    2. The base value for popularity index is based on when the course reached cap.  It is a linear interpolation between the last time ticket for which it was open and the first for which it was closed.  For example, if a course offering reached cap 50% of the way between the time ticket start for students with 6 earned credits and that for students with 3 earned credits, its popularity index was 4.5.
    3. If the cap was reached but then raised, only the date/time at which the *final* cap was reached is relevant.
    4. If the final cap was never reached, the number of remaining slots is translated into a negative popularity index as follows: the number of remaining slots is divided by the number of students who signed up during the last time ticket (students with 0 credit hours) of registration and multiplied by -3.  If no students signed up during the last time ticket, the popularity index should be displayed as 'N/A' and treated as negative infinity in all calculations for which it is used.
3. The popularity ranking reflects how quickly the course closed compared to other courses offered that term.  The goal of calculating this value is to give the student a subjective idea of how popular one course is relative to another.
    1. The popularity index is an ordinal ranking (1, 2, etc., corresponding to 1st, 2nd, and so on).
    2. The first course offering to reach its registration cap in a term is #1.  The second course offering to reach its registration cap is #2, and so on.
    3. Course offerings which do not reach their registration caps are ranked below the course offerings which did in order of the number of students enrolled in each at close of registration.
    4. For a particular course, if the cap was reached but then raised, only the date/time at which the *original* cap was reached is relevant.
######2.1.3.4.2 Grade and withdrawal split
What proportion of the class receives an 'A', according to critique.gatech.edu.

1. The previous course offering considered will be chosen  with the following order of preferences.
    1. If grades are available from at least one OMSCS section of the same class taught by the same instructor, the most recent OMSCS section will be considered.
    2. If grades are not available from any OMSCS sections, the totals across all sections of the same class taught by the same instructor will be considered.
2. The grade split will be calculated as (A count)/(A count + B count + C count + D count + F count).  Withdrawals will not be considered.
3. The withdrawal split will be calculated as (A count + B count + C count + D count + F count)/(A count + B count + C count + D count + F count + W count).
######2.1.3.4.3 Workload
The median estimated weekly workload (from course reviews for previous offerings), along with the 85% mark and the 15% mark (i.e., 85% of students thought it took less work than this; 15% of students thought it took less work than this).

1. The previous course offering whose reviews are considered will be chosen with the following order of preferences.
    1. If at least 20 reviews are available from the most recent offering of this course, only reviews from that offering will be considered.
    2. If fewer than 20 reviews are available from the most recent offering of this course, the 3 most recent offerings of the course will be considered.
######2.1.3.4.4 Difficulty
The average estimated difficulty (from course reviews for previous offerings).

The previous course offering whose reviews are considered will be chosen with the same preference rules as for 2.1.3.4.3: Workload.
######2.1.3.4.5 Value
The average estimated value (from course reviews for previous offerings).

The previous course offering whose reviews are considered will be chosen with the same preference rules as for 2.1.3.4.3: Workload.
####2.1.4 Course browser
<!-- From the readme: "Course browser: UI which displays a course list with past reviews for a course, as well as other details such as popularity (how quickly it fills up during registration) and metadata (does it use ProctorU? etc.)." -->
#####2.1.4.1 Available filters
#####2.1.4.2 Displayed metadata
#####2.1.4.3 Displayed review content
#####2.1.4.4 Users taking this course
####2.1.5 Course review interface
<!-- From the readme: "Review interface: form(s) where the user can leave thoughts on courses they've completed.  Automatically updates user's course history as well." -->

#####2.1.5.1 Review prompts
1. When the user updates their history to indicate that they've taken a course in a past term, they should be prompted to review that course.  If they opt to review, the review should automatically be associated with the term they selected.
2. When a user first logs in after the end of a term in which their plan had listed them taking one or more courses, they should be prompted to review those courses.  If they opt to review, the review should automatically be associated with the just-completed term.
3. When the user is viewing a course, they should have the option to review.  In this case, a user who opts to review must manually select the term in which they took the course.

#####2.1.5.2 Public feedback
######2.1.5.2.1 Effort estimate
The user will be asked to estimate the average/max/min effort for the course.  This will take the form of hours/week.  The permissible range for this is 0-168.
######2.1.5.2.2 Difficulty estimate
The user will be asked to estimate the difficulty of the course.  The permissible values for this are Trivial/Very Easy/Somewhat Easy/Moderate/Somewhat Hard/Very Hard/Brutal.
######2.1.5.2.3 Value estimate
The user will be asked to give a rating (1-5 stars) of how much they learned from the course.
######2.1.5.2.4 Comments
The user will be invited to leave a freeform text review about the course.  The textual portion of the review is optional.

#####2.1.5.3 Private feedback
######2.1.5.3.1 Grade
The user will have the option to enter their grade for the course - A/B/C/D/F/W.  If no grade is entered, the site will assume they earned a passing grade (and did not withdraw).

Collecting the grade allows us to determine how many credit hours the user has earned; it also allows us to (eventually) make inferences about what courses predict success in what other courses.  **Under no circumstances will a user's grade be displayed to other users on the site;** the grade's purpose is purely to improve course recommendations.  Grades are self-reported and are not confirmed with the Georgia Tech transcript system.

######2.1.5.3.2 Anonymity
For each review, the user will have the option of listing it publicly or anonymously.

1. If the user lists the review publicly, it will be associated with them on the site.
    1. If their history is also set to publically- or community-viewable, the review will be displayed in the user history seen by any user viewing their profile.
    2. Their display name (and full name, if public) will be listed with the review everywhere the review is displayed.
    3. The review will include a link to their profile.
2. If the user lists the review anonymously, it will not be linked to them anywhere on the site.
    1. Only they will see the review linked off their profile's history page.
    2. Anywhere else the review is displayed, it will be attributed to "Anonymous".
    3. The review will not link to any profile.
3. A user can switch the anonymity setting for an individual review from the list of reviews on their profile.

Regardless of the anonymity setting chosen for the review, any grade the user enters will **not** be displayed along with the review.

#####2.1.5.4 Automatic updates to history
Regardless of which path the user takes to review the course (updating their history, reviewing from the course summary page, ...), leaving a review for the course will automatically add it to their history for the term they reviewed.

####2.1.6 Legacy review importer

###2.2 Non-Functional Requirements
####2.2.1 Platform
Any web application MVC framework should provide adequate support for the functionality needed.  In order to attract additional contributors to the project, however, the *ideal* framework is whichever one is preferred by OMSCS students with web development experience and/or an affinity for this project.

A [Google+ group poll](https://plus.google.com/106280202960862943182/posts/CyTx1Pdcnu3) showed strong support for Angular JS, and also for Django.
####2.2.2 Speed

####2.2.3 Scalability

####2.2.4 Privacy

###2.3 Future Items

####2.3.1 Social features
At some point, we may want to allow students to "friend" each other so they can see which of their friends are in their classes.

####2.3.2 Recommendation features
Right now, all reviews (possibly restricted by term) are considered when calculating the projected workload for a course, the student rating, etc.  Eventually the system should have a way of assigning higher weights to reviews left by users similar to you (for some definition of similar).  It should also move away from the heavy specialization/topic area + rating focus to a more sophisticated recommendation system ("students who took X also took Y", "students who liked X also liked Y").

####2.3.3 Other prerequisites
Right now, the system doesn't capture the concept of prerequisite skills.  Ideally, the system should capture the fact that certain skills or courses outside the OMSCS program are good preparation for particular courses.

This will likely require a two-part approach: (1) users will need to indicate their skills/outside prerequisites on their profiles, and (2) users will need the option to suggest an outside prerequisite when reviewing a course.  These could potentially be combined into one UI element (e.g., when reviewing a course the user is prompted to select the one thing which helped them the most from a list of outside prerequisites; that is then added to their profile *and* suggested as a course prereq).

####2.3.4 Claiming old reviews
The system will be seeded with several old reviews from the Unofficial Course Review Spreadsheet.  Right now, there's no way to map those to users in the omscs-advisor system - so you could (1) leave another review after having left one in the spreadsheet, and (2) continue to get nagged to review despite having left one in the spreadsheet.  We may want to introduce a mechanism by which a user can "claim" their old reviews.  Then again, these reviews will age out of the system eventually; perhaps we should just wait.

####2.3.5 Course metadata for summer
Most parts of the system distinguish between summer and other terms because not all courses are available in summer and the ones which are may have somewhat different content.  However, the course metadata section does not (yet).  This needs to be revised.