# GitHub Art Generator

This project is a GitHub Art Generator that allows you to create pixel art which will be reflected in your GitHub commit history. The tool provides an `index.html` file where you can draw your art, save it, and then apply it to your GitHub repository.

## How to Use

1. **Open the Website**: Open the `index.html` file in your web browser.
2. **Draw Your Art**: Use the interface to draw your pixel art.
3. **Save Your Art**: Click the save button to download the `script.py` file containing your art data.
4. **Initialize a Git Repository**:
    ```sh
    git init
    git remote add origin <your-repo-url>
    ```
5. **Run the Script**: Execute the `script.py` file to create the commits.
    ```sh
    python script.py
    ```
6. **Push to GitHub**: Force push to your GitHub repository to update your commit history.
    ```sh
    git push --force
    ```

## Requirements

- Python 3.x
- Git

## Example

1. Open `index.html` in your browser.
2. Draw your pixel art.
3. Save the art to download `script.py`.
4. Initialize a git repository and add the remote origin.
5. Run the script to create the commits.
6. Force push to update your GitHub commit history.

