from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Sample student data
students = [
    {'name': 'John Doe', 'major': 'Chemistry', 'year': 2023, 'GPA': 3.5, 'marks': 15},
    {'name': 'Jane Smith', 'major': 'Physics', 'year': 2023, 'GPA': 3.8, 'marks': 80},
    {'name': 'Mike Johnson', 'major': 'Mathematics', 'year': 2022, 'GPA': 3.2, 'marks': 35},
    {'name': 'Sarah Brown', 'major': 'Computer Science', 'year': 2024, 'GPA': 3.9, 'marks': 85},
    {'name': 'David Lee', 'major': 'Chemistry', 'year': 2023, 'GPA': 3.6, 'marks': 28},
    {'name': 'Emily Wilson', 'major': 'Physics', 'year': 2022, 'GPA': 3.4, 'marks': 70},
    {'name': 'Chris Carter', 'major': 'Computer Science', 'year': 2023, 'GPA': 3.7, 'marks': 82},
    {'name': 'Lisa Davis', 'major': 'Mathematics', 'year':2024, 'GPA': 3.5, 'marks': 75},
    {'name': 'Alex Martin', 'major': 'Computer Science', 'year': 2022, 'GPA': 3.1, 'marks': 30},
    {'name': 'Sophia Anderson', 'major': 'Physics', 'year': 2021, 'GPA': 3.9, 'marks': 88}
]

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/filter', methods=['POST'])
def filter_students():
    data = request.get_json()
    filter_by = data['filter_by']

    if filter_by == 'min_marks':
        filtered_students = [student for student in students if student['marks'] < 40]
    elif filter_by == 'max_marks':
        filtered_students = [student for student in students if student['marks'] > 41]
    elif filter_by == 'all':
        filtered_students = students
    elif filter_by == 'major':
        major = data.get('filter_value', '') 
        filtered_students = [student for student in students if student['major'] == major]
    elif filter_by == 'year':
        year = data.get('filter_value', '') 
        if year:
            filtered_students = [student for student in students if student['year'] == int(year)]
        else:
            filtered_students = students
    elif filter_by == 'gpa_range':
        min_gpa = data.get('filter_value', {}).get('min_gpa', '') 
        max_gpa = data.get('filter_value', {}).get('max_gpa', '') 
        try:
            min_gpa = float(min_gpa)
            max_gpa = float(max_gpa)
        except ValueError:
            min_gpa = max_gpa = 0
        filtered_students = [student for student in students if min_gpa <= student['GPA'] <= max_gpa]
    else:
        filtered_students = students

    return jsonify(filtered_students)

@app.route('/get_all_students', methods=['GET'])
def get_all_students():
    return jsonify(students)


if __name__ == '__main__':
    app.run(debug=True)
