# ZAMINSTAGRAM 

## THIS TOOL IS ON DEVELOPMENT, INSTAGRAM MIGHT DETECT THE AUTOMATIZATION ON YOUR ACCOUNT AND BAN/RESTRICT YOUR ACCOUNT, BE CAREFUL AND FEEL FREE TO EDIT THE CODE BY YOUR OWN

This Python script automates the process of generating an image with a random color background and uploading it as your Instagram profile picture at regular intervals. The images can be letters, words, or any PNG with a transparent background.
### YOU CAN USE MY OTHER CODE FOR MAKING CUSTOM PHRASES, SYMBOLS, LETTERS OR NUMBERS IN PNG WITH A CUSTOM FONT https://github.com/zamudioo/zamudio.png/tree/main
## Features

- *Random Background Generator*: Takes a transparent PNG image (like a letter or a word) and randomly changes its background color.
- *Instagram Login Automation*: Logs into Instagram automatically using saved cookies to avoid logging in every time.
- *Profile Picture Update*: Changes your Instagram profile picture at intervals (e.g., every 12 hours).

## Prerequisites

1. Install Required Libraries:
   Install the necessary Python packages by running:
   ```bash
   pip install selenium requests pillow

2. Google Chrome and ChromeDriver:

3. Ensure you have Google Chrome installed.

4. Download the appropriate version of ChromeDriver and place it in your system path or the project folder.

5.  Instagram Account: You need a valid Instagram account for logging in and updating the profile picture.

## How to Use

First-Time Setup

1. GUI-Based Login: On the first run, the script will open Chrome with an Instagram login page. You must manually log in as usual using the credentials provided in the script. A Chrome extension (chaff.crx) is also loaded during this step.


2. Save Cookies: After logging in, the browser will automatically close, and the session cookies will be saved in a file (cookies.json). These cookies are used to keep your session active, so you don't need to log in manually again.



## Step-by-Step Execution

1. Update the Script Variables: Open the script and edit the following variables:

*USER*: Your Instagram username.

*PWD*: Your Instagram password.

*PATH_PHOTO*: The path to the PNG file you want to upload with a transparent background.

*EXTENSION_PATH*: The path to the Chrome extension file (chaff.crx).



2. Run the Script: Run the script with Python. On the first execution, it will open a browser window for you to log into Instagram manually.
```bash
python script.py
```

3. Automatic Profile Updates: After the first run, the script will run in the background, generating a new image with a random background every 12 hours and updating your Instagram profile picture.



## How the Code Works

1. Login Automation:

The script loads a Chrome browser with a specified extension and opens Instagram.

The user manually logs in (the first time).

The browser closes automatically, and the session cookies are saved for future use.

Cookies are reused in subsequent runs to avoid logging in repeatedly.


2. Image Generation:

A PNG image with a transparent background (such as a letter or word) is loaded.

The script generates a random background color and merges it with the transparent PNG.

The final image is saved as foto.png.
.

![foto](https://github.com/user-attachments/assets/3eb79990-f4a4-49a7-b970-430ecf3e1c03) 
![foto](https://github.com/user-attachments/assets/dcdf63aa-1557-44ef-a86b-1734080656f7)




3. Profile Picture Update:


Once logged in, the script uploads the generated image (foto.png) to the Instagram profile at intervals (e.g., every 12 hours).


## Folder Structure

```
├── cookies.json           # Saved Instagram session cookies
├── foto.png               # Generated profile picture with random background
├── letter/                # Folder containing PNG images (letters/words)
│   └── letter.png         # Example PNG image with a transparent background
├── chaff.crx              # Chrome extension for the first-time login
└── script.py              # The main Python script
```

## Important Notes

1. First-Time Manual Login: You must manually log in to Instagram during the first run. After that, saved cookies will handle the login automatically.


2. Cookie Management: If Instagram cookies expire, you will need to log in again manually. The script will prompt you when that happens.
