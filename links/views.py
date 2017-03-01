from django.shortcuts import render


import logging
logger = logging.getLogger(__name__)

def newbies(request):
    return render(request, "newbies.html", {})

def resources(request):
    return render(request, "resources.html", {})

def registration(request):
    return render(request, "registration.html", {})

def community(request):
    return render(request, "community.html", {})

def orientation(request):
    return render(request, "videos.html", {
        'name': 'OMSCS Orientation',
        'link_groups': {
            'Welcome': {
                'Welcome to Georgia Tech!': 'https://www.youtube.com/watch?v=wEGkk6L7yq0&ab_channel=Udacity',
                'About the Program': 'https://www.youtube.com/watch?v=UrIECnGEoIc&ab_channel=Udacity',
                'Equivalence with the On-Campus Program': 'https://www.youtube.com/watch?v=YPWIqpobKVE&ab_channel=Udacity',
                'Tools of the Program': 'https://www.youtube.com/watch?v=NPhCEEAAuPU&ab_channel=Udacity',
                'Online Resources': 'https://www.youtube.com/watch?v=POZupbKoEeI&ab_channel=Udacity',
                'Give us feedback!': 'https://www.youtube.com/watch?v=OPrnUFU3xf0&ab_channel=Udacity',
                '(Survey link)': 'http://goo.gl/forms/I77LGpR1UG',
                '(Program website)': 'http://www.omscs.gatech.edu/',
                '(Registrar)': 'http://www.registrar.gatech.edu/',
                '(Academic calendar)': 'http://www.registrar.gatech.edu/calendar/',
            },
            'OSCAR & Registration': {
                'OSCAR & Registration: Introduction': 'https://www.youtube.com/watch?v=_sLDDthT0oY&ab_channel=Udacity',
                'Accessing OSCAR': 'https://www.youtube.com/watch?v=oJ9IsETGt3k&ab_channel=Udacity',
                'Time Tickets and Holds': 'https://www.youtube.com/watch?v=G0fxlQdPBAY&ab_channel=Udacity',
                'Finding Classes': 'https://www.youtube.com/watch?v=XkiR2u8r_Ao&ab_channel=Udacity',
                'Class Information': 'https://www.youtube.com/watch?v=WuAXsrsci3k&ab_channel=Udacity',
                'Adding Classes': 'https://www.youtube.com/watch?v=eFAsIGLmfI4&ab_channel=Udacity',
                'Dropping and Withdrawing': 'https://www.youtube.com/watch?v=VLLZp5ftb-0&ab_channel=Udacity',
                'Wait Lists': 'https://www.youtube.com/watch?v=JTu5P4k9gMk&ab_channel=Udacity',
                'Getting Your Grades': 'https://www.youtube.com/watch?v=cKhllzUaN3g&ab_channel=Udacity',
                'Graduating!': 'https://www.youtube.com/watch?v=6S3pC4Da4oc&ab_channel=Udacity',
                '(OSCAR)': 'http://oscar.gatech.edu/',
                '(Registrar)': 'http://registrar.gatech.edu/',
            },
            'T-Square': {
                'T-Square: Introduction': 'https://www.youtube.com/watch?v=ursJMRmjrFQ&ab_channel=Udacity',
                'Accessing T-Square': 'https://www.youtube.com/watch?v=10qX_iRIQ38&ab_channel=Udacity',
                'T-Square Settings': 'https://www.youtube.com/watch?v=dQ2SdauiX4U&ab_channel=Udacity',
                'Tools of T-Square': 'https://www.youtube.com/watch?v=Zlc887hubpA&ab_channel=Udacity',
                'Assignments': 'https://www.youtube.com/watch?v=oD_zL_kDrYg&ab_channel=Udacity',
                'Gradebook': 'https://www.youtube.com/watch?v=VAtRaQIf5kI&ab_channel=Udacity',
                'Tests, Quizzes, and Surveys': 'https://www.youtube.com/watch?v=u5T21pc3_cU&ab_channel=Udacity',
                'Resources': 'https://www.youtube.com/watch?v=Nwg90LD35bw&ab_channel=Udacity',
                'Udacity and Piazza': 'https://www.youtube.com/watch?v=P-EFmOuUmM0&ab_channel=Udacity',
                '(T-Square)': 'http://t-square.gatech.edu/',
            },
            'Udacity': {
                'Udacity: Introduction': 'https://www.youtube.com/watch?v=A4CWbNmQX-E&ab_channel=Udacity',
                'Accessing Course Materials': 'https://www.youtube.com/watch?v=pyqirZW_sT8&ab_channel=Udacity',
                'The Main Pages': 'https://www.youtube.com/watch?v=u21fsINzTPs&ab_channel=Udacity',
                'Within a Course': 'https://www.youtube.com/watch?v=xUODtTalOX0&ab_channel=Udacity',
                'Form Exercises': 'https://www.youtube.com/watch?v=5895Bljbafg&ab_channel=Udacity',
                'Programming Exercises': 'https://www.youtube.com/watch?v=uNVZXt3xLNo&ab_channel=Udacity',
                '(Udacity)': 'http://www.udacity.com/',
            },
            'Piazza': {
                'Piazza: Introduction': 'https://www.youtube.com/watch?v=EuOutoWMwHQ&ab_channel=Udacity',
                'Getting Started: The Piazza Home Screen': 'https://www.youtube.com/watch?v=51X5kzNeUcM&ab_channel=Udacity',
                'Your Piazza Profile': 'https://www.youtube.com/watch?v=Brkv2QnVfnU&ab_channel=Udacity',
                'Reading The Topic List': 'https://www.youtube.com/watch?v=sY_MOP-XsiU&ab_channel=Udacity',
                'Reading The Topics': 'https://www.youtube.com/watch?v=xQVaz8SNMvE&ab_channel=Udacity',
                'Navigation': 'https://www.youtube.com/watch?v=DZ7zp15G3-A&ab_channel=Udacity',
                'New Posts': 'https://www.youtube.com/watch?v=9hZhFzM5h9E&ab_channel=Udacity',
                'Replying': 'https://www.youtube.com/watch?v=Rs610voLvI8&ab_channel=Udacity',
                '(Piazza)': 'http://www.piazza.com/',
            },
            'Other Tools': {
                'Other Tools: Introduction': 'https://www.youtube.com/watch?v=xFri3KTW3-s&ab_channel=Udacity',
                'Passport': 'https://www.youtube.com/watch?v=nNBDM7E69bQ&ab_channel=Udacity',
                'Proctortrack': 'https://www.youtube.com/watch?v=yvLzWtRNfVs&ab_channel=Udacity',
                'Google+': 'https://www.youtube.com/watch?v=_RIe4rpm6GA&ab_channel=Udacity',
                # Actually, you won't be prompted to join... offer a correction here?
                'Webex': 'https://www.youtube.com/watch?v=6ACIVBeXxJE&ab_channel=Udacity',
                'HipChat': 'https://www.youtube.com/watch?v=CRbL97rE5VE&ab_channel=Udacity',
                'Peer Feedback': 'https://www.youtube.com/watch?v=paLMTpUfC4o&ab_channel=Udacity',
                'Other Resources?': 'https://www.youtube.com/watch?v=2Im4Ef24clA&ab_channel=Udacity',
                '(Passport)': 'http://passport.gatech.edu/',
                '(Proctortrack)': 'http://testing.verificient.com/',
                '(Google+)': 'https://plus.google.com/communities/108902554607547634726',
                '(Webex)': 'http://gatech.webex.com/',
                '(HipChat)': 'http://gatech-omscs.hipchat.com/',
                '(HipChat Invite)': 'https://www.hipchat.com/invite/153319/901163c4c719efdd2d1ea5bdf1621cb9',
                '**(Slack)': 'http://omscs-study.slack.com/',
                '(Peer Feedback)': 'http://peerfeedback.gatech.edu/',
            },
            'Tips': {
                'Tips: Introduction': 'https://www.youtube.com/watch?v=I4mlKa_Wa4s&ab_channel=Udacity',
                'Start with only one class.': 'https://www.youtube.com/watch?v=cqcjhYWut0o&ab_channel=Udacity',
                'Establish a routine.': 'https://www.youtube.com/watch?v=JvBet8RjoRo&ab_channel=Udacity',
                'Prepare in advance.': 'https://www.youtube.com/watch?v=excMadc_3Zc&ab_channel=Udacity',
                'Embrace the community.': 'https://www.youtube.com/watch?v=iWBV-27w20E&ab_channel=Udacity',
                'Welcome to Georgia Tech!': 'https://www.youtube.com/watch?v=dqMm_T6KS-A&ab_channel=Udacity',
            },
        }
    })

