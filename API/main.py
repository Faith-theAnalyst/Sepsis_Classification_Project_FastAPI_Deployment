from fastapi import FastAPI,HTTPException
from typing import Literal,List
import uvicorn
from pydantic import BaseModel
import pandas as pd
import joblib, os

sep_pipeline = joblib.load('./Assets/RandomForestClassifier_pipeline.joblib')
encoder = joblib.load('./Assets/encoder.joblib')


app = FastAPI(
    title= 'Sepsis Classification FastAPI',
    description='FastAPI to classify Sepsis condition (Positive / Negative)',
    version= '0.104.1'
)


class Sepsis(BaseModel):
    PRG: int
    PL: int 
    PR: int 
    SK : int
    TS: int 
    M11 : float
    BD2 : float
    Age : int
    Insurance: int
    

@app.get('/')  
def get_home():
    return{
        'Welcome to the Sepsis Classification FastAPI'
        '\n Add /docs to the url to continue'
    }
    
      
@app.post('/classify')
def sep_classification(sepsis:Sepsis):
    try:
        df = pd.DataFrame([sepsis.model_dump()])

        prediction = sep_pipeline.predict(df)
        decoded_pred = encoder.inverse_transform([prediction])[0]
        
        #return {'prediction': decoded_pred}
    
        output = sep_pipeline.predict_proba(df)

        confidence_score = output.max(axis=-1)[0]
        pred_index = output.argmax(axis=-1)[0]
        
        return {'prediction': decoded_pred,
                'ConfidenceScore': confidence_score}

        

    except Exception as e:
        error_detail = str(e)
        raise HTTPException(status_code=500, detail=f"Error during classification: {error_detail}")


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)