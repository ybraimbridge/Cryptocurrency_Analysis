import streamlit as st

st.title("ETH Page")

with st.container():
    st.image(
        "https://s2.coinmarketcap.com/static/img/coins/200x200/1027.png", width=50,
    )

    eth_option = st.selectbox(
        "Choose which graph to view..",
        (
            "ETH_100k",
            "Price",
            "transaction fees",
            "AAC",
            "marketcap_dominance",
            "volatility",
        ),
    )
    st.header(eth_option)

    # col1, col2 = st.columns(2, gap="small")

    # with col1:

    if eth_option == "ETH_100k":
        st.image(
            "hvplot_images/ethereum_graphs/ethereum_100K.png", use_column_width=True
        )

    if eth_option == "Price":
        st.image(
            "hvplot_images/ethereum_graphs/ethereum_price.png", use_column_width=True,
        )

    if eth_option == "transaction fees":
        st.image(
            "hvplot_images/ethereum_graphs/ethereum_transaction_fees.png",
            use_column_width=True,
        )

    if eth_option == "aac":
        st.image(
            "hvplot_images/ethereum_graphs/ethereum_aac.png", use_column_width=True
        )

    if eth_option == "marketcap_dominance":
        st.image(
            "hvplot_images/ethereum_graphs/ethereum_marketcap_dominance.png",
            use_column_width=True,
        )

    if eth_option == "volatility":
        st.image(
            "hvplot_images/ethereum_graphs/ethereum_volatility.png",
            use_column_width=True,
        )

