# Logical Defense Grid (LDG)

## ⚠️ SECURITY WARNING / セキュリティ警告
**This project handles cryptographic keys. You MUST store `private_key.pem` in a physical Air-Gapped environment. NEVER commit the private key to any repository. If the key is leaked, the security of this system is void.**

(このプロジェクトは暗号鍵を扱います。`private_key.pem`（秘密鍵）は物理的なオフライン環境で厳重に保管してください。絶対にリポジトリにコミットしてはいけません。鍵が流出した場合、このシステムのセキュリティは無効化されます。)

---

## 1. Concept / コンセプト
A security framework where the system remains non-functional unless a valid physical signature is verified.

(正当な物理的署名が検証されない限り、システムが一切稼働しない「Fail-Closed（失敗時閉鎖）」型のセキュリティフレームワークです。)

---

## 2. Setup Guide / セットアップ手順

### Step 1: Install Dependencies / 依存ライブラリのインストール
Ensure Python 3.11+ is installed. Run the following command:
(Python 3.11以上が必要です。以下のコマンドを実行してください:)

`pip install -r requirements.txt`

### Step 2: Generate Assets / 資産の生成 (オフライン作業推奨)
Generate a key pair and sign the policy file.
(鍵ペアの生成と、ポリシーファイルへの署名を行います。)

`python tools/generate_assets.py`

*Result (生成物):*
- `private_key.pem` (KEEP SECRET! / 秘密鍵：厳重保管)
- `public_key.pem` (Public key for verification / 検証用公開鍵)
- `policy.json.sig` (Digital signature / デジタル署名)

### Step 3: Build Container / コンテナの構築
Build the immutable execution environment.
(書き換え不可能な実行環境（コンテナ）を構築します。)

`docker build -t ldg-fortress .`

### Step 4: Execution / 実行
Run the system with a read-only filesystem.
(読み取り専用のファイルシステムとしてシステムを稼働させます。)

`docker run --rm --read-only ldg-fortress`

---

## 3. Verification / 動作検証
To verify the defense mechanism, try modifying `policy.json` and run again. The system will halt immediately.

(防御機構を検証するには、`policy.json`の内容を1文字でも書き換えてから再度実行してください。システムは即座に停止（Fail-Closed）します。)
