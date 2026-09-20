import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Global Superstore Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0b1f3a;
    --navy-2: #102d4f;
    --blue: #2563eb;
    --blue-light: #eaf2ff;
    --teal: #0f9f8f;
    --purple: #7c3aed;
    --orange: #d97706;
    --red: #dc4c64;
    --bg: #f4f7fb;
    --card: #ffffff;
    --border: #e2e8f0;
    --text: #102a4c;
    --muted: #64748b;
}

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background: var(--bg);
}

.main .block-container {
    max-width: 1540px;
    padding: 1.4rem 2rem 2.5rem 2rem;
}

[data-testid="stHeader"] {
    background: var(--navy);
}

[data-testid="stToolbar"] {
    background: var(--navy);
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0b1f3a 0%,
        #102d4f 100%
    );
    border-right: 1px solid #1c4168;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 1rem 0.9rem;
}

[data-testid="stSidebar"] * {
    font-family: "Inter", sans-serif;
}

.sidebar-brand {
    padding: 12px 10px 22px 10px;
    margin-bottom: 18px;
    border-bottom: 1px solid rgba(255,255,255,0.13);
}

.sidebar-icon {
    width: 45px;
    height: 45px;
    border-radius: 13px;
    background: linear-gradient(135deg, #2563eb, #3b82f6);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 21px;
    margin-right: 10px;
    vertical-align: middle;
    box-shadow: 0 7px 18px rgba(37,99,235,0.28);
}

.sidebar-title {
    display: inline-block;
    vertical-align: middle;
    color: #ffffff;
    font-size: 16px;
    line-height: 1.35;
    font-weight: 800;
}

.sidebar-section {
    color: #8fb0d3;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    margin: 22px 7px 10px 7px;
}

[data-testid="stSidebar"] label {
    color: #d9e7f5 !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] .stRadio > label {
    display: none !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 7px;
}

[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 9px;
    padding: 8px 10px;
    color: #dce8f5 !important;
    transition: all 0.15s ease;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.08);
    border-color: rgba(96,165,250,0.4);
}

[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #dce8f5 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: #ffffff !important;
    border-color: #ffffff !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
    color: #173b68 !important;
    font-weight: 750 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: #102b4b !important;
    border: 1px solid #315274 !important;
    border-radius: 10px !important;
    min-height: 44px !important;
    box-shadow: none !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
    border-color: #4c82bb !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] span {
    color: #f3f7fb !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] input {
    color: white !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] {
    background: #2f6fed !important;
    border: 1px solid #4a83f4 !important;
    border-radius: 7px !important;
    color: white !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] span {
    color: white !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] svg {
    fill: #ffffff !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] svg {
    color: #9db4cc !important;
    fill: #9db4cc !important;
}

[data-testid="stSidebar"] [data-baseweb="popover"] {
    background: #ffffff !important;
}

[data-testid="stSidebar"] [role="option"] {
    color: #243b53 !important;
}

[data-testid="stSidebar"] [role="option"]:hover {
    background: #eef5ff !important;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.10) !important;
}

.main-header {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 24px 28px;
    margin-bottom: 28px;
    box-shadow: 0 9px 30px rgba(15,23,42,0.055);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 15px;
}

.header-icon {
    width: 56px;
    height: 56px;
    border-radius: 15px;
    background: #eaf2ff;
    color: #2563eb;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
    flex-shrink: 0;
}

.header-title {
    color: var(--text);
    font-size: 29px;
    font-weight: 800;
    line-height: 1.15;
    margin: 0;
}

.header-subtitle {
    color: var(--muted);
    font-size: 13px;
    margin-top: 7px;
}

.header-right {
    display: flex;
    align-items: center;
    gap: 13px;
}

.updated-label {
    text-align: right;
    color: #94a3b8;
    font-size: 10px;
    line-height: 1.5;
}

.updated-label strong {
    color: #475569;
    font-size: 11px;
}

.user-circle {
    width: 39px;
    height: 39px;
    border-radius: 50%;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 14px;
}

.user-name {
    color: #334155;
    font-size: 12px;
    font-weight: 700;
}

.section-heading {
    color: var(--text);
    font-size: 21px;
    font-weight: 800;
    margin: 27px 0 14px 0;
}

