# 都市冷却コスト便益シミュレーション

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

## 目的

無策時の医療費・冷房エネルギー費・熱災害コストを、20年間の冷却介入・費用・クレジット収益と比較する。初期費用と遅延して発生する回避損失を、一貫した評価軸で見える化する。

## 前提と指標

デフォルト値：評価年数・割引率・損害成長率、3つの初期損失カテゴリ、CAPEX/OPEX/MRV、削減率、WBGT・表面温度変化、クレジット単価・発行量・成長率。

CSVは毎年の物理指標・コスト・収益・割引価値・累積指標を出力する。金額はイラストレーション通貨単位で示す。

## 実行方法

```bash
pip install -r requirements.txt
python urban_cooling_cost_benefit_sim.py
```

スクリプトは `outputs/` を自動生成し、決定論的に動作する。

## 出力ファイルと解釈

`urban_cooling_cost_benefit_results.csv`、`cumulative_cost_comparison.png`、`annual_avoided_costs.png`、`net_benefit_and_payback.png`、`cooling_indicators.png`、`roi_sensitivity.png`。

累積グラフの前に年別グラフを読むこと。回収期間は累積正味キャッシュフローが初めてプラスになる年。NPVは設定割引率を適用し、ROIは初期CAPEXに対する総未割引正味便益で算出する。感度グラフは1つの仮定を変化させる（確率分布ではない）。

## 限界

これは概念的な意思決定支援モデルであり、予測ではない。すべての仮定は透明性があり、政策・投資判断前に地域の実測データに置き換えること。配分効果・税・ファイナンス構造・不確実性・極端なテールリスクはモデル化していない。便益カテゴリ間の二重計上を避け、工学・保険数理・財務・法務の専門的レビューを受けること。

## ベースケース結果

| 指標 | 結果 |
|---|---:|
| 評価期間 | 20年 |
| 回収期間 | 11年目 |
| 主な便益 | 医療費・冷房エネルギー・熱損失の回避、クレジット収益 |
| 主な制約 | CAPEX・OPEX・MRV |
| 解釈 | 回避損失が中期的に蓄積する自治体モデル |

累積グラフはCAPEXにより序盤に大きな負担が生じ、医療費・電力費・熱損害コスト回避が時間とともに積み上がることを示す。ベースケースでは11年目頃に回収に達する。

## 出力グラフ

### 累積コスト比較

![Cumulative Cost Comparison](outputs/cumulative_cost_comparison.png)

### 年別回避コスト

![Annual Avoided Costs](outputs/annual_avoided_costs.png)

### 正味便益と回収期間

![Net Benefit and Payback](outputs/net_benefit_and_payback.png)

### 冷却指標

![Cooling Indicators](outputs/cooling_indicators.png)

### ROI感度分析

![ROI Sensitivity](outputs/roi_sensitivity.png)

## シナリオ比較

![Scenario Payback Comparison](outputs/scenario_payback_comparison.png)

このグラフは保守・ベース・高リスクの3つの将来ケースを比較する。基礎データは [`outputs/scenario_comparison.csv`](outputs/scenario_comparison.csv) で確認できる。

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
