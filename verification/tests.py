"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["x*x*x-12*x*x-42", "x-3"],
            "answer": ["x*x-9*x-27", "-123"]
        },
        {
            "input": ["x*x-1", "x+1"],
            "answer": ["x-1", ""]
        },
        {
            "input": ["x*x*x+6*x*x+12*x+8", "x+2"],
            "answer": ["x*x+4*x+4", ""]
        },
        {
            "input": ["x*x*x*x*x+5*x+1", "x*x"],
            "answer": ["x*x*x", "5*x+1"]
        },
        {
            "input": ["x*x*x*x+x*x*x+x*x+x+1", "x+1"],
            "answer": ["x*x*x+x", "1"]
        },
        {
            "input": ["5*x*x-10*x+15", "x*x-2*x+3"],
            "answer": ["5", ""]
        },

        {
            "input": ["4*x*x-12*x+9", "2*x-3"],
            "answer": ["2*x-3", ""]
        },
        {
            "input": ["x*x+1", "x*x*x"],
            "answer": ["", "x*x+1"]
        },
        {
            "input": ["7*x*x*x*x*x-3*x*x*x+5*x", "x*x-3*x-9"],
            "answer": ["7*x*x*x+21*x*x+123*x+558", "2786*x+5022"]
        },
        {
            "input": ["x+1", "x-1"],
            "answer": ["1", "2"]
        },
        {
            "input": ["x-1", "x+1"],
            "answer": ["1", "-2"]
        }

    ],
    "Extra": [
        {
            "input": ["x*x*x-13*x*x-41", "x-3"],
            "answer": ["x*x-10*x-30", "-131"]
        },
        {
            "input": ["x*x-4", "x+2"],
            "answer": ["x-2", ""]
        },
        {
            "input": ["x*x*x+9*x*x+27*x+27", "x+3"],
            "answer": ["x*x+6*x+9", ""]
        },
        {
            "input": ["x*x*x*x*x+3*x+1", "x*x"],
            "answer": ["x*x*x", "3*x+1"]
        },
        {
            "input": ["2*x*x*x*x+2*x*x*x+2*x*x+2*x+2", "2*x+2"],
            "answer": ["x*x*x+x", "2"]
        },
        {
            "input": ["6*x*x-12*x+18", "x*x-2*x+3"],
            "answer": ["6", ""]
        },

        {
            "input": ["9*x*x-18*x+9", "3*x-3"],
            "answer": ["3*x-3", ""]
        },
        {
            "input": ["2*x*x+1", "x*x*x"],
            "answer": ["", "2*x*x+1"]
        },
        {
            "input": ["7*x*x*x*x*x-3*x*x*x+5*x", "x*x-3*x-9"],
            "answer": ["7*x*x*x+21*x*x+123*x+558","2786*x+5022"]
        },
        {
            "input": ["x+2", "x-1"],
            "answer": ["1", "3"]
        },
        {
            "input": ["x-1", "x+2"],
            "answer": ["1", "-3"]
        }

    ]
}
