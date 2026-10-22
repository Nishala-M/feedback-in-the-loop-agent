# Feedback-in-the-Loop Agent

## Overview
A beginner-friendly Python project that demonstrates how an agent can save user feedback and use the latest feedback to adjust future responses.

## Workflow
1. The user submits a request.
2. The agent generates a response.
3. The user provides feedback about how the response should improve.
4. The agent saves the feedback in a JSON file.
5. On the next run, the agent uses the latest feedback to choose a response style.

## Features
- Generates simple responses for leave-request prompts.
- Accepts feedback from the user.
- Saves feedback in `feedback.json`.
- Uses the latest feedback to select short or detailed responses.
- Retains feedback between program runs.

## Technologies Used
- Python 3
- JSON
- File handling
- Conditional statements
- Functions

## How to Run
1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

   ```bash
   python main.py
   ```

4. Enter a request, such as `write a leave request`.
5. Provide feedback when prompted.
6. Run the program again to see how saved feedback affects the response.

## Example Feedback
```text
write response in detailed way
```

The program saves the feedback and can use it to generate a more detailed leave-request response on the next run.

## Learning Objective
Understand a basic feedback loop in which user feedback is stored and influences later program behavior.

**Note:** This is a rule-based Python simulation. It does not train an AI model or independently understand arbitrary feedback.

## Author
Nishala M.