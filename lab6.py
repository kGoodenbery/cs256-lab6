#   # STEP 1
def parse_course_record(course_string):
    '''Takes a string of course data, sanitizes it, and returns the separated values as a dictionary.
    Arguments:
    course_string -- string representing a course taken

    '''
    # break string into a list 'tokens' with the .split method (delimiter: ',')
    # using a for loop, clean up each item in tokens with .strip and .upper * (make sure to reassign!)
        # * ask professor whether these want to be formatted a specific way, or just be consistent across entries.
        #   just putting everything in caps is very convenient for a hypothetical program
        #   but it does require fully capitalizing the reference dictionary too - don't forget that bit
        # oh actually is it only the status that needs standardized? does this program assume the rest is computer-entered or smth?
    # convert credits (tokens[2]) into an integer
    # create dictionary 'course' with keys 'code', 'name', 'credit', and 'status'
        # assign the contents of tokens as values, in index order (so 'code':[0], 'name':[1], etc)
    # return course
    # testing defined in main
    pass


#   # STEP 2
def get_gen_ed_category(course_code, gen_ed_mapping):
    '''Takes a course code and the Gen Ed category map, and returns the category that course belongs to.
    Arguments:
    course_code -- string representing the course code
    gen_ed_mapping -- dict representing each Gen Ed category

    '''
    # write a for loop to iterate through the gen_ed_mapping keys
        # if the course_code is in the values of a key, then return that key
    #else (loop end, so if the course_code doesn't match any of the categories), return "UNCATEGORIZED"
    # testing detailed in main
    pass


#   # STEP 3
def audit_credits(student_bins):
    '''takes student_bins and calculates total credits per Gen Ed category.
    Arguments:
    student-bins -- dict representing classes the student has taken in each Gen Ed category
    '''
    # initialize dict 'credit_totals' with all category keys plus 'UNCATEGORIZED', all with value 0 for now
    # nested for loops: outer loop goes through 'key in student_bin'
        # inner loop goes through 'class in student_bin[key]' (to access the tuples)
        # increment credit_totals[key] by class[1] (credit_totals and student_bin have matching key sets)
    # return credit_totals
    # testing detailed in main
    pass


#   # STEP 4
def bin_student_courses(transcript, gen_ed_mapping):
    '''Takes a student transcript, sorts completed courses into their Gen Ed categories, and returns a
    dictionary of category keys and (code, credit) tuples
    Arguments:
    transcript -- tuple of (messy) strings
    gen_ed_mapping -- dict of gen ed categories and the classes that belong to them

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
    # master dictionary from the lab document, transformed to all caps for compatibility with the parse function:
    sample_categories = {
    "CREATIVITY AND INNOVATION": ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330"],
    "COMMUNICATION AND EXPRESSION": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"],
    "EQUITY, DIVERSITY, AND INCLUSION": ["ART-450", "ENG-214", "ES-220", "GSWS-312","MUS-205"],
    "INQUIRY AND ANALYSIS": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482"],
    "NUMERICAL LITERACY": ["CS-200", "MTH-111", "CS-346", "STAT-243Z"],
    "PURPOSEFUL LEARNING": ["WR-121Z","WR-122Z", "WR-123"]
    }
    

    #   # Step 1 Testing
    # using the sample transcript from the doc
    # call parse_course_record() and print the result using each of the strings below as the argument:
    # print(parse_course_record("    MTH-111, Pre-calculus, 4, COMPLETED    "))
    # print(parse_course_record("  WR-121z, Composition I, 3, Completed   "))
    # print(parse_course_record("  WR-122z,  Composition II, 3, Incomplete   "))
    # print(parse_course_record("     GSWS-210, Violence Prevention, 4, completed"))
    # do i need to list expected outcomes for this? expected outcomes are just "the string but a dict now, and cleaner"


    #   # Step 2 Testing
    # mapping dictionary from the doc is initialized at the top of main
    # hard-code some test values from the sample transcript, plus one that isn't in the dictionary
    # test_values = ['MTH-111', 'WR-121Z', 'WR-122Z', 'GSWS-210', 'FAKE-100']
    # for code in test_values: # much faster way to test each variable
    #     print(get_gen_ed_category(code, sample_categories))
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
    "CREATIVITY AND INNOVATION": ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330",
                                  "COMM-222", "CS-210", "ES-327", "SPAN-319", "TA-220"],
    "COMMUNICATION AND EXPRESSION": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311",
                                     "COMM-214", "COMM-330", "CS-310", "DCIN-200", "EMDA-202"],
    "EQUITY, DIVERSITY, AND INCLUSION": ["ART-450", "ENG-214", "ES-220", "GSWS-312","MUS-205",
                                         "BI-468", "CCJ-231", "COMM-200", "GSWS-222", "MUS-206"],
    "INQUIRY AND ANALYSIS": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482",
                             "ARTH-346", "BA-483", "DCIN-201", "DCIN-362", "EMDA-250"],
    "NUMERICAL LITERACY": ["CS-200", "MTH-111", "CS-346", "STAT-243Z", "BA-218", "CS-346", "ES-101", "MTH-212"],
    "PURPOSEFUL LEARNING": ["WR-121Z","WR-122Z", "WR-123"] # oh thats literally all the PL classes
    }
    # define a 'transcript' tuple with messy course strings, including:
        # at least one completed course for every category plus one that belongs to none of them
        # at least two completed courses in at least one category
        # at least one incomplete course
        # im just gonna make them all worth 5 credits for ease of testing. and i dont feel like looking up the class names rn
        # lmk if you want me to test it with actual names when i write the code but imma just name em by their category
    transcript = (" ART-133, creativity+innovation 1, 5, completed", "eng-105,  creativity+innovation 2, 5, incomplete",
                  "   BI-130, comm+expression 1, 5, Completed    ", "  ES-220, equ+div+incl 1,  5, completed  ",
                  "CS-200, numerical literacy 1  , 5, cOMPLETED ", "   DCIN-201, inquiry+analysis 1, 5, COMPLETED",
                  "WR-121z, purposeful learning 1, completed", "WR-121Z, purposeful learning 2, 5, comPLETed",
                  "Fake-101, UC, 5, complete") # okay thats one per category plus one that isnt, 2 in PL, and an incomplete in CI
    # call bin_student_courses(trancript, gen_ed_categories) and store the result in student_final_bins
        # print(student_final_bins) to check that it worked right
    # call audit_credits(student_final_bins) and store the result in a variable
        # print that variable to check on it
pass