.section-subtitle {
    color: #718096;
    font-size: 12px;
    margin-top: -7px;
    margin-bottom: 15px;
}

.kpi-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 17px;
    min-height: 158px;
    padding: 19px;
    box-shadow: 0 7px 24px rgba(15,23,42,0.055);
    position: relative;
    overflow: hidden;
}

.kpi-card::after {
    content: "";
    position: absolute;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    right: -30px;
    bottom: -30px;
    opacity: 0.05;
    background: currentColor;
}

.kpi-blue {
    border-top: 3px solid #2563eb;
    color: #2563eb;
}

.kpi-teal {
    border-top: 3px solid #0f9f8f;
    color: #0f9f8f;
}

.kpi-purple {
    border-top: 3px solid #7c3aed;
    color: #7c3aed;
}

.kpi-orange {
    border-top: 3px solid #d97706;
    color: #d97706;
}

.kpi-red {
    border-top: 3px solid #dc4c64;
    color: #dc4c64;
}

.kpi-icon {
    width: 39px;
    height: 39px;
    border-radius: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    margin-bottom: 12px;
}

.icon-blue {
    background: #eaf2ff;
    color: #2563eb;
}

.icon-teal {
    background: #e5f7f3;
    color: #0f8d7f;
}

.icon-purple {
    background: #f1ebff;
    color: #7c3aed;
}

.icon-orange {
    background: #fff3df;
    color: #d97706;
}

.icon-red {
    background: #ffecef;
    color: #dc4c64;
}

.kpi-title {
    color: #718096;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.55px;
    margin-bottom: 5px;
}

.kpi-value {
    color: var(--text);
    font-size: 24px;
    font-weight: 800;
    line-height: 1.2;
}

.kpi-footer {
    color: #169b79;
    font-size: 10px;
    font-weight: 650;
    margin-top: 9px;
}

.chart-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 5px 10px 0 10px;
    box-shadow: 0 6px 21px rgba(15,23,42,0.045);
}

.insight-card {
    background: linear-gradient(100deg,#ffffff 0%,#f5f9ff 100%);
    border: 1px solid #dce7f5;
    border-left: 4px solid #2563eb;
    border-radius: 14px;
    padding: 16px 19px;
    margin: 24px 0;
    box-shadow: 0 5px 16px rgba(15,23,42,0.04);
}

.insight-title {
    color: #1d4ed8;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 5px;
}

.insight-text {
    color: #53657a;
    font-size: 12px;
    line-height: 1.65;
}

.data-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 15px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(15,23,42,0.045);
}

.page-banner {
    background: linear-gradient(
        135deg,
        #0b1f3a 0%,
        #123b67 100%
    );
    border-radius: 18px;
    padding: 25px 28px;
    margin-bottom: 24px;
    color: white;
    box-shadow: 0 9px 25px rgba(11,31,58,0.15);
}

.page-banner-title {
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 6px;
}

.page-banner-text {
    color: #c8d9eb;
    font-size: 12px;
}

.mini-stat {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 17px;
    box-shadow: 0 5px 17px rgba(15,23,42,0.04);
}

.mini-stat-label {
    color: #718096;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.mini-stat-value {
    color: var(--text);
    font-size: 22px;
    font-weight: 800;
    margin-top: 5px;
}

.footer {
    text-align: center;
    color: #8b99aa;
    font-size: 10px;
    padding: 32px 0 8px 0;
}

.stRadio label {
    color: #334155 !important;
    font-weight: 650 !important;
}

.stRadio label p {
    color: #334155 !important;
    font-weight: 650 !important;
}

.stRadio div[role="radiogroup"] {
    gap: 7px;
}

.stRadio div[role="radiogroup"] label {
    background: #ffffff;
    border: 1px solid #dbe3ec;
    border-radius: 8px;
    padding: 5px 11px;
}

.stSelectbox label,
.stMultiSelect label {
    color: #42546b !important;
    font-weight: 650 !important;
}

div[data-testid="stDownloadButton"] button {
    background: #2563eb !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 700 !important;
}

div[data-testid="stDownloadButton"] button:hover {
    background: #1d4ed8 !important;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
}

button[kind="secondary"] {
    border-color: #dbe3ec !important;
}

@media (max-width: 1000px) {
    .header-right {
        display: none;
    }

    .main .block-container {
        padding: 1rem;
    }

    .header-title {
        font-size: 23px;
    }
}

