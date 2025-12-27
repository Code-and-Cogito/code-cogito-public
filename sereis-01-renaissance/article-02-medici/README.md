# Article 02 - 美第奇銀行網絡分析

## 這是什麼？

用Python和NetworkX重建美第奇銀行的歐洲分行網絡（1397-1494），並模擬匯票系統如何讓銀行家繞過教會的高利貸禁令。

## 快速開始

### 安裝需求

```bash
pip install networkx matplotlib numpy
```

### 運行程式

```bash
# 分析銀行網絡
python basic_medici_network.py

# 模擬匯票利潤
python bill_of_exchange_simulation.py
```

## 輸出

**程式一：銀行網絡分析**
- 終端機：分行營業額排名、網絡統計、關鍵發現
- 圖片：`medici_bank_network.png` - 輪軸式網絡視覺化

**程式二：匯票利潤計算**
- 終端機：詳細利潤計算過程、年化報酬率、與現代金融產品對比

## 關鍵發現

**美第奇銀行網絡：**
- 總分行數：8個
- 營運時間：97年（1397-1494）
- 總營業額：405,000佛羅林/年
- 網絡結構：輪軸式（hub-and-spoke）

**匯票系統：**
- 年化報酬率：約16.67%
- 規避方式：利息偽裝成「匯率差」
- 合法性：不違反教會高利貸禁令
- 創新性：金融工程的早期形式

## 相關文章

閱讀完整分析：[美第奇家族的金融帝國](https://code-cogito.com/%e7%be%8e%e7%ac%ac%e5%a5%87%e5%ae%b6%e6%97%8f%e7%9a%84%e9%87%91%e8%9e%8d%e5%b8%9d%e5%9c%8b/)

## 完整版（開發中）

基礎版包含8個分行和簡單匯票計算，完整版將包含：
- ✓ 97年時間序列分析（1397-1494）
- ✓ 動態分行開設/關閉追蹤
- ✓ 帕齊陰謀的網絡影響分析
- ✓ 匯票利潤完整模型（多幣種、風險分析）
- ✓ 蒙地卡羅模擬（匯率波動）
- ✓ 與現代金融產品對比
- ✓ 互動式利潤計算器
- ✓ PDF教學文件（40頁）



## 檔案說明

- `basic_medici_network.py` - 銀行網絡分析與視覺化
- `bill_of_exchange_simulation.py` - 匯票利潤計算模擬
- `data_branches.csv` - 分行數據（位置、營業額、年份）
- `README.md` - 本文件

## License

MIT License - 自由使用，請註明出處

---

**Code & Cogito** - 用程式碼解構歷史，用數據理解哲學

GitHub: https://github.com/Code-and-Cogito/code-cogito-public
