# FastAPI Tab Content Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fill the empty FastAPI tab in `index.html` with the RAG API lesson from `fastapi_rag_lesson.html`, using the same Block/TOC/`.say`/`.cb` pattern as the Streams tab.

**Architecture:** Replace the empty `#panel-fastapi` element with a Streams-style `page` shell (sticky TOC + `main.content`). Port narration and code into Blocks 0–7. Rely on existing `initSectionToc({ panelId: "panel-fastapi", ... })` and `.cb` copy wiring; do not add new CSS/JS or touch other tabs.

**Tech Stack:** Static HTML in `index.html`; content source `fastapi_rag_lesson.html`; no new dependencies.

**Spec:** `docs/superpowers/specs/2026-11-11-fastapi-tab-content-design.md`

---

## File map

| File | Role |
|------|------|
| `index.html` | **Modify only** `#panel-fastapi` (currently empty `div` around lines 2217–2223). Keep attributes `id`, `role`, `aria-labelledby`, `hidden`. |
| `fastapi_rag_lesson.html` | **Read-only source** for narration text and code snippets. Do not edit. |
| Other tabs / `<script>` / CSS | **Do not modify.** |

---

### Task 1: Panel shell, title, Block 0 (overview)

**Files:**
- Modify: `index.html` (`#panel-fastapi`)
- Source: `fastapi_rag_lesson.html` sections `#overview` (lines ~48–66)

- [ ] **Step 1: Replace the empty FastAPI panel with the Streams-style shell + Block 0**

Find this exact block:

```html
    <div
      class="tab-panel"
      id="panel-fastapi"
      role="tabpanel"
      aria-labelledby="tab-fastapi"
      hidden
    ></div>
```

Replace with:

```html
    <div
      class="tab-panel"
      id="panel-fastapi"
      role="tabpanel"
      aria-labelledby="tab-fastapi"
      hidden
    >
      <div class="page">
        <aside class="toc" id="toc-fastapi">
          <div class="toc-bar">
            <button
              type="button"
              id="toc-fastapi-toggle"
              aria-expanded="false"
              aria-controls="nav-fastapi"
            >
              Contents
            </button>
            <button
              type="button"
              id="toc-fastapi-close"
              aria-label="Close contents"
            >
              Close
            </button>
          </div>
          <nav id="nav-fastapi" aria-label="FastAPI RAG API sections"></nav>
        </aside>

        <main class="content">
          <h1>Building a RAG API with FastAPI</h1>
          <p class="lead">
            FastAPI · Pydantic · LangGraph · Intermediate. Turn the existing
            Python RAG script into an HTTP API with
            <code>POST /index</code> and <code>POST /ask</code>, without
            redesigning the retrieval or generation pipeline.
          </p>

          <!-- BLOCK 0 -->
          <section id="fastapi-overview">
            <h2>Block 0. What we are going to build</h2>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                In the previous lesson, we built a RAG pipeline that downloads a
                website, splits its content into chunks, stores embeddings in
                ChromaDB, retrieves relevant chunks and generates an answer with
                LangGraph and a local Ollama model.
              </p>
              <p>
                In this lesson, we do not redesign that pipeline. We add a thin
                HTTP layer with FastAPI so another application can call it.
              </p>
              <p>
                We will expose two endpoints:
                <code>POST /index</code> to download and index the configured
                source URL, and <code>POST /ask</code> to accept a question and
                return the answer plus source URLs.
              </p>
              <p>
                <strong>Teaching focus:</strong> FastAPI exposes the existing
                Python functions. LangGraph remains responsible for the RAG
                workflow; ChromaDB remains the vector store.
              </p>
            </div>

            <h3>Suggested video breakdown</h3>
            <table>
              <thead>
                <tr>
                  <th>Video</th>
                  <th>Content</th>
                  <th>Approx.</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. Introduction to FastAPI</td>
                  <td>
                    Why expose the RAG pipeline through HTTP; endpoints,
                    requests and responses.
                  </td>
                  <td>5–7 min</td>
                </tr>
                <tr>
                  <td>2. Setup and Pydantic models</td>
                  <td>
                    Install FastAPI; create the app and request/response
                    schemas.
                  </td>
                  <td>6–8 min</td>
                </tr>
                <tr>
                  <td>3. Indexing endpoint</td>
                  <td>
                    Adapt <code>index_documents()</code> to return a useful
                    result and expose <code>POST /index</code>.
                  </td>
                  <td>6–8 min</td>
                </tr>
                <tr>
                  <td>4. Ask endpoint</td>
                  <td>
                    Reuse the LangGraph invocation and expose
                    <code>POST /ask</code>.
                  </td>
                  <td>7–9 min</td>
                </tr>
                <tr>
                  <td>5. Run and test</td>
                  <td>
                    Start the server and test both endpoints in Swagger UI.
                  </td>
                  <td>5–7 min</td>
                </tr>
              </tbody>
            </table>
          </section>

          <!-- remaining blocks added in later tasks -->
        </main>
      </div>
    </div>
```

