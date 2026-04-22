Read src/models.py and src/storage.py first.

Create src/app.py — a Streamlit web app for Trip Notes.

---

## sys.path fix (required — add at the very top of the file)

```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

This ensures that `from src.ai_assistant import ...` resolves correctly when the file
is run as `streamlit run src/app.py` from the trip_notes/ directory.

---

## Imports

```python
import streamlit as st
from src.ai_assistant import ask, TRAVEL_SYSTEM_PROMPT
from src.storage import load_trips
```

Do NOT import run_agent, rag_ask, or ensure_index yet — those come in later exercises.

---

## Page config (must be the first Streamlit call)

```python
st.set_page_config(layout="wide", page_title="Trip Notes AI", page_icon="✈️")
```

---

## Session state initialization

Place this block immediately after the imports and page config:

```python
if "trips" not in st.session_state:
    st.session_state["trips"] = load_trips()
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "search_history" not in st.session_state:
    st.session_state["search_history"] = []
if "agent_history" not in st.session_state:
    st.session_state["agent_history"] = []
```

---

## Sidebar

```python
st.sidebar.title("✈️ Trip Notes AI")

trips = st.session_state["trips"]
trip_names = [t.name for t in trips] if trips else ["(no trips yet)"]
selected_name = st.sidebar.selectbox("📍 Current trip", trip_names)
current_trip = next((t for t in trips if t.name == selected_name), None)

# Notes display
if current_trip and current_trip.notes:
    with st.sidebar.expander(f"📋 Notes ({len(current_trip.notes)})"):
        for note in current_trip.notes:
            st.write(f"• {note}")
elif current_trip:
    st.sidebar.caption("No notes yet for this trip.")

# Briefing button
if st.sidebar.button("Generate Briefing"):
    if current_trip and current_trip.notes:
        with st.sidebar.spinner("Generating..."):
            notes_text = "\n".join(current_trip.notes)
            briefing_prompt = (
                f"Generate a concise travel briefing for {current_trip.name} "
                f"based on these traveler notes:\n{notes_text}"
            )
            result = ask(briefing_prompt, system_prompt=TRAVEL_SYSTEM_PROMPT)
        st.sidebar.markdown(result)
    else:
        st.sidebar.warning("Add some notes first.")
```

---

## Main area — three tabs

```python
tab1, tab2, tab3 = st.tabs(["💬 Chat", "🔍 Search", "🤖 Agent"])

with tab1:
    # Ex2: Chat tab will go here
    st.info("Coming soon — Exercise 2")

with tab2:
    # Ex3: Search tab will go here
    st.info("Coming soon — Exercise 3")

with tab3:
    # Ex4: Agent tab will go here
    st.info("Coming soon — Exercise 4")
```

---

## Notes

- Do not add any custom CSS or HTML.
- Do not import or reference run_agent or rag_ask in this file yet.
- The file should run cleanly with `streamlit run src/app.py` from the trip_notes/ directory.
- If load_trips() returns an empty list, the selectbox should show "(no trips yet)" and the briefing button should show the warning message.
