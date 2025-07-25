import pandas as pd
from pycaret.regression import *


df_encoded=pd.read_csv("df_encoded.csv")

from pycaret.regression import setup, compare_models, pull

reg_setup = setup(
    data=df_encoded,
    target='claim',
    session_id=42,
    train_size=0.8,
    normalize=True,  
    verbose=False    
)


best_models = compare_models(n_select=3, sort='R2')  


tuned_model = tune_model(best_models[0])


evaluate_model(tuned_model)


final_model = finalize_model(tuned_model)
predictions = predict_model(final_model)

save_model(final_model, 'best_model')