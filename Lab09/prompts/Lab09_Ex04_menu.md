In my Trip Notes project, src/main.py already has a menu with options [1] through [7].

src/ai_assistant.py now has both ask() and rag_ask().
src/rag.py has build_index(force=False) and search_guides().

Add two new menu options to src/main.py:

[8] Search my guides
  - Display label: "[8] Search my guides"
  - Prompt the user: "Your question: "
  - Call rag_ask(question) from src.ai_assistant
  - Print the returned answer
  - Note: search_guides() inside rag_ask() automatically builds the index
    if chroma_db/ is empty — no manual step needed

[9] Rebuild search index
  - Display label: "[9] Rebuild search index"
  - Print: "Rebuilding index from guides/..."
  - Call build_index(force=True) from src.rag
  - Print: "Done. Use [8] to search your updated guides."

Required imports to add:
  from src.ai_assistant import rag_ask
  from src.rag import build_index

Keep all existing menu options [1]–[7] completely unchanged.
Update the menu display to include the two new options.
