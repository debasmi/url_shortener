
# URL Shortener Application

## **Site is live [here](https://debasmi.pythonanywhere.com).**


## **To run locally on your machine follow the steps given below:**

This is a simple Flask-based URL shortener application. It allows users to input a long URL and generates a shortened version for easy sharing.

---

## **Prerequisites**
- Python 3.x installed on your system.
- `pip` (Python package manager) installed.

---

## **Setup and Installation**

### **1. Fork the Repository**
Before cloning the repository, you need to fork it to your own GitHub account:
1. Go to the repository: [https://github.com/debasmi/url_shortener](https://github.com/debasmi/url_shortener).
2. Click the **Fork** button in the top-right corner of the page.
3. This will create a copy of the repository under your GitHub account.

---

### **2. Clone the Repository**
After forking, clone your forked repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### **3. Set Up a Virtual Environment (Optional but Recommended)**

#### **For macOS/Linux:**
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

#### **For Windows:**
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

---

### **4. Install Dependencies**
Install the required Python packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### **5. Run the Application**

#### **For macOS/Linux and Windows:**
1. Start the Flask application:
   ```bash
   python app.py
   ```
2. The application will start running, and you should see output similar to:
   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   * Debugger is active!
   * Debugger PIN: XXX-XXX-XXX
   ```

---

### **6. Access the Application**
1. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
2. Enter a long URL in the input field and submit it to generate a shortened URL.
3. Use the shortened URL to redirect to the original URL.

---

### **7. Stop the Application**
To stop the application, press `CTRL + C` in the terminal where the application is running.

---

## **Database**
- The application uses an SQLite database (`urls.db`) to store the original and shortened URLs.
- The database will be automatically created in the project directory when you run the application for the first time.

---

## **Dependencies**
The following Python packages are required to run this application:
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

These are listed in the `requirements.txt` file.

---

## **Support**
If you encounter any issues or have questions, please open an issue in the repository.


## **Demo**

<img width="888" alt="Screenshot 2025-02-18 at 1 09 05 AM" src="https://github.com/user-attachments/assets/47ea8a35-a62d-4125-9422-e1b82fdd4ce1" />
<img width="888" alt="Screenshot 2025-02-18 at 1 11 56 AM" src="https://github.com/user-attachments/assets/88e167b8-cc23-4e2b-835d-e2d8f42b4f5e" />
<img width="888" alt="Screenshot 2025-02-18 at 1 12 08 AM" src="https://github.com/user-attachments/assets/822a8bb3-789e-478e-b680-ce904105eb7b" />




