Read src/app.py first.

In src/app.py, replace the `st.info("Coming soon — Exercise 4")` line inside the Agent tab (tab3) with a ReAct agent interface. Do not change tab1, tab2, or the sidebar.

---

## New import to add at the top of app.py

Add this line to the import block if it is not already present:

```python
from src.tools import run_agent, TOOL_DEFINITIONS
```

---

## Agent tab (tab3) replacement

```python
with tab3:
    st.subheader("AI Travel Agent")
    st.caption("The agent uses tools: budget calculation, live weather, and guide search.")

    # Question input
    question = st.text_area(
        "Your question:",
        placeholder="e.g. I have $1200 for 8 days in Tokyo. Check the weather and break down my budget.",
        key="agent_question",
    )

    # Submit button
    if st.button("Ask the Agent") and question.strip():
        with st.spinner("Agent is working..."):
            answer = run_agent(question)

        st.markdown(answer)

        # Show which tools are available
        tool_names = [t["function"]["name"] for t in TOOL_DEFINITIONS]
        with st.expander("Tools available to this agent"):
            for name in tool_names:
                st.write(f"• {name}")

        # Save to history
        st.session_state["agent_history"].append({
            "question": question,
            "answer": answer,
        })

    # Previous queries (all except the one just added, shown newest-first)
    if st.session_state["agent_history"]:
        previous = st.session_state["agent_history"][:-1] if question.strip() else st.session_state["agent_history"]
        if previous:
            st.divider()
            st.caption("Previous queries this session:")
            for item in reversed(previous):
                label = item["question"][:60] + "..." if len(item["question"]) > 60 else item["question"]
                with st.expander(f"Q: {label}"):
                    st.write(item["answer"])
```

---

## Notes

- `run_agent()` prints `[Tool call]` and `[Tool result]` lines to the terminal where you ran `streamlit run`. These do not appear in the browser — that is expected.
- `TOOL_DEFINITIONS` is the list of tool schemas defined in tools.py. We read the function names from it to show the user which tools the agent can call.
- The agent tab uses a `st.text_area` (not `st.chat_input`) because agent questions are typically longer and benefit from a resizable box.
- `st.button("Ask the Agent")` does not need a key because it is the only button in tab3.
- Do not change tab1, tab2, or the sidebar section.
- After saving, run `streamlit run src/app.py`, go to the Agent tab, and test with a compound question like: "I have $1500 for 10 days in Paris. Check the weather there and break down my budget." Watch the terminal for tool call output while the spinner is running in the browser.
