# travel_shiori 作業手順

## 変更をGitHub Pagesに反映するまでの流れ

### 1. ファイルを編集する
HTMLファイルなど必要なファイルを修正する。

### 2. ブランチを作成してコミット・プッシュ
```bash
git checkout -b claude/<作業内容>
git add <変更ファイル>
git commit -m "<変更内容の説明>"
git push -u origin claude/<作業内容>
```

### 3. GitHubでPull Requestを作成
- **base**: `main`（マージ先）
- **compare**: `claude/<作業内容>`（マージ元）

※ baseとcompareを逆にすると「差分なし」と表示されるので注意。

### 4. PRをマージする

### 5. GitHub Pagesへの反映を待つ
マージ後、数分待つとブラウザに反映される。
強制リロード（`Ctrl+Shift+R`）で確認。

## ファイル構成
- `index.html` / `index2.html` / `index_1.html` - メインページ
- `files/` - 関連ファイル
- `*.pdf` - 観光地PDF（guell_park, sagrada_familia）
