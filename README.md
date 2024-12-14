# Google Form Auto-Filler Script

This Python script uses **Selenium** to automatically fill out a Google Form and take a screenshot of the filled-out form. It is designed to work with Chrome and requires the **Chrome WebDriver** to run.

## Requirements

- Python 3.x
- Selenium library
- Chrome browser and ChromeDriver
- `time` module (included in Python standard library)

### Installation

1. **Install Python 3.x**: Ensure that you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Selenium**:
   Use pip to install Selenium by running:
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:
   - Download the ChromeDriver version that matches your installed Chrome version from [ChromeDriver](https://sites.google.com/chromium.org/driver/).
   - Ensure that ChromeDriver is placed in a directory included in your system’s `PATH` or provide the path directly in your script.

## Usage

1. Clone or download this repository.

2. Modify the `google_form_url` in the script with the link to the Google Form you want to fill out.

3. Run the script:

   ```bash
   python auto_fill_form.py
   ```

The script will:

- Open the specified Google Form.
- Automatically fill out the form with predefined sample data.
- Click the "Submit" button.
- Take a screenshot of the form after submission and save it as `screenshot.png`.

## Code Explanation

1. **Chrome WebDriver Configuration**:  
   The script uses `webdriver.ChromeOptions()` to configure Chrome to remain open after script execution by setting the `"detach"` option to `True`.

2. **Filling the Google Form**:  
   The script uses XPath to locate the form's input fields and fills them with predefined values (name, phone number, email, address, etc.).

3. **Form Submission**:  
   After filling out the fields, the script clicks the "Submit" button to submit the form.

4. **Screenshot Capture**:  
   After form submission, a screenshot is taken and saved in the current directory as `screenshot.png`.

5. **Error Handling**:  
   Any errors encountered during execution are caught in a `try-except` block and are printed to the console.

6. **Browser Closure**:  
   After the process is completed (or in case of an error), the browser is closed with a `quit()` command.

## Notes

- Ensure that the Google Form is publicly accessible or accessible to the user running the script.
- Modify the input data in the script as needed for your use case.
- The script currently assumes that there are exactly six text input fields and one textarea field. If the form structure changes, the XPath queries may need adjustment.

## Troubleshooting

- **WebDriver not found**: Ensure that `chromedriver` is correctly installed and its path is included in the system’s `PATH`.
- **Form not found**: If the XPath does not match the form elements, inspect the form's HTML structure and update the XPath in the script.
