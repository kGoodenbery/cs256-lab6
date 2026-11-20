#   # STEP 1
def parse_course_record(course_string):
    ''' Cleans up course data, splits it into four tokens, and converts the 'credit' token to integer.

    Parameters:
      course_string (str)

    Returns:
      course (dict): maps labels (str) to tokens (str, int)
    '''

    # break string into a list 'tokens' with the .split method (delimiter: ',')
    tokens = course_string.split(',')
    # using a for loop, clean up each item in tokens with .strip and .upper (make sure to reassign!)
        # make sure to also capitalize the Zs in the course codes in gen_ed_categories
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip().upper()
    # convert credits (tokens[2]) into an integer
    tokens[2] = int(tokens[2])
    # create dictionary 'course' with keys 'code', 'name', 'credit', and 'status'
        # assign the contents of tokens as values, in index order (so 'code':[0], 'name':[1], etc)
    course = {'code':tokens[0], 'name':tokens[1], 'credit':tokens[2], 'status':tokens[3]}
    # return course
    return course
# testing detailed in main


#   # STEP 2
def get_gen_ed_category(course_code, gen_ed_mapping):
    ''' Finds what Gen Ed category a course belongs to.

    Parameters:
      course_code (str),
      gen_ed_mapping (dict):
        - Keys: category names (str)
        - Values: list of strings

    Returns:
      category (str)
    '''

    # have to initialize category
    category = ""
    # write a for loop to iterate through the gen_ed_mapping keys
    for key in gen_ed_mapping:
        # if the course_code is in the values of a key, assign 'category' with that key
        if course_code in gen_ed_mapping[key]:
            category = key
    #if category is still unassigned, assign "uncategorized"
    if category == "":
        category = 'Uncategorized'
    
    return category
# testing detailed in main


#   # STEP 3
def audit_credits(student_bins):
    ''' Calculates total credits per Gen Ed category.

    Parameters:
      student_bins (dict):
        - Keys: category name (str),
        - Values: list of tuples (course_code: str, credits: int)

    Returns:
      totals (dict): maps category names (str) to total credits (int)
    '''
    # this docstring is a direct copy of the example in the 11/17 slides. i liked it a lot so im using it as a framework

    # initialize dict 'totals' with all category keys plus 'UNCATEGORIZED', all with value 0 for now
    totals = {
    "Creativity and Innovation": 0,
    "Communication and Expression": 0,
    "Equity, Diversity, and Inclusion": 0,
    "Inquiry and Analysis": 0,
    "Numerical Literacy": 0,
    "Purposeful Learning": 0,
    "Uncategorized": 0
    }
    # nested for loops: outer loop goes through 'key in student_bin'
        # inner loop goes through 'class in student_bin[key]' (to access the tuples)
        # increment credit_totals[key] by class[1] (totals and student_bin have matching key sets)
    # return totals
    # testing detailed in main
    pass


#   # STEP 4
def bin_student_courses(transcript, gen_ed_mapping):
    ''' Parses a student transcript and sorts completed courses into their Gen Ed categories.
    
    Parameters:
      transcript (tuple of strings),
      gen_ed_mapping (dict):
        - Keys: category names (str)
        - Values: list of strings
    
    Returns:
      bins (dict): with Gen Ed categories as keys, and lists of (code, credit) tuples for values
        - Keys: category names (str)
        - Values: lists of tuples (code: str, credit: int)
    '''

    # initialize dictionary 'bins' with empty lists for all categories + "UNCATEGORIZED"
    # loop over transcript - for course in transcript:
        # call parse_course_records(course), assign to 'record'
        # call get_gen_ed_category(record[code], gen_ed_mapping), assign to 'category'
        # if record['status'] == 'COMPLETED', append (record['code'], record['credits']) tuple to bins[category]
    # return bins
    # testing detailed in main
    pass


# step 5 is below in main()


