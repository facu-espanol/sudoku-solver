from fastapi import FastAPI, HTTPException

app = FastAPI(title="Sudoku API")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/solve")
def solve(payload: dict):
    # TODO: implementar usando prolog_adapter.engine (cuando integremos Prolog)
    raise HTTPException(status_code=501, detail="Not implemented yet")
