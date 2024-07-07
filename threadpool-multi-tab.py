import concurrent.futures
import time
from DrissionPage import ChromiumOptions, WebPage

# Example synchronous task (replace with your actual synchronous code)
def synchronous_task(task_id, page):
    print(f"Synchronous task {task_id} started")
    tab = page.new_tab()
    tab.get('https://baidu.com')
    title = tab.title
    print(f"Page title: {title}")
    tab.close()
    print(f"Synchronous task {task_id} completed")

# Function to initialize and return a WebPage instance
def get_session():
    co = ChromiumOptions()
    co.auto_port()
    co.headless(False)
    browser_path = r"C:\Users\Administrator\AppData\Local\ms-playwright\chromium-1124\chrome-win\chrome.exe"
    co.set_paths(browser_path=browser_path)

    page = WebPage(chromium_options=co)
    return page

# Function to run synchronous tasks using threading
def run_synchronous_tasks(page):
    # Create a list of tasks (functions)
    tasks = [lambda i=i: synchronous_task(i, page) for i in range(1, 10)]

    # Execute tasks concurrently using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda task: task(), tasks)

# Main function to coordinate tasks and manage resources
def main():
    start_time = time.time()

    # Get the WebPage instance
    page = get_session()

    try:
        # Run synchronous tasks concurrently using threading
        run_synchronous_tasks(page)

    finally:
        # Clean up: close the browser instance
        page.quit()

    # Calculate and print the total execution time
    print(f"Time taken for execution: {time.time() - start_time} seconds")

# Entry point to start the script
if __name__ == "__main__":
    main()
