# Student Grade Management System

A full-stack web application for managing student grades and teacher accounts, built with modern technologies and deployed on AWS. This project demonstrates proficiency in frontend development, backend API design, database management, and cloud deployment.

## 🚀 Live Demo

**Application URL:** http://54.172.200.184/

**Demo Credentials:**
- Username: `admin`
- Password: `admin#1234`

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Key Features & Implementation](#key-features--implementation)
- [API Endpoints](#api-endpoints)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)
- [Project Highlights](#project-highlights)

## Overview

The Student Grade Management System is a comprehensive web application designed to streamline grade management for educational institutions. Teachers can securely log in, manage student records, and track academic performance across multiple subjects (Math, English, Physics). The system provides a complete CRUD (Create, Read, Update, Delete) interface for both teacher and student account management.

## Features

### 🔐 Authentication & Authorization
- Secure login system with session-based authentication
- Cookie-based session management
- Protected routes with middleware validation
- Role-based access control (teacher accounts only)

### 👨‍🏫 Teacher Management
- Add new teacher accounts
- View all teacher accounts
- Edit teacher information (name, password)
- Delete teacher accounts
- Duplicate name validation

### 👨‍🎓 Student Management
- Add new student records with grade information
- View comprehensive student list with grades
- Edit student information and grades
- Delete student records
- Track grades across multiple subjects (Math, English, Physics)

### 🎨 User Interface
- Modern, responsive design using View UI Plus
- Intuitive navigation with Vue Router
- Real-time data updates
- User-friendly forms and validation

## Technology Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Vue Router 4** - Client-side routing
- **Axios** - HTTP client for API communication
- **View UI Plus** - UI component library
- **Vite** - Next-generation frontend build tool
- **HTML5, CSS3, JavaScript (ES6+)**

### Backend
- **Python 3** - Programming language
- **Flask** - Lightweight web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **Flask-CORS** - Cross-origin resource sharing
- **Gevent** - Production WSGI server
- **PyMySQL** - MySQL database connector

### Database
- **MySQL** - Relational database management system
- **SQLAlchemy** - Database abstraction layer

### DevOps & Deployment
- **AWS** - Cloud hosting platform
- **Nginx** - Web server and reverse proxy
- **Git** - Version control

### Development Tools
- PyCharm - Python IDE
- Postman - API testing
- Chrome DevTools - Debugging

## Project Structure

```
pythonProject1/
├── server/                 # Backend server
│   ├── server.py        # Flask application & API endpoints
│   ├── config.dev.ini   # Development configuration
│   ├── config.prod.ini  # Production configuration
│   └── requirement.txt  # Python dependencies
├── web1/                 # Frontend application
│   ├── src/
│   │   ├── components/  # Vue components
│   │   ├── view/        # Page views
│   │   │   ├── Login.vue
│   │   │   ├── studentdata.vue
│   │   │   └── teacherdata.vue
│   │   ├── router.js    # Vue Router configuration
│   │   └── App.vue      # Root component
│   ├── dist/            # Production build
│   ├── package.json     # Node.js dependencies
│   └── vite.config.js   # Vite configuration
├── project.sql          # Database schema
└── README.md            # Project documentation
```

## Key Features & Implementation

### 1. RESTful API Design
- Implemented RESTful endpoints following industry best practices
- Consistent JSON response format with error handling
- Proper HTTP methods (GET, POST) for different operations

### 2. Database Architecture
- Normalized database schema with proper relationships
- Efficient query execution using parameterized queries
- Data validation at both frontend and backend levels

### 3. Security Implementation
- Session-based authentication using secure cookies
- Input validation and sanitization
- SQL injection prevention through parameterized queries
- CORS configuration for secure cross-origin requests

### 4. Frontend-Backend Integration
- Asynchronous API calls using Axios
- JSON data exchange format
- Error handling and user feedback
- State management for user sessions

### 5. Production Deployment
- Configured production-ready WSGI server (Gevent)
- Environment-based configuration management
- Nginx reverse proxy setup
- AWS EC2 deployment

## API Endpoints

### Authentication
- `POST /login` - User authentication
- `POST /logout` - Session termination

### Teacher Management
- `GET /teacher_lists` - Retrieve all teachers
- `POST /teacher_add` - Create new teacher account
- `POST /teacher_edit` - Update teacher information
- `POST /teacher_delete` - Remove teacher account

### Student Management
- `GET /student_lists` - Retrieve all students with grades
- `POST /student_add` - Create new student record
- `POST /student_edit` - Update student information and grades
- `POST /student_delete` - Remove student record

## Installation & Setup

### Prerequisites
- Python 3.x
- Node.js and npm
- MySQL database
- Git

### Backend Setup

1. Navigate to the server directory:
```bash
cd server
```

2. Install Python dependencies:
```bash
pip install -r requirement.txt
```

3. Configure database connection in `config.prod.ini`:
```ini
[mysql]
host = your_host
port = 3306
user = your_username
password = your_password
database = your_database
```

4. Initialize database:
```bash
mysql -u username -p database_name < ../project.sql
```

5. Run the server:
```bash
python server.py
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd web1
```

2. Install dependencies:
```bash
npm install
```

3. Configure API endpoint in your environment file

4. Run development server:
```bash
npm run dev
```

5. Build for production:
```bash
npm run build
```

## Deployment

The application is deployed on AWS with the following architecture:
- **Frontend**: Served via Nginx from static files
- **Backend**: Flask application running on Gevent WSGI server
- **Database**: MySQL database instance
- **Configuration**: Environment-based config files for dev/prod separation

## Project Highlights

### Technical Skills Demonstrated
✅ **Full-Stack Development**: End-to-end application development from frontend to backend  
✅ **Modern JavaScript Framework**: Vue.js 3 with Composition API  
✅ **RESTful API Design**: Well-structured backend API with proper HTTP methods  
✅ **Database Management**: MySQL database design and ORM usage  
✅ **Authentication & Security**: Session management and secure authentication  
✅ **Cloud Deployment**: AWS deployment with production configuration  
✅ **DevOps**: Nginx configuration and server management  
✅ **Version Control**: Git for project management  

### Problem-Solving
- Implemented secure authentication system with session management
- Designed scalable database schema for educational data
- Created intuitive UI for complex data management operations
- Optimized API responses for efficient data transfer
- Configured production environment for reliability and performance

### Best Practices
- Separation of concerns (frontend/backend)
- Environment-based configuration
- Error handling and validation
- Code organization and modularity
- Security considerations (SQL injection prevention, CORS)

---

**Note**: This project demonstrates practical application of full-stack development skills and is suitable for portfolio presentation in job applications.


<img width="1282" height="937" alt="image" src="https://github.com/user-attachments/assets/7a2a8fa4-b41f-4716-9d4b-bd4471aa8832" />
