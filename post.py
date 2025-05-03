This Python script automates the process of sharing a Facebook photo post to multiple Facebook groups using screen automation via pyautogui. The workflow is divided into batches, each targeting a set number of groups per cycle. The script performs the following tasks:

    Opens a specific Facebook photo URL in the default web browser.

    Clicks on the 'Share' button, then selects the 'Share to Groups' option.

    Uses tab navigation to reach a specific group based on a counter and simulates an Enter key press to select it.

    Clicks the 'Post' button to share the content.

    Closes the browser tab after posting.

    Repeats this process for a specified number of groups, organized into batches.

    Sleeps for a predefined duration between batches (default: 6 hours).

    Logs each action, including retries and any failures, to assist with debugging or tracking.

The script includes retry logic for image recognition, logging for process tracking, and a counter to maintain the correct group targeting across iterations.

    ⚠️ Note: This script relies on image-based UI automation and may be affected by screen resolution, browser zoom, or UI changes on Facebook. It is your responsibility to ensure compliance with Facebook's terms of service and to use automation ethically.
