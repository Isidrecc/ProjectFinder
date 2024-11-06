#FIRST VERSION OF THE CRAWLSPIDER ONLY WITH ONE URL
#IN THE NEXT STEP WE WILL FEED THE CRAWLSPIDER WITH THE RESULT OF THE FILE 1_DeepLinks.py
#FOR FURTHER STEPS WE WILL ALSO TRY TO DOWNLOAD ALL THE PDFs IN EVERY URLs


import subprocess
import os
import sys


def run_deep_links():
    try:
        # Running DeepLinks.py
        print("Running 1_DeepLinks.py...")
        subprocess.run([sys.executable, '1_DeepLinks.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run DeepLinks.py: {e}")
        sys.exit(1)


def run_project_finder():
    try:
        # Running ProjectFinder.py with Scrapy
        print("Running 2_ProjectFinder.py using Scrapy...")
        #subprocess.run(['scrapy', 'runspider', '2_ProjectFinder.py'], check=True)
        subprocess.run([sys.executable, '-m', 'scrapy', 'runspider', '2_ProjectFinder.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run ProjectFinder.py: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Scrapy executable not found: {e}")
        sys.exit(1)


def run_json_to_csv():
    try:
        # Running json2csv.py
        print("Running 3_json2csv.py...")
        subprocess.run([sys.executable, '3_json2csv.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run json2csv.py: {e}")
        sys.exit(1)


def main():
    # Change to the directory containing the scripts (if needed)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    # Run the scripts sequentially
    run_deep_links()
    run_project_finder()
    run_json_to_csv()


if __name__ == "__main__":
    main()