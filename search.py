import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,csvfile):
    # 検索対象取得
    df=pd.read_csv(f"./{csvfile}")
    source=list(df["name"])

    # 検索
    if word == "":
        # print("名前を入力してください")
        eel.output("名前を入力してください")
    elif word in source:
        # print("『{}』はあります".format(word))
        eel.output(f"『{word}』はいます")
    else:
        # print("『{}』はありません".format(word))
        eel.output(f"『{word}』はいません")
        # 追加
        # add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        # if add_flg=="1":
        source.append(word)
        # print("『{}』を追加しました".format(word))
        eel.output(f"『{word}』を追加しました")
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(f"./{csvfile}",encoding="utf_8-sig")
    # print(source)
