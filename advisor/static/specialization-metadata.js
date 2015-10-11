/**
 * Created by arkaaito on 10/4/15.
 */
specializationMetadata = [
    {
        "specializationName": "Interactive Intelligence",
        "specializationId": "II",
        "allOf":[
            {"oneOf":["CS6300", "CS6505"]},
            {"twoOf":["CS7637", "CS7641"]}
        ],
        "oneOf":[
            {"twoOf":["CS6440", "CS6460", "CS7634"]},
            {"twoOf":["CS6795", "CS7610", "CS8803CC"]}
        ]
    },
    {
        "specializationName": "Machine Learning",
        "specializationId": "ML",
        "allOf":[
            {"oneOf":["CS6505"]},
            {"oneOf":["CS7641"]}
        ],
        "threeOf":["CS7646"]
    },
    {
        "specializationName": "Computational Perception & Robotics",
        "specializationId": "CPR",
        "allOf":[
            {"oneOf":["CS6505"]},
            {"oneOf":["CS6601", "CS7641"]},
            {"allOf":["CS6475", "CS6476", "CS8803AIR"]}
            // this is a simplification, should be redone when additional CPR courses are available
            // note: Computer Vision is listed as CS7495 on the page, but the actual course number is CS6476.
        ]
    },
    {
        "specializationName": "Computing Systems",
        "specializationId": "Sys",
        "allOf":[
            "CS6505",
            {"twoOf":["CS6210", "CS6250", "CS6290", "CS6300", "CS6400"]}
        ],
        "threeOf":["CS6035", "CS6262", "CS6310"]
    },
    {
        "specializationName": "High-Performance Computing",
        "specializationId": "HPC",
        "allOf":["CSE6140", "CSE6220"],
        "threeOf":["CS6290"]
    }
];