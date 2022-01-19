students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# How many students are there?
print(f"The number of students is {len(students)}")
# How many students prefer light coffee? For each type of coffee roast?
coffee_preferences= [student["coffee_preference"] for student in students]
coffee_freq = {}
for coffee_p in coffee_preferences:
    if coffee_p in coffee_freq:
        coffee_freq[coffee_p]+=1
    else:
        coffee_freq[coffee_p]=1

print(f"Coffee preferences: {coffee_freq}")
# How many types of each pet are there?
pets = len(set([student['pets'][0]['species'] for student in students if len(student['pets'])>0]))
print(f"The number of pets is {pets}")
# How many grades does each student have? Do they all have the same number of grades?
num_grades = {student['student']:len(student['grades']) for student in students}
print(f"The students have the following number of grades each: {num_grades}")
if len(set(num_grades.values()))>1:
    print("Not all students have the same number of grades")
else:
    print("All students have the same number of grades")
# What is each student's grade average?
avg_grades = {student['student']:sum((student['grades']))/len((student['grades'])) for student in students}
# How many pets does each student have?
num_pets = {student['student']:len(student['pets']) for student in students}
# How many students are in web development? data science?
class_info = [student['course'] for student in students]
web_dev = len([x for x in class_info if x == 'web development'])
data_science = len([x for x in class_info if x == 'data science'])
print(f"{web_dev} students are in web development, {data_science} are in data science")
# What is the average number of pets for students in web development?
num_pets = {student['student']:len(student['pets']) for student in students if student['course']=='web development'}
avg_num_pets = sum(num_pets.values())/len(num_pets)
print(f" The average number of pets for students in web development is {avg_num_pets}")
# What is the average pet age for students in data science?
pet_data = [student['pets'] for student in students if student['course']=='data science']
pet_ages = [pet['age'] for ind_pet in pet_data for pet in ind_pet]
avg_pet_age = sum(pet_ages)/len(pet_ages)
print(f"Average age of pet for students in data science is {avg_pet_age}")
# What is most frequent coffee preference for data science students?
coffee_preferences= [student["coffee_preference"] for student in students if student['course']=='data science']
coffee_freq = {}
for coffee_p in coffee_preferences:
    if coffee_p in coffee_freq:
        coffee_freq[coffee_p]+=1
    else:
        coffee_freq[coffee_p]=1
print(f"Most frequent coffee preferences for data science students: {max(coffee_freq)}")
# What is the least frequent coffee preference for web development students?
coffee_preferences= [student["coffee_preference"] for student in students if student['course']=='web development']
coffee_freq = {}
for coffee_p in coffee_preferences:
    if coffee_p in coffee_freq:
        coffee_freq[coffee_p]+=1
    else:
        coffee_freq[coffee_p]=1
print(f"Least frequent coffee preferences for web development students: {min(coffee_freq)}")
# What is the average grade for students with at least 2 pets?
grades = [student["grades"] for student in students if len(student['pets'])>=2]
avg_grade=sum(sum(grades,[]))/len(sum(grades,[]))
print(f"Average grade of a student with at least 2 pets: {avg_grade}")
# How many students have 3 pets?
students_w_3 = len([student for student in students if len(student['pets'])==3])
print(f"{students_w_3} student(s) have 3 pets")
# What is the average grade for students with 0 pets?
grades = [student["grades"] for student in students if len(student['pets'])==0]
avg_grade=sum(sum(grades,[]))/len(sum(grades,[]))
print(f"Average grade of a student with 0 pets: {avg_grade}")
# What is the average grade for web development students? data science students?
wd_grades = [student["grades"] for student in students if student["course"]=='web development']
wd_avg_grade=sum(sum(wd_grades,[]))/len(sum(wd_grades,[]))
print(f"Average grade of a web development student: {wd_avg_grade}")

ds_grades = [student["grades"] for student in students if student["course"]=='data science']
ds_avg_grade=sum(sum(ds_grades,[]))/len(sum(ds_grades,[]))
print(f"Average grade of a data science student: {ds_avg_grade}")

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
dc_grades = [student["grades"] for student in students if student["coffee_preference"]=='dark']
avg_dc_grades = [sum(ind_grades)/len(ind_grades) for ind_grades in dc_grades]
print(f"Dark coffee drinkers have average grades in the following range: {min(avg_dc_grades)} - {max(avg_dc_grades)}")

# What is the average number of pets for medium coffee drinkers?

num_pets = {student['student']:len(student['pets']) for student in students if student['coffee_preference']=='medium'}
avg_num_pets = sum(num_pets.values())/len(num_pets)
print(f" The average number of pets for students who drink medium coffee is {avg_num_pets}")
# What is the most common type of pet for web development students?

pets = [student["pets"] for student in students if student['course']=='web development']
pet_species = [pet[0]["species"] for pet in pets]

pet_type_freq = {}
for pet_t in pet_species:
    if pet_t in pet_type_freq:
        pet_type_freq[pet_t]+=1
    else:
        pet_type_freq[pet_t]=1

print(f"Types of pet for web development students: {pet_type_freq}")

# What is the average name length?

name_length = [len(student["student"]) for student in students]
avg_name_length = sum(name_length)/len(name_length)
print(f"The average name length is {avg_name_length} characters")

# What is the highest pet age for light coffee drinkers?

pet_data = [student['pets'] for student in students if student['coffee_preference']=='light']
pet_ages = [pet['age'] for ind_pet in pet_data for pet in ind_pet]

print(f"Highest pet age for light coffee drinkers is {max(pet_ages)}")