</style>
""")

@st.cache_data
def load_data():
    data = pd.read_excel("Global Superstore.xls")
    data.columns = data.columns.str.strip()

    data["Order Date"] = pd.to_datetime(
        data["Order Date"],
        errors="coerce"
    )

    data["Ship Date"] = pd.to_datetime(
        data["Ship Date"],
        errors="coerce"
    )

    numeric_columns = [
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
        "Shipping Cost"
    ]

    for column in numeric_columns:
        if column in data.columns:
            data[column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    data["Year"] = data["Order Date"].dt.year
    data["Quarter"] = "Q" + data["Order Date"].dt.quarter.astype(str)
    data["Month"] = data["Order Date"].dt.month
    data["Month Name"] = data["Order Date"].dt.strftime("%b")
    data["Year Month"] = data["Order Date"].dt.to_period("M").astype(str)

    return data


def html(content):
    st.html(content)


def money(value):
    return f"${value:,.0f}"


def number(value):
    return f"{value:,.0f}"


def chart_layout(fig, height=400):
    fig.update_layout(
        height=height,
        template="plotly_white",
        margin=dict(l=50, r=25, t=55, b=45),
        font=dict(
            family="Inter, Arial",
            color="#334155",
            size=12
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        hoverlabel=dict(
            bgcolor="white",
            bordercolor="#dbe3ec",
            font_color="#102a4c",
            font_size=12
        ),
        legend=dict(
            font=dict(
                color="#475569",
                size=11
            )
        )
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        linecolor="#dbe3ec",
        tickfont=dict(
            color="#52647a",
            size=11
        ),
        title_font=dict(
            color="#334155",
            size=12
        )
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#e8eef5",
        zeroline=False,
        linecolor="#dbe3ec",
        tickfont=dict(
            color="#52647a",
            size=11
        ),
        title_font=dict(
            color="#334155",
            size=12
        )
    )

    return fig


df = load_data()

years = sorted(
    df["Year"].dropna().unique().tolist()
)

regions = sorted(
    df["Region"].dropna().unique().tolist()
)

categories = sorted(
    df["Category"].dropna().unique().tolist()
)

segments = sorted(
    df["Segment"].dropna().unique().tolist()
)


with st.sidebar:

    html("""
    <div class="sidebar-brand">
        <span class="sidebar-icon">▥</span>
        <span class="sidebar-title">
            Global Superstore<br>
            Analytics
        </span>
    </div>
    """)

    html("""
    <div class="sidebar-section">
        Navigation
    </div>
    """)

    navigation = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Sales Analysis",
            "Profit Analysis",
            "Category Insights",
            "Geographic Analysis",
            "Product Performance",
            "Drill Down",
            "Data Explorer"
        ],
        label_visibility="collapsed"
    )

    html("""
    <div class="sidebar-section">
        Dashboard Filters
    </div>
    """)

    selected_years = st.multiselect(
        "Year",
        years,
        default=years
    )

    selected_regions = st.multiselect(
        "Region",
        regions,
        default=regions
    )

    selected_categories = st.multiselect(
        "Category",
        categories,
        default=categories
    )

    selected_segments = st.multiselect(
        "Segment",
        segments,
        default=segments
    )

    html("""
    <div style="
        margin-top:24px;
        padding:14px 5px;
        border-top:1px solid rgba(255,255,255,0.10);
        text-align:center;
        color:#8ea8c5;
        font-size:9px;
        font-weight:700;
        letter-spacing:1px;
        line-height:1.7;
    ">
        GLOBAL SUPERSTORE<br>
        BUSINESS INTELLIGENCE
    </div>
    """)


filtered_df = df.copy()

if selected_years:
    filtered_df = filtered_df[
        filtered_df["Year"].isin(selected_years)
    ]

if selected_regions:
    filtered_df = filtered_df[
        filtered_df["Region"].isin(selected_regions)
    ]

if selected_categories:
    filtered_df = filtered_df[
        filtered_df["Category"].isin(selected_categories)
    ]

if selected_segments:
    filtered_df = filtered_df[
        filtered_df["Segment"].isin(selected_segments)
    ]


total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order ID"].nunique()

average_order_value = (
    total_sales / total_orders
    if total_orders > 0
    else 0
)

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)


html("""
<div class="main-header">

    <div class="header-left">

        <div class="header-icon">
            ▣
        </div>

        <div>
            <div class="header-title">
                Global Superstore Analytics
            </div>

            <div class="header-subtitle">
                Interactive Business Dashboard & KPI Visualizations
            </div>
        </div>

    </div>

    <div class="header-right">

        <div class="updated-label">
            Last Updated<br>
            <strong>September 20, 2026</strong>
        </div>

        <div class="user-circle">
            S
        </div>

        <div class="user-name">
            Samiksha
        </div>

    </div>

