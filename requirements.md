# **Requirements Document -- omscs-advisor**

##1 User Requirements

See the omscs-advisor README.md document.

##2 System Requirements

These subsections contain all the software requirements at a level of detail sufficient to enable designers/developers to design/develop a system that satisfies those requirements, and testers to test that the system satisfies those requirements. This part of the document should provide a numbered (possibly hierarchical) list of simple, complete, and consistent functional and non-functional requirements.

###2.1 Functional Requirements
####2.1.1 User data
<!-- From the readme: "User profile & history: interface which lets the user record a desired specialization and timetable for graduation, history data, and everything else which might be relevant to personalizing his course plan (really hate group projects?)." -->
#####2.1.1.1 Account creation
#####2.1.1.2 User profile
#####2.1.1.3 User history
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
8. The planning algorithm will only recommend a particular course if it projects a >50% probability the user can successfully enroll, based on their expected time ticket.  (See 2.1.3.2.1, course popularity profile.)
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

####2.1.3 Course metadata
<!-- The only major item not listed in the readme.  Not a stand-alone system piece at all, but the format needs to be very carefully defined because it will be quasi-manually maintained by users who may not otherwise be involved in the development process for omscs-advisor. -->
Course metadata updates will be added into the system through ... // TODO
#####2.1.3.1 Defined attributes
######2.1.3.1.1 Number
The official course number, e.g., CS 6300.
######2.1.3.1.2 Title
The official course title, e.g., Software Development Process.
######2.1.3.1.3 Instructors
The official instructor(s) for the course, e.g., Alex Orso.
######2.1.3.1.4 First offered
The term in which the course was first offered.  If the first offered term is in the past, terms prior to that one must not be listed as options when the user is adding this course to their history.  If the first offered term is in the future, the course must not be added to any user's plan in a term prior to that one.
######2.1.3.1.5 Available in summer
Whether or not the course is available in summer.  If it is not, the course must not be added to any user's plan in a summer term.
######2.1.3.1.6 Syllabus link
A link to the official syllabus (if available) on [the main OMSCS site](http://www.omscs.gatech.edu/courses/).
######2.1.3.1.7 Readiness link
A link to any official readiness survey or description of the course's recommended prerequisites.
######2.1.3.1.8 Timed proctored exams
The number of exams proctored through ProctorU.
######2.1.3.1.9 Timed non-proctored exams
The number of exams with time limits enforced through T-Square but no ProctorU requirement.
######2.1.3.1.10 Untimed exams
The number of untimed, open book exams, also known as "take-home exams".
######2.1.3.1.11 Group projects
The number of assignments, of any kind (coding or non-coding), that must be done with members of an instructor-assigned group.
######2.1.3.1.12 Coding assignments
The number of coding projects that must be done alone.
######2.1.3.1.13 Non-coding assignments
The number of non-coding projects (e.g., papers and problem sets) that must be done alone.
######2.1.3.1.14 Udacity required?
Whether or not the course requires completing all Udacity quizzes / watching all Udacity videos while logged into your GATech account.
######2.1.3.1.15 Primary specialization
The specialization to which this course may be applied.  If this course is applicable to multiple specializations (most of them), one of them will be selected subjectively.  Note that this is used to determine how a course is displayed in certain parts of the UI, but it does *not* affect how the planner selects courses.
######2.1.3.1.16 All specializations
All specializations to which this course may be applied.
#####2.1.3.2 Calculated attributes
######2.1.3.2.1 Popularity
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
######2.1.3.2.2 Grade and withdrawal split
What proportion of the class receives an 'A', according to critique.gatech.edu.

1. The previous course offering considered will be chosen  with the following order of preferences.
    1. If grades are available from at least one OMSCS section of the same class taught by the same instructor, the most recent OMSCS section will be considered.
    2. If grades are not available from any OMSCS sections, the totals across all sections of the same class taught by the same instructor will be considered.
2. The grade split will be calculated as (A count)/(A count + B count + C count + D count + F count).  Withdrawals will not be considered.
3. The withdrawal split will be calculated as (A count + B count + C count + D count + F count)/(A count + B count + C count + D count + F count + W count).
######2.1.3.2.3 Workload
######2.1.3.2.4 Difficulty
######2.1.3.2.5 Value

#####2.1.3.3 Import format
####2.1.4 Course browser
<!-- From the readme: "Course browser: UI which displays a course list with past reviews for a course, as well as other details such as popularity (how quickly it fills up during registration) and metadata (does it use ProctorU? etc.)." -->
#####2.1.4.1 Available filters
#####2.1.4.2 Displayed metadata
#####2.1.4.3 Displayed review content
#####2.1.4.4 Users taking this course
####2.1.5 Course review interface
<!-- From the readme: "Review interface: form(s) where the user can leave thoughts on courses they've completed.  Automatically updates user's course history as well." -->
#####2.1.5.1 Public feedback
#####2.1.5.2 Private feedback
#####2.1.5.3 Automatic updates to history

####2.1.6 Legacy review importer

###2.2 Non-Functional Requirements
####2.2.1 Platform
Any web application MVC framework should provide adequate support for the functionality needed.  In order to attract additional contributors to the project, however, the *ideal* framework is whichever one is preferred by OMSCS students with web development experience and/or an affinity for this project.

A [Google+ group poll](https://plus.google.com/106280202960862943182/posts/CyTx1Pdcnu3) showed strong support for Angular JS, and also for Django.
####2.2.2 Speed

####2.2.3 Scalability

####2.2.4 Privacy