# MAIN FUNCTION
def main():
    # sample dictionary from the lab document, for initial testing of get_gen_ed_category and bin_student_courses
    sample_categories = {
    "Creativity and Innovation": ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330"],
    "Communication and Expression": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"],
    "Equity, Diversity, and Inclusion": ["ART-450", "ENG-214", "ES-220", "GSWS-312","MUS-205"],
    "Inquiry and Analysis": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482"],
    "Numerical Literacy": ["CS-200", "MTH-111", "CS-346", "STAT-243Z"],
    "Purposeful Learning": ["WR-121Z","WR-122Z", "WR-123"]
    }
    

    #   # Step 1 Testing
    # using the sample transcript from the doc
    # call parse_course_record() and print the result using each of the strings below as the argument:
    # print(parse_course_record("    MTH-111, Pre-calculus, 4, COMPLETED    "))
    # print(parse_course_record("  WR-121z, Composition I, 3, Completed   "))
    # print(parse_course_record("  WR-122z,  Composition II, 3, Incomplete   "))
    # print(parse_course_record("     GSWS-210, Violence Prevention, 4, completed"))
    # decided to write out expected outcomes in the doc instead of the code


    #   # Step 2 Testing
    # mapping dictionary from the doc is initialized at the top of main
    # hard-code some test values from the sample transcript, plus one that isn't in the dictionary
    test_values = ['MTH-111', 'WR-121Z', 'WR-122Z', 'GSWS-210', 'MUS-101']
    for code in test_values: # much faster way to test each variable
        print(get_gen_ed_category(code, sample_categories))
    # expected results, in order: Numerical Literacy, Purposeful Learning, PL again, Creativity+Innovation, Uncategorized


    #   # Step 3 Testing
    # student_bins = { # hard-coded sample, pared down from the sample category dict
    # "CREATIVITY AND INNOVATION": [("ART-133", 2), ("MUS-330", 4)],
    # "COMMUNICATION AND EXPRESSION": [("ARTH-204", 3)],
    # "EQUITY, DIVERSITY, AND INCLUSION": [("GSWS-312", 4)],
    # "INQUIRY AND ANALYSIS": [("ENG-280", 2), ("COMM-482", 4)],
    # "NUMERICAL LITERACY": [("CS-200", 4), ("CS-346", 4)],
    # "PURPOSEFUL LEARNING": [("WR-121Z", 4)],
    # "UNCATEGORIZED": [("CS-210", 2)]
    # }
    # call audit_credits(student_bins)
    # expected results: CI:6, CE:3, EDI:4, IA:6, NL:8, PL:4, UC:2


    #   # Step 4 Testing
    # define a sample transcript, 2 courses
    # sample_transcript = [("ART-291", 4), ("ES-200", 2)]
    # call bin_student_courses(sample_transcript, sample_categories) and print the result
    # expected results: {CI: (ART-291, 4), EDI:("ES-200", 2), other cats empty}
    # then add more courses and call again:
    # sample_transcript [("ART-291", 4), ("ES-200", 2), ("ARTH-204", 4), ("CS-200", 2), ("ENG-214", 4), ("ENG-105", 2), ("BI-101", 2), ("WR-123", 4)]
    # ill just check this one against the dictionary when i run it, im too zapped to do it now


    #   # STEP 5: Final Pipeline Integration & Testing
    # define a larger dictionary of courses for 'gen_ed_categories'. (ill add another 4, 5 classes per category? should do for now)
    extended_categories = {
    "Creativity and Innovation": ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330",
                                  "COMM-222", "CS-210", "ES-327", "SPAN-319", "TA-220"],
    "Communication and Expression": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311",
                                     "COMM-214", "COMM-330", "CS-310", "DCIN-200", "EMDA-202"],
    "Equity, Diversity, and Inclusion": ["ART-450", "ENG-214", "ES-220", "GSWS-312","MUS-205",
                                         "BI-468", "CCJ-231", "COMM-200", "GSWS-222", "MUS-206"],
    "Inquiry and Analysis": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482",
                             "ARTH-346", "BA-483", "DCIN-201", "DCIN-362", "EMDA-250"],
    "Numerical Literacy": ["CS-200", "MTH-111", "CS-346", "STAT-243Z", "BA-218", "CS-346", "ES-101", "MTH-212"],
    "Purposeful Learning": ["WR-121Z","WR-122Z", "WR-123"] # oh thats literally all the PL classes
    }
    # define a 'transcript' tuple with messy course strings, including:
        # im just gonna make them all worth 5 credits for ease of testing. and i dont feel like looking up the class names rn
        # lmk if you want me to test it with actual names when i write the code but imma just name em by their category
    
    transcript = (" ART-133, creativity+innovation 1, 4, completed", "eng-105,  creativity+innovation 2, 4, incomplete",
                  "   BI-130, comm+expression 1, 4, Completed    ", "  ES-220, equ+div+incl 1,  4, completed  ",
                  "CS-200, numerical literacy 1  , 4, cOMPLETED ", "   DCIN-201, inquiry+analysis 1, 4, COMPLETED",
                  "WR-121z, purposeful learning 1, 4, Completed", "WR-121Z, purposeful learning 2, 4, comPLETed",
                  "Fake-101, UC, 5, complete") # okay thats one per category plus one that isnt, 2 in PL, and an incomplete in CI
    
    # call bin_student_courses(trancript, gen_ed_categories) and store the result in student_final_bins
        # print(student_final_bins) to check that it worked right
    # call audit_credits(student_final_bins) and store the result in a variable
        # print that variable to check on it

print()
main()
print()