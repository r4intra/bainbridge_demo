import pandas as pd
from code.utils.rxnorm_api_caller import RxNormIngredientATCConceptCall

drugs = pd.read_csv('/Users/shaunwalters/Desktop/DRUG18Q2.csv')['prod_ai'].unique()


# 5389 calls to API...

proto_df = []
for d in drugs:
    api_call = RxNormIngredientATCConceptCall(d)
    proto_df.append((d, api_call.rxcui, api_call.atc_code))

df = pd.DataFrame.from_records(proto_df, columns=('prod_ai', 'rxcui', 'atc_code'))

df.to_csv('/Users/shaunwalters/Desktop/atc_mapping.csv', index=False)
