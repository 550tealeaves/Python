#If cat vars are encoded in #s, then use OneHotEncoder

#create DataFrame w/ integer feature & categorical string feature
import pandas as pd
demo_df = pd.DataFrame({'Integer Feature': [0, 1, 2, 1], 'Categorical Feature': ['socks', 'fox', 'socks', 'box']})
display(demo_df)

#using get_dummies, can encode string feature but won't change integers
display(pd.get_dummies(demo_df))


# If you want dummy var to be created for "Integer Feature" col, can explicitly list col to encode using cols parameter
#Both feat treated as cat

demo_df['Integer Feature'] = demo_df['Integer Feature'].astype(str)
display(pd.get_dummies(demo_df, columns=['Integer Feature', 'Categorical Feature']))