</div>
""")


if navigation == "Dashboard":

    html("""
    <div class="section-heading">
        Business Overview
    </div>
    """)

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:
        html(f"""
        <div class="kpi-card kpi-blue">
            <div class="kpi-icon icon-blue">$</div>
            <div class="kpi-title">TOTAL SALES</div>
            <div class="kpi-value">{money(total_sales)}</div>
            <div class="kpi-footer">● Current filtered period</div>
        </div>
        """)

    with k2:
        html(f"""
        <div class="kpi-card kpi-teal">
            <div class="kpi-icon icon-teal">◆</div>
            <div class="kpi-title">TOTAL PROFIT</div>
            <div class="kpi-value">{money(total_profit)}</div>
            <div class="kpi-footer">● Current filtered period</div>
        </div>
        """)

    with k3:
        html(f"""
        <div class="kpi-card kpi-purple">
            <div class="kpi-icon icon-purple">▣</div>
            <div class="kpi-title">TOTAL ORDERS</div>
            <div class="kpi-value">{number(total_orders)}</div>
            <div class="kpi-footer">● Unique orders</div>
        </div>
        """)

    with k4:
        html(f"""
        <div class="kpi-card kpi-orange">
            <div class="kpi-icon icon-orange">◉</div>
            <div class="kpi-title">AVERAGE ORDER VALUE</div>
            <div class="kpi-value">{money(average_order_value)}</div>
            <div class="kpi-footer">● Sales per order</div>
        </div>
        """)

    with k5:
        html(f"""
        <div class="kpi-card kpi-red">
            <div class="kpi-icon icon-red">%</div>
            <div class="kpi-title">PROFIT MARGIN</div>
            <div class="kpi-value">{profit_margin:.2f}%</div>
            <div class="kpi-footer">● Profit / Sales</div>
        </div>
        """)

    html("""
    <div class="section-heading">
        Sales Trend Over Time
    </div>
    """)

    metric = st.radio(
        "Metric",
        ["Sales", "Profit", "Quantity"],
        horizontal=True,
        label_visibility="collapsed"
    )

    monthly = (
        filtered_df
        .groupby(
            "Year Month",
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Year Month")
    )

    fig = px.area(
        monthly,
        x="Year Month",
        y=metric
    )

    fig.update_traces(
        line=dict(
            color="#2563eb",
            width=2.7
        ),
        fillcolor="rgba(37,99,235,0.15)"
    )

    fig.update_layout(
        height=430,
        template="plotly_white",
        margin=dict(
            l=55,
            r=30,
            t=25,
            b=50
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(
            family="Inter, Arial",
            color="#334155"
        ),
        xaxis=dict(
            title="Date",
            showgrid=False,
            tickfont=dict(
                color="#52647a"
            )
        ),
        yaxis=dict(
            title=metric,
            showgrid=True,
            gridcolor="#e8eef5",
            tickfont=dict(
                color="#52647a"
            )
        )
    )

    html('<div class="chart-card">')

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displaylogo": False,
            "responsive": True
        }
    )

    html('</div>')

    html("""
    <div class="section-heading">
        Business Performance
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:

        category_data = (
            filtered_df
            .groupby(
                "Category",
                as_index=False
            )
            .agg(
                Sales=("Sales", "sum"),
                Profit=("Profit", "sum")
            )
        )

        category_long = category_data.melt(
            id_vars="Category",
            value_vars=[
                "Sales",
                "Profit"
            ],
            var_name="Metric",
            value_name="Amount"
        )

        fig_category = px.bar(
            category_long,
            x="Category",
            y="Amount",
            color="Metric",
            barmode="group",
            color_discrete_map={
                "Sales": "#2563eb",
                "Profit": "#0f9f8f"
            }
        )

        fig_category = chart_layout(
            fig_category,
            390
        )

        fig_category.update_layout(
            title="Sales & Profit by Category",
            legend_title=""
        )

        st.plotly_chart(
            fig_category,
            width="stretch"
        )

    with c2:

        subcategory_data = (
            filtered_df
            .groupby(
                "Sub-Category",
                as_index=False
            )["Profit"]
            .sum()
            .sort_values(
                "Profit",
                ascending=False
            )
        )

        fig_sub = px.bar(
            subcategory_data,
            x="Profit",
            y="Sub-Category",
            orientation="h",
            color_discrete_sequence=[
                "#0f9f8f"
            ]
        )

        fig_sub = chart_layout(
            fig_sub,
            390
        )

        fig_sub.update_layout(
            title="Profit by Sub-Category"
        )

        st.plotly_chart(
            fig_sub,
            width="stretch"
        )

    html("""
    <div class="section-heading">
        Geographic & Product Performance
    </div>
    """)

    c3, c4 = st.columns(2)

    with c3:

        country_data = (
            filtered_df
            .groupby(
                "Country",
                as_index=False
            )["Sales"]
            .sum()
        )

        fig_map = px.choropleth(
            country_data,
            locations="Country",
            locationmode="country names",
            color="Sales",
            hover_name="Country",
            color_continuous_scale=[
                "#dbeafe",
                "#2563eb"
            ]
        )

        fig_map.update_layout(
            title="Sales by Country",
            title_font=dict(
                size=16,
                color="#102a4c"
            ),
            height=430,
            margin=dict(
                l=0,
                r=0,
                t=45,
                b=0
            ),
            paper_bgcolor="white",
            geo=dict(
                bgcolor="white"
            )
        )

        st.plotly_chart(
            fig_map,
            width="stretch"
        )

    with c4:

        products = (
            filtered_df
            .groupby(
                "Product Name",
                as_index=False
            )["Sales"]
            .sum()
            .sort_values(
                "Sales",
                ascending=False
            )
            .head(10)
            .sort_values("Sales")
        )

        fig_products = px.bar(
            products,
            x="Sales",
            y="Product Name",
            orientation="h",
            color_discrete_sequence=[
                "#2563eb"
            ]
        )

        fig_products = chart_layout(
            fig_products,
            430
        )

        fig_products.update_layout(
            title="Top 10 Products by Sales"
        )

        st.plotly_chart(
            fig_products,
            width="stretch"
        )

    html(f"""
    <div class="insight-card">

        <div class="insight-title">
            Business Insight
        </div>

        <div class="insight-text">
            The selected filters contain
            <strong>{number(len(filtered_df))}</strong>
            records and
            <strong>{number(total_orders)}</strong>
            unique orders, generating
            <strong>{money(total_sales)}</strong>
            in sales and
            <strong>{money(total_profit)}</strong>
            in profit.
            The resulting profit margin is
            <strong>{profit_margin:.2f}%</strong>.
        </div>

    </div>
    """)