def cs6035(request):
    return render(request, "videos.html", {
        'name': 'CS6035: Introduction to Information Security',
        'link_groups': {}
    })

def cs6210(request):
    return render(request, "videos.html", {
        'name': 'CS6210: Advanced Operating Systems',
        'link_groups': {}
    })

def cse6220(request):
    return render(request, "videos.html", {
        'name': 'CSE6220: Intro to High-Performance Computing',
        'link_groups': {}
    })

def cse6242(request):
    return render(request, "videos.html", {
        'name': 'CSE6242: Data and Visual Analytics',
        'link_groups': {}
    })

def cs6250(request):
    return render(request, "videos.html", {
        'name': 'CS6250: Computer Networks',
        'link_groups': {}
    })

def cs6262(request):
    return render(request, "videos.html", {
        'name': 'CS6262: Network Security',
        'link_groups': {}
    })

def cs6290(request):
    return render(request, "videos.html", {
        'name': 'CS6290: High-Performance Computer Architecture',
        'link_groups': {}
    })

def cs6300(request):
    return render(request, "videos.html", {
        'name': 'CS6300: Software Development Process',
        'link_groups': {}
    })

def cs6310(request):
    return render(request, "videos.html", {
        'name': 'CS6310: Software Architecture and Design',
        'link_groups': {}
    })

