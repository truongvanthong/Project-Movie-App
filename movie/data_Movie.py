import pandas as pd
from data_helpers import *
    
def add_data_to_list(df, data):
    for i, row in df.iterrows():
        data.append(DataObject().create(row['title'], row['year'], row['genre'], row['plot'], row['poster'], row['rating'], row['trailor']))
    return data

if __name__ == "__main__":
    
     # -------------------------
    # đọc dữ liệu từ file csv
    df = pd.read_csv('data_Done.csv')
    
    # chia dữ liệu thành hai DataFrame
    df_1 = df[:4000]
    df_2 = df[4001:]
    
    # thêm dữ liệu vào danh sách
    data = []
    data = add_data_to_list(df_1, data)
    data = add_data_to_list(df_2, data)
    
    # hiển thị số lượng phim trong danh sách
    print(f'Total number of movies: {len(data)}')
    # -------------------------