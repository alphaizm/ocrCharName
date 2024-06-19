import re
import easyocr
from define import *

def ocr_process():
    print('OCR Process')
    # OCR処理
    # reader = easyocr.Reader(['en','ja'], False)#日本語：ja, 英語：en

    # ディレクトリ内のファイル一覧を取得
    files = os.listdir(get_dir_img())
    pattern = get_cropped()

    # 正規表現にマッチするファイルを取得
    matching_files = [f for f in files if re.match(pattern, f)]

    ocr_lang = ['ja', 'en'] #日本語：ja, 英語：en
    ocr_data = []
    for file in matching_files:
        print('\tPNG:' + file)

        for lang in ocr_lang:
            print('\t\tLANG:' + lang)
            reader = easyocr.Reader([lang], False)
            result = reader.readtext(get_img_path(file))

            for row in result:
                # row[0]：[左上,右上, 右下, 左下] の座標
                # row[1]：テキスト
                # row[2]：確信度
                print("\t\t\t" + str(row))
                ocr_data.append(row[1])

    return ocr_data

# ocr_process()
