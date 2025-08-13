import fastapi
from fastapi import FastAPI, HTTPException
from .recommender import reco_engine

app = FastAPI(
    title="Hybrid Recommender API",
    description="An API that provides product recommendations.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recommender API. Go to /docs for usage."}


@app.get("/recommend/{user_id}", tags=["Recommendations"])
def recommend_products(user_id: str):
    """
    Get hybrid product recommendations for a given user.
    """
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id parameter is required.")
        
    try:
        recommendations = reco_engine.get_hybrid_recs(user_id, n=10)
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found for this user.")
        return {"user_id": user_id, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))