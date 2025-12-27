# Article 01 - 佛羅倫斯網絡分析

## 這是什麼？

用Python和NetworkX重建15世紀義大利8個主要城市的貿易網絡，分析佛羅倫斯如何成為文藝復興的樞紐。

## 快速開始

### 安裝需求

```bash
pip install networkx matplotlib numpy
```

### 運行程式

```bash
python basic_florence_network.py
```

## 輸出

**終端機：**
- 網絡基本資訊（節點數、邊數、密度）
- 中介中心性排名
- 佛羅倫斯vs競爭對手對比
- 關鍵發現（佛羅倫斯是威尼斯的2.22倍）

**圖片：**
- `florence_network_basic.png` - 網絡視覺化圖

## 關鍵發現

**佛羅倫斯的中介中心性：**
- 是威尼斯的 **2.22倍**
- 是米蘭的 **1.82倍**
- 是羅馬的 **9.92倍**

→ 更多資訊、資金、人才流經佛羅倫斯  
→ 佛羅倫斯是15世紀義大利的網絡中心

## 相關文章

閱讀完整分析：[佛羅倫斯為何成為文藝復興搖籃？](https://code-cogito.com/%e4%bd%9b%e7%be%85%e5%80%ab%e6%96%af%e7%82%ba%e4%bd%95%e6%88%90%e7%82%ba%e6%96%87%e8%97%9d%e5%be%a9%e8%88%88%e6%90%96%e7%b1%83/)

## 完整版（開發中）

基礎版包含8個城市，完整版將包含：
- ✓ 20個城市完整網絡
- ✓ 150年時間序列分析（1350-1500）
- ✓ 真實地理座標映射
- ✓ 多維網絡分析（貿易+金融+文化）
- ✓ Plotly互動式地圖
- ✓ PDF教學文件（35頁）


## 檔案說明

- `basic_florence_network.py` - 主程式（網絡分析與視覺化）
- `data_basic.csv` - 城市數據（人口、座標）
- `README.md` - 本文件

## License

MIT License - 自由使用，請註明出處

---

**Code & Cogito** - 用程式碼解構歷史，用數據理解哲學

GitHub: https://github.com/Code-and-Cogito/code-cogito-public
