Read src/app.py first.

Replace the `st.info("Coming soon — Exercise 2")` placeholder inside the Chat tab with a working chat interface. Do not modify the sidebar, tab2, or tab3.

---

## Layout

```
💬 Chat  │  🔍 Search  │  🤖 Agent

Chat with AI
General travel assistant — ask anything.

┌──────────────────────────────────────────────┐
│  👤  What are good things to pack for a      │
│      rainy-season trip to Southeast Asia?    │
│                                              │
│  🤖  Great question! For rainy season...     │
│                                              │
│  👤  Which of those also work for cold       │
│      mountain trips?                         │
│                                              │
│  🤖  For colder mountain conditions...       │
└──────────────────────────────────────────────┘

[ Ask about travel...                     ↵ ]   ← pinned at bottom of tab

[ Clear chat ]
```

---

## Behavior requirements

- Display all messages in `st.session_state["chat_history"]` as a conversation using `st.chat_message` with the message's role (`"user"` or `"assistant"`)
- Accept new input via `st.chat_input` — it renders pinned at the bottom of the tab automatically
- When the user submits a message:
  1. Append the user message to `"chat_history"`
  2. Call `ask(user_input, system_prompt=TRAVEL_SYSTEM_PROMPT)` with a spinner showing "Thinking..."
  3. Display the assistant response immediately
  4. Append the assistant response to `"chat_history"`
- "Clear chat" button: clears `st.session_state["chat_history"]` and reruns the app

---

## Critical constraints

- `ask` and `TRAVEL_SYSTEM_PROMPT` are already imported in Exercise 1 — do not add duplicate imports
- `st.chat_input` and `st.button` each need a unique `key` parameter because Streamlit requires all interactive widgets to have unique keys across the whole page — use `key="clear_chat"` for the button
- Do NOT use `key=` on `st.chat_input` in tab1 (leave it as the default); tabs 2 and 3 will need explicit keys
- Do not change the sidebar, tab2, or tab3 code
