import os
import re
from PIL import Image
from define import *

# 抜き出す領域を指定
POS_LEFT = 370
POS_TOP = 400
POS_RGHT = 1040
POS_BTM = 1500

def crop_process():
    print('Crop Process')
    # ディレクトリ内のファイル一覧を取得
    files = os.listdir(get_dir_img())
    pattern = get_screenshot()

    # 正規表現にマッチするファイルを取得
    matching_files = [f for f in files if re.match(pattern, f)]

    # 取得ファイルでループ
    cnt = 0
    for file in matching_files:
        print("\t" + file)

        # 画像を開く
        img_raw = Image.open(get_img_path(file))

        # 画像を抜き出す
        img_cropped = img_raw.crop((POS_LEFT, POS_TOP, POS_RGHT, POS_BTM))

        # 画像を保存
        save_name = get_crop_path(cnt)
        img_cropped.save(save_name)
        cnt += 1

# crop_process()
