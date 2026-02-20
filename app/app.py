import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

# =========================
# ENTÊTE – VERSION STABLE ET PRO
# =========================

# -------------------------
# Entête principale en haut
# -------------------------
st.markdown("""
    <div style="background-color:#eaf2f8; padding:20px; border-radius:10px; text-align:center;">
        <h1 style="color:#2E86C1; margin-bottom:5px;">Fiche Technique du sujet PFE</h1>
        <h4 style="color:#1B4F72; margin-top:0;"> Déploiment d'un assistant interne sécurisé basé sur RAG pour la gestion documentaire</h4>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # petit espace entre les sections

# -------------------------
# Informations de l’étudiant et encadrants en dessous
# -------------------------
st.markdown("""
    <div style="background-color:#f9f9f9; border:2px solid #4CAF50; padding:15px; border-radius:10px; max-width:600px; margin:auto;">
        <p style="margin:6px 0;"><strong>Étudiant :</strong> Ettouyjer Yasmine</p>
        <p style="margin:6px 0;"><strong>Encadrants :</strong> Mme Mouna Kaouni & Mr Moulay Driss Laanaoui</p>
        <p style="margin:6px 0;"><strong>Entreprise :</strong> Atlas Cloud Services, Benguerir</p>
        <p style="margin:6px 0;"><strong>Date de début :</strong> 18 février 2026</p>
    </div>
""", unsafe_allow_html=True)





# =========================
# ONGLETS
# =========================
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Contexte & Problématique",
    "État de l’art",
    "Justification scientifique",
    "Architecture & Méthodologie",
    "Analyse des risques & Monitoring",
    "Planning",
    "Diagrammes BPMN"
])

# =========================
# TAB 1 – CONTEXTE & PROBLÉMATIQUE
# =========================
with tab1:
    st.header("Contexte & Problématique")
    st.write("""
    Le projet vise à concevoir un assistant interne intelligent basé sur le modèle 
    Retrieval-Augmented Generation (RAG) pour améliorer l’accès aux documents internes 
    (guides techniques, procédures, rapports, documentations API) au sein d’Atlas Cloud.
    
    Problématiques :
    - Fragmentation des informations et perte de temps
    - Dépendance à l’expertise individuelle
    - Risque de réponses incohérentes ou obsolètes
    """)

# =========================
# TAB 2 – ÉTAT DE L’ART
# =========================
with tab2:
    st.header("État de l’art")
    st.write("""
    Le RAG a été introduit par Patrick Lewis et al. (NeurIPS 2020). 
    Cette approche combine :
    - **Récupération documentaire** pour extraire les informations pertinentes
    - **Modèle génératif** pour produire des réponses contextualisées
    
    Autres travaux récents : 
    - Études sur les embeddings vectoriels (FAISS, Chroma, Weaviate)
    - Applications RAG en entreprises pour centraliser la connaissance interne
    """)

    # Expander pour les références académiques
    with st.expander(" Références académiques"):
        st.write("""
        - Lewis et al., NeurIPS 2020 : Retrieval-Augmented Generation
        - FAISS, Chroma, Weaviate : bases vectorielles
        - LangChain : pipeline modulaire pour RAG
        """)

# =========================
# TAB 3 – JUSTIFICATION SCIENTIFIQUE
# =========================
with tab3:
    st.header("Justification scientifique")
    st.write("""
    Ce projet est justifié scientifiquement par :
    1. La nécessité de réduire les hallucinations dans les réponses génératives
    2. L’amélioration de la précision des réponses via RAG
    3. La traçabilité et la vérifiabilité des sources
    """)

# =========================
# TAB 4 – ARCHITECTURE & MÉTHODOLOGIE
# =========================
with tab4:
    st.header("Technologies récentes intégrées")
    st.write("""
    - LLM modernes (API OpenAI / modèles open-source récents)
    - Retrieval-Augmented Generation (RAG avancé)
    - Bases vectorielles optimisées (FAISS, Chroma, Weaviate)
    - Embeddings de nouvelle génération
    - Pipeline modulaire via LangChain
    - Interface interactive Streamlit
    - Monitoring via logging structuré
    """)


    st.subheader("Pipeline technique")
    st.image("Flowchart.drawio.png", caption="pipeline techniquede notre projet")


    st.subheader("Déploiement sur la plateforme Atlas Cloud Service")
    st.image("Déploiment RAG sur ACS.png", caption="Déploiment du systeme RAG sur la plateforme ACS")

    st.subheader("Méthodologie d’évaluation scientifique")
    st.write("""
    - Precision, Recall@k, F1-score
    - Taux d’hallucination
    - Temps moyen de réponse
    - Satisfaction utilisateur (questionnaire)
    """)
# =========================
# TAB 5 – ANALYSE DES RISQUES & MONITORING
# =========================
with tab5:
    st.header(" Analyse des risques &  Monitoring")

    # Création de deux colonnes pour séparer Risques et Mitigation
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚠️ Risques Techniques")
        st.write("""
        - Qualité variable des documents sources
        - Latence élevée
        - Hallucinations du modèle
        """)

        st.subheader("⚠️ Risques Organisationnels")
        st.write("""
        - Résistance au changement
        - Adoption limitée par les utilisateurs
        """)

    with col2:
        st.subheader("🛠️ Mitigation Technique")
        st.write("""
        - Nettoyage et normalisation
        - Optimisation des index vectoriels
        - Vérification des sources
        """)

        st.subheader("🛠️ Mitigation Organisationnelle")
        st.write("""
        - Phase de tests utilisateurs
        - Intégration progressive
        """)

    # Ajouter un expander pour le monitoring
    with st.expander("📊 Monitoring & Observabilité"):
        st.write("""
        - **Journalisation** des requêtes et réponses
        - **Dashboard** d’utilisation pour suivi en temps réel
        - Analyse des **requêtes fréquentes**
        - Suivi des **KPIs** pour amélioration continue
        - Historique des anomalies et alertes
        """)

 

# =========================
# TAB 6 – PLANNING & LIVRABLES
# =========================
with tab6:
    st.header("Planning sur 6 mois")
    planning = {
        "Phase": [
            "Mois 1 : Analyse & Revue bibliographique",
            "Mois 2 : Préparation des données",
            "Mois 3 : Implémentation pipeline RAG",
            "Mois 4 : Optimisation & Sécurisation",
            "Mois 5 : Évaluation & Tests utilisateurs",
            "Mois 6 : Documentation & Industrialisation"
        ]
    }
    st.table(planning)


# =========================
# TAB 7 – DIAGRAMMES BPMN
# =========================
with tab7:
    st.header("Diagrammes BPMN – Processus métier")
    st.image("diagramme BPMN.png", caption="Diagramme d’architecture entreprise niveau PFE")
