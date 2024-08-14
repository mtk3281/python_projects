# PyQt5 Notepad App

## Overview

This is a simple notepad application built using PyQt5, a set of Python bindings for Qt libraries. The application features a text editor with basic functionalities such as creating, opening, saving files, and text formatting options like font size adjustment and dark/light mode.

## Features

- **New File**: Create a new blank file.
- **Open File**: Open an existing text file.
- **Save File**: Save changes to the current file.
- **Save As**: Save the current document to a new file.
- **Undo/Redo**: Undo or redo text changes.
- **Cut/Copy/Paste**: Standard text operations.
- **Dark Mode/Light Mode**: Toggle between dark and light themes.
- **Font Size Adjustment**: Increase or decrease the font size.

## Installation

### Prerequisites

- Python 3.x
- PyQt5

### Setup

1. **Clone the Repository**

    ```sh
    git clone https://github.com/mtk3281/PyQt5-Notepad-App.git
    cd PyQt5-Notepad-App
    ```

2. **Create and Activate a Virtual Environment**

    ```sh
    python -m venv myenv
    ```

    **Activate the virtual environment:**

    - On Windows:

        ```sh
        myenv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source myenv/bin/activate
        ```

3. **Install Dependencies**

    ```sh
    pip install PyQt5
    ```

4. **Run the Application**

    ```sh
    python app.py
    ```

    The application window will appear allowing you to use the notepad features.

## Project Structure

- `app.py`: Main Python file containing the PyQt5 application code.
- `main.ui`: Qt Designer file for the user interface.
- `note.ico`: Icon file for the application window.


