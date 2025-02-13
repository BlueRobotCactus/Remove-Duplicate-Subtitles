# Remove Duplicated Subtitles in an SRT File

This script removes **identical consecutive subtitle blocks** from an `.srt` file.

## Requirements

* Python 3.x must be installed on your system. If you don’t have it, you can download it from python.org
* Works with UTF-8 encoded `.srt` files

## Usage

1. Place the `.srt` file you want to process in the same directory as `remove_duplicates.py`
2. Rename the file to `input.srt`
3. Open a command-line interface (ex: Terminal, Command Prompt, Git Bash, PowerShell)
4. Navigate to the directory containing the script
5. Run the script using:

   ```sh
   python remove_duplicates.py
   ```

6. The script creates a new `.srt` file with duplicate blocks removed, saved as `output.srt`

## Notes

* A block is only considered a duplicate if **both the text and timestamps are identical**.
* This script **does not** remove repeated lines that appear at different timestamps
* It **does not** remove repeated lines within the same subtitle block&mdash;only entire duplicate blocks
* The output file maintains correct subtitle numbering

## Example

### **Before (`input.srt`)**
```srt
1
00:00:01,500 --> 00:00:04,000
No, I am your father

2
00:00:01,500 --> 00:00:04,000
No, I am your father

3
00:00:04,500 --> 00:00:07,000
NOOOOOOOOOOO!
NOOOOOOOOOOO!

4
00:00:07,500 --> 00:00:10,000
No, I am your father

5
00:00:10,500 --> 00:00:13,000
No, I am your father
```

### **After (`output.srt`)**
```srt
1
00:00:01,500 --> 00:00:04,000
No, I am your father

2
00:00:04,500 --> 00:00:07,000
NOOOOOOOOOOO!
NOOOOOOOOOOO!

3
00:00:07,500 --> 00:00:10,000
No, I am your father

4
00:00:10,500 --> 00:00:13,000
No, I am your father
```

I realize this is a pretty niche issue, but I once downloaded a subtitle file that had every block duplicated so I made this to fix that. Hopefully it helps others who run into the same or similar problem.