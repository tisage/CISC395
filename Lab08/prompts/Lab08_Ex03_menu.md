I have a Trip Notes CLI app. Read src/main.py and src/ai_assistant.py first.

src/main.py has a working menu loop with options [1]–[5].
src/ai_assistant.py has ask() and TRAVEL_SYSTEM_PROMPT.

Update src/main.py to add option [6] Ask AI:

1. Add to imports at the top:
   from src.ai_assistant import ask, TRAVEL_SYSTEM_PROMPT

2. Add "[6] Ask AI a travel question" to the menu display.

3. Add a handler for choice "6":
   a. Input: "Your question: "
   b. Call ask(question, system_prompt=TRAVEL_SYSTEM_PROMPT)
   c. If the result is None (API error), print an error message and return to menu
   d. Print the AI response
   e. Ask: "Save this as a note on a trip? (y/n): "
   f. If "y":
      - Print all saved trips numbered (use collection.get_all())
      - Input: "Trip number: " (convert to int, subtract 1 for index)
      - Get the trip with collection.get_by_index(index)
      - Call trip.add_note(response)
      - Call save_trips(collection)
      - Print: "Saved as a note on [trip name]."
   g. If "n": return to menu

Write the updated file directly to src/main.py.
