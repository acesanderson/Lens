# Mentor: Learning Path Generation by Keyword

Mentor is a tool designed to help users search through a courses database efficiently by using keywords. Whether you prefer strict matching or fuzzy matching, Mentor caters to both needs, ensuring you can find courses that best fit your goals.

## Features

- **Keyword Search**: Find courses containing specific keywords in their title, metadata, or detailed course content.
- **Fuzzy Matching**: Provides an option for fuzzy searching, allowing for more flexible and ambiguous keyword matching.
- **Interactive Mode**: Enables users to enter keywords interactively and toggles fuzzy matching.
- **Batch Search**: Supports searching for multiple keywords simultaneously and returns common courses across these searches.

## System Requirements

- Python 3.7 or higher
- MongoDB instance or access via SSH tunnel.
- Libraries: `pymongo`, `argparse`, `rich`, `rapidfuzz`

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/mentor.git
   ```

2. Navigate into the cloned directory:
   ```bash
   cd mentor
   ```

3. Install the required packages:
   ```bash
   pip install pymongo rich rapidfuzz
   ```

## Usage

Mentor can be run in both static and interactive modes from the command line. Here’s how you can use it:

### Static Mode

Run the script by providing a keyword directly:

```bash
python mentor.py "your_keyword_here"
```

- Use the `-f` or `--fuzzy` option to enable fuzzy matching:
  ```bash
  python mentor.py "your_keyword_here" -f
  ```

### Interactive Mode

Launch Mentor in interactive mode with the `-i` or `--interactive` flag:

```bash
python mentor.py -i
```

- In this mode, input keywords directly into the console when prompted.
- Type `exit` to close the interactive session.
- Type `fuzzy` to toggle the fuzzy matching setting on/off.

### Batch Keyword Search

For searching multiple keywords at once, separate keywords by new lines:

```bash
python mentor.py
keyword1
keyword2
keyword3
```

## Configuration

Before running the tool, ensure that your MongoDB instance is properly set up and accessible either locally or through an SSH tunnel.

## Contributions

We welcome contributions to Mentor! Feel free to fork the project and submit pull requests. Make sure to follow the existing coding style and include unit tests for any new functionality.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue on GitHub, and we’ll be glad to assist.

--- 

This readme aims to be helpful whether you're setting up Mentor yourself or collaborating with a developer to get it running. Happy learning!
