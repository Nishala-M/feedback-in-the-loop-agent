
import json
import os

FEEDBACK_FILE = "feedback.json"


def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            return json.load(file)
    return []


def generate_response(request, feedback):
    latest_feedback = feedback[-1].lower() if feedback else ""

    if "short" in latest_feedback:
        style = "short"
    elif "detail" in latest_feedback or "long" in latest_feedback:
        style = "detailed"
    else:
        style = "simple"

    if "leave" in request.lower():
        if style == "short":
            return (
                "Subject: Leave Request\n\n"
                "I request leave for personal reasons. Thank you."
            )

        elif style == "detailed":
            return (
                "Subject: Leave Request\n\n"
                "Dear Manager,\n\n"
                "I am writing to request leave due to personal reasons. "
                "I would appreciate your approval for my leave. "
                "Please let me know if you need any additional information.\n\n"
                "Thank you for your understanding.\n\n"
                "Best regards"
            )

        else:
            return (
                "Subject: Leave Request\n\n"
                "I would like to request leave for personal reasons. Thank you."
            )

    return f"Here is a {style} response for your request: {request}"


def main():
    print("=== Feedback-in-the-Loop Agent ===")

    request = input("Enter your request: ").strip()

    if not request:
        print("Please enter a request.")
        return

    feedback = load_feedback()
    response = generate_response(request, feedback)

    print("\nAgent response:")
    print(response)

    user_feedback = input(
        "\nWhat should the agent improve next time? "
    ).strip()

    if user_feedback:
        feedback.append(user_feedback)

        with open(FEEDBACK_FILE, "w") as file:
            json.dump(feedback, file, indent=4)

        print("\nFeedback saved successfully!")
        print("The latest feedback will guide the next response.")
    else:
        print("\nNo feedback provided. Nothing was saved.")


if __name__ == "__main__":
    main()
