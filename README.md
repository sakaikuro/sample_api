# 技術テスト

## 実行

### 起動

docker-compose up -d --build

### リクエスト送信&DB 保存

http://127.0.0.1:5001/

path を入力し送信

### 停止&削除

docker-compose down --rmi all

### DB 管理

http://127.0.0.1:8080/

## 備考

- デフォルトのパス（/image/~）を送信すると「success」、それ以外を送信すると「Error:E50012」が返却（いずれも DB に保存される）
- DB のデータは mysql > data でコンテナと共有
- 起動時にエラーが出た場合は、mysql > data 内のファイルを削除し再度起動

## プログラム内容

- APP
  - 機能：リクエストの送信と結果を DB へ保存
  - フレームワーク：Flask
  - 簡易 UI 付き
- API
  - 機能：image_path を受け取り推論結果を返却
  - フレームワーク：Flask
  - 推論機能なし
- MySQL
  - 機能：リクエスト結果を保管
- phpMyApdmin
  - 機能：MySQL の DB を Web ブラウザにて管理
