import sqlite3

connection = sqlite3.connect("campusassist.db")

cursor = connection.cursor()

# Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT UNIQUE,
    name TEXT,
    department TEXT,
    year TEXT,
    email TEXT,
    password TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO students
(student_id, name, department, year, email, password)
VALUES
(
    'STU001',
    'Student Name',
    'Computer Science',
    '2nd Year',
    'student@campusassist.com',
    '1234'
)
""")

# Faculty table
cursor.execute("""
CREATE TABLE IF NOT EXISTS faculty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_id TEXT UNIQUE,
    name TEXT,
    department TEXT,
    designation TEXT,
    email TEXT,
    password TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO faculty
(faculty_id, name, department, designation, email, password)
VALUES
(
    'FAC001',
    'Faculty Name',
    'Computer Science',
    'Assistant Professor',
    'faculty@campusassist.com',
    '1234'
)
""")

# Assignments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    subject TEXT,
    due_date TEXT,
    status TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO assignments
(id, title, subject, due_date, status)
VALUES
(
    1,
    'Web Development Project',
    'Web Development',
    '08 October 2026',
    'Pending'
)
""")

cursor.execute("""
INSERT OR IGNORE INTO assignments
(id, title, subject, due_date, status)
VALUES
(
    2,
    'Python Programming',
    'Python Programming',
    '12 October 2026',
    'Pending'
)
""")

cursor.execute("""
INSERT OR IGNORE INTO assignments
(id, title, subject, due_date, status)
VALUES
(
    3,
    'Database Assignment',
    'Database Management',
    '15 October 2026',
    'Not Started'
)
""")

cursor.execute("""
INSERT OR IGNORE INTO assignments
(id, title, subject, due_date, status)
VALUES
(
    4,
    'AI Mini Project',
    'Artificial Intelligence',
    '18 October 2026',
    'Pending'
)
""")

# Announcements table
cursor.execute("""
CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    date TEXT,
    description TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO announcements
(id, title, date, description)
VALUES
(
    1,
    'Internal Examination',
    '05 October 2026',
    'Internal examination schedule has been announced.'
)
""")

cursor.execute("""
INSERT OR IGNORE INTO announcements
(id, title, date, description)
VALUES
(
    2,
    'Web Development Workshop',
    '10 October 2026',
    'A workshop on modern web development will be conducted.'
)
""")

cursor.execute("""
INSERT OR IGNORE INTO announcements
(id, title, date, description)
VALUES
(
    3,
    'Campus Event',
    '20 October 2026',
    'Annual campus event will be conducted on campus.'
)
""")

cursor.execute("""
INSERT OR IGNORE INTO announcements
(id, title, date, description)
VALUES
(
    4,
    'Assignment Submission',
    '25 October 2026',
    'Students must complete and submit their assignments.'
)
""")

# Timetable table
cursor.execute("""
CREATE TABLE IF NOT EXISTS timetable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    time TEXT,
    subject TEXT
)
""")

# Sample timetable
timetable_data = [
    ("Monday", "9:00 - 10:00", "Python Programming"),
    ("Monday", "10:00 - 11:00", "Database Management"),
    ("Monday", "11:15 - 12:15", "Web Development"),
    ("Monday", "1:00 - 2:00", "Artificial Intelligence"),

    ("Tuesday", "9:00 - 10:00", "Database Management"),
    ("Tuesday", "10:00 - 11:00", "Python Programming"),
    ("Tuesday", "11:15 - 12:15", "Artificial Intelligence"),
    ("Tuesday", "1:00 - 2:00", "Web Development"),

    ("Wednesday", "9:00 - 10:00", "Web Development"),
    ("Wednesday", "10:00 - 11:00", "Artificial Intelligence"),
    ("Wednesday", "11:15 - 12:15", "Python Programming"),
    ("Wednesday", "1:00 - 2:00", "Database Management"),

    ("Thursday", "9:00 - 10:00", "Artificial Intelligence"),
    ("Thursday", "10:00 - 11:00", "Web Development"),
    ("Thursday", "11:15 - 12:15", "Database Management"),
    ("Thursday", "1:00 - 2:00", "Python Programming"),

    ("Friday", "9:00 - 10:00", "Python Programming"),
    ("Friday", "10:00 - 11:00", "Web Development"),
    ("Friday", "11:15 - 12:15", "Artificial Intelligence"),
    ("Friday", "1:00 - 2:00", "Database Management")
]

for day, time, subject in timetable_data:
    cursor.execute("""
    INSERT OR IGNORE INTO timetable
    (day, time, subject)
    VALUES (?, ?, ?)
    """, (day, time, subject))

connection.commit()
connection.close()

print("Student, Faculty, Assignments, Announcements and Timetable database created successfully!")