elif navigation == "Sales Analysis":

    html("""
    <div class="page-banner">
        <div class="page-banner-title">
            Sales Analysis
        </div>
        <div class="page-banner-text">
            Explore sales trends, yearly performance and regional sales distribution.
        </div>
    </div>
    """)

    monthly = (
        filtered_df
        .groupby(
            "Year Month",
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Year Month")
    )

    fig = px.line(
        monthly,
        x="Year Month",
        y="Sales",
        markers=True,
        color_discrete_sequence=[
            "#2563eb"
        ]
    )

    fig = chart_layout(
        fig,
        450
    )

    fig.update_layout(
        title="Monthly Sales Performance"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    c1, c2 = st.columns(2)

    with c1:

        yearly = (
            filtered_df
            .groupby(
                "Year",
                as_index=False
            )["Sales"]
            .sum()
        )

        fig_year = px.bar(
            yearly,
            x="Year",
            y="Sales",
            color_discrete_sequence=[
                "#2563eb"
            ]
        )

        fig_year = chart_layout(
            fig_year,
            380
        )

        fig_year.update_layout(
            title="Sales by Year"
        )

        st.plotly_chart(
            fig_year,
            width="stretch"
        )

    with c2:

        region_sales = (
            filtered_df
            .groupby(
                "Region",
                as_index=False
            )["Sales"]
            .sum()
            .sort_values(
                "Sales",
                ascending=False
            )
        )

        fig_region = px.bar(
            region_sales,
            x="Sales",
            y="Region",
            orientation="h",
            color_discrete_sequence=[
                "#0f9f8f"
            ]
        )

        fig_region = chart_layout(
            fig_region,
            380
        )

        fig_region.update_layout(
            title="Sales by Region"
        )

        st.plotly_chart(
            fig_region,
            width="stretch"
        )


elif navigation == "Profit Analysis":

    html("""
    <div class="page-banner">
        <div class="page-banner-title">
            Profit Analysis
        </div>
        <div class="page-banner-text">
            Analyze profitability across categories and regions.
        </div>
    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:

        profit_category = (
            filtered_df
            .groupby(
                "Category",
                as_index=False
            )["Profit"]
            .sum()
            .sort_values(
                "Profit",
                ascending=False
            )
        )

        fig = px.bar(
            profit_category,
            x="Category",
            y="Profit",
            color_discrete_sequence=[
                "#0f9f8f"
            ]
        )

        fig = chart_layout(
            fig,
            400
        )

        fig.update_layout(
            title="Profit by Category"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with c2:

        profit_region = (
            filtered_df
            .groupby(
                "Region",
                as_index=False
            )["Profit"]
            .sum()
            .sort_values(
                "Profit",
                ascending=False
            )
        )

        fig = px.bar(
            profit_region,
            x="Region",
            y="Profit",
            color_discrete_sequence=[
                "#7c3aed"
            ]
        )

        fig = chart_layout(
            fig,
            400
        )

        fig.update_layout(
            title="Profit by Region"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


elif navigation == "Category Insights":

    html("""
    <div class="page-banner">
        <div class="page-banner-title">
            Category Insights
        </div>
        <div class="page-banner-text">
            Compare category sales, profit, quantity and profit margins.
        </div>
    </div>
    """)

    category_summary = (
        filtered_df
        .groupby(
            "Category",
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
    )

    category_summary["Profit Margin"] = (
        category_summary["Profit"]
        / category_summary["Sales"]
        * 100
    )

    st.dataframe(
        category_summary,
        width="stretch",
        hide_index=True
    )

    fig = px.scatter(
        category_summary,
        x="Sales",
        y="Profit",
        size="Quantity",
        color="Category",
        color_discrete_sequence=[
            "#2563eb",
            "#0f9f8f",
            "#7c3aed"
        ]
    )

    fig = chart_layout(
        fig,
        450
    )

    fig.update_layout(
        title="Category Sales vs Profit"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


elif navigation == "Geographic Analysis":

    html("""
    <div class="page-banner">
        <div class="page-banner-title">
            Geographic Analysis
        </div>
        <div class="page-banner-text">
            Explore sales and profitability across countries.
        </div>
    </div>
    """)

    country_summary = (
        filtered_df
        .groupby(
            "Country",
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig = px.choropleth(
        country_summary,
        locations="Country",
        locationmode="country names",
        color="Sales",
        hover_name="Country",
        hover_data=[
            "Sales",
            "Profit",
            "Quantity"
        ],
        color_continuous_scale=[
            "#dbeafe",
            "#2563eb"
        ]
    )

    fig.update_layout(
        height=600,
        margin=dict(
            l=0,
            r=0,
            t=20,
            b=0
        ),
        paper_bgcolor="white",
        geo=dict(
            bgcolor="white"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.dataframe(
        country_summary.head(20),
        width="stretch",
        hide_index=True
    )


elif navigation == "Product Performance":

    html("""
    <div class="page-banner">
        <div class="page-banner-title">
            Product Performance
        </div>
        <div class="page-banner-text">
            Identify top-selling products and compare product-level performance.
        </div>
    </div>
    """)

    product_summary = (
        filtered_df
        .groupby(
            "Product Name",
            as_index=False
        )
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    top_products = (
        product_summary
        .head(15)
        .sort_values("Sales")
    )

    fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        color_discrete_sequence=[
            "#2563eb"
        ]
    )

    fig = chart_layout(
        fig,
        600
    )

    fig.update_layout(
        title="Top 15 Products by Sales"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.dataframe(
        product_summary.head(25),
        width="stretch",
        hide_index=True
    )


elif navigation == "Drill Down":

    html("""
    <div class="page-banner">
        <div class="page-banner-title">
            Interactive Drill Down
        </div>
        <div class="page-banner-text">
            Move between year, quarter, month and category-level analysis.
        </div>
    </div>
    """)

    level = st.selectbox(
        "Select Analysis Level",
        [
            "Year",
            "Quarter",
            "Month"
        ]
    )

    if level == "Year":

        drill = (
            filtered_df
            .groupby(
                "Year",
                as_index=False
            )
            .agg(
                Sales=("Sales", "sum"),
                Profit=("Profit", "sum"),
                Quantity=("Quantity", "sum")
            )
        )

        x_col = "Year"

    elif level == "Quarter":

        drill = (
            filtered_df
            .groupby(
                "Quarter",
                as_index=False
            )
            .agg(
                Sales=("Sales", "sum"),
                Profit=("Profit", "sum"),
                Quantity=("Quantity", "sum")
            )
        )

        x_col = "Quarter"

    else:

        drill = (
            filtered_df
            .groupby(
                [
                    "Month",
                    "Month Name"
                ],
                as_index=False
            )
            .agg(
                Sales=("Sales", "sum"),
                Profit=("Profit", "sum"),
                Quantity=("Quantity", "sum")
            )
            .sort_values("Month")
        )

        x_col = "Month Name"

    metric = st.selectbox(
        "Select Metric",
        [
            "Sales",
            "Profit",
            "Quantity"
        ]
    )

    fig = px.bar(
        drill,
        x=x_col,
        y=metric,
        color_discrete_sequence=[
            "#2563eb"
        ]
    )

    fig = chart_layout(
        fig,
        450
    )

    fig.update_layout(
        title=f"{metric} by {level}"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    category_options = sorted(
        filtered_df["Category"]
        .dropna()
        .unique()
        .tolist()
    )

    if category_options:

        category = st.selectbox(
            "Select Category",
            category_options
        )

        category_df = filtered_df[
            filtered_df["Category"] == category
        ]

        subcategory = (
            category_df
            .groupby(
                "Sub-Category",
                as_index=False
            )["Sales"]
            .sum()
            .sort_values(
                "Sales",
                ascending=False
            )
        )

        fig_sub = px.bar(
            subcategory,
            x="Sub-Category",
            y="Sales",
            color_discrete_sequence=[
                "#0f9f8f"
            ]
        )

        fig_sub = chart_layout(
            fig_sub,
            400
        )

        fig_sub.update_layout(
            title=f"{category} - Sub-Category Sales"
        )

        st.plotly_chart(
            fig_sub,
            width="stretch"
        )


elif navigation == "Data Explorer":

    html("""
    <div class="page-banner">
        <div class="page-banner-title">
            Data Explorer
        </div>
        <div class="page-banner-text">
            View, inspect and download the currently filtered dataset.
        </div>
    </div>
    """)

    c1, c2, c3 = st.columns(3)

    with c1:
        html(f"""
        <div class="mini-stat">
            <div class="mini-stat-label">
                Filtered Records
            </div>
            <div class="mini-stat-value">
                {number(len(filtered_df))}
            </div>
        </div>
        """)

    with c2:
        html(f"""
        <div class="mini-stat">
            <div class="mini-stat-label">
                Unique Orders
            </div>
            <div class="mini-stat-value">
                {number(total_orders)}
            </div>
        </div>
        """)

    with c3:
        html(f"""
        <div class="mini-stat">
            <div class="mini-stat-label">
                Total Sales
            </div>
            <div class="mini-stat-value">
                {money(total_sales)}
            </div>
        </div>
        """)

    st.write("")

    st.dataframe(
        filtered_df,
        width="stretch",
        height=520,
        hide_index=True
    )

    csv_data = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Filtered Data",
        data=csv_data,
        file_name="filtered_global_superstore.csv",
        mime="text/csv"
    )


html("""
<div class="footer">
    Global Superstore Analytics
    &nbsp; • &nbsp;
    Interactive Dashboard & KPI Visualizations
    &nbsp; • &nbsp;
    Python
    &nbsp; • &nbsp;
    Streamlit
    &nbsp; • &nbsp;
    Pandas
    &nbsp; • &nbsp;
    Plotly
</div>
""")