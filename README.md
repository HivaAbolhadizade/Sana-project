<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sana - School Student Information System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            margin-bottom: 10px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        pre {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            background-color: #ecf0f1;
            padding: 2px 5px;
            border-radius: 3px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Sana - School Student Information System</h1>

    <p><strong>Recognition:</strong> The Sana project was awarded the best project of the term for its comprehensive analysis and implementation.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#project-overview">Project Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#technology-stack">Technology Stack</a></li>
        <li><a href="#contributors">Contributors</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
    </ul>

    <h2 id="project-overview">Project Overview</h2>
    <p><strong>Sana</strong> is a web-based system designed to help educational institutions manage student discipline records effectively. This system allows administrators to register students, document disciplinary actions, and generate comprehensive reports on student behavior. Sana was created with the goal of improving the discipline management process in schools, making it easier for administrators to track and address disciplinary issues.</p>
    <p>The project was developed as part of the <strong>Systems Analysis and Design</strong> course under the guidance of <strong>Dr. Mahdieh Ghazvini</strong>. The project was recognized as the best project of the term, praised for its thorough software analysis and intuitive design.</p>

    <h2 id="features">Features</h2>
    <ul>
        <li><strong>Student Registration:</strong> Easily register and manage student information.</li>
        <li><strong>Discipline Management:</strong> Record and track disciplinary actions taken against students.</li>
        <li><strong>Report Generation:</strong> Generate detailed reports on disciplinary activities.</li>
        <li><strong>User-Friendly Interface:</strong> Navigate the system with ease thanks to an intuitive design.</li>
        <li><strong>Responsive Design:</strong> Access the system from any device, thanks to its responsive front-end design.</li>
    </ul>

    <h2 id="installation">Installation</h2>
    <p>To get started with Sana, follow these steps:</p>
    <ol>
        <li><strong>Clone the repository:</strong>
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
    </ol>

    <h2 id="usage">Usage</h2>
    <p>After installation, you can start using the Sana system:</p>
    <ul>
        <li><strong>Register Students:</strong> Add new students to the system with their relevant details.</li>
        <li><strong>Manage Discipline:</strong> Document any disciplinary actions taken against students.</li>
        <li><strong>Generate Reports:</strong> Create reports to analyze disciplinary trends and individual student records.</li>
        <li><strong>User Management:</strong> Assign roles and manage user permissions to ensure proper access control.</li>
    </ul>

    <h2 id="technology-stack">Technology Stack</h2>
    <ul>
        <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
        <li><strong>Backend:</strong> Django</li>
        <li><strong>Database:</strong> SQLite (default), can be configured to use other databases like PostgreSQL</li>
        <li><strong>Other Libraries:</strong>
            <ul>
                <li>Django Rest Framework (for API)</li>
                <li>Bootstrap (for responsive design)</li>
            </ul>
        </li>
    </ul>

    <h2 id="contributors">Contributors</h2>
    <p>The Sana project was developed by the following team members:</p>
    <ul>
        <li><strong>Your Name:</strong> Project Analyst, Backend and Frontend Developer</li>
        <li><strong>Kimia Mashhadizadeh:</strong> Frontend Developer</li>
        <li><strong>Mobina Babaei:</strong> Frontend Developer</li>
        <li><strong>Maryam Maqsoodi:</strong> Backend Developer</li>
        <li><strong>Mahta Akhgar:</strong> Backend Developer</li>
    </ul>

    <h2 id="contributing">Contributing</h2>
    <p>We welcome contributions to enhance the Sana project! To contribute, please follow these steps:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
        <li>Make your changes.</li>
        <li>Commit your changes (<code>git commit -m 'Add new feature'</code>).</li>
        <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
        <li>Open a Pull Request.</li>
    </ol>

    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>

    <h2 id="acknowledgements">Acknowledgements</h2>
    <ul>
        <li><strong>Dr. Mahdieh Ghazvini:</strong> For her guidance and support throughout the project.</li>
        <li><strong>Developers:</strong> A big thank you to all the contributors who made this project possible.</li>
        <li><strong>Inspiration:</strong> This project was inspired by the need for an effective student discipline management system in educational institutions.</li>
    </ul>
</div>

</body>
</html>
