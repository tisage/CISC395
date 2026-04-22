Read src/app.py first.

In src/app.py, replace the `st.info("Coming soon — Exercise 2")` line inside the Chat tab (tab1) with a full chat interface. Do not change tab2, tab3, or the sidebar.

---

## Chat tab (tab1) replacement

```python
with tab1:
    st.subheader("Chat with AI")
    st.caption("General travel assistant — ask anything.")

    # Display chat history
    for msg in st.session_state["chat_history"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Handle new input
    user_input = st.chat_input("Ask about travel...")
    if user_input:
        st.session_state["chat_history"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask(user_input, system_prompt=TRAVEL_SYSTEM_PROMPT)
            st.write(response)
        st.session_state["chat_history"].append({"role": "assistant", "content": response})

    # Clear button
    if st.button("Clear chat", key="clear_chat"):
        st.session_state["chat_history"] = []
        st.rerun()
```

---

## Notes

- `ask` and `TRAVEL_SYSTEM_PROMPT` are already imported from src.ai_assistant in Exercise 1 — do not add duplicate imports.
- `st.chat_input` renders pinned at the bottom of the tab area automatically.
- The `key="clear_chat"` parameter is required because there will be buttons in other tabs; Streamlit requires unique keys across all buttons on the page.
- Do not change tab2, tab3, or the sidebar section.
- After saving, run `streamlit run src/app.py` and verify that typing a message shows both the user bubble and the assistant response, and that clicking "Clear chat" removes all messages.
