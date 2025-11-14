import sys
import os
from string import Template

# ---------- config ----------
TEMPLATE_FILE = 'leetcode_skeleton.txt'
# ----------------------------

def usage():
    print('usage: python gen.py <number> "<dash-separated-title>"')
    sys.exit(1)

def main():
    if len(sys.argv) == 3:
        # Use command line arguments
        num, title = sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 1:
        # No arguments provided, get input from console
        print("Please enter the LeetCode problem details:")
        num = input("Problem number: ").strip()
        title = input("Problem title (dash-separated): ").strip()
    else:
        usage()

    # Validate input
    if not num.isdigit():
        print("Error: Problem number must be a digit.")
        sys.exit(1)
    
    # Format the number to 4 digits with leading zeros
    num = num.zfill(4)

    if not title.replace('-', '').replace('_', '').isalnum():
        usage()

    # Create problems directory if it doesn't exist
    problems_dir = 'problems'
    if not os.path.exists(problems_dir):
        os.makedirs(problems_dir)
    
    filename = os.path.join(problems_dir, f'{num}_{title}.py')

    if not os.path.isfile(TEMPLATE_FILE):
        print(f'Template file "{TEMPLATE_FILE}" not found.')
        sys.exit(1)

    with open(TEMPLATE_FILE, encoding='utf-8') as f:
        tmpl = Template(f.read())

    content = tmpl.safe_substitute(
        NUMBER=num,
        TITLE=title,
        TITLE_SNAKE=title.replace('-', '_'),
        TITLE_CAMEL=' '.join(w.capitalize() for w in title.split('-'))
    )

    if os.path.exists(filename):
        print(f'File "{filename}" already exists – aborting.')
        sys.exit(1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Created {filename}')

if __name__ == '__main__':
    main()