- [ ] **Step 2: Verify shell IDs and Block 0 exist**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
html = Path('/Users/pavel/work/COURSE/html_web_courses_en/index.html').read_text()
needed = [
  'id="panel-fastapi"',
  'id="toc-fastapi"',
  'id="toc-fastapi-toggle"',
  'id="toc-fastapi-close"',
  'id="nav-fastapi"',
  'id="fastapi-overview"',
  'Building a RAG API with FastAPI',
]
missing = [s for s in needed if s not in html]
print('MISSING', missing if missing else 'none')
assert not missing
# panel must not be empty self-closing style
start = html.index('id="panel-fastapi"')
chunk = html[start:start+800]
assert 'toc-fastapi' in chunk
print('OK Task 1')
PY
```

Expected: `MISSING none` and `OK Task 1`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "$(cat <<'EOF'
Add FastAPI tab shell and overview block.

EOF
)"
```

---

### Task 2: Blocks 1–2 (intro + setup/models)

**Files:**
- Modify: `index.html` (inside `#panel-fastapi` `main.content`, after Block 0)
- Source: `fastapi_rag_lesson.html` `#video1`, `#video2` (lines ~68–133)

- [ ] **Step 1: Insert Block 1 and Block 2 before `</main>` inside the FastAPI panel**

Insert this HTML after the Block 0 `</section>` and before `</main>`:

```html
          <!-- BLOCK 1 -->
          <section id="fastapi-intro">
            <h2>Block 1. Introduction to FastAPI</h2>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                In the previous lesson, we built a complete RAG pipeline using
                Python, LangChain, LangGraph, ChromaDB, and Ollama.
              </p>
              <p>
                Our application can already do two important things: index
                information from a website and answer questions using the
                indexed content.
              </p>
              <p>
                But there is one limitation: everything currently runs inside a
                Python script. We interact with the application through the
                terminal, which is not very convenient when we want to integrate
                it with other applications.
              </p>
              <p>
                In this lesson, we're going to solve this problem. We'll use
                FastAPI to turn our existing Python application into an HTTP
                API.
              </p>
              <p>
                Instead of calling Python functions directly, we'll expose them
                through HTTP endpoints. We'll create <code>POST /index</code> to
                index documents and <code>POST /ask</code> to send a question
                and receive an answer with its sources.
              </p>
              <p>
                We'll also use Pydantic to validate incoming requests and define
                the structure of our API responses.
              </p>
              <p>
                We won't change the RAG logic itself. We'll simply wrap our
                existing functionality with FastAPI. By the end of this lesson,
                we'll have a working RAG API that can be integrated into a
                frontend application or used by other backend services and AI
                agents.
              </p>
              <p>
                <strong>Before:</strong>
                <code>Terminal → Python script → RAG pipeline</code>
              </p>
              <p>
                <strong>After:</strong>
                <code>HTTP request → FastAPI → RAG pipeline → HTTP response</code>
              </p>
            </div>
          </section>

          <!-- BLOCK 2 -->
          <section id="fastapi-setup">
            <h2>Block 2. Setup and Pydantic models</h2>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                Before writing our API, we need to install FastAPI. We'll keep
                using the same project and the same <code>main.py</code> file
                from the previous lesson.
              </p>
              <p>
                Run the following command in the terminal. The
                <code>standard</code> extra includes the standard dependencies
                and CLI tooling we'll use to run the development server.
              </p>
            </div>

            <div class="cb">
              <span class="lang">bash</span>
              <pre><code>uv add "fastapi[standard]"</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                FastAPI uses Pydantic for request validation. Pydantic models
                describe the data our API expects and validate incoming requests
                automatically. For example, our question must be a string with a
                sensible length, and whitespace-only input should be rejected.
              </p>
            </div>

            <h3>1. Add the imports</h3>
            <div class="cb">
              <span class="lang">python</span>
              <pre><code>from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator</code></pre>
            </div>

            <h3>2. Create the FastAPI application</h3>
            <div class="cb">
              <span class="lang">python</span>
              <pre><code>app = FastAPI(
    title="RAG API",
    description="RAG application built with LangGraph and ChromaDB",
    version="1.0.0",
)</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                The <code>app</code> object is the entry point for incoming HTTP
                requests. The title and description will also appear in the
                generated API documentation.
              </p>
            </div>

            <h3>3. Define request and response models</h3>
            <div class="cb">
              <span class="lang">python</span>
              <pre><code>class AskRequest(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=2000,
        description="Question to ask the RAG system",
    )

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Question cannot be empty")

        return value


class AskResponse(BaseModel):
    answer: str
    sources: list[str]


class IndexResponse(BaseModel):
    message: str
    indexed_chunks: int</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                <code>BaseModel</code> defines a schema, <code>Field</code> adds
                constraints and documentation, and
                <code>field_validator</code> lets us add custom validation.
                Invalid request data is rejected by FastAPI with HTTP 422 before
                the endpoint function runs.
              </p>
              <p>
                <strong>Version note:</strong> This example uses Pydantic v2
                syntax: <code>field_validator</code>. It is not the older
                Pydantic v1 <code>validator</code> decorator.
              </p>
            </div>
          </section>
```

