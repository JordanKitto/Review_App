
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2023.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 10193944
student_name   = "Jordan Kitto"
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 2 Description----------------------------------#
#
#  In this assessment task you will combine your knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive "app" that allows its user to view and save
#  data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  together with some non-Python support files.
#
#--------------------------------------------------------------------#



#-----Set up---------------------------------------------------------#
#
# This section imports standard Python 3 modules sufficient to
# complete this assignment.  Don't change any of the code in this
# section, but you are free to import other Python 3 modules
# to support your solution, provided they are standard ones that
# are already supplied by default as part of a normal Python/IDLE
# installation.
#
# However, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite database functions.  [You WILL need
# to use some of these in your solution.]
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Validity Check-------------------------------------------------#
#
# This section confirms that the student has declared their
# authorship.  You must NOT change any of the code below.
#

if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print("\nCannot find requested document '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print("\nAccess denied to document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except URLError as message: # probably the wrong server address
        print("\nCannot access web server at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              "the document at URL '" + str(url) + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters")
        print("Error message was:", message, "\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("\nUnable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#

import tkinter as tk
from tkinter import ttk
from webbrowser import open as urldisplay
import urllib.request
import re
import sqlite3
import os
from urllib.error import URLError

class StarRating(tk.Frame):
    def __init__(self, master=None, callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.stars = 0
        self.callback = callback
        self.star_buttons = []
        self.configure(bg="#333333")

        # Creating star buttons and adding them to the frame
        for i in range(1, 6):
            star_button = tk.Button(self, text=f"★ {i}", command=lambda i=i: self.set_stars(i), font=("Arial", 12), relief=tk.FLAT, bg="#222222", fg="white", activebackground="gold", activeforeground="black")
            star_button.grid(row=0, column=i-1, padx=2)
            self.star_buttons.append(star_button)

        # Creating a reset button
        reset_button = tk.Button(self, text="Reset", command=self.reset_stars, font=("Arial", 12), fg="white", relief=tk.RAISED, bg="#333333")
        reset_button.grid(row=1, column=0, columnspan=5, pady=10)

    def set_stars(self, stars):
        # Update the selected stars and configure the button colors accordingly
        self.stars = stars
        for i, star_button in enumerate(self.star_buttons):
            if i < stars:
                star_button.config(bg="gold")
            else:
                star_button.config(bg="#222222")
        if self.callback:
            self.callback(self.stars)

    def reset_stars(self):
        # Reset the selected stars and button colors
        self.stars = 0
        for star_button in self.star_buttons:
            star_button.config(bg="#222222")
        if self.callback:
            self.callback(self.stars)

class EntertainmentReviewApp:
    def __init__(self, master):
        self.master = master
        master.title("Media Ratings, Reviews and Recommendations")
        master.geometry("550x850")
        master.config(bg="#333333")

        # Loading the logo image
        self.logo = tk.PhotoImage(file="review_logo.png")  # Update the image path if necessary
        self.logo_label = tk.Label(master, image=self.logo, bg="#333333")
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Instruction label
        self.instruction = tk.Label(master, text="Please select what type of entertainment you wish to review:", font=("Arial", 14), fg="lightskyblue", bg="#333333")
        self.instruction.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Dropdown menu for selecting the entertainment type
        self.media_types = ["Live Radio", "Live Shows", "Live TV!"]
        self.media_type_urls = {
            "Live Radio": "https://www.abc.net.au/triplej/featured-music",
            "Live Shows": "https://thetivoli.com.au/events",
            "Live TV!": "https://www.9now.com.au/live/channel-9"
        }
        self.selected_type = tk.StringVar()
        self.selected_type.set(self.media_types[0])
        self.dropdown = ttk.Combobox(master, textvariable=self.selected_type, values=self.media_types, font=("Arial", 12), state="readonly")
        self.dropdown.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Button for showing the summary
        self.summary_button = tk.Button(master, text="Show Summary", command=self.show_summary, font=("Arial", 12), fg="white", relief=tk.RAISED, bg="#333333")
        self.summary_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # Button for showing the URL
        self.show_url_button = tk.Button(master, text="Show URL", command=self.show_url, font=("Arial", 12), fg="white", relief=tk.RAISED, bg="#333333")
        self.show_url_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Rating label
        self.rating_label = tk.Label(master, text="Rate your selection:", font=("Arial", 14), fg="lightskyblue", bg="#333333")
        self.rating_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Star rating widget
        self.rating_widget = StarRating(master, callback=self.save_rating)
        self.rating_widget.grid(row=6, column=0, columnspan=2, pady=10)

        # Button for saving the review
        self.save_button = tk.Button(master, text="Save Review", command=self.save_review, font=("Arial", 12), fg="white", relief=tk.RAISED, bg="#333333")
        self.save_button.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")

    def get_site_info(self, url, pattern1, pattern2):
        try:
            response = urllib.request.urlopen(url)
        except URLError:
        # Handle the exception, e.g. by retrying the request, logging the error, or notifying the user
            return "Could not access the site", "Could not access the site"

        html = response.read().decode()

        info1 = re.search(pattern1, html, re.IGNORECASE)
        info2 = re.search(pattern2, html, re.IGNORECASE)

        if info1:
            info1 = info1.group(1)
        else:
            info1 = "Could not find information"

        if info2:
            info2 = info2.group(1)
        else:
            info2 = "Could not find information"

        return info1, info2

    def show_url(self):
        # Display the URL of the selected media in a new window
        url = self.media_type_urls[self.selected_type.get()]
        url_window = tk.Toplevel(self.master)
        url_window.geometry("350x150")
        url_window.title("URL Page")
        url_window.config(bg="#333333")

        url_label = tk.Label(url_window, text="The URL of the selected media is:", font=("Arial", 12, "bold"), fg="mintcream", bg="#333333")
        url_label.pack(pady=20)

        url_value_label = tk.Label(url_window, text=url, cursor="hand2", fg="lightskyblue", font=("Arial", 12, 'underline'), bg="#333333")
        url_value_label.bind("<Button-1>", lambda e: urldisplay(url))
        url_value_label.pack()

    def show_summary(self):
        # Display a summary of the selected media in a new window
        summary_window = tk.Toplevel(self.master)
        summary_window.geometry("250x150")
        summary_window.title("Summary Page")
        summary_window.config(bg="#333333")

        url = self.media_type_urls[self.selected_type.get()]
        label1 = tk.Label(summary_window)
        label1.pack()
        label2 = tk.Label(summary_window)
        label2.pack()

        custom_message = ""

        if self.selected_type.get() == "Live Radio":
            custom_message = "Live on Triple J Radio"
            pattern1 = '<span class="KeyboardFocus_keyboardFocus__uwAUh" data-component="KeyboardFocus">(.*?)</span>'
            pattern2 = '<p class="Typography_base__k7c9F TracklistCard_secondaryTitle__e1gyh Typography_sizeMobile16__Wygfe Typography_lineHeightMobile24__xwyV0 Typography_regular__Aqp4p Typography_colourInherit__xnbjy" data-component="Text">(.*?)</p>'
        elif self.selected_type.get() == "Live Shows":
            custom_message = "What's on at the Tivoli!"
            pattern1 = '<div class="image-title">(.*?)</div>'
            pattern2 = '<div class="image-subtitle">\s*(.*?)\s*</div>'
        elif self.selected_type.get() == "Live TV!":
            custom_message = "Live on Channel 9 Go"
            pattern1 = '<div class="D-80HH" itemprop="channel/title">(.*?)</div>'
            pattern2 = '<time class="_2iAoyY" datetime="[0-9]+m">(.*?)</time>'
        else:
            pattern1 = pattern2 = ""

        custom_message_label = tk.Label(summary_window, text=custom_message, font=("Arial", 12, "bold"), fg="lightskyblue", bg="#333333")
        custom_message_label.pack()

        info1, info2 = self.get_site_info(url, pattern1, pattern2)

        label1 = tk.Label(summary_window, text=info1, font=("Arial", 11, "bold"), fg="mintcream", bg="#333333")
        label1.pack(pady=10)
        label2 = tk.Label(summary_window, text=info2, font=("Arial", 11, "bold"), fg="mintcream", bg="#333333")
        label2.pack()

    def save_rating(self, rating):
        # Callback function to save the selected rating
        self.rating_widget.stars = rating

    def reset_rating(self):
        # Reset the selected rating
        self.rating_widget.stars = 0
        for star_button in self.rating_widget.star_buttons:
            star_button.config(bg="#222222")

    def save_review(self):
        if self.rating_widget.stars < 1:
            # Display an error message if the rating is less than 1
            error_window = tk.Toplevel(self.master)
            error_window.geometry("250x150")
            error_window.title("Error")
            error_window.config(bg="#333333")

            error_message_label = tk.Label(error_window, text="Rating needs to be 1 or higher.", font=("Arial", 12, "bold"), fg="Red", bg="#333333")
            error_message_label.pack(pady=20)

            close_button = tk.Button(error_window, text="Close", command=error_window.destroy, font=("Arial", 12), fg="white", relief=tk.RAISED, bg="#333333")
            close_button.pack(pady=20)
        else:
            # Save the review in a database
            print(f"Review saved: {self.selected_type.get()} with a rating of {self.rating_widget.stars} stars")

            db_file = 'reviews.db'
            if not os.path.exists(db_file):
                error_window = tk.Toplevel(self.master)
                error_window.geometry("250x150")
                error_window.title("Database Error")
                error_window.config(bg="#333333")

                error_message_label = tk.Label(error_window, text="Database not found.", font=("Arial", 12, "bold"), fg="Red", bg="#333333")
                error_message_label.pack(pady=20)

                close_button = tk.Button(error_window, text="Close", command=error_window.destroy, font=("Arial", 12), fg="white", relief=tk.RAISED, bg="#333333")
                close_button.pack(pady=20)
                return

            conn = sqlite3.connect(db_file)
            c = conn.cursor()

            c.execute('''
                CREATE TABLE IF NOT EXISTS REVIEWS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    TYPE TEXT,
                    RATING INTEGER,
                    INFO1 TEXT,
                    INFO2 TEXT,
                    URL TEXT
                )
            ''')

            url = self.media_type_urls[self.selected_type.get()]
            pattern1 = pattern2 = ""

            if self.selected_type.get() == "Live Radio":
                pattern1 = '<span class="KeyboardFocus_keyboardFocus__uwAUh" data-component="KeyboardFocus">(.*?)</span>'
                pattern2 = '<p class="Typography_base__k7c9F TracklistCard_secondaryTitle__e1gyh Typography_sizeMobile16__Wygfe Typography_lineHeightMobile24__xwyV0 Typography_regular__Aqp4p Typography_colourInherit__xnbjy" data-component="Text">(.*?)</p>'
            elif self.selected_type.get() == "Live Shows":
                pattern1 = '<div class="image-title">(.*?)</div>'
                pattern2 = '<div class="image-subtitle">\s*(.*?)\s*</div>'
            elif self.selected_type.get() == "Live TV!":
                pattern1 = '<div class="D-80HH" itemprop="channel/title">(.*?)</div>'
                pattern2 = '<time class="_2iAoyY" datetime="[0-9]+m">(.*?)</time>'

            info1, info2 = self.get_site_info(url, pattern1, pattern2)

            c.execute('''
                INSERT INTO REVIEWS (TYPE, RATING, INFO1, INFO2, URL)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.selected_type.get(), self.rating_widget.stars, info1, info2, url))

            conn.commit()
            conn.close()

            saved_window = tk.Toplevel(self.master)
            saved_window.geometry("200x150")
            saved_window.title("Saved")
            saved_window.config(bg="#333333")

            saved_message_label = tk.Label(saved_window, text="Your rating has been saved!", font=("Arial", 12), fg="white", bg="#333333")
            saved_message_label.pack(pady=20)

            close_button = tk.Button(saved_window, text="Close", command=saved_window.destroy, font=("Arial", 12), fg="white", relief=tk.RAISED, bg="#333333")
            close_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = EntertainmentReviewApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


