# 観光資源回復シミュレーション

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

このシミュレーションは、自然冷却・水循環回復・景観再生・生物多様性回復・地域経済活性化を通じた観光資源回復のクーリングクレジット事業モデルを支援する。

対応する事業モデル：

- `Cooling-Credit-Framework/docs/business_models/TOURISM_RESOURCE_RECOVERY_COOLING_CREDIT_MODEL.md`

## 目的

このモデルは、主に従来型インフラと集客施策に頼る観光開発と、観光地を快適で価値ある場所にする自然資産を回復する開発の両経路を比較する。

## 比較シナリオ

| シナリオ | 内容 |
|---|---|
| Degraded Destination | 熱・水質低下・生態系ダメージ・景観価値の弱体化が続く |
| Conventional Tourism Development | ホテル・イベント・道路・集客策が増えるが、自然冷却と生態系回復は弱いまま |
| Cooling Tourism Recovery | 水循環回復・緑化・ミスト冷却・湖/サンゴ礁/水辺の修復・MRVが快適性と観光地価値を改善する |
| Integrated Regenerative Destination | 観光収益・クーリングクレジット収益・生物多様性・水質・冷却・地域再投資が互いに強化し合う |

## 主な出力

スクリプトは `outputs/tourism_resource_recovery_timeseries.csv` とグラフを生成する。

- `tourism_cooling_credit_value.png`
- `destination_comfort_index.png`
- `natural_cooling_asset_index.png`
- `water_landscape_ecosystem_index.png`
- `visitor_stay_income_index.png`
- `overtourism_risk_index.png`

## 実行方法

```bash
python tourism_resource_recovery_simulation.py
```

必要なパッケージ：

```bash
pip install numpy pandas matplotlib
```

## 解釈 / 注意

これは概念的な決定論モデルであり、観光予測・気候予測・投資推奨ではない。実用前に、地域の気温・WBGT・水質・滞在者数・生物多様性・MRVデータで仮定を置き換えること。

## Author / 著者

Master / inchacomusho / InchaComisho

## License / ライセンス

CC BY 4.0
