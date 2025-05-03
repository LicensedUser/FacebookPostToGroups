import pyautogui
import webbrowser
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def locate_and_click(image, retries=3, confidence=0.85):
    for attempt in range(retries):
        try:
            coords = pyautogui.locateCenterOnScreen(image, confidence=confidence)
            if coords:
                pyautogui.click(coords)
                return True  # Success
            else:
                logging.warning(f"{image} not found, retrying ({attempt + 1}/{retries})...")
        except pyautogui.ImageNotFoundException:
            logging.error(f"Image '{image}' not found on screen (attempt {attempt + 1}/{retries}).")
        time.sleep(2)  # Wait between retries
    return False  # Failed after retries

# Settings
groups_per_batch = 20
total_groups = 200
batches = total_groups // groups_per_batch  # 10 batches
sleep_between_batches = 21600  # Sleep 1 minute between batches
batch_index = 0  # starts from batch 1
groupposted = 1  # Initialize the counter for group posting

while True:
    logging.info(f"\nStarting batch {batch_index + 1} of {batches}")
    
    # Start a loop for all the groups in the current batch
    for group_index in range(groups_per_batch):
        logging.info(f"\nPosting to group {group_index + 1} of batch {batch_index + 1}...")
        
        # Open the Facebook photo page
        webbrowser.open('https://www.facebook.com/photo/?fbid=122139342044597977&set=a.122139342236597977')
        time.sleep(20)  # Wait for the page to load
        
        # Retry locating and clicking the Share button
        if not locate_and_click("1.png"):
            logging.warning("Couldn't find 'Share' button, skipping group...")
            # Increment groupposted even if the share button is not found
            groupposted += 1
            if groupposted > total_groups:
                groupposted = 1  # Reset to 1 after reaching 200
            continue  # Skip to the next group
        
        time.sleep(10)

        # Retry locating and clicking the 'Groups' option
        if not locate_and_click("2.png"):
            logging.warning("Couldn't find 'Groups' option, skipping group...")
            # Increment groupposted even if the 'Groups' option is not found
            groupposted += 1
            if groupposted > total_groups:
                groupposted = 1  # Reset to 1 after reaching 200
            continue  # Skip to the next group
        
        time.sleep(20)

        # Calculate the dynamic number of Tab presses based on groupposted
        tab_offset = groupposted * 2
        logging.info(f"Pressing 'Tab' {tab_offset} times to reach this group...")

        # Press 'Tab' to get to the desired group
        for _ in range(tab_offset):
            pyautogui.press('tab')
            time.sleep(2)

        time.sleep(2)
        pyautogui.press('enter')  # Select the current group
        time.sleep(20)

        # Retry locating and clicking the 'Post' button (if needed)
        if not locate_and_click("3.png"):
            logging.warning("Couldn't find 'Post' button, skipping group...")
            # Increment groupposted even if the 'Post' option is not found
            groupposted += 1
            if groupposted > total_groups:
                groupposted = 1  # Reset to 1 after reaching 200
            continue  # Skip to the next group

        time.sleep(20)

        # Close the tab after posting
        pyautogui.hotkey('ctrl', 'w')  # Close the current tab
        
        # Increment groupposted after each group, even if it was skipped
        groupposted += 1
        if groupposted > total_groups:
            groupposted = 1  # Reset to 1 after reaching 200

    # Move to the next batch (wrap around if we've reached the last one)
    batch_index = (batch_index + 1) % batches

    logging.info(f"Sleeping {sleep_between_batches} seconds before starting next batch...")
    time.sleep(sleep_between_batches)
