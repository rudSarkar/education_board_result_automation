This Python script automates the process of fetching exam results from the Bangladesh Education Board Results website using Playwright.

### Requirements
* Python 3.x
* Playwright
* dotenv

### Installation

1. Clone the repository:

```
https://github.com/rudSarkar/education_board_result_automation.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

### Usage

1. Set up your environment variables in a `.env` file:
```
exam_name=ssc
exam_year=2024
exam_board=rajshahi
exam_roll=612642
exam_reg=1312650452
```

2. Run the script:

```
python main.py
```

This script will launch a browser in headless mode, If you want to run the script with the browser visible, you can set `headless` to `False` in the script.

### Notes
* The script will keep running until it successfully saves the PDF file.
* Ensure that the provided credentials are correct and correspond to a valid examination result on the website.