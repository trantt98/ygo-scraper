import pandas as pd

df = pd.read_json('./Dataset/scraped_data.json')
df = df.rename(columns={'card_name': 'Card Name', 'card_name_english': 'Card Name (English)', 'card_name_german': 'Card Name (German)',
                        'card_name_japanese': 'Card Name (Japanese)', 'card_type': 'Card Type', 'attribute': 'Attribute',
                        'property': 'Property', 'types': 'Types', 'level': 'Level', 'passcode': 'Passcode',
                        'card_effect_types': 'Card Effect Types', 'statuses': 'Statuses'})

df['Card Name (German)'] = df['Card Name (German)'].str.replace('Check translation', '').str.strip()
df['Card Name (Japanese)'] = df['Card Name (Japanese)'].str.replace('Check translation', '').str.strip()

print(df['Property'].head())
