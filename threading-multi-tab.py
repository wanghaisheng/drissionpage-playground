import threading
import time
from queue import Queue
from DrissionPage import ChromiumOptions, WebPage

# Semaphore to limit concurrency
semaphore = threading.Semaphore(5)  # Allow up to 5 concurrent tasks

def tab_worker(task_id, page):
    with semaphore:
        print(f"Task {task_id} started")

        # Perform some work synchronously (simulated with sleep)
        time.sleep(1)

        # Create a new tab and perform actions
        tab = page.new_tab()
        tab.get('https://baidu.com')  # Replace with your actual synchronous method
        title = tab.title  # Replace with your actual synchronous method
        print(f"Page title: {title}")

        # Close the tab
        tab.close()

        print(f"Task {task_id} completed")

def get_session():
    co = ChromiumOptions()
    co.auto_port()
    co.headless(False)
    browser_path = r"C:\Users\Administrator\AppData\Local\ms-playwright\chromium-1124\chrome-win\chrome.exe"
    co.set_paths(browser_path=browser_path)

    page = WebPage(chromium_options=co)
    return page

def run_tasks():
    page = get_session()

    # Create threads for each task
    threads = []
    for i in range(1, 10):
        thread = threading.Thread(target=tab_worker, args=(i, page))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Clean up: close the browser instance
    page.quit()

def main():
    start_time = time.time()

    # Run the tasks
    run_tasks()

    # Calculate and print the total execution time
    print(f"Time taken for execution with concurrency limited by semaphore: {time.time() - start_time} seconds")

if __name__ == "__main__":
    main()
