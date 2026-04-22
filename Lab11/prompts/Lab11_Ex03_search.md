Read src/app.py first.

In src/app.py, replace the `st.info("Coming soon — Exercise 3")` line inside the Search tab (tab2) with a RAG search interface. Do not change tab1, tab3, or the sidebar.

---

## New imports to add at the top of app.py

Add these two lines to the import block if they are not already present:

```python
from src.ai_assistant import rag_ask
from src.rag import ensure_index
```

---

## Call ensure_index() at startup

Add this line immediately after the session state initialization block (before the sidebar code). This builds or loads the RAG index once when the app starts, so it is ready before any tab renders:

```python
ensure_index()
```

---

## Search tab (tab2) replacement

```python
with tab2:
    st.subheader("Search My Guides")
    st.caption("Answers grounded in your guides/ documents.")

    # Display search history
    for msg in st.session_state["search_history"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Handle new input
    search_input = st.chat_input("Search your guides...", key="search_input")
    if search_input:
        st.session_state["search_history"].append({"role": "user", "content": search_input})
        with st.chat_message("user"):
            st.write(search_input)
        with st.chat_message("assistant"):
            with st.spinner("Searching guides..."):
                response = rag_ask(search_input)
            st.write(response)
        st.session_state["search_history"].append({"role": "assistant", "content": response})

    # Clear button
    if st.button("Clear search", key="clear_search"):
        st.session_state["search_history"] = []
        st.rerun()
```

---

## Notes

- `st.chat_input` requires a unique `key` parameter when used in multiple tabs (`"search_input"` here; tab1 uses the default key).
- `st.button` also needs a unique key (`"clear_search"` here vs `"clear_chat"` in tab1).
- `ensure_index()` should be called exactly once at module level, not inside the tab block.
- The Search tab uses `st.session_state["search_history"]` — a separate list from `"chat_history"` — so clearing one tab does not affect the other.
- Do not change tab1, tab3, or the sidebar section.
- After saving, run `streamlit run src/app.py`. The first load may take a few seconds while ensure_index() builds the index. Subsequent loads will be faster.
