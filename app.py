# app.py
import streamlit as st

st.set_page_config(page_title="ハート計算アプリ", layout="wide")
st.title("🎵 メンバーカード & ライブカード ハート計算アプリ")

colors_dict = {1: "ピンク", 2: "赤", 3: "黄", 4: "緑", 5: "青", 6: "紫"}
colors_code = {1:"#ffb6c1", 2:"#ff6347", 3:"#ffff66", 4:"#90ee90", 5:"#87cefa", 6:"#dda0dd"}

st.write("ピンク：1, 赤：2, 黄：3, 緑：4, 青：5, 紫：6")

# メンバー色の選択
colors_selected = st.multiselect(
    "参加メンバーの色を選択",
    options=list(colors_dict.keys()),
    format_func=lambda x: colors_dict[x]
)

# 入力チェック：重複や空選択
if colors_selected:
    if len(colors_selected) != len(set(colors_selected)):
        st.error("⚠️ 同じ色が複数選択されています。重複しないようにしてください。")
    else:
        st.markdown("---")
        st.subheader("💖 メンバーカードのハート数")
        heart = []

        # 横並び入力
        cols = st.columns(len(colors_selected))
        for idx, c in enumerate(colors_selected):
            heart_val = cols[idx].number_input(f"{colors_dict[c]}", min_value=0, step=1, key=f"heart_{c}")
            heart.append(heart_val)

        st.markdown("---")
        st.subheader("🎶 ライブカードの必要ハート数")
        live = []
        cols_live = st.columns(len(colors_selected) + 1)  # +1 は黒カード用
        for idx, c in enumerate(colors_selected):
            live_val = cols_live[idx].number_input(f"{colors_dict[c]}", min_value=0, step=1, key=f"live_{c}")
            live.append(live_val)
        black = cols_live[-1].number_input("黒", min_value=0, step=1, key="live_black")

        st.markdown("---")
        if st.button("計算"):
            yaju = 0
            remaining = [0]*len(colors_selected)

            for i in range(len(colors_selected)):
                diff = live[i] - heart[i]
                if diff < 0:
                    yaju += -diff
                else:
                    remaining[i] = diff

            kmr = black - yaju

            st.subheader("📝 残り必要ハート数")
            # 色付き表示
            for i, c in enumerate(colors_selected):
                st.markdown(
                    f"<div style='background-color:{colors_code[c]}; padding:10px; border-radius:5px; color:black'>{colors_dict[c]}：{remaining[i]}</div>",
                    unsafe_allow_html=True
                )
            st.markdown(
                f"<div style='background-color:black; color:white; padding:10px; border-radius:5px'>黒：{kmr}</div>",
                unsafe_allow_html=True
            )