# 土壌回復農業シミュレーション

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

## 目的

劣化した土壌と回復した土壌を、期待収量・干ばつ損失・水分・投入コスト節減・農場キャッシュフローで比較する。初期費用と遅延して発生する回避損失を、一貫した評価軸で見える化する。

## 前提と指標

デフォルト値：面積・収量・価格、収量低下と干ばつリスク、回復コスト、水分・収量の改善、干ばつ・肥料・水の削減、クレジット収益。

CSVは毎年の物理指標・コスト・収益・割引価値・累積指標を出力する。金額はイラストレーション通貨単位で示す。

## 実行方法

```bash
pip install -r requirements.txt
python soil_recovery_agriculture_sim.py
```

スクリプトは `outputs/` を自動生成し、決定論的に動作する。

## 出力ファイルと解釈

`soil_recovery_agriculture_results.csv`、`yield_comparison.png`、`soil_moisture_index.png`、`agricultural_net_benefit.png`、`input_cost_savings.png`、`agriculture_roi_sensitivity.png`。

累積グラフの前に年別グラフを読むこと。回収期間は累積正味キャッシュフローが初めてプラスになる年。NPVは設定割引率を適用し、ROIは初期CAPEXに対する総未割引正味便益で算出する。感度グラフは確率分布ではない。

## 限界

これは概念的な意思決定支援モデルであり、予測ではない。政策・投資判断前に地域の実測データに置き換えること。便益カテゴリ間の二重計上を避け、専門的レビューを受けること。

## ベースケース結果

| 指標 | 結果 |
|---|---:|
| 評価期間 | 20年 |
| 回収期間 | デフォルト前提では回収なし |
| 主な便益 | 収量安定・干ばつ損失および投入コスト削減 |
| 主な制約 | 農場直接キャッシュフローが不足 |
| 解釈 | 食料・水・公共・サプライチェーンのより広い評価が必要 |

デフォルト前提のもとでは、土壌回復モデルは回収に至らない。これは失敗したモデルではなく、農場直接収益だけでは回復コストを賄えない可能性を示す。

## 出力グラフ

### 収量比較

![Yield Comparison](outputs/yield_comparison.png)

### 土壌水分指標

![Soil Moisture Index](outputs/soil_moisture_index.png)

### 農業正味便益

![Agricultural Net Benefit](outputs/agricultural_net_benefit.png)

### 投入コスト節減

![Input Cost Savings](outputs/input_cost_savings.png)

### 農業ROI感度分析

![Agriculture ROI Sensitivity](outputs/agriculture_roi_sensitivity.png)

## シナリオ比較

![Scenario Payback Comparison](outputs/scenario_payback_comparison.png)

基礎データは [`outputs/scenario_comparison.csv`](outputs/scenario_comparison.csv) で確認できる。

## 弱い結果の読み方

[How to Read Weak Results](../HOW_TO_READ_WEAK_RESULTS.md) を参照のこと。

---

## Author / 著者

Master / inchacomusho / InchaComisho

独立した日本人コンセプトデザイナー・観察者・提案者・AIチューナー・人工叡智の定義者。

---

## Collaborative AI and Co-Creation Team / 協働AIチーム

- G（ChatGPT）
- Mini（Gemini）
- Cruz（Claude）
- Real（Perplexity）
- Lola（Dola）
- Mana（Manus）

---

## Published / 公開月

2026年6月

---

## License / ライセンス

CC BY 4.0

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
クーリングクレジット・フレームワークの定義者、自然冷却価値評価プロトコルの創設者・原著作者。  
温暖化因果構造と完全解決策の定義者・体系化者。

マスターは、地球温暖化を単なるCO₂濃度の問題ではなく、森林喪失、土壌劣化、水循環断絶、水の相転移の弱体化、大気循環・海洋循環・食の循環／有機物循環の弱体化、蒸散・雲形成・降雨循環の弱体化、自然冷却フィードバックの停止として統合的に捉え、その解決策を排出削減、炭素固定源回復、物理的冷却、自然冷却機能の再起動、MRV、クーリングクレジット、文明OSへ接続する公開フレームワークとして提示している。

自然法則思想、地球循環再生、AIとの共創を中心に、NOTE・GitHub・各種公開媒体を通じて公開活動を行う。
