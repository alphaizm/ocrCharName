import plotly.graph_objects as go
import pandas as pd
from define import *
from manage_csv import *

csv_data = csv_read_list_data(get_list_name_alliance())

dic_add = {}
dic_add[get_list_date_key()] = []
for row in csv_data:
    char_name = row[get_list_name_key()]

    if 'template' != char_name:
        dic_add[char_name] = []

# -10~0日分のデータを取得
for idx in range(-90, 1):
    str_day = get_date(get_date_spec_YYYYMMDD(idx))
    dic_add[get_list_date_key()].append(str_day)

    for row in csv_data:
        char_name = row[get_list_name_key()]

        if 'template' != char_name:
            total_num = row[str_day]
            dic_add[char_name].append(total_num)

# データフレームの初期化
df = pd.DataFrame(dic_add)

# Create traces
fig = go.Figure()
for col in df.columns:
    if col != get_list_date_key():
        fig.add_trace(go.Scatter(
            x=df[get_list_date_key()],
            y=df[col],
            name=col,
            hovertemplate='%{fullData.name}<br>Date: %{x}<br>Total: %{y}<extra></extra>'  # カスタムホバーテンプレート
        ))

# fig.update_traces(hoverinfo='name+x+y')
fig.update_layout(title='[kyu]同盟員の総力推移',
                    xaxis_title='Date',
                    yaxis_title='総力',
                    yaxis=dict(
                        tickformat=',',  # 'XXX,XXX,XXX' の形式で表示
                    )
                )

# fig.show()
fig.write_html("_Alliance_kyu.html")
# 出力終了のダイアログ
print('◆◆◆◆同盟員の総力推移の出力は完了')
