# Combine Code Files

## Overview

The `Combine Code  Files` script is a Python tool designed to traverse a directory and its subdirectories to find and combine various types of code and web-related files into a single output file. This can be particularly useful for developers, IT professionals, or anyone who needs to analyze or consolidate code files from different programming languages into a single document.

### Main Purpose

The primary goal of this script is to convert and consolidate various code files into a `.txt` format. This makes the files easily readable by large language models, facilitating tasks like code analysis, documentation, and automated processing.

## Features

- Combines files with the following extensions:
  - **PHP** (`.php`)
  - **JavaScript** (`.js`)
  - **CSS** (`.css`)
  - **HTML** (`.html`, `.htm`)
  - **Python** (`.py`)
  - **Ruby** (`.rb`)
  - **Java** (`.java`)
  - **C/C++** (`.c`, `.cpp`, `.h`)
  - **C#** (`.cs`)
  - **Swift** (`.swift`)
  - **Go** (`.go`)
  - **Perl** (`.pl`, `.pm`)
  - **TypeScript** (`.ts`)
  - **Shell Scripts** (`.sh`, `.bash`)
  - **XML** (`.xml`)
  - **JSON** (`.json`)
  - **YAML** (`.yaml`, `.yml`)

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/combine-web-files.git
    cd combine-web-files
    ```

2. **Run the script:**

    Execute the script using Python:

    ```bash
    python combine_web_files.py
    ```

3. **Follow the prompts:**

    - Enter the root directory path where your files are located.
    - Enter the desired output file name (including the `.txt` extension).

4. **Output:**

    The script will create a `.txt` file containing all the contents of the specified file types, with each file's path and content clearly separated for easy readability.

## Example

If you have a directory with multiple subdirectories containing files of various types (e.g., `.php`, `.js`, `.py`), running this script will consolidate all these files into a single `.txt` file, making it easier to process with large language models or other text analysis tools.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
