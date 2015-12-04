/**
 * Created by arkaaito on 10/4/15.
 */
specializationMetadata = [
    {
        "specializationName": "Interactive Intelligence",
        "specializationId": "II",
        "allOf":[
            {"allOf":[
                {"oneOf":["SDP", "CCA"]}, // CS6300, CS6505
                {"twoOf":["KBAI", "ML"]} // CS7637, CS7641
            ]},
            {"oneOf":[
                {"twoOf":["HIT", "EdTech", "AIS"]}, // CS6440, CS6460, CS7634
                {"twoOf":["ICS", "MAD", "CC"]} // CS6795, CS7610, CS8803-CC
            ]}
        ]
    },
    {
        "specializationName": "Machine Learning",
        "specializationId": "ML",
        "allOf":[
            {"allOf":[
                {"oneOf":["CCA"]}, // CS6505
                {"oneOf":["ML"]}, // CS7641
            ]},
            {"threeOf":["ML4T"]} // CS7646
        ]
    },
    {
        "specializationName": "Computational Perception & Robotics",
        "specializationId": "CPR",
        "allOf":[
            {"oneOf":["CCA"]}, // CS6505
            {"oneOf":["AI", "ML"]}, // CS6601, CS7641
            {"allOf":["CP", "CV", "AIR"]} // CS6475, CS6476, CS8803-AIR
            // this is a simplification, should be redone when additional CPR courses are available
            // note: Computer Vision is listed as CS7495 on the page, but the actual course number is CS6476.
        ]
    },
    {
        "specializationName": "Computing Systems",
        "specializationId": "Sys",
        "allOf":[
            {"allOf":[
                "CCA", // CS6505
                {"twoOf":["AOS", "CN", "HPCA", "SDP", "DBSys"]} // CS6210, CS6250, CS6290, CS6300, CS6400
            ]},
            {"threeOf":["InfoSec", "NetSec", "SAD"]} // CS6035, CS6262, CS6310
        ]
    }
    /*
    R.I.P.
    {
        "specializationName": "High-Performance Computing",
        "specializationId": "HPC",
        "allOf":["CSE6140", "CSE6220"],
        "threeOf":["CS6290"]
    }
    */
];