#WAP for IOE Entrance system , that takes the details of the student 
#...,like previous degree(diploma,+2 science); if the criteria meets let them to 
#..appear the entrance exam.- Later, if the  student pass the entrance  exam
#Again, check whichb faculty the students
#....is eligible to  enroll & suggest by displaying  the options like (BEL, BCT, BEI & so on ).

#CODE<>///
# ============================================================
# Project: IOE Entrance Admission System
# Author : Your Name
# Language: Python
# Description:
# This program simulates a simple IOE admission system.
# It checks:
#   1. Previous qualification
#   2. Entrance exam score
#   3. IOE rank
# Finally, it displays the faculties the student is eligible
# to choose based on the obtained rank.
# ============================================================

print("=" * 55)
print("        WELCOME TO IOE ENTRANCE ADMISSION SYSTEM")
print("=" * 55)

# ---------------------------
# Student Information
# ---------------------------
name = input("Enter your full name: ")
degree = input("Enter your previous degree (+2science/Diploma): ")

print("\nChecking eligibility...\n")

# ------------------------------------------------------------
# Step 1: Verify Previous Qualification
# ------------------------------------------------------------
if degree == "+2science" or degree == "Diploma":

    print(" Eligible to appear in the IOE Entrance Examination.")

    # --------------------------------------------------------
    # Step 2: Check Entrance Exam Score
    # --------------------------------------------------------
    score = float(input("\nEnter your entrance exam score: "))
    cutoff_score = 46

    if score >= cutoff_score:

        print("\n Congratulations!")
        print("You have passed the entrance examination.")

        # ----------------------------------------------------
        # Step 3: Check IOE Rank
        # ----------------------------------------------------
        rank = int(input("\nEnter your IOE Rank: "))

        print("\n==========================================")
        print("Eligible Faculties")
        print("==========================================")

        # Rank 1 - 600
        if rank <= 600:
            print("Excellent Rank!")
            print("You are eligible for ALL faculties.\n")
            print("1. BCT  - Computer Engineering")
            print("2. BEI  - Electronics, Communication & Information Engineering")
            print("3. BCE  - Civil Engineering")
            print("4. BEL  - Electrical Engineering")
            print("5. BME  - Mechanical Engineering")
            print("6. BGE  - Geomatics Engineering")

        # Rank 601 - 1600
        elif rank <= 1600:
            print("You are eligible for:\n")
            print("1. BEI  - Electronics, Communication & Information Engineering")
            print("2. BCE  - Civil Engineering")
            print("3. BEL  - Electrical Engineering")
            print("4. BME  - Mechanical Engineering")
            print("5. BGE  - Geomatics Engineering")

        # Rank 1601 - 2500
        elif rank <= 2500:
            print("You are eligible for:\n")
            print("1. BCE  - Civil Engineering")
            print("2. BEL  - Electrical Engineering")
            print("3. BME  - Mechanical Engineering")
            print("4. BGE  - Geomatics Engineering")

        # Rank 2501 - 3000
        elif rank <= 3000:
            print("You are eligible for:\n")
            print("1. BEL  - Electrical Engineering")
            print("2. BME  - Mechanical Engineering")
            print("3. BGE  - Geomatics Engineering")

        # Rank 3001 - 3600
        elif rank <= 3600:
            print("You are eligible for:\n")
            print("1. BME  - Mechanical Engineering")
            print("2. BGE  - Geomatics Engineering")

        # Rank 3601 - 6000
        elif rank <= 6000:
            print("You are eligible for:\n")
            print("1. BGE  - Geomatics Engineering")

        # Rank above 6000
        else:
            print("Sorry!")
            print("Your rank does not qualify for the listed faculties.")

    else:
        print("\n Sorry!")
        print("Your entrance score is below the minimum cutoff.")
        print("Minimum Required Score:", cutoff_score)

else:
    print(" Sorry!")
    print("Only students with +2 Science or Diploma are eligible.")

print("\n==========================================")
print("Thank you for using the IOE Admission System.")
print("Best of Luck for your Future!")
print("==========================================")
