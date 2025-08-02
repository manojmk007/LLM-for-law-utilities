# 🇮🇳 Indian Law-Focused LLM  
**Fine-Tuned RoBERTa Model for Indian Legal Research**

## 📌 Project Overview

This project introduces a transformer-based Legal Language Model (LLM) tailored for Indian law, leveraging **RoBERTa** and fine-tuned on **859 annotated Central Acts of India**. It empowers statute-aware question answering, section-level legal mapping, and contextual understanding of Indian legislation.

## 🎯 Features

- ✅ Fine-tuned RoBERTa on structured Indian legal documents  
- ✅ Section-wise context understanding & retrieval  
- ✅ Statute-aware question answering  
- ✅ Deployed on AWS EC2 via Docker & Flask  
- ✅ OAuth2 security and DVC-based version control  
- ✅ 88.6% F1-score on legal QA benchmark  
- ✅ Real-time query interface for legal professionals

## 🧠 Model Architecture

- **Base Model**: `roberta-base`  
- **Fine-Tuning Dataset**: 859 JSON legal documents annotated with chapter, section, and clause mappings  
- **Tokenizer**: Byte-Pair Encoding (BPE)  
- **Training Framework**: HuggingFace Transformers, PyTorch  
- **Evaluation Metric**: F1-Score, EM (Exact Match)

## 🔍 Dataset

- **Source**: Indian Central Government Acts  
- **Format**:
```json
{
  "Act Title": "THE NATIONAL HOUSING BANK ACT, 1987",
  "Chapters": {
    "0": {
      "Name": "PRELIMINARY",
      "Sections": {
        "Section 1.": {
          "heading": "Short title, extent and commencement.",
          "paragraphs": {
            "0": "This Act may be called..."
          }
        }
      }
    }
  }
}
```
- **Total Files**: 859 JSON files  
- **Preprocessing**: Flattened to QA pairs for RoBERTa fine-tuning

## 🚀 Deployment

- **Platform**: AWS EC2  
- **Containerization**: Docker  
- **Frontend**: **Flask** web framework  
- **Security**: OAuth2 Auth with session timeout  
- **APIs**: RESTful endpoints for inference

## 🧪 Results

- **F1-Score**: 88.6%  
- **Exact Match**: 81.3%  
- **Validation Loss**: 0.43  
- **Legal Retrieval Time**: Reduced by 40%  
- **Tested On**: Legal QA queries, 150 samples

## 🔐 Security and Versioning

- **OAuth2 Authentication**  
- **DVC (Data Version Control)** for dataset and model reproducibility  
- **Docker Image** with separate containers for API, frontend (Flask), and inference logic

## 📈 Future Enhancements

- Multilingual legal support (IndicBERT, mBART)  
- Chatbot interface for legal advisory  
- Case law and judgment prediction module  
- Blockchain-based legal text integrity  
- Explainable AI with attention visualization  
- Mobile app support (Flutter or React Native)

## 🧑‍💻 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/indian-legal-llm.git
cd indian-legal-llm

# Build Docker image
docker build -t legal-llm .

# Run container
docker run -p 5000:5000 legal-llm
```

Then open: `http://localhost:5000` (Flask App)

## 📚 References

- Chalkidis et al., “LexGLUE,” NeurIPS 2021  
- Zhong et al., “LegalBERT,” ACL 2020  
- Magesh et al., “AI on Trial,” Stanford HAI 2024  
- Liu et al., “RoBERTa,” arXiv 2019