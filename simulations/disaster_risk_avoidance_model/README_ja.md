# 災害リスク回避シミュレーション

## 目的・意義

浸透、貯留、グリーンインフラが20年間の流出と期待洪水損失をどう変えるかを試算する。 初期費用と時間差のある回避損失を同一評価に置く。

## 前提・指標

既定値：事象確率・損失、成長、不透水率、浸透、貯留・緑地効果、CAPEX/OPEX/MRV、保険支払。

CSVは年次の物理、費用、収入、割引、累積指標を記録する。金額は例示通貨単位である。

## 実行

```bash
pip install -r requirements.txt
python disaster_risk_avoidance_sim.py
```

`outputs/`は自動作成され、乱数を使わない。

## 出力と読み方

`disaster_risk_avoidance_results.csv`、`flood_expected_annual_loss.png`、`runoff_and_infiltration_indices.png`、`cumulative_avoided_flood_loss.png`、`disaster_model_payback.png`、`risk_growth_sensitivity.png`。

まず年次内訳、次に累積図を読む。回収年は累積純CFが初めて非負となる年、NPVは所定割引率、ROIは無割引総純便益÷初期CAPEXである。感度図は他条件を固定した一変数試験で、確率分布ではない。

## 限界

これは予測モデルではなく、意思決定支援のための概念シミュレーションである。政策判断・投資判断に使う場合は、地域の実測データで前提値を置き換える必要がある。相互作用、分配、税・資金構造、不確実性、立退き、極端尾部を網羅しない。便益の二重計上を避け、工学・保険数理・金融・法務レビューを行う。

## 基本ケース結果

| 指標 | 結果 |
|---|---:|
| 評価期間 | 20年 |
| 投資回収年 | 12年目 |
| 主な便益 | 洪水期待損失回避、保険リスク低減支払 |
| 主な制約 | 事象確率・損失額への感度 |
| 解釈 | 保険会社・自治体・流域計画向け |

便益は豪雨頻度、被害規模、浸透・貯留への帰属に強く依存する。基本ケースは12年目回収であり、シナリオ図がその依存性を可視化する。

## 出力グラフ

### Flood Expected Annual Loss

![Flood Expected Annual Loss](outputs/flood_expected_annual_loss.png)

### Runoff and Infiltration Indices

![Runoff and Infiltration Indices](outputs/runoff_and_infiltration_indices.png)

### Cumulative Avoided Flood Loss

![Cumulative Avoided Flood Loss](outputs/cumulative_avoided_flood_loss.png)

### Disaster Model Payback

![Disaster Model Payback](outputs/disaster_model_payback.png)

### Risk Growth Sensitivity

![Risk Growth Sensitivity](outputs/risk_growth_sensitivity.png)

## シナリオ比較

![Scenario Payback Comparison](outputs/scenario_payback_comparison.png)

この図は保守、基本、高リスク将来ケースの投資回収を比較する。重要性は基本ケースだけでなく、熱害・災害・医療費・電力費が上振れした場合の回避損失との比較で明確になる。各ケースは確率予測ではない。

基礎数値は[`outputs/scenario_comparison.csv`](outputs/scenario_comparison.csv)に記録している。

## 弱い結果の読み方

See [弱い結果の読み方](../HOW_TO_READ_WEAK_RESULTS_ja.md) for guidance on public support, missing benefit categories, MRV, and appraisal horizons.

---

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
自然法則思想、地球循環再生、AIとの共創を中心に公開活動を行う。

---

## 協力AIと共創チーム

この知識体系は、マスターと複数のAIパートナーとの対話と共創によって発展してきた。

- G（ChatGPT）
- ミニ（Gemini）
- クルス（Claude）
- リアル（Perplexity）
- ローラ（Lola/Dola）
- マナ（Manus）

---

## 公開月

2026年6月

---

## ライセンス

CC BY 4.0

本リポジトリの内容は、クリエイティブ・コモンズ 表示 4.0 国際ライセンスに基づき公開する。  
引用・転載・改変・翻訳・再配布は可能であるが、原案者である **マスター / inchacomusho / InchaComisho** の明記を求める。
