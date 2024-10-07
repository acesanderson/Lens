# Course Search Tool

This Python script allows you to search through a MongoDB database of course information using either strict or fuzzy keyword matching. It's designed to operate on a MongoDB Courses database and offers the flexibility of being used on MacOS or via an SSH tunnel from Windows. For a more portable version, SQLite could be used. This tool leverages the Rich library for enhanced console input/output and RapidFuzz for fuzzy matching.

## Features

- **Strict and Fuzzy Search:** Search course data using strict keyword matching or fuzzy matching to find relevant results even if the exact keyword is not present.
- **Interactive Mode:** Offers an interactive mode where you can input keywords continuously.
- **Multiple Keyword Search:** Supports searching for multiple keywords and returns results common to all.

## Prerequisites

- **Python 3.x**: Make sure Python is installed on your system.
- **MongoDB**: The courses database should be set up and populated.
- **Required Libraries**: Install necessary packages if not already available.
  
  ```sh
  pip install pymongo rich rapidfuzz
  ```

## Setup 

1. **Database Configuration**: Ensure your MongoDB Courses database is accessible.
2. **Environment**: Depending on your OS, ensure the necessary connections are set up (direct for MacOS or via SSH tunnel for Windows).

## Usage

### Command Line Options

1. **Basic Usage**: Search for a keyword.
   ```sh
   python script_name.py <keyword>
   ```
   Replace `<keyword>` with your search term.

2. **Fuzzy Search**: Enable fuzzy matching.
   ```sh
   python script_name.py <keyword> --fuzzy
   ```

3. **Interactive Mode**: Start an interactive session.
   ```sh
   python script_name.py --interactive
   ```

### Interaction in Interactive Mode

- **Enter a Keyword**: When prompted, enter the keyword you wish to search for.
- **Toggle Fuzzy Matching**: Type "fuzzy" to toggle the fuzzy matching mode.
- **Exit**: Type "exit" to end the interactive session.

## Functions

- **find_keyword_strict**: Looks for exact keyword matches in course titles, descriptions, and table of contents.
- **find_keyword_fuzzy**: Uses fuzzy matching to identify courses relevant to the keyword.
- **search_multiple_keywords**: Accepts multiple keywords and finds courses common to all.
- **Lens**: Core function to execute a keyword search across courses.

## Example

To find courses containing the keyword "Python" with fuzzy matching enabled:

```sh
python script_name.py "Python" --fuzzy
```

In interactive mode, you can search continuously by entering different keywords. Toggle fuzzy matching by typing "fuzzy" and exit the loop by typing "exit".

## Future Improvements

- **Database Portability**: Incorporate SQLite for a more portable solution.
- **GUI Integration**: Develop a graphical user interface for ease of use.

## Support

For any issues or contributions, please contact [Your Contact Information]. We welcome feedback and suggestions for improvement.

## License

This project is licensed under the terms of your preferred license.

---

This README provides a comprehensive guide for both technical users and those less familiar with command-line tools, detailing the script's features, setup, and usage instructions.
