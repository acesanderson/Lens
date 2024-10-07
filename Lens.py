"""
This uses my MongoDB Courses database, either on MacOS or SSH tunnel from Windows.
A portable version of this would likely use SQLite.
"""

from Get import get_all_courses, Course # for Course dataclass + pymongo access
import argparse                         # for command line arguments
from rich import console                # for console input/output
from rapidfuzz import fuzz              # for fuzzy matching

console = console.Console(width=100)

def find_keyword_strict(keyword: str, course: Course) -> str:
    """
    For a single course, find the keyword in the course metadata + TOC.
    """
    if keyword.lower() in course.course_title.lower():
        return course.course_title
    if keyword.lower() in course.metadata['Course Description'].lower():
        return course.course_title
    if keyword.lower() in course.course_TOC_verbose.lower():
        return course.course_title

def find_keyword_fuzzy(keyword, course, threshold=70):
    """
    For a single course, perform fuzzy matching of the keyword in the course metadata + TOC.
    """
    for text in [
        course.course_title,
        course.metadata['Course Description'],
        course.course_TOC_verbose,
    ]:
        match_score = fuzz.partial_ratio(keyword.lower(), text.lower())
        if match_score >= threshold:
            return course.course_title
    return None

def find_keyword(keyword, course, fuzzy = False):
    """
    For a single course, find the keyword in the course transcript.
    """
    if keyword:
        if fuzzy:
            return find_keyword_fuzzy(keyword, course)
        else:
            return find_keyword_strict(keyword, course)

def Lens(keyword: str, courses: list, fuzzy: bool = False):
    """
    Importable function to search for a keyword in course data.
    If you import, you also want to import get_all_courses, and run
    `courses = get_all_courses()` before calling this function.
    """
    output = []
    for course in courses:
        found = find_keyword(keyword, course, fuzzy)
        if found:
            console.print(found)
            output.append(found)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a keyword in course data.")
    parser.add_argument("keyword", type=str, nargs = "?", help="The keyword to search for in course data.")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode.")
    parser.add_argument("-f", "--fuzzy", action="store_true", help="Fuzzy match.")
    args = parser.parse_args()
    keyword = args.keyword
    with console.status("[green]Loading courses...[/green]", spinner="dots"):
        courses = get_all_courses()
    if args.fuzzy:
        fuzzy = True
    else:
        fuzzy = False
    if args.interactive:
        while True:
            if keyword:
                console.print(f"[green]Searching for keyword: {keyword}[/green]")
            else:
                keyword = console.input("[green]Enter a keyword to search for in course data: [/green]")
            if keyword == "exit":
                break
            if keyword == "fuzzy":
                fuzzy = not fuzzy # Toggle setting
                console.print(f"Fuzzy matching set to {fuzzy}")
                keyword = ""
                continue
            output = Lens(keyword=keyword, courses=courses, fuzzy=fuzzy)
            keyword = ""
    else:
        output = Lens(keyword=keyword, courses=courses, fuzzy=fuzzy)
        




