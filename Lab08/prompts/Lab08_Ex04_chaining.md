I have a Trip Notes CLI app. Read src/ai_assistant.py first.
It has ask() and TRAVEL_SYSTEM_PROMPT already defined.

Add a new function to src/ai_assistant.py:

generate_trip_briefing(destination_name: str, country: str) -> dict

This function makes two sequential API calls (prompt chaining):

Call 1 — Overview:
  prompt: f"Give a 3-sentence travel overview of {destination_name}, {country}.
            Cover: what it's like to visit, best season to go, and one must-see attraction."
  Use: system_prompt=TRAVEL_SYSTEM_PROMPT

Call 2 — Packing list (uses Call 1 output):
  prompt: f"Based on this destination overview:\n{overview}\n\n
            Write a 5-item packing list specific to {destination_name}."
  Use: system_prompt=TRAVEL_SYSTEM_PROMPT

Return: {"overview": overview, "packing_list": packing_list}

If either call returns None (API error), return None.

Also update the if __name__ == "__main__" block to test generate_trip_briefing:
  result = generate_trip_briefing("Tokyo", "Japan")
  if result:
      print("Overview:", result["overview"])
      print("Packing list:", result["packing_list"])

Write the updated file directly to src/ai_assistant.py.
