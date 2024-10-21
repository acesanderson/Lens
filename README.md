# Lens: Keyword Search on Courses

Keyword search through course data.

## Features

- **Strict Search**: Conduct precise keyword searches on course titles, descriptions, and tables of contents.
- **Fuzzy Search**: Use fuzzy matching to locate keywords even if they are not exact matches.
- **Multiple Keyword Support**: Find courses that contain all of a list of specified keywords.
- **Interactive Mode**: Engage with the program in real-time to input multiple queries without restarting the application.

## Prerequisites

To use Lens, you'll need:

- **Python**: Ensure you have Python installed on your machine. Lens is compatible with Python 3.6 and above.
- **MongoDB**: Your course data should be stored in a MongoDB instance. The code is designed to function on MacOS or via an SSH tunnel from Windows. ==NOTE: this makes it impossible to use except on my computer, I can package this into SQL database for portability at later date==
- **Dependencies**: The following Python libraries are required:
  - `pymongo`: To access MongoDB from your Python script.
  - `rich`: For creating an interactive and visually appealing console interface.
  - `rapidfuzz`: For performing fuzzy matching.

You can install these dependencies using pip:
```bash
pip install pymongo rich rapidfuzz
```

## Getting Started

1. **Clone the Repository**: Download the Lens project codebase to your local machine.
   
   ```bash
   git clone https://github.com/your-username/lens.git
   cd lens
   ```

2. **Set Up Courses Data**: Ensure your MongoDB instance is running and contains your course data. If you don't have this setup yet, you'll need to upload your course data into MongoDB.

3. **Run Lens Program**: Execute the script in your terminal using the following command:
   
   ```bash
   python lens.py <keyword>
   ```

   Replace `<keyword>` with the term you are searching for.

## Using Lens

### Argument Options

When running the script, you can opt for different modes of operation:

- `-i, --interactive`: Run Lens in interactive mode. This lets you input multiple queries and switch settings without restarting the program.
  
  ```bash
  python lens.py -i
  ```

- `-f, --fuzzy`: Enable fuzzy matching to capture keyword variations that are not exact matches.

  ```bash
  python lens.py -f <keyword>
  ```

### Interactive Mode

In interactive mode, you can use the following commands:
- **Enter a Keyword**: Simply type a keyword and press Enter to search.
- **Toggle Fuzzy Mode**: Type `fuzzy` to toggle fuzzy mode on or off.
- **Exit**: Type `exit` to close the program.

### Searching Multiple Keywords

For searching with multiple keywords, input keywords separated by newline characters or in separate input lines in interactive mode. The program will return courses that contain all specified keywords.

## Troubleshooting

If you encounter issues, ensure the following:
- MongoDB is correctly set up and accessible from Lens.
- The necessary Python libraries are installed.
- You're entering the correct command syntax when running the script.

