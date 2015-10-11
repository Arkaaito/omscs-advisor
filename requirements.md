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
The planner allows the user to set the following parameters with on-page elements, defaulting to the values configured in the user's profile:

* Starting term
* Hours per week (configurable per semester)
* Preferred specializations
* Secondary specializations
* Target graduation date
* Exclusions

It considers the following additional information for logged-in users:

* Courses already completed
* Admit status

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
6. The format for effective and end dates is <term-name><year-code>.  A year code may be two digits or four digits (so "Fall16" and "Fall2016" are both valid representations of Fall Term, 2016).  Term names should be case-insensitive (so "Fall16" and "FALL16" are both valid representations).  Effective and end dates are inclusive.

#####2.1.3.1 Course metadata format
The course metadata will be contained in a file named course-metadata.js.

This file will contain one (1) array named courseMetadata.  Each entry in the array will be an object.

These fields are used to describe the set of course offerings to which a given metadata object should be applied:

* `Id`: unique identifier for the course.  All metadata objects with the same ID are considered to apply to the same course, and represent different values for its properties at different points in time.
* `Summer`: (boolean) if true, the attributes in this bundle apply only to summer offerings of the course.  If false, they apply only to spring and fall terms.  Note that in the absence of at least one metadata entry for a given course id that sets `Summer=true`, the course is assumed *not* to be available in summer terms.
* `EffectiveFrom`: if the first entry for a course, the course was not available / is not available prior to this date.  If a subsequent entry, the changes in this entry go into effect on this date.
* `EffectiveUntil`: the course will be unavailable after this date.

The following fields will be recognized and applied to all terms in the given range:

* `Number`: (string) official course number.
* `Title`: (string) official course title.
* `Summary`: (string) course summary from Udacity.
* `Instructors`: (array of strings) official instructor name, last name first; e.g., "Orso, Alessandro".
* `Syllabus`: (nullable string) link to the syllabus.
* `Readiness`: (nullable string) link to the readiness quiz or set of bullet points.
* `UdacityRequired`: (boolean)
* `PiazzaRequired`: (boolean)
* `Specialization`: (string) the specialization ID of the specialization which should be displayed for the course in parts of the UI where only the "primary" specialization should be displayed.  Note that this attribute is cosmetic; the actual data about what specializations a course fits into (and how) is encoded in the specialization metadata.

The following fields will be recognized and applied to only summer terms (if summer=true) or non-summer terms (otherwise):

* `ProctoredExams`: (nonnegative integer)
* `TimedExams`: (nonnegative integer)
* `OpenBookExams`: (nonnegative integer)
* `GroupProjects`: (nonnegative integer)
* `CodingAssignments`: (nonnegative integer)
* `WrittenAssignments`: (nonnegative integer)

