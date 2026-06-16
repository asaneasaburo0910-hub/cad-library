import os
import json

# 💡 SVGが保存されているルートフォルダの名前（環境に合わせて書き換えてください）
# リポジトリ直下にフォルダがある場合は、対象のフォルダ名をリストに入れます。
TARGET_FOLDERS = ['electrical', 'telecom'] 

def generate_symbols_json():
    symbols = []
    
    # 指定されたフォルダを順番にチェック
    for folder in TARGET_FOLDERS:
        if not os.path.exists(folder):
            print(f"警告: フォルダ '{folder}' が見つかりません。スキップします。")
            continue
            
        # フォルダ内のファイルを走査
        for file_name in os.listdir(folder):
            # .svg ファイルだけを対象にする
            if file_name.endswith('.svg'):
                file_path = f"{folder}/{file_name}"
                # 拡張子を除いたファイル名を「名前」にする
                name = os.path.splitext(file_name)[0]
                
                # 自動でJSONの1要素を作成
                symbol_data = {
                    "id": name.lower().replace(" ", "-"), # IDは小文字・ハイフン繋ぎ
                    "name": name,                          # ファイル名をそのまま名前に
                    "category": folder,                    # フォルダ名をカテゴリに
                    "file": file_path                      # 正しいファイルパス
                }
                symbols.append(symbol_data)
    
    # symbols.json として保存（インデント付きで綺麗に整形、日本語の文字化け防止）
    with open('symbols.json', 'w', encoding='utf-8') as f:
        json.dump(symbols, f, ensure_ascii=False, indent=2)
        
    print(f"成功: {len(symbols)} 個のSVGブロックを 'symbols.json' に登録しました！")

if __name__ == "__main__":
    generate_symbols_json()