- [ ] **Step 2: Verify Blocks 1–2**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
html = Path('/Users/pavel/work/COURSE/html_web_courses_en/index.html').read_text()
for s in ['id="fastapi-intro"', 'id="fastapi-setup"', 'uv add "fastapi[standard]"', 'class AskRequest(BaseModel):', 'field_validator']:
    assert s in html, s
print('OK Task 2')
PY
```

Expected: `OK Task 2`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "$(cat <<'EOF'
Add FastAPI intro and setup blocks.

EOF
)"
```

---

### Task 3: Blocks 3–4 (index + ask endpoints)

**Files:**
- Modify: `index.html` (after Block 2, before `</main>`)
- Source: `fastapi_rag_lesson.html` `#video3`, `#video4` (lines ~135–237)

- [ ] **Step 1: Insert Block 3 and Block 4**

```html
          <!-- BLOCK 3 -->
          <section id="fastapi-index">
            <h2>Block 3. Indexing endpoint</h2>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                Now let's create our first API endpoint. Remember the
                <code>index_documents()</code> function from the previous
                lesson? It already downloads the website, splits the content
                into chunks, generates embeddings and stores everything in
                ChromaDB.
              </p>
              <p>
                We don't need to rewrite that logic. We only need to make one
                small change: previously, the function printed the number of
                indexed chunks to the terminal. An API needs to return data, so
                we'll return that number from the function and use it in the
                HTTP response.
              </p>
            </div>

            <h3>1. Change the existing function</h3>
            <div class="say">
              <b class="t">Narration</b>
              <p>
                Replace the old <code>index_documents()</code> function with
                this version. The indexing steps stay the same; the function now
                returns the number of chunks.
              </p>
            </div>

            <div class="cb">
              <span class="lang">python</span>
              <pre><code>def index_documents() -> int:
    documents = load_data(SOURCE_URL)
    chunks = split_documents(documents)

    ids = [
        hashlib.sha256(
            f"{chunk.metadata['source']}:{i}:{chunk.page_content}".encode()
        ).hexdigest()
        for i, chunk in enumerate(chunks)
    ]

    vector_store.add_documents(
        documents=chunks,
        ids=ids,
    )

    print(f"Indexed {len(chunks)} chunks from {SOURCE_URL}")

    return len(chunks)</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                <strong>Why change it?</strong> The HTTP endpoint needs a value
                it can put into its response. Returning
                <code>len(chunks)</code> makes the function reusable from both
                an API endpoint and other Python code. The print statement is
                retained as a helpful server log, but it is no longer the only
                output.
              </p>
            </div>

            <h3>2. Add the endpoint</h3>
            <div class="cb">
              <span class="lang">python</span>
              <pre><code>@app.post(
    "/index",
    response_model=IndexResponse,
)
def index_endpoint():
    try:
        indexed_chunks = index_documents()

        return IndexResponse(
            message="Documents indexed successfully",
            indexed_chunks=indexed_chunks,
        )

    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail=f"Failed to download source: {error}",
        ) from error

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Indexing failed: {error}",
        ) from error</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                The <code>@app.post("/index")</code> decorator registers a POST
                route. The <code>response_model</code> documents and validates
                the shape of the successful response. We return 502 when
                fetching the source website fails, and 500 for other indexing
                errors.
              </p>
            </div>
          </section>

          <!-- BLOCK 4 -->
          <section id="fastapi-ask">
            <h2>Block 4. Ask endpoint</h2>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                Now let's create our second endpoint. It will allow users to ask
                questions about the documents we've indexed.
              </p>
              <p>
                We'll reuse the same LangGraph workflow. The only difference is
                where the question comes from: instead of reading it from the
                terminal, we'll receive it in the body of an HTTP request.
              </p>
              <p>
                Before invoking the graph, we'll check that the Chroma
                collection contains documents. If it is empty, we'll return a
                clear error telling the user to index the documents first.
              </p>
            </div>

            <h3>1. Keep the graph invocation in a reusable function</h3>
            <div class="say">
              <b class="t">Narration</b>
              <p>
                If your existing file already has this function, keep it. If it
                only has the terminal-based <code>ask_question()</code> that
                prints the answer, replace that terminal-oriented version with
                this return-value version.
              </p>
            </div>

            <div class="cb">
              <span class="lang">python</span>
              <pre><code>def ask_question(question: str) -> dict:
    result = rag_graph.invoke(
        {
            "question": question,
            "context": "",
            "sources": [],
            "answer": "",
        }
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"],
    }</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                <strong>Why change it?</strong> The old terminal function
                printed the result. An API endpoint needs structured Python data
                to serialize into JSON. Returning a dictionary lets FastAPI
                build the HTTP response, while the LangGraph call itself remains
                unchanged.
              </p>
            </div>

            <h3>2. Add the endpoint</h3>
            <div class="cb">
              <span class="lang">python</span>
              <pre><code>@app.post(
    "/ask",
    response_model=AskResponse,
)
def ask_endpoint(request: AskRequest):
    if vector_store._collection.count() == 0:
        raise HTTPException(
            status_code=409,
            detail="No indexed documents. Run POST /index first.",
        )

    try:
        result = ask_question(request.question)
        return AskResponse(**result)

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate answer: {error}",
        ) from error</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                FastAPI validates the incoming body against
                <code>AskRequest</code>. We then pass the validated question to
                the existing RAG function and return an
                <code>AskResponse</code>.
              </p>
              <p>
                <strong>Teaching simplification:</strong>
                <code>vector_store._collection.count()</code> accesses Chroma's
                underlying collection. It is concise for this introductory
                lesson, although the underscore indicates a private
                implementation detail. We use it here to avoid introducing
                another abstraction.
              </p>
            </div>
          </section>
```

