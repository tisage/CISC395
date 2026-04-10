In my Trip Notes project (run from trip_notes/):

- src/rag.py already exists with:
    search_guides(query: str, n_results: int = 3) -> list[str]
    (auto-builds the index if chroma_db/ is empty)

- src/ai_assistant.py already has:
    ask(prompt: str, system_prompt: str = None, temperature: float = 0.7) -> str

Add a function rag_ask(question: str) -> str to src/ai_assistant.py:

1. Import search_guides from src.rag
   (use: from src.rag import search_guides)

2. Call search_guides(question, n_results=3) to get relevant chunks

3. If chunks is empty or None:
   return "No guides found. Add .txt, .md, or .pdf files to guides/ and select [9] Rebuild index."

4. Join chunks with "\n\n---\n\n" as separator to form context

5. Build this system prompt (use an f-string):
   "You are a travel assistant. Answer the question using ONLY the context below.
    If the answer is not in the context, say: I don't have information about that in my guides.

    Context:
    {context}"

6. Call ask(question, system_prompt=rag_system_prompt) and return the result

Place rag_ask() after the existing ask() function.
Do not modify ask() or any existing code.