def cs6340(request):
    return render(request, "videos.html", {
        'name': 'CS6340: Software Analysis and Test',
        'link_groups': {}
    })

def cs6400(request):
    return render(request, "videos.html", {
        'name': 'CS6400: Database Systems Concepts and Design',
        'link_groups': {}
    })

def cs6440(request):
    return render(request, "videos.html", {
        'name': 'CS6440: Intro to Health Informatics',
        'link_groups': {}
    })

def cs6460(request):
    return render(request, "videos.html", {
        'name': 'CS6460: Educational Technology',
        'link_groups': {}
    })

def cs6475(request):
    return render(request, "videos.html", {
        'name': 'CS6475: Computational Photography',
        'link_groups': {}
    })

def cs6476(request):
    return render(request, "videos.html", {
        'name': 'CS6476: Computer Vision',
        'link_groups': {}
    })

def cs6505(request):
    return render(request, "videos.html", {
        'name': 'CS6505: Computability, Complexity and Algorithms',
        'link_groups': {}
    })

def cs6601(request):
    return render(request, "videos.html", {
        'name': 'CS6601: Artificial Intelligence',
        'link_groups': {
            '1.': {
                'Course Introduction': 'https://www.youtube.com/watch?v=oy1PwA6I22g&ab_channel=Udacity',
                'Course Outline [unavailable]': '#',
                'Overview': 'https://www.youtube.com/watch?v=uoSrsXpgmZ0&ab_channel=Udacity',
                'Challenge Question Introduction': 'https://www.youtube.com/watch?v=lL0kTx10Yh8&ab_channel=Udacity',
                'Challenge Question [before]': 'https://www.youtube.com/watch?v=o71jGWxKBaY&ab_channel=Udacity',
                'Challenge Question [after]': 'https://www.youtube.com/watch?v=U4DbMPBOW5E&ab_channel=Udacity',
                'Isolation': 'https://www.youtube.com/watch?v=BYqGXP95QLc&ab_channel=Udacity',
                'Building a Game Tree': 'https://www.youtube.com/watch?v=92VDHI0s7DI&ab_channel=Udacity',
                'Which of These Are Valid Moves? [before]': 'https://www.youtube.com/watch?v=gsSp5nBlTP8&ab_channel=Udacity',
                'Which of These Are Valid Moves? [after]': 'https://www.youtube.com/watch?v=jJ6dS7itftM&ab_channel=Udacity',
                'Building a Game Tree (Contd.)': 'https://www.youtube.com/watch?v=2EETczdx2t4&ab_channel=Udacity',
                'Isolation Game Tree with Leaf Values': 'https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/images/isolation-L6_leafValues.svg',
                'How Do We Tell the Computer Not to Lose?': 'https://www.youtube.com/watch?v=mLZZCtXkBHw&ab_channel=Udacity',
                'MIN and MAX Levels': 'https://www.youtube.com/watch?time_continue=1&v=dRBNRN_3t20&ab_channel=Udacity',
                'Propagating Values Up the Tree': 'https://www.youtube.com/watch?v=WpHKf4righw&ab_channel=Udacity',
                'Computing MIN MAX Values [before]': 'https://www.youtube.com/watch?v=xVY-uOiCcRM&ab_channel=Udacity',
                'Computing MIN MAX Values [after]': 'https://www.youtube.com/watch?v=w46-PyfRAWo&ab_channel=Udacity',
                'Choosing the Best Branch': 'https://www.youtube.com/watch?v=ftcZMraEokg&ab_channel=Udacity',
                'Aside: Reading the Book': 'https://www.youtube.com/watch?v=nTNOxVrC874&ab_channel=Udacity',
                'Searching Simple Games Reading [unavailable]': '#',
                'Max Number of Nodes Visited': 'https://www.youtube.com/watch?v=oY286RU8u8U&ab_channel=Udacity',
                'Max Moves [before]': 'https://www.youtube.com/watch?v=tl9CDh4Ooq8&ab_channel=Udacity',
                'Max Moves [after]': 'https://www.youtube.com/watch?v=nExt1uHfhhc&ab_channel=Udacity',
                'The Branching Factor': 'https://www.youtube.com/watch?v=SXsEWK3CNaw&ab_channel=Udacity',
                'Number of Nodes in a Game Tree [before]': 'https://www.youtube.com/watch?v=3OLwxE9ejbY&ab_channel=Udacity',
                'Number of Nodes in a Game Tree [after]': 'https://www.youtube.com/watch?v=OiDByg7hmqc&ab_channel=Udacity',
                'The Branching Factor (Contd.)': 'https://www.youtube.com/watch?v=mPi1eUToCjk&ab_channel=Udacity',
                'Max Number of Nodes': 'https://www.youtube.com/watch?v=x4l3DUlBAMw&ab_channel=Udacity',
                'Depth-Limited Search': 'https://www.youtube.com/watch?v=EZ8pO3PEFYU&ab_channel=Udacity',
                'Evaluation Function Intro': 'https://www.youtube.com/watch?v=hWPQrnLmYOk&ab_channel=Udacity',
                'Testing the Evaluation Function [before]': 'https://www.youtube.com/watch?v=zBdMKbgJ4HU&ab_channel=Udacity',
                'Testing the Evaluation Function [after]': 'https://www.youtube.com/watch?time_continue=1&v=FryRdCHb0y0&ab_channel=Udacity',
                'Testing the Evaluation Function Part 2 [before]': 'https://www.youtube.com/watch?v=O6AOr3Im6_8&ab_channel=Udacity',
                'Testing the Evaluation Function Part 2 [after]': 'https://www.youtube.com/watch?v=AzjVqG1LZo8&ab_channel=Udacity',
                'Testing Evaluation Functions': 'https://www.youtube.com/watch?v=6x-zfTyo81I&ab_channel=Udacity',
                'Testing the Evaluation Function Part 3 [before]': 'https://www.youtube.com/watch?v=1ns6OMenIvc&ab_channel=Udacity',
                'Testing the Evaluation Function Part 3 [after]': 'https://www.youtube.com/watch?v=_uiwip5it8U&ab_channel=Udacity',
                'Quiescent Search': 'https://www.youtube.com/watch?v=zpZf9TmI1NY&ab_channel=Udacity',
                'A Problem': 'https://www.youtube.com/watch?v=UP3v66znF7I&ab_channel=Udacity',
                'Iterative Deepening': 'https://www.youtube.com/watch?v=vy5wR-gk_Js&ab_channel=Udacity',
                'Understanding Exponential Time': 'https://www.youtube.com/watch?v=i4lD5p1vNtk&ab_channel=Udacity',
                'Exponential b=3 [before]': 'https://www.youtube.com/watch?v=HvrVY9RtwDU&ab_channel=Udacity',
                'Exponential b=3 [after]': 'https://www.youtube.com/watch?v=wcymdZfVo3U&ab_channel=Udacity',
                'Varying the Branching Factor': 'https://www.youtube.com/watch?v=-SwomcrNuQA&ab_channel=Udacity',
                'Horizon Effect': 'https://www.youtube.com/watch?v=3gkCpeU-3Wc&ab_channel=Udacity',
                'Horizon Effect (Contd.)': 'https://www.youtube.com/watch?v=Ph76X98ieck&ab_channel=Udacity',
                'Good Evaluation Functions [before]': 'https://www.youtube.com/watch?v=iUS_j66XmMU&ab_channel=Udacity',
                'Good Evaluation Functions [after]': 'https://www.youtube.com/watch?v=Hizo0Dr0NZ0&ab_channel=Udacity',
                'Evaluating Evaluation Functions': 'https://www.youtube.com/watch?v=Ng43Pq0-CLo&ab_channel=Udacity',
                'Alpha-Beta Pruning': 'https://www.youtube.com/watch?v=2_g9Kbmsqn0&ab_channel=Udacity',
                'Minimax Quiz [before]': 'https://www.youtube.com/watch?v=8CZZiwds8X8&ab_channel=Udacity',
                'Minimax Quiz [after]': 'https://www.youtube.com/watch?v=eRB93Dr5iM8&ab_channel=Udacity',
                'Alpha-Beta Pruning Quiz 1 [before]': 'https://www.youtube.com/watch?v=X0pMjJj7Lig&ab_channel=Udacity',
                'Alpha-Beta Pruning Quiz 1 [after]': 'https://www.youtube.com/watch?v=vsTBPFAgxLY&ab_channel=Udacity',
                'Alpha-Beta Pruning Quiz 2 [before]': 'https://www.youtube.com/watch?v=b6_1wSgs-2E&ab_channel=Udacity',
                'Alpha-Beta Pruning Quiz 2 [after]': 'https://www.youtube.com/watch?v=3fzETdaSGfA&ab_channel=Udacity',
                'Thad\'s Asides': 'https://www.youtube.com/watch?v=8BiZifMsF0o&ab_channel=Udacity',
                'Searching Complex Games Reading [unavailable]': '#',
                'Solving 5x5 Isolation': 'https://www.youtube.com/watch?v=IawyLVnyFf8&ab_channel=Udacity',
                '3-Player Games': 'https://www.youtube.com/watch?v=NSvurEyGn9k&ab_channel=Udacity',
                '3-Player Games Quiz [before]': 'https://www.youtube.com/watch?v=8E1OpOrxFck&ab_channel=Udacity',
                '3-Player Games Quiz [after]': 'https://www.youtube.com/watch?v=lUca2VPCR7k&ab_channel=Udacity',
                '3-Player Alpha-Beta Pruning': 'https://www.youtube.com/watch?v=pLMfSUp_Ckw&ab_channel=Udacity',
                '3-Player MAX-MAX-MAX Pruning [before]': 'https://www.youtube.com/watch?v=j2G5MrLozt8&ab_channel=Udacity',
                '3-Player MAX-MAX-MAX Pruning [after]': 'https://www.youtube.com/watch?v=mtKPk1JmbBk&ab_channel=Udacity',
                'Multi-player Alpha-Beta Pruning Reading': 'http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/Korf_Multi-player-Alpha-beta-Pruning.pdf',
                'Probabilistic Games': 'https://www.youtube.com/watch?v=YMDCSCAA5yg&ab_channel=Udacity',
                'Sloppy Isolation': 'https://www.youtube.com/watch?v=rxyyqogIdg4&ab_channel=Udacity',
                'Sloppy Isolation Expectimax': 'https://www.youtube.com/watch?v=DkTzxfi9woU&ab_channel=Udacity',
                'Expectimax Alpha-Beta Pruning': 'https://www.youtube.com/watch?v=orpXPtA7ITQ&ab_channel=Udacity',
                'Probabilistic Alpha-Beta Pruning [before]': 'https://www.youtube.com/watch?v=TxIePyar1Ic&ab_channel=Udacity',
                'Probabilistic Alpha-Beta Pruning [after]': 'https://www.youtube.com/watch?v=YS5CmZbGMww&ab_channel=Udacity',
                'Probabilistic Games Reading [unavailable]': '#',
                '(Thad Starner wearing a Google Glass)': 'https://www.youtube.com/watch?v=vhUt4ecB70I&ab_channel=Udacity',
                '(Isolation Extras)': 'https://www.youtube.com/watch?v=n_ExdXeLNTk',
            },
            '2.': {

            },
            '3.': {

            },
            '4.': {

            },
            '5.': {

            },
            '6.': {

            },
            '7.': {

            },
            '8.': {

            },
            '9.': {

            },
            '10.': {

            }
        }
    })

