from Get import get_all_courses, Course # for Course dataclass + pymongo access
import argparse                         # for command line arguments
from rich import console                # for console input/output
from rapidfuzz import fuzz              # for fuzzy matching


console = console.Console(width=100)

def find_keyword_strict(keyword: str, course: Course) -> str:
    """
    For a single course, find the keyword in the course transcript.
    """
    if keyword.lower() in course.course_title.lower():
        return course.course_title
    if keyword.lower() in course.metadata['Course Description'].lower():
        return course.course_title
    if keyword.lower() in course.course_TOC_verbose.lower():
        return course.course_title
    if keyword.lower() in course.course_transcript.lower():
        return course.course_title

def find_keyword_fuzzy(keyword, course, threshold=70):
    """
    For a single course, perform fuzzy matching of the keyword in the course transcript.
    """
    for text in [
        course.course_title,
        course.metadata['Course Description'],
        course.course_TOC_verbose,
        course.course_transcript
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
        if args.fuzzy:
            return find_keyword_fuzzy(keyword, course)
        else:
            return find_keyword_strict(keyword, course)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a keyword in course transcripts.")
    parser.add_argument("keyword", type=str, nargs = "?", help="The keyword to search for in course transcripts.")
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
                keyword = console.input("[green]Enter a keyword to search for in course transcripts: [/green]")
            if keyword == "exit":
                break
            if keyword == "fuzzy":
                fuzzy = not fuzzy # Toggle setting
                print(f"Fuzzy matching set to {fuzzy}")
                keyword = ""
                continue
            for course in courses:
                found = find_keyword(keyword, course, fuzzy)
                if found:
                    console.print(found)
            keyword = ""
    else:
        for course in courses:
            found = find_keyword(keyword, course, fuzzy)
            if found:
                console.print(found)





