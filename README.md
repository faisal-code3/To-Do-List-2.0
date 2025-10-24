# To-Do List 2.0

This is a simple To-Do List web application built using Flask, HTML, and CSS (Sass).  
It uses Flask’s template inheritance and server-side rendering (SSR) to organize pages efficiently and keep the structure clean.

## Features
- Add, edit, and delete tasks  
- Responsive layout built with HTML and Sass  
- Flask backend for routing and rendering templates  
- Template inheritance for reusable layouts  
- Server-side rendering for better performance and security  

## Technologies Used
- Python (Flask)
- HTML, CSS (Sass)
- Jinja2 Templates
- Git and GitHub for version control

## How to Run
1. Clone the repository  
   ```
   git clone https://github.com/faisal-code3/To-Do-List-2.0.git
   ```

2. Navigate into the project folder  
   ```
   cd To-Do-List-2.0
   ```

3. Create and activate a virtual environment  
   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

4. Install dependencies  
   ```
   pip install -r requirements.txt
   ```

5. Run the Flask app  
   ```
   python app.py
   ```

6. Open the browser and go to  
   ```
   http://127.0.0.1:5000
   ```

## Project Structure
```
To-Do-List-2.0/
│
├── static/
│   └── styles.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── other templates...
│
├── app.py
├── requirements.txt
└── README.md
```

## License
This project is licensed under the MIT License.  
© 2025 Faisal
