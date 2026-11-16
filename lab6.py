#   # STEP 1: parse_course_record(course_string)
'''Takes a string of course data, sanitizes it, and returns the separated values as a dictionary.
Arguments:
course_string -- string representing a course taken

'''
# break string into a list 'tokens' with the .split method (delimiter: ',')
# using a for loop, clean up each item in tokens with .strip and .upper * (make sure to reassign!)
    # * ask professor whether these want to be formatted a specific way, or just be consistent across entries.
    #   just putting everything in caps is very convenient for a hypothetical program
    #   but it does require fully capitalizing the reference dictionary too - don't forget that bit
# convert credits (tokens[2]) into an integer
# create dictionary 'course' with keys 'code', 'name', 'credit', and 'status'
    # assign the contents of tokens as values, in index order (so 'code':[0], 'name':[1], etc)
# return course


#   # STEP 2: get_gen_ed_category(course_code, gen_ed_mapping)
'''Takes a course code and the Gen Ed category map, and returns the category that course belongs to.
Arguments:
course_code -- string representing the course code
gen_ed_mapping -- dict representing each Gen Ed category

'''
# write a for loop to iterate through the gen_ed_mapping keys
    # if the course_code is in the values of a key, then return that key
#else (loop end, so if the course_code doesn't match any of the categories), return "UNCATEGORIZED"


#   # STEP 3: audit_credits(student_bins)
'''takes student_bins and calculates total credits per Gen Ed category.
Arguments:
student-bins -- dict representing classes the student has taken in each Gen Ed category
'''
# initialize dict 'credit_totals' with all category keys plus 'UNCATEGORIZED', all with value 0 for now
# nested for loops: outer loop goes through 'key in student_bin'
    # inner loop goes through 'class in student_bin[key]' (to access the tuples)
    # increment credit_totals[key] by class[1] (credit_totals and student_bin have matching key sets)
# return credit_totals


#   # STEP 4: bin_student_courses(transcript, gen_ed_mapping)
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


# step 5 is below in main()


# MAIN FUNCTION
# master dictionary from the lab document, transformed to all caps for compatibility with the parse function:
'''
gen_ed_categories = {
"CREATIVITY AND INNOVATION": ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330"],
"COMMUNICATION AND EXPRESSION": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"],
"EQUITY, DIVERSITY, AND INCLUSION": ["ART-450", "ENG-214", "ES-220", "GSWS-312","MUS-205"],
"INQUIRY AND ANALYSIS": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482"],
"NUMERICAL LITERACY": ["CS-200", "MTH-111", "CS-346", "STAT-243Z"],
"PURPOSEFUL LEARNING": ["WR-121Z","WR-122Z", "WR-123"]
}
'''

#   # Step 1 Testing
# using the sample transcript from the doc
# call parse_course_record(x) and print the result for each of the strings below:
# "    MTH-111, Pre-calculus, 4, COMPLETED    "
# "  WR-121z, Composition I, 3, Completed   "
# "  WR-122z,  Composition II, 3, Incomplete   "
# "     GSWS-210, Violence Prevention, 4, completed"


#   # Step 2 Testing
# mapping dictionary from the doc is initialized at the top of main()
# hard-code some test values from the sample transcript, plus one that isn't in the dictionary
# test_values = ['MTH-111', 'WR-121Z', 'WR-122Z', 'GSWS-210', 'FAKE-100']
# for code in test_values: # much faster way to test all variables
    # call get_gen_ed_category(code, gen_ed_categories) and print the result


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


#   # Step 4 Testing
# define a sample transcript, 2 courses
# call bin_student_courses(sample, gen_ed_mapping)
# then add more courses and call again


#   # STEP 5: Final Pipeline Integration & Testing
# define a larger dictionary of courses for 'gen_ed_categories'
# define a 'transcript' tuple with messy course strings, including:
    # at least one completed course for every category plus one that belongs to neither
    # at least two completed courses in at least one category
    # at least one incomplete course
# call bin_student_courses(trancript, gen_ed_categories) and store the result in student_final_bins
    # and then print(student_final_bins) to check that it worked right
# call audit_credits(student_final_bins) and store the result in a variable
    # print that variable to check on it