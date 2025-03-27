import pandas as pd
import folium
import random
from IPython.display import display
import webbrowser
import tempfile

def load_data():
    global rank_gu_df, rank_dong_df, hospital_df, real_estate_df, gu_df, dong_df
    rank_gu_df = pd.read_csv('/home/lee/dev_ws/projects/project01/eda-repo-2/service/rank_gu.csv')
    rank_dong_df = pd.read_csv('/home/lee/dev_ws/projects/project01/eda-repo-2/service/rank_dong.csv')
    hospital_df = pd.read_csv('/home/lee/dev_ws/projects/project01/eda-repo-2/service/hospital.csv')
    real_estate_df = pd.read_csv('/home/lee/dev_ws/projects/project01/eda-repo-2/service/real_estate.csv')
    gu_df = pd.read_csv('/home/lee/dev_ws/projects/project01/eda-repo-2/service/gu.csv')
    dong_df = pd.read_csv('/home/lee/dev_ws/projects/project01/eda-repo-2/service/dong.csv')

def select_category():
    while True:
        print("우리 아이를 위한 동네에서 가장 중요한 것은:\n1. 교육\n2. 안전\n3. 공공시설")
        choice = input("번호 입력: ")
        if choice in ['1', '2', '3']:
            print('당신의 아이를 위한 BEST 5를 보여드릴게요!')
            return int(choice)
        else:
            print("다시 골라 주세요.")

def get_top5_average(rank_cols):
    rank_gu_df['avg_rank'] = round((rank_gu_df[rank_cols].mean(axis=1)),2)
    top5 = rank_gu_df.nlargest(5, 'avg_rank')
    
    top5 = top5.merge(gu_df[['gu_id', 'gu_name']], on='gu_id', how='left')
    return top5[['gu_name', 'avg_rank', 'gu_id']]

def select_gu(top5_df):
    print("TOP 5 구 중 하나를 선택하세요:")
    for idx, row in top5_df.iterrows():
        print(f"{idx + 1}. {row['gu_name']} - 평균 랭킹: {row['avg_rank']}")
    
    choice = int(input("번호로 골라주세요! : "))
    selected_gu_id = top5_df.iloc[choice - 1]['gu_id']
    return selected_gu_id

def select_preference():
    print("추가적으로 원하는 것은 \n1. 의료 접근성\n2. 주거비")
    return int(input("번호 입력: "))

def show_hospital_info(gu_id):
    top_dongs = rank_dong_df[rank_dong_df['gu_id'] == gu_id].nlargest(3, 'rank_hospital')[['gu_id', 'rank_hospital', 'dong_id']]
    
    top_dongs = top_dongs.merge(dong_df[['dong_id', 'dong_name']], on='dong_id', how='left')
    
    print("TOP 3를 뽑아봤습니다!\n 하나를 선택해주세요:")
    for idx, row in top_dongs.iterrows():
        print(f"{idx + 1}. {row['dong_name']} - 병원 순위: {row['rank_hospital']}")
    
    choice = int(input("번호로 골라주세요! : "))
    selected_dong_id = top_dongs.iloc[choice - 1]['dong_id']
    
    selected_hospitals = hospital_df[hospital_df['dong_id'] == selected_dong_id].sample(n=min(3, len(hospital_df)), random_state=42)
    if selected_hospitals.empty:
        print("병원이 없습니다ㅠㅠ")
    else:
        display(selected_hospitals)
        show_hospital_map(selected_hospitals)

def show_hospital_map(hospitals):
    map_center = [37.5665, 126.9780]
    m = folium.Map(location=map_center, zoom_start=12)
    for _, row in hospitals.iterrows():
        folium.Marker(
            location=[random.uniform(37.55, 37.58), random.uniform(126.97, 126.99)],
            popup=row['hospital_name'],
            tooltip=row['hospital_name']
        ).add_to(m)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmpfile:
        m.save(tmpfile.name)
        webbrowser.open(f'file://{tmpfile.name}') 

def show_real_estate_info(gu_id):
    top_dongs = rank_dong_df[rank_dong_df['gu_id'] == gu_id].nlargest(3, 'rank_rent')[['gu_id', 'rank_rent', 'dong_id']]

    top_dongs = top_dongs.merge(dong_df[['dong_id', 'dong_name']], on='dong_id', how='left')
    
    print("주거비가 낮은 TOP 3 입니다!\n 하나를 선택해주세요:")
    for idx, row in top_dongs.iterrows():
        print(f"{idx + 1}. {row['dong_name']} - 주거비 순위: {row['rank_rent']}")
    
    choice = int(input("번호로 골라주세요! : "))
    selected_dong_id = top_dongs.iloc[choice - 1]['dong_id']
    
    selected_real_estates = real_estate_df[real_estate_df['dong_id'] == selected_dong_id]
    display(selected_real_estates)

def main():
    load_data()
    while True:
        category = select_category()
        if category == 1:
            top5 = get_top5_average(['rank_school', 'rank_academy'])
        elif category == 2:
            top5 = get_top5_average(['rank_traffic_accident', 'rank_crime', 'rank_unhealthy_facility'])
        elif category == 3:
            top5 = get_top5_average(['rank_park', 'rank_library'])
        else:
            print("다시 골라주세요.")
            continue
        
        gu_id = select_gu(top5)
        preference = select_preference()
        
        if preference == 1:
            show_hospital_info(gu_id)
        elif preference == 2:
            show_real_estate_info(gu_id)
        else:
            print("다시 골라주세요.")
        
        restart = input("다시 시작할까요? (1.Yes / 2.No): ")
        if restart != '1':
            print("이용해 주셔서 감사합니다.")
            break

if __name__ == "__main__":
    main()
