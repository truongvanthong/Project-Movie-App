import pandas as pd
from data_helpers import *
    
def add_data_to_list(df, data):
    for index, row in df.iterrows():
        try:
            # Tạo object và thêm vào list data
            # title,year,genres,overview,language,poster,rating,trailer,runtime,budget,revenue,directors,director_images,top_cast,top_cast_images
            data.append(DataObject().create(
                title=row['title'],
                year=row['year'],
                genre=row['genres'],
                plot=row['overview'],
                lang=row['language'], 
                poster=row['poster'],
                rating=row['rating'],
                trailor=row['trailer'],
                runtime = row['runtime'],
                budget = row['budget'],
                revenue = row['revenue'],
                director = row['directors'],
                director_img = row['director_images'],
                top_cast = row['top_cast'],
                top_cast_img = row['top_cast_images']
            ))
        except Exception as e:
            print(f"Error adding {row['title']} to data: {e}")
    return data

if __name__ == "__main__":
    
     # -------------------------
    # đọc dữ liệu từ file csv
    df = pd.read_csv('output_MAIN.csv')
    
    # chia dữ liệu thành hai DataFrame
    df_1 = df[:5000]
    df_2 = df[5000:]
    
    # thêm dữ liệu vào danh sách
    data = []
    data = add_data_to_list(df_1, data)
    data = add_data_to_list(df_2, data)
    
    # hiển thị số lượng phim trong danh sách
    print(f'Total number of movies: {len(data)}')
    # -------------------------