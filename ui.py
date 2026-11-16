"""Shared, locally rendered styles for the learning pages."""
import streamlit as st


def page_intro(number, title, subtitle):
    st.markdown('''<style>
    .block-container {max-width:1120px;padding-top:2.8rem;padding-bottom:4rem;}
    .learn-hero {padding:clamp(24px,4vw,44px);border-radius:24px;
      background:linear-gradient(125deg,#10283f,#164e63 65%,#0f766e);
      color:#fff;margin-bottom:28px;box-shadow:0 12px 35px #10283f18;}
    .learn-hero .eyebrow {font-size:.78rem;letter-spacing:.15em;color:#99f6e4;font-weight:700;}
    .learn-hero h1 {font-size:clamp(1.8rem,4vw,2.8rem);line-height:1.25;color:#fff;padding:16px 0 12px;}
    .learn-hero p {color:#d9eef2;line-height:1.8;margin:0;max-width:750px;}
    .learn-card {padding:24px;border:1px solid #dbe5ec;border-radius:18px;
      background:var(--secondary-background-color,#f3f6fa);height:100%;margin-bottom:16px;}
    .learn-card .tag {font-size:.76rem;color:#0f766e;font-weight:800;letter-spacing:.08em;}
    .learn-card h3 {font-size:1.25rem;margin:12px 0;}
    .learn-card p {line-height:1.8;margin:0;}
    div[data-testid="stMetric"] {border:1px solid #dbe5ec;border-radius:16px;padding:16px;}
    div[data-testid="stForm"] {border-radius:20px;}
    @media(max-width:640px) {.block-container{padding-top:1.5rem;} .learn-hero{border-radius:16px;}}
    </style>''', unsafe_allow_html=True)
    st.markdown(f'''<section class="learn-hero"><div class="eyebrow">MACHINE LEARNING LAB · {number}</div>
    <h1>{title}</h1><p>{subtitle}</p></section>''', unsafe_allow_html=True)


def card(tag, title, body):
    st.markdown(f'<article class="learn-card"><div class="tag">{tag}</div><h3>{title}</h3><p>{body}</p></article>', unsafe_allow_html=True)
