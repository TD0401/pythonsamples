import pandas as pd

data = pd.read_csv("../../../../resources/athena.txt")
df = pd.DataFrame(data)

df2 = pd.DataFrame(columns=['city','property_type','amenities'])
for tup in df.itertuples():
    if(tup[1]!='111'):
        df2 = df2.append({'city': tup[1], 'property_type': 'Apartment', 'amenities': tup[4]}, ignore_index=True)
        df2 = df2.append({'city': tup[1], 'property_type': 'Homestay', 'amenities': tup[5]}, ignore_index=True)
        df2 = df2.append({'city': tup[1], 'property_type': 'Hostel', 'amenities': tup[6]}, ignore_index=True)
        df2 = df2.append({'city': tup[1], 'property_type': 'Villa', 'amenities': tup[7]}, ignore_index=True)
        df2 = df2.append({'city': tup[1], 'property_type': 'Cottage', 'amenities': tup[8]}, ignore_index=True)

    df2 = df2.append({'city': tup[2], 'property_type': 'Apartment', 'amenities': tup[4]}, ignore_index=True)
    df2 = df2.append({'city': tup[2], 'property_type': 'Homestay', 'amenities': tup[5]}, ignore_index=True)
    df2 = df2.append({'city': tup[2], 'property_type': 'Hostel', 'amenities': tup[6]}, ignore_index=True)
    df2 = df2.append({'city': tup[2], 'property_type': 'Villa', 'amenities': tup[7]}, ignore_index=True)
    df2 = df2.append({'city': tup[2], 'property_type': 'Cottage', 'amenities': tup[8]}, ignore_index=True)

    df2 = df2.append({'city': tup[3], 'property_type': 'Apartment', 'amenities': tup[4]}, ignore_index=True)
    df2 = df2.append({'city': tup[3], 'property_type': 'Homestay', 'amenities': tup[5]}, ignore_index=True)
    df2 = df2.append({'city': tup[3], 'property_type': 'Hostel', 'amenities': tup[6]}, ignore_index=True)
    df2 = df2.append({'city': tup[3], 'property_type': 'Villa', 'amenities': tup[7]}, ignore_index=True)
    df2 = df2.append({'city': tup[3], 'property_type': 'Cottage', 'amenities': tup[8]}, ignore_index=True)

df2.to_csv("../../../../resources/athena_modified.txt", index=None)