def cs6750(request):
    return render(request, "videos.html", {
        'name': 'CS6750: Human-Computer Interaction',
        'link_groups': {}
    })

def cs7637(request):
    return render(request, "videos.html", {
        'name': 'CS7637: Knowledge-Based Artificial Intelligence - Cognitive Systems',
        'link_groups': {}
    })

def cs7641(request):
    return render(request, "videos.html", {
        'name': 'CS7641: Machine Learning',
        'link_groups': {}
    })

def cs7646(request):
    return render(request, "videos.html", {
        'name': 'CS7646: Machine Learning for Trading',
        'link_groups': {}
    })

def cse8803(request):
    return render(request, "videos.html", {
        'name': 'CSE8803-O01: Big Data for Health Informatics',
        'link_groups': {}
    })

def cs8803_01(request):
    return render(request, "videos.html", {
        'name': 'CS8803: Artificial Intelligence for Robotics',
        'link_groups': {}
    })

def cs8803_02(request):
    return render(request, "videos.html", {
        'name': 'CS8803: Introduction to Operating Systems',
        'link_groups': {}
    })

def cs8803_03(request):
    return render(request, "videos.html", {
        'name': 'CS8803: Reinforcement Learning',
        'link_groups': {}
    })

def cs8803_04(request):
    return render(request, "videos.html", {
        'name': 'CS8803: Embedded Software',
        'link_groups': {}
    })

def cs8803_07(request):
    return render(request, "videos.html", {
        'name': 'CS8803: Cyber-Physical Systems Security',
        'link_groups': {}
    })

def cs8803_GA(request):
    return render(request, "videos.html", {
        'name': 'CS8803: Graduate Algorithms',
        'link_groups': {}
    })
