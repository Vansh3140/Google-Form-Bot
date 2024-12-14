# Google-Form Filler

This project automates the submission of a Google Form using Selenium and provides a Flask-based interface to send an email with relevant attachments. Below is a detailed breakdown of the files and their functionalities.

---

## Files Overview

### 1. `index.html`
#### **Purpose**:
A simple HTML page that serves as the user interface to trigger the email-sending functionality.

#### **Features**:
- Contains a single form with a button to submit the request to the Flask app.
- Minimalistic design with no additional user inputs.

#### **Code Breakdown**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Submission</title>
</head>
<body>
    <h1>Submit Your Assignment</h1>
    <form action="/send_email" method="POST">
        <button type="submit">Send Email</button>
    </form>
</body>
</html>
```

#### **How It Works**:
- When the button is clicked, a POST request is sent to the `/send_email` endpoint in the Flask app.
- The email-sending logic is handled entirely by the backend.

---

### 2. `send_email.py`
#### **Purpose**:
A Python script that uses Flask and the SMTP library to send an email with attachments.

#### **Features**:
- **Flask Integration**:
  - Hosts a web server with two routes:
    - `/`: Renders the `index.html` page.
    - `/send_email`: Sends an email upon form submission.
- **Email Configuration**:
  - Sends an email with a subject, body, and attachments.
  - Includes the sender, recipient, and CC fields.
- **Attachments**:
  - Attaches a screenshot (`screenshot.png`) and a resume (`resume.pdf`).
- **Environment Variable Usage**:
  - Uses `.env` to securely load the sender's email password.

#### **Key Code Snippet**:
```python
@app.route('/send_email', methods=['POST'])
def send_email():
    # Email configuration
    sender_email = "chdvanshsingh@gmail.com"
    sender_password = os.getenv('password')
    receiver_email = "tech@themedius.ai"
    cc_email = "hr@themedius.ai"
    subject = "Python (Selenium) Assignment - Vansh Singh Chaudhary"

    # Creating the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['CC'] = cc_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Email body and attachments are added here
    ...

    # Sending the email using SMTP
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    return "Email sent successfully!"
```

#### **How It Works**:
1. Loads `index.html` for the homepage.
2. Sends an email when the `/send_email` endpoint is triggered via a POST request.
3. Attaches required files and sends them via Gmail's SMTP server.

---

### 3. `screenshot.py`
#### **Purpose**:
A Python script using Selenium to automate the submission of a Google Form and take a screenshot after successful submission.

#### **Features**:
- **Automated Google Form Filling**:
  - Opens a pre-defined Google Form using Chrome WebDriver.
  - Fills out various fields, including text, date, and textarea fields, with sample data.
- **Screenshot Capture**:
  - Takes a screenshot after form submission and saves it as `screenshot.png`.

#### **Key Code Snippet**:
```python
# Locating and filling the address field
address_field = driver.find_element(by=By.XPATH, value="//textarea")
address_field.send_keys('Village ABC Distt. XYZ ABC state')

# Filling out additional input fields with sample data
input_list[3].send_keys('111111')

# Locating and setting the date in the date input field
date_field = driver.find_element(By.XPATH, "//input[@type='date']")
date_field.send_keys('2024-12-31')

# Locating and clicking the submit button
submit = driver.find_element(by=By.XPATH, value="//span[text()='Submit']")
submit.click()

# Taking a screenshot of the page after form submission
driver.save_screenshot("screenshot.png")
```

#### **How It Works**:
1. Opens the Google Form.
2. Automatically fills the form with pre-defined inputs.
3. Clicks the submit button and captures a screenshot of the result.
4. Saves the screenshot as `screenshot.png` for use in the email.

---

### Environment Setup

#### **Prerequisites**:
- Python 3.x installed.
- Required Python libraries:
  - Flask
  - Selenium
  - `python-dotenv`

#### **Installation Steps**:
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up `.env` File**:
   - Create a `.env` file in the root directory.
   - Add your Gmail password:
     ```
     password=your_gmail_password
     ```

5. **Download ChromeDriver**:
   - Download the ChromeDriver compatible with your Chrome version from [here](https://chromedriver.chromium.org/downloads).
   - Place it in the project directory or in your system PATH.

---

### Running the Project

#### **Step 1: Automate Google Form Submission**
Run the Selenium script to fill out the Google Form and generate a screenshot:
```bash
python screenshot.py
```
This creates a file named `screenshot.png` in the project directory.

#### **Step 2: Start the Flask App**
Run the Flask app to start the email-sending service:
```bash
python send_email.py
```
Access the application at `http://127.0.0.1:5000/`.

#### **Step 3: Send the Email**
- Open the app in your browser.
- Click the **Send Email** button to trigger the `/send_email` endpoint.

---

### Outputs

#### **Generated Outputs**:
1. `screenshot.png`: Captured after Google Form submission.

---

### Future Improvements
1. **Dynamic Form Inputs**:
   - Allow user input for form data via the Flask UI.
2. **Error Handling**:
   - Add comprehensive error messages for both Selenium and Flask.
3. **UI Enhancements**:
   - Use CSS for a better user experience.
4. **File Management**:
   - Allow dynamic upload of attachments via the web interface.

