# Sana - School Student Information System
Recognition: The Sana project was awarded the best project of the term for its comprehensive analysis and implementation.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centered Image</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full viewport height */
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://github.com/user-attachments/assets/92ea27d5-d3e7-4443-835a-93e3650c46ba" alt="description" width="400">
    </div>
</body>
</html>


## Project Overview
Sana is a web-based system designed to help educational institutions manage student discipline records effectively. This system allows administrators to register students, document disciplinary actions, and generate comprehensive reports on student behavior. Sana was created to improve the discipline management process in schools, making it easier for administrators to track and address disciplinary issues.

The project was developed as part of the Systems Analysis and Design course under the guidance of Dr. Mahdieh Ghazvini. The project was recognized as the best project of the term, praised for its thorough software analysis and intuitive design.

## Features
Student Registration: Easily register and manage student information.
Discipline Management: Record and track disciplinary actions taken against students.
Report Generation: Generate detailed reports on disciplinary activities.
User-Friendly Interface: Navigate the system with ease thanks to an intuitive design.
Responsive Design: Access the system from any device, thanks to its responsive front-end design.

## Installation
To get started with Sana, follow these steps:

Clone the repository:
            <pre><code>git clone https://github.com/yourusername/sana-project.git
cd sana-project</code></pre>
        </li>
        <li><strong>Set up the virtual environment:</strong>
            <pre><code>python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li><strong>Install dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Apply migrations:</strong>
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li><strong>Run the development server:</strong>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><strong>Access the application:</strong>
            <p>Open your web browser and go to <a href="http://localhost:8000">http://localhost:8000</a>.</p>
        </li>

## Usage
After installation, you can start using the Sana system:

Register Students: Add new students to the system with their relevant details.
Manage Discipline: Document any disciplinary actions taken against students.
Generate Reports: Create reports to analyze disciplinary trends and individual student records.
User Management: Assign roles and manage user permissions to ensure proper access control.
Technology Stack
Frontend: HTML, CSS, JavaScript
Backend: Django
Database: SQLite (default), can be configured to use other databases like PostgreSQL
Other Libraries:
Django Rest Framework (for API)
Bootstrap (for responsive design)
## Contributors
The following team members developed the Sana project:

Hiva Abolhadizadeh: Project Analyst, Backend and Frontend Developer
Kimia Mashhadizadeh: Frontend Developer
Maryam Maqsoodi: Backend Developer
Mahta Akhgar: Backend Developer
Mobina Babaei: Frontend Developer

## Contributing
We welcome contributions to enhance the Sana project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a Pull Request.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
