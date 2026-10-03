from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_student():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        ("STU001",)
    )

    student = cursor.fetchone()
    connection.close()

    return student


def get_faculty():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM faculty WHERE faculty_id = ?",
        ("FAC001",)
    )

    faculty = cursor.fetchone()
    connection.close()

    return faculty


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/student-login", methods=["GET", "POST"])
def student_login():
    if request.method == "POST":
        student_id = request.form["studentId"]
        password = request.form["password"]

        connection = sqlite3.connect("campusassist.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id = ? AND password = ?",
            (student_id, password)
        )

        student = cursor.fetchone()
        connection.close()

        if student:
            return redirect("/student-dashboard")

        return render_template(
            "student_login.html",
            error="❌ Invalid Student ID or Password"
        )

    return render_template("student_login.html")


@app.route("/student-dashboard")
def student_dashboard():
    return render_template("student_dashboard.html")


@app.route("/courses")
def courses():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    connection.close()

    return render_template(
        "courses.html",
        courses=courses
    )


@app.route("/timetable")
def timetable():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM timetable ORDER BY id")
    timetable = cursor.fetchall()

    connection.close()

    return render_template(
        "timetable.html",
        timetable=timetable
    )


@app.route("/announcements")
def announcements():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM announcements")
    announcements = cursor.fetchall()

    connection.close()

    return render_template(
        "announcements.html",
        announcements=announcements
    )


@app.route("/assignments")
def assignments():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM assignments")
    assignments = cursor.fetchall()

    connection.close()

    return render_template(
        "assignments.html",
        assignments=assignments
    )


@app.route("/profile")
def profile():
    student = get_student()
    return render_template(
        "profile.html",
        student=student
    )


@app.route("/faculty-login")
def faculty_login():
    return render_template("faculty_login.html")


@app.route("/faculty-dashboard")
def faculty_dashboard():
    return render_template("faculty_dashboard.html")


@app.route("/students")
def students():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return render_template(
        "students.html",
        students=students
    )


@app.route("/faculty-courses")
def faculty_courses():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    connection.close()

    return render_template(
        "faculty_course.html",
        courses=courses
    )


@app.route("/add-course", methods=["POST"])
def add_course():
    course_name = request.form["course_name"]
    instructor = request.form["instructor"]
    credits = request.form["credits"]

    connection = sqlite3.connect("campusassist.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO courses
        (course_name, instructor, credits)
        VALUES (?, ?, ?)
        """,
        (course_name, instructor, credits)
    )

    connection.commit()
    connection.close()

    return redirect("/faculty-courses")


@app.route("/faculty-assignments")
def faculty_assignments():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM assignments")
    assignments = cursor.fetchall()

    connection.close()

    return render_template(
        "faculty_assignments.html",
        assignments=assignments
    )


@app.route("/add-assignment", methods=["POST"])
def add_assignment():
    title = request.form["title"]
    subject = request.form["subject"]
    due_date = request.form["due_date"]

    connection = sqlite3.connect("campusassist.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO assignments
        (title, subject, due_date, status)
        VALUES (?, ?, ?, ?)
        """,
        (title, subject, due_date, "Active")
    )

    connection.commit()
    connection.close()

    return redirect("/faculty-assignments")


@app.route("/faculty-announcements")
def faculty_announcements():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM announcements")
    announcements = cursor.fetchall()

    connection.close()

    return render_template(
        "faculty_announcements.html",
        announcements=announcements
    )


@app.route("/add-announcement", methods=["POST"])
def add_announcement():
    title = request.form["title"]
    date = request.form["date"]
    description = request.form["description"]

    connection = sqlite3.connect("campusassist.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO announcements
        (title, date, description)
        VALUES (?, ?, ?)
        """,
        (title, date, description)
    )

    connection.commit()
    connection.close()

    return redirect("/faculty-announcements")


@app.route("/faculty-timetable")
def faculty_timetable():
    connection = sqlite3.connect("campusassist.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM timetable ORDER BY id")
    timetable = cursor.fetchall()

    connection.close()

    return render_template(
        "faculty_timetable.html",
        timetable=timetable
    )


@app.route("/faculty-profile")
def faculty_profile():
    faculty = get_faculty()

    return render_template(
        "faculty_profile.html",
        faculty=faculty
    )


@app.route("/campus-info")
def campus_info():
    return render_template("campus_info.html")


@app.route("/student-data")
def student_data():
    student = get_student()

    if student:
        return f"""
        <h1>Student Database</h1>
        <p>Student ID: {student['student_id']}</p>
        <p>Name: {student['name']}</p>
        <p>Department: {student['department']}</p>
        <p>Year: {student['year']}</p>
        <p>Email: {student['email']}</p>
        """
    else:
        return "<h1>Student not found</h1>"


if __name__ == "__main__":
    app.run(debug=True)