- [ ] **Step 2: Verify Blocks 3–4**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
html = Path('/Users/pavel/work/COURSE/html_web_courses_en/index.html').read_text()
for s in ['id="fastapi-index"', 'id="fastapi-ask"', 'def index_endpoint():', 'def ask_endpoint(request: AskRequest):', 'status_code=409']:
    assert s in html, s
print('OK Task 3')
PY
```

Expected: `OK Task 3`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "$(cat <<'EOF'
Add FastAPI index and ask endpoint blocks.

EOF
)"
```

---

### Task 4: Block 5 (run and test)

**Files:**
- Modify: `index.html` (after Block 4, before `</main>`)
- Source: `fastapi_rag_lesson.html` `#video5` (lines ~240–267)

- [ ] **Step 1: Insert Block 5**

```html
          <!-- BLOCK 5 -->
          <section id="fastapi-run">
            <h2>Block 5. Run and test</h2>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                Now let's run our application. Previously, we executed the
                Python script directly. This time, we'll start a web server
                using the FastAPI CLI.
              </p>
            </div>

            <div class="cb">
              <span class="lang">bash</span>
              <pre><code>uv run fastapi dev main.py</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                FastAPI starts a local development server. Open
                <code>http://127.0.0.1:8000/docs</code> in your browser. This is
                Swagger UI, an interactive API documentation page generated
                automatically by FastAPI.
              </p>
            </div>

            <h3>Test 1 — Index documents</h3>
            <div class="say">
              <b class="t">Narration</b>
              <p>
                Open <code>POST /index</code>, click <strong>Try it out</strong>,
                then <strong>Execute</strong>. The application downloads the
                configured website, splits its content, generates embeddings and
                stores the chunks in ChromaDB.
              </p>
            </div>

            <div class="cb">
              <span class="lang">json</span>
              <pre><code>{
  "message": "Documents indexed successfully",
  "indexed_chunks": 12
}</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                The number above is illustrative; the actual count depends on
                the content returned by the configured website.
              </p>
            </div>

            <h3>Test 2 — Ask a question</h3>
            <div class="say">
              <b class="t">Narration</b>
              <p>
                Open <code>POST /ask</code> and send this JSON request:
              </p>
            </div>

            <div class="cb">
              <span class="lang">json</span>
              <pre><code>{
  "question": "May I get a promo code for the Advanced course?"
}</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                The API passes the question to LangGraph. The graph retrieves
                relevant content from ChromaDB, sends it to the language model
                and returns the answer with source URLs.
              </p>
            </div>

            <div class="cb">
              <span class="lang">json</span>
              <pre><code>{
  "answer": "The retrieved context says ...",
  "sources": [
    "https://aismartcode.vercel.app/"
  ]
}</code></pre>
            </div>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                We have now transformed our standalone RAG script into an HTTP
                API. The existing RAG pipeline is still doing the retrieval and
                generation; FastAPI simply makes that functionality accessible
                to other applications.
              </p>
              <p>
                <strong>Accuracy note:</strong> don't promise that the sample
                question about an Advanced-course promo code will return a real
                code. The answer depends on what is actually present in the
                indexed page and the model's retrieved context.
              </p>
            </div>
          </section>
```

- [ ] **Step 2: Verify Block 5**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
html = Path('/Users/pavel/work/COURSE/html_web_courses_en/index.html').read_text()
for s in ['id="fastapi-run"', 'uv run fastapi dev main.py', 'http://127.0.0.1:8000/docs', 'indexed_chunks']:
    assert s in html, s
print('OK Task 4')
PY
```

Expected: `OK Task 4`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "$(cat <<'EOF'
Add FastAPI run-and-test block.

EOF
)"
```

---

### Task 5: Block 6 (complete main.py)

**Files:**
- Modify: `index.html` (after Block 5, before `</main>`)
- Source: `fastapi_rag_lesson.html` `#complete` — the full `<pre><code>` body from the complete `main.py` snippet (source file lines 395–698 inclusive of the Python code)

- [ ] **Step 1: Insert Block 6 with the complete file**

Build this section:

```html
          <!-- BLOCK 6 -->
          <section id="fastapi-complete">
            <h2>Block 6. Complete main.py</h2>

            <div class="say">
              <b class="t">Narration</b>
              <p>
                This is the consolidated version students should have at the end
                of the lesson. It keeps the original RAG flow and adds the API
                layer.
              </p>
            </div>

            <div class="cb">
              <span class="lang">python</span>
              <pre><code><!-- PASTE EXACT Python from fastapi_rag_lesson.html complete main.py code block: from "# 1. Python standard library" through the end of ask_endpoint --></code></pre>
            </div>
          </section>
```

**Required paste rule:** Open `fastapi_rag_lesson.html`, locate the codebox labeled `main.py · complete version`, and copy the **entire** Python source from the first line `# 1. Python standard library` through the final `from error` of `ask_endpoint` into the `<pre><code>` above. Do not omit imports, graph assembly, or either endpoint. Do not HTML-escape beyond what is needed for valid HTML (`<` in generics is not present in this snippet; keep the code as plain text inside `<code>`).

The pasted code must include all of these markers:

- `from fastapi import FastAPI, HTTPException`
- `class AskRequest(BaseModel):`
- `def index_documents() -> int:`
- `rag_graph = builder.compile()`
- `def ask_question(question: str) -> dict:`
- `@app.post(` with `"/index"`
- `@app.post(` with `"/ask"`

- [ ] **Step 2: Verify Block 6 completeness**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re
html = Path('/Users/pavel/work/COURSE/html_web_courses_en/index.html').read_text()
assert 'id="fastapi-complete"' in html
m = re.search(r'id="fastapi-complete".*?</section>', html, re.S)
assert m, 'section missing'
body = m.group(0)
for s in [
  'from fastapi import FastAPI, HTTPException',
  'class AskRequest(BaseModel):',
  'def index_documents() -> int:',
  'rag_graph = builder.compile()',
  'def ask_question(question: str) -> dict:',
  '"/index"',
  '"/ask"',
  'response_model=AskResponse',
]:
    assert s in body, s
print('OK Task 5', 'chars', len(body))
PY
```

Expected: `OK Task 5` with a large `chars` count (typically >8000)

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "$(cat <<'EOF'
Add complete FastAPI RAG main.py reference block.

EOF
)"
```

---

### Task 6: Block 7 (teaching notes) + acceptance verification

**Files:**
- Modify: `index.html` (after Block 6, before `</main>`)
- Source: `fastapi_rag_lesson.html` `#notes` teaching bullet list only (lines ~703–709). **Exclude** Student exercise and Suggested next lesson.

- [ ] **Step 1: Insert Block 7**

```html
          <!-- BLOCK 7 -->
          <section id="fastapi-notes">
            <h2>Block 7. Teaching notes</h2>

            <ul>
              <li>
                <strong>Synchronous endpoints:</strong> we use regular
                <code>def</code> endpoints and synchronous calls because the
                existing requests, Chroma and LangGraph flow is synchronous.
                This keeps the lesson focused.
              </li>
              <li>
                <strong>Streaming:</strong> the endpoint returns the completed
                answer as JSON. A streaming API is intentionally out of scope
                for this lesson.
              </li>
              <li>
                <strong>Re-indexing:</strong> deterministic SHA256 IDs make IDs
                stable for identical chunks. If source content changes, old
                chunk IDs may remain in the collection; replacement/deletion
                behavior can be a later improvement.
              </li>
              <li>
                <strong>Error responses:</strong> 422 means request validation
                failed; 409 means the collection is empty; 502 means the source
                website could not be fetched; 500 means an unexpected
                server-side failure.
              </li>
              <li>
                <strong>Local dependencies:</strong> Ollama must be running and
                the configured chat and embedding models must be available
                before testing the endpoints.
              </li>
            </ul>
          </section>
```

Also remove any leftover placeholder comment such as `<!-- remaining blocks added in later tasks -->` if still present.

- [ ] **Step 2: Full acceptance check against the spec**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
import re
html = Path('/Users/pavel/work/COURSE/html_web_courses_en/index.html').read_text()

# All block ids present
ids = [
  'fastapi-overview','fastapi-intro','fastapi-setup','fastapi-index',
  'fastapi-ask','fastapi-run','fastapi-complete','fastapi-notes',
]
missing = [i for i in ids if f'id="{i}"' not in html]
assert not missing, missing

# TOC wiring still present (must not have been removed)
assert 'panelId: "panel-fastapi"' in html
assert 'tocId: "toc-fastapi"' in html

# Out-of-scope content must NOT appear as dedicated sections
assert 'id="fastapi-changes"' not in html
assert 'Suggested next lesson' not in html.split('id="panel-fastapi"')[1].split('id="panel-')[0]
assert 'Student exercise' not in html.split('id="panel-fastapi"')[1].split('id="panel-')[0]

# Markup conventions
panel = html.split('id="panel-fastapi"')[1].split('class="tab-panel"')[0]
assert 'class="say"' in panel
assert 'class="cb"' in panel
assert 'class="callout"' not in panel  # do not import lesson-only classes

# Other panels still exist
for pid in ['panel-home','panel-basics','panel-agent','panel-streams','panel-advanced']:
    assert f'id="{pid}"' in html, pid

print('ACCEPTANCE OK')
PY
```

Expected: `ACCEPTANCE OK`

- [ ] **Step 3: Manual smoke in browser (optional but recommended)**

Open `index.html`, click the **FastAPI** tab, confirm:

1. TOC lists Blocks 0–7
2. Copy buttons appear on `.cb` blocks
3. Complete `main.py` renders as one code block

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "$(cat <<'EOF'
Finish FastAPI tab with teaching notes.

EOF
)"
```

---

## Spec coverage checklist

| Spec requirement | Task |
|------------------|------|
| Streams-style panel shell + TOC IDs | Task 1 |
| Title + lead | Task 1 |
| Block 0 overview + video table | Task 1 |
| Block 1 intro | Task 2 |
| Block 2 setup/models | Task 2 |
| Block 3 index endpoint | Task 3 |
| Block 4 ask endpoint | Task 3 |
| Block 5 run/test | Task 4 |
| Block 6 complete main.py | Task 5 |
| Block 7 teaching notes | Task 6 |
| Exclude changes/exercise/next lesson | Task 6 acceptance |
| No CSS/JS / other-tab edits | All tasks |
| `.say` / `.cb` conventions | Tasks 1–6 |
| Acceptance criteria 1–5 | Task 6 Step 2–3 |

## Plan self-review

1. **Spec coverage:** All content-map rows have tasks; out-of-scope items are explicitly excluded in Task 6 checks.
2. **Placeholders:** Task 5 uses an explicit paste rule from a named source region with verification markers (not a vague “add code later”).
3. **Consistency:** Section ids match the design doc (`fastapi-*`); TOC element ids match existing `initSectionToc` registration.
