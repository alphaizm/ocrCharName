import plotly.graph_objects as go
import pandas as pd
from define import *
from manage_csv import *

# csv_data = csv_read_list_data(get_list_name_alliance())
csv_data = csv_read_list_data(get_list_name_server())

dic_data = {}
dic_rank = {}
dic_data[get_list_date_key()] = []
dic_rank[get_list_date_key()] = []
for row in csv_data:
    char_name = row[get_list_name_key()]

    if 'template' != char_name:
        dic_data[char_name] = []
        dic_rank[char_name] = []

# -10~0日分のデータを取得
for idx in range(-133, 1):
    str_day = get_date(get_date_spec_YYYYMMDD(idx))
    dic_data[get_list_date_key()].append(str_day)
    dic_rank[get_list_date_key()].append(str_day)

    dic_day = get_data_dict_by_day(str_day, csv_data)
    sorted_dict_day = sorted(dic_day.items(), key=lambda x: int(x[1]), reverse=True)

    rank = 1
    for row in sorted_dict_day:
        char_name = row[0]
        total_num = row[1]

        if 'template' != char_name:
            dic_data[char_name].append(total_num)
            dic_rank[char_name].append(rank)
            rank += 1

    # for row in csv_data:
    #     char_name = row[get_list_name_key()]

    #     if 'template' != char_name:
    #         total_num = row[str_day]
    #         dic_data[char_name].append(total_num)

# dic_addの各要素数をデバッグ出力
for key in dic_data.keys():
    print(key + '：' + str(len(dic_data[key])))

# データフレームの初期化
df = pd.DataFrame(dic_data)

# Create traces
fig = go.Figure()
for col in df.columns:
    if col != get_list_date_key():
        # 日毎にランキングを算出
        # daily_ranks = df[col].rank(ascending=False, method='min').astype(int)
        
        # 総力が0の場合は「範囲外」とする
        ary_text = []
        for rank, total in zip(dic_rank[col], dic_data[col]):
            if total != 0:
                ary_text.append(f"Rank: {rank}")
            else:
                ary_text.append("範囲外")
        
        fig.add_trace(go.Scatter(
            x=df[get_list_date_key()],
            y=df[col],
            name=col,
            text=ary_text,  # ランキングまたは範囲外をテキストとして追加
            hovertemplate='%{fullData.name}<br>Date: %{x}<br>Total: %{y}<br>%{text}<extra></extra>'  # カスタムホバーテンプレートにランキングまたは範囲外を追加
        ))

fig.update_layout(title='[サーバー]ランキング100位の総力推移',
# fig.update_layout(title='[kyu]同盟員の総力推移',
                    xaxis_title='Date',
                    yaxis_title='総力',
                    yaxis=dict(
                        tickformat=',',  # 'XXX,XXX,XXX' の形式で表示
                    )
                )

# fig.show()
# fig.write_html("_Alliance_kyu.html")
fig.write_html("_Server_Ranking100.html")
# 出力終了のダイアログ
print('◆◆◆◆総力推移の出力は完了')
