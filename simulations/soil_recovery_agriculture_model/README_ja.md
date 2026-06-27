# 土壌回復・農業シミュレーション

## 目的・意義

期待収量、干ばつ損失、水分、投入節減、農業CFで劣化土壌と回復土壌を比較する。 初期費用と時間差のある回避損失を同一評価に置く。

## 前提・指標

既定値：面積、収量・価格、劣化・干ばつ、回復費、土壌水分・安定性、肥料・水削減、クレジット収入。

CSVは年次の物理、費用、収入、割引、累積指標を記録する。金額は例示通貨単位である。

## 実行

```bash
pip install -r requirements.txt
python soil_recovery_agriculture_sim.py
```

`outputs/`は自動作成され、乱数を使わない。

## 出力と読み方

`soil_recovery_agriculture_results.csv`、`yield_comparison.png`、`soil_moisture_index.png`、`agricultural_net_benefit.png`、`input_cost_savings.png`、`agriculture_roi_sensitivity.png`。

まず年次内訳、次に累積図を読む。回収年は累積純CFが初めて非負となる年、NPVは所定割引率、ROIは無割引総純便益÷初期CAPEXである。感度図は他条件を固定した一変数試験で、確率分布ではない。

## 限界

これは予測モデルではなく、意思決定支援のための概念シミュレーションである。政策判断・投資判断に使う場合は、地域の実測データで前提値を置き換える必要がある。相互作用、分配、税・資金構造、不確実性、立退き、極端尾部を網羅しない。便益の二重計上を避け、工学・保険数理・金融・法務レビューを行う。

## 基本ケース結果

| 指標 | 結果 |
|---|---:|
| 評価期間 | 20年 |
| 投資回収年 | 基本ケースでは未回収 |
| 主な便益 | 収量安定、干ばつ損失・投入費削減 |
| 主な制約 | 農地単体の直接CFが不足 |
| 解釈 | 食料・水・公的支援・供給網の複合評価が必要 |

基本ケースでは、土壌回復・農業モデルは投資回収に至らない。これは失敗ではなく重要な示唆である。農地単体の直接収益だけでは回復費用を賄いにくく、食料安全保障、水資源保全、干ばつリスク、サプライチェーン安定、地域雇用、公的支援、食品企業負担、クレジット収益を含む複合評価が必要である。

## 出力グラフ

### Yield Comparison

![Yield Comparison](outputs/yield_comparison.png)

### Soil Moisture Index

![Soil Moisture Index](outputs/soil_moisture_index.png)

### Agricultural Net Benefit

![Agricultural Net Benefit](outputs/agricultural_net_benefit.png)

### Input Cost Savings

![Input Cost Savings](outputs/input_cost_savings.png)

### Agriculture ROI Sensitivity

![Agriculture ROI Sensitivity](outputs/agriculture_roi_sensitivity.png)

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