Some fields appear above without further explanation; all are used directly with no further processing, and as such also appear in section 2.1.3.3 (where more details are given).

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
######2.1.3.3.4 Summary
The one-sentence summary taken from Udacity, if available.
######2.1.3.3.5 Instructors
The official instructor(s) for the course, e.g., Alessandro Orso.
######2.1.3.3.6 First offered
The term in which the course was first offered.  If the first offered term is in the past, terms prior to that one must not be listed as options when the user is adding this course to their history.  If the first offered term is in the future, the course must not be added to any user's plan in a term prior to that one.
######2.1.3.3.7 Available in summer
Whether or not the course is available in summer.  If it is not, the course must not be added to any user's plan in a summer term.
######2.1.3.3.8 Syllabus link
A link to the official syllabus (if available) on [the main OMSCS site](http://www.omscs.gatech.edu/courses/).
######2.1.3.3.9 Readiness link
A link to any official readiness survey or description of the course's recommended prerequisites.
######2.1.3.3.10 Timed proctored exams
The number of exams proctored through ProctorU.
######2.1.3.3.11 Timed non-proctored exams
The number of exams with time limits enforced through T-Square but no ProctorU requirement.
######2.1.3.3.12 Untimed exams
The number of untimed, open book exams, also known as "take-home exams".
######2.1.3.3.13 Group projects
The number of assignments, of any kind (coding or non-coding), that must be done with members of an instructor-assigned group.
######2.1.3.3.14 Coding assignments
The number of coding projects that must be done alone.
######2.1.3.3.15 Non-coding assignments
The number of non-coding projects (e.g., papers and problem sets) that must be done alone.
######2.1.3.3.16 Udacity required?
Whether or not the course requires completing all Udacity quizzes / watching all Udacity videos while logged into your GATech account.
######2.1.3.3.17 Primary specialization
The specialization to which this course may be applied.  If this course is applicable to multiple specializations (most of them), one of them will be selected subjectively.  Note that this is used to determine how a course is displayed in certain parts of the UI, but it does *not* affect how the planner selects courses.
######2.1.3.3.18 All specializations
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

By default, the list of courses will include all available courses for the selected term.  They will be sorted according to average star rating in the current or previous term.

The user will be able to set the following filters when browsing courses.

* Term: defaults to the *next* term (i.e., the first one for which add/drop has not yet closed)
* Area: defaults to "all"; maps to the list of specializations; shows courses with any association with the selected specialization

The user will be able to sort by the following fields:

* Course number
* Course name
* Popularity index
* Average workload
* Average difficulty
* Average value

#####2.1.4.2 Displayed metadata

The filter/list thumbnails for each course will include the following info:

* Course number
* Course name
* Instructor
* Popularity index (see 2.1.3.4.1)
* Workload range & average
* Average difficulty rating
* Average value (i.e., star) rating
* Summary text from Udacity

The detail screen for a course will show all course attributes in 2.1.3.3 and 2.1.3.4, except for the unique course ID (which is an internal identifier).  It will also show the "All Time" version of each attribute in 2.1.3.4, marked appropriately.

#####2.1.4.3 Displayed review content

The detail screen for a course will show the most recent 3 reviews for the selected offering of that course.  (A link will allow the user to display all reviews; this will include reviews first from the selected offering, and then from other offerings.)

Each review will include the public info listed in section 2.1.5.2, along with the date the review was left and the term to which it applies.  If the user has chosen to leave the review anonymously, the review will display a generic profile image and an attribution to "Anonymous".  Otherwise the review will include the user's name (display or full name depending on their privacy settings) and profile image, which will link to their profile.

#####2.1.4.4 Users taking this course

The detail screen for a course will show up to 10 other users who are taking the course.  Users displayed in this section will be drawn from the pool of users whose plans are public to others with the viewer's status.  (E.g., if the viewer is a guest, the user can only be displayed if their plan has visibility: guest.  If the viewer is a confirmed student, the user can be displayed if their plan has visibility: guest, visibility: member, or visibility: confirmed.)

Users will be sorted by how many courses they have previously taken with the viewer; users who have overlapped in more courses will be preferred for display.  Within each group (e.g., 2 shared courses), users who share the viewer's specialization will be displayed in preference to users who do not.

Each user will be displayed with a thumbnail containing their profile picture (if set), full name (if shared - username otherwise), and specialization.  Clicking the thumbnail will take the viewer to their public profile.

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
The user will be asked to estimate the difficulty of the course.  The permissible values for this are Trivial/Very Easy/Easy/Somewhat Easy/Moderate/Somewhat Hard/Hard/Very Hard/Brutal.
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
Currently, several reviews for OMSCS courses have been created in the Unofficial Course Review Survey.

1. The system should have a mechanism for importing UCRS reviews which predate the omscs-advisor launch date.
    1. The difficulty values will be mapped into omscs-advisor difficulty values as follows:
        * Brain-dead easy -> Trivial
        * Whatever you want -> Trivial
        * Useless -> Trivial
        * Average -> Moderate
        * Somewhat Difficult -> Somewhat Hard
        * Very Difficult -> Very Hard
    2. Ranges given for workload in the form 'X to Y', 'X - Y', or 'X-Y' will be mapped to the lower and upper effort estimates - the midpoint of each review's range will be treated as the average effort estimate for it.  Ranges given for workload in the form 'X+' will be treated as ranges of X to (2*X).  Single values will be used for lower, upper *and* average effort estimate.
    3. If no semester is given, the review will be attributed to the first semester in which the course was offered.
    4. General Comments will be imported into the review body.
    5. Difficulty and effort are mandatory.  Reviews for which these cannot be parsed will not be imported.
2. The system should display legacy reviews on the course page.
    1. Reviews will be displayed with attribution to the student listed in the sheet (if name is given), or "A Student" (if no name is given).
    2. Non-legacy reviews will be given precedence over UCRS reviews (i.e., the non-legacy reviews will be displayed first in the list).
3. The system should include legacy reviews in the workload, difficulty, and value estimates used by the planner.

###2.2 Non-Functional Requirements
####2.2.1 Platform
Any web application MVC framework should provide adequate support for the functionality needed.  In order to attract additional contributors to the project, however, the *ideal* framework is whichever one is preferred by OMSCS students with web development experience and/or an affinity for this project.

A [Google+ group poll](https://plus.google.com/106280202960862943182/posts/CyTx1Pdcnu3) showed strong support for Angular JS, and also for Django.

####2.2.2 Speed
The only piece of the application where performance is likely to be an issue is the planner itself.  Depending on the algorithm used and how many factors are considered when ranking/arranging courses, this could become quite time-consuming.

Wait times up to 30 seconds are acceptable.  However, if wait times are over 3 seconds, the user should be distracted with an entertaining loading/progress message.

Some suggested messages are:

* Rescuing Dr. Littman from airport security... (guard X of 6)
* Extracting requirements from Dr. Rugaber... (requirement X of 20)
* Sending e-mails to Mimi... (message X of 1,000)
* Feeding Dr. Goel... (frog X of 4)
* Cloning Dr. Joyner... (clone X of 17)
* Identifying birds... (raven X of 9)
* Reacquiring robots... (robot X of 300)
* Teasing T-Square... (taunt X of 15)
* Rebooting TAs... (TA X of 12)
* Crashing VMs... (VM X of 34)
* Educating technology... (lesson X of 100)
* Reeducating technology... (lesson X of 200)
* Reconfiguring Skynet... (Terminator X of 5287)
* Tempting fate... (temptation X of 622)
* Teaching machines... (machine X of 53)
* Processing developments in software... (development X of 80)
* "Encouraging" Buzzport... (threat X of 8)
* Learning Qs... (Q X of 50)
* Learning cues... (cue X of 50)
* Learning queues... (queue X of 50)
* Queueing learns... (learn X of 50)
* Dynamically reprogramming...
* Initializing Nate Payne...

####2.2.3 Scalability
As of now (Fall 2015), the OMSCS program has admitted approximately 2,000 students.  We speculate that the program will eventually scale to as many as 10,000 simultaneous students.  omscs-advisor should be able to support simultaneous use by one tenth of this student population with no request timeouts or failures.

Once omscs-advisor is generalized to non-OMSCS MOOC students and online degree candidates at other schools, the scope could become even broader.  [Dhawal Shah](https://www.edsurge.com/n/2013-12-22-moocs-in-2013-breaking-down-the-numbers) stated at the end of 2013 that 10 million students had enrolled in MOOCs to date and class-central.com received over 700k visits in 2013.  If very successful, omscs-advisor could expect the same kind of scale.  However, OMSCS students will likely continue to have an outsized importance in performance terms, as (1) OMSCS students will always be the core constituency of omscs-advisor, (2) the planner, which is the most computationally demanding piece of the system, has relevance only to OMSCS students, and (3) OMSCS student usage of the planner is likely to spike sharply at certain times (e.g., when admissions letters are sent out).

####2.2.4 Privacy
It is likely that omscs-advisor will come to have a social component, as the initial feature set will index users by interests and future work might introduce additional search features (e.g., finding other users in your specialization or your classes) and interaction features (e.g., friending, following or study groups).

For users to enjoy this aspect of the system, **they must have control over their information and must not be surprised by the ways in which it is used**.  In service of this goal, users should not be required to make public *any* information about themselves.  Every piece of a user's profile, including any plans or history information they choose to set, must have configurable privacy options (in the initial phase: show this to all, show this to verified users, or show this to no one).  And every review or tip a user leaves must give them the option of anonymity.

###2.3 Future Items

####2.3.1 Social features
At some point, we may want to allow students to "friend" each other so they can see which of their friends are in their classes.

####2.3.2 Recommendation features
Right now, all reviews (possibly restricted by term) are considered when calculating the projected workload for a course, the student rating, etc.  Eventually the system should have a way of assigning higher weights to reviews left by users similar to you (for some definition of similar).  It should also move away from the heavy specialization/topic area + rating focus to a more sophisticated recommendation system ("students who took X also took Y", "students who liked X also liked Y").

####2.3.3 Other prerequisites
Right now, the system doesn't capture the concept of prerequisite skills.  Ideally, the system should capture the fact that certain skills or courses outside the OMSCS program are good preparation for particular courses.

This will likely require a two-part approach: (1) users will need to indicate their skills/outside prerequisites on their profiles, and (2) users will need the option to suggest an outside prerequisite when reviewing a course.  These could potentially be combined into one UI element (e.g., when reviewing a course the user is prompted to select the one thing which helped them the most from a list of outside prerequisites; that is then added to their profile *and* suggested as a course prereq).

We could start out with a more general "What I Wish I Knew" section which each user could optionally fill out after leaving a course review, and perhaps do keyword extraction on it to seed our list of recognized prerequisites.  Allowing user upvotes on this would lead to a very useful resource.

Maybe we can just seed the list manually.  What are the major items I’ve heard about so far?

* UML
* Java
* Python
* Image processing
* Probability and statistics
* Linear algebra
* C

What’s the most useful info for a user to have?  The general area of a prerequisite, or a concrete suggested tutorial for it?
	…e.g., another MOOC?

####2.3.4 Non-OMSCS MOOCs

How would I integrate non-OMSCS MOOCs?  The challenges are more or less as follows:

* Non-OMSCS MOOCs are not on the same schedule as OMSCS MOOCs.  Could put in your own completion date.  Challenging that we can’t narrow it down to the actual available options.
* Hard to get a comprehensive list of non-OMSCS MOOCs.  Should check to see if class-central has a list API.
* Useful to build up equivalence classes.  E.g., "This course ~= this other course (so you can take either to give you the needed prerequisites for a Java development course)."
* Grades are not measured on the same scale.

How would we get people to enter them in?

* On the course history page, add a radio button for OMSCS vs. non-OMSCS.
* Non-OMSCS form can prompt you to select a platform, a general subject area (according to that platform’s classification), and tags.  The tags will have autocomplete suggestions based on our list.  We may have to do some manual review periodically to see if we’re getting a lot of fragmentation (e.g., "Java" vs. "Java programming").
* We should also have a link - "Can’t find your course?"
* Clicking this should allow you to paste in a link to the course.  If it’s from a platform we know (i.e. have a course home parser for) we should match the course with the DB or import it, then return them to the page with the form prepopulated.  Otherwise, it should get e-mailed to us so we can investigate and add something for that particular platform if appropriate.  (The user should get notified when the course gets added.  It’s probably too much of a pain to then automatically add it to their history.)
* Alternatively we could allow them to add a stub/dummy course to their profile, which gets updated if/when we add it.

Let’s think about this a bit more.  Actually, this may be the best way, because people who are heavily involved in outside MOOCs may be interested in filling in their profile with these.

Maybe we have a four-tiered structure:

* OMSCS courses, which have all of the stuff associated with the GATech semesters and start dates/end dates.
* Eminent courses, which will have individualized offering info with specific start dates/end dates.  These will probably be (mostly) the first offerings of major MOOC platforms: ai-class.com, ml-class.com, MITx Circuits and Systems, etc.  These exist mainly so that people who were in, e.g., the first or second offering of Thrun’s AI course can find each other socially.
* Known courses, which will have unchanging metadata (title, etc.), but will ask the user to manually put in their end/completion date.
* Unknown courses, which will ask the user to manually put in anything they’d like to associate with the course.

How do we ensure that users know what the correct URL is for a given class?  Maybe we need to support multiple URL schemes per platform.

Tracking these URLs as part of the system also makes it easier later if we want to allow trusted users (as opposed to devs) to moderate suggested courses.

-----

Should make a chart of functionality available to different user classes: guests, unverified, verified, frogs & froggy friends, and admins

Should make a chart of functionality available for different course types: OMSCS courses, eminent courses, known courses, and unknown courses

-----

Before we do the clever prerequisite inference stuff, can we invite users to explicitly specify a prerequisite suggestion when they review a course?  We'll give them a default list consisting of the other courses already listed in their profile/course history.  Maybe we'll *require* that they have the course listed in their profile/course history already, and give them the link to edit their history if there's really something missing that they've taken.  This would avoid the problem of people listing "speculative" prerequisites (i.e. "I think it would really have helped if I had taken this before...").

####2.3.5 Credentials
It might be nice to let users who have done nanodegrees, etc., put those things in their history/plans.

Would allow people to find others who have done the [nano]degrees they're considering.  Would also allow people who are planning those things in the future to find other OMSCS students who will be in their cohort.

####2.3.6 Claiming old reviews
The system will be seeded with several old reviews from the Unofficial Course Review Spreadsheet.  Right now, there's no way to map those to users in the omscs-advisor system - so you could (1) leave another review after having left one in the spreadsheet, and (2) continue to get nagged to review despite having left one in the spreadsheet.  We may want to introduce a mechanism by which a user can "claim" their old reviews.  Then again, these reviews will age out of the system eventually; perhaps we should just wait.

####2.3.7 Course metadata for summer
Most parts of the system distinguish between summer and other terms because not all courses are available in summer and the ones which are may have somewhat different content.  However, the course metadata section does not (yet).  This needs to be revised.