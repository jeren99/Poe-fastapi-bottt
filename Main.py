from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/poe")
async def poe_webhook(request: Request):
    data = await request.json()
    query = data.get("query", "")
    return {"response": f"Sorduğun şey: '{query}'"}
