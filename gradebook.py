#kabir's grades fall22-spring23

# Fall Term 2022 data
fall22_gradebook = [
    ["BAEP-472: The Science of Peak Performance", "A-"],
    ["IR-101xgw: International Relations", "A"],
    ["ENGL-176g: Los Angeles: the City, the Novel, the Movie", "A"],
    ["BAEP-473: Sales Mindset for Entrepreneurs", "A"],
    ["BUAD-310g: Applied Business Statistics", "A"],
    ["ACAD-177: Digital Toolbox: Design", "A-"]
]

# Spring Term 2023 data
spring23_gradebook = [
    ["WRIT-340: Advanced Writing", "A"],
    ["ACAD-309g: Dreams and Madness: The Art of Japan's Golden Age of Animation", "A"],
    ["BUAD-311: Operations Management", "B+"],
    ["BAEP-469: Growth Hacking: Scaling Startups", "A-"]
]

# Adding new subject and grades
spring23_gradebook.append(["BAEP499: Blockchain Entrepreneurship", "Fail"])  # Initial grade before making it pass

# Adjusting grades for "BAEP499: Blockchain Entrepreneurship" to "Pass"
for course in spring23_gradebook:
    if course[0] == "BAEP499: Blockchain Entrepreneurship":
        course[1] = "Pass"
        break

# Display Fall Term 2022 gradebook
print("Fall Term 2022 Gradebook:")
print(fall22_gradebook)
print()  

# Display Spring Term 2023 gradebook
print("Spring Term 2023 Gradebook:")
print(spring23_gradebook)
print()  

# Combine Fall22 gradebook and Spring Term 2023 gradebooks
full_gradebook = fall22_gradebook + spring23_gradebook

# Display full gradebook
print("Full Gradebook:")
print(full_gradebook)
