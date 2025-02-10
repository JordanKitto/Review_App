# Media Ratings, Reviews and Recommendations

"Media Ratings, Reviews and Recommendations" is an interactive application developed as an individual assessment for QUT's IFB104 "Building IT Systems" (Semester 1, 2023). This project allows users to review different types of entertainment—including Live Radio, Live Shows, and Live TV—by retrieving live information from online sources, rating the media using a star-based widget, and saving their reviews to a local SQLite database.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)


## Overview

This project is designed to provide a robust, user-friendly interface for interacting with online media sources. Users can:
- Choose a media type (Live Radio, Live Shows, or Live TV) from a dropdown menu.
- Retrieve and display URLs and summary information from the corresponding online source.
- Rate the media using a custom star rating widget.
- Save their review and rating, along with related metadata, to a local SQLite database.

The application leverages Python’s standard libraries (including Tkinter, sqlite3, and urllib) along with regular expressions for pattern matching.

## Features

- **Intuitive GUI:** A polished user interface built with Tkinter.
- **Dynamic Media Selection:** Choose from different media types with a simple dropdown.
- **Live Data Retrieval:** Automatically fetch URL and summary information from online sources.
- **Star Rating System:** Rate your media experience using an interactive star-based widget.
- **Review Persistence:** Save your review details to a SQLite database for future reference.
- **Error Handling:** Informative status messages and error dialogs to guide user interactions.

## Technologies Used

- **Python 3** – Primary programming language.
- **Tkinter** – For building the graphical user interface.
- **SQLite** – For local data storage.
- **Regular Expressions** – For extracting data from web content.
- **urllib** – For web operations and downloading content.

## Installation

1. **Clone the Repository:**

git clone https://github.com/yourusername/media-review-app.git

2. **Usage:**
Run the Application:
python assignment.py

![image](https://github.com/user-attachments/assets/785a05ad-3ba3-4a2b-9e2a-546b0d780330)


3. **Select a Media Type:**
Use the dropdown menu to choose one of the following:
- Live Radio
- Live Shows
- Live TV!

5. **View URL & Summary:**
- Click Show URL to open a window displaying the media source's URL (clickable to open in your browser).
- Click Show Summary to retrieve and display summary information from the selected online source.
   
![image](https://github.com/user-attachments/assets/db22bf79-9105-4f37-9ced-6901250cdffd)


6. **Rate and Save Your Review:**
- Use the star rating widget to rate the media.
- Click Save Review to store your review (including media type, rating, and summary data) in the SQLite database.
- In case of any errors (such as a missing rating), appropriate error messages will be displayed within the GUI.
![image](https://github.com/user-attachments/assets/0d14d07b-a185-4807-a142-ae3a17b56402)

