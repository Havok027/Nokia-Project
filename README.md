![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento/In%20Development-orange?style=flat-square)

# 📡 TSSR Automation & Photo AI (Nokia-TIM Brasil)

[PT-BR] Este projeto automatiza o fluxo de criação de documentos **TSSR (Technical Site Survey Report)** para a malha Nokia-TIM Brasil. Ele resolve o problema da fragmentação de dados técnicos e a demora na organização de evidências fotográficas em campo.

[EN] This project automates the creation of **TSSR (Technical Site Survey Report)** documents for the Nokia-TIM Brazil network. It solves the problem of fragmented technical data and the time-consuming manual organization of field photo evidence.

---

## 🛠️ O que o projeto faz? | What does the project do?

### 1. Engine de Dados (ETL) | Data Engine (ETL)
* **PT:** Cruza e processa automaticamente três bases críticas da Nokia: **SPAZIO**, **PLANO_NOMINAL** e **MAE**.
* **EN:** Automatically merges and processes three critical Nokia databases: **SPAZIO**, **PLANO_NOMINAL**, and **MAE**.

### 2. Automação Documental | Documentation Automation
* **PT:** Gera descritivos técnicos padronizados e exporta dados tratados diretamente para o Excel, preenchendo o máximo de campos possíveis para a documentação TSSR.
* **EN:** Generates standardized technical descriptions and exports treated data directly to Excel, pre-filling as many fields as possible for TSSR documentation.

### 3. Smart Photo Organizer (IA/ML)
* **PT:** Módulo de Machine Learning que classifica fotos automaticamente (GABINETES, ANTENAS, etc.) e as vincula ao relatório final.
* **EN:** Machine Learning module that automatically classifies photos (CABINETS, ANTENNAS, etc.) and links them to the final report.

---

## 🚀 Roadmap de Desenvolvimento | Development Roadmap

- [x] **Arquitetura & Planejamento / Architecture & Planning** (Abril/April 2024)
  - Definição das bibliotecas / Library definition (`Pandas`, `Openpyxl`).
- [x] **Módulo de Extração Individual / Individual Extraction Module** (Em andamento / In Progress)
  - Leitura isolada das planilhas e tratamento inicial / Isolated reading and initial data cleaning.
- [ ] **Script de Merge (Unificação) / Merge Script (Unification)**
  - Cruzamento das bases via Site ID / Merging databases via Site ID.
- [ ] **Gerador de Textos TSSR / TSSR Text Generator**
  - Lógica de automação para descritivos Nokia-TIM / Automation logic for Nokia-TIM descriptions.
- [ ] **Classificação de Imagens / Image Classification (ML)**
  - Treinamento do modelo de fotos / Photo model training.
- [ ] **Integração Final / Final Integration**
  - Exportação completa (Dados + Fotos) / Complete export (Data + Photos).

---

> **Disclaimer:** > [PT] Este projeto é uma ferramenta de auxílio técnico. Dados sensíveis de rede devem ser manuseados seguindo as políticas de segurança.
> [EN] This project is a technical aid tool. Sensitive network data must be handled according to security policies.