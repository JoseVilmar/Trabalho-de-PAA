# Trabalho-de-PAA
---

## ANÁLISE DE COMPLEXIDADE

### **Algoritmo Guloso:**
```
Complexidade de Tempo: O(k × |P| × |I|)

Detalhamento:
- Loop externo: k iterações
- Loop interno: testa |P| plantas
- Para cada planta: verifica |I| interesses

Exemplo: k=3, |P|=10, |I|=8
→ 3 × 10 × 8 = 240 operações

Complexidade de Espaço: O(|P| × |I|)
- Matriz de cobertura
```

### **Força Bruta:**
```
Complexidade de Tempo: O(C(|P|,k) × |I|)

Onde C(|P|,k) = |P|! / (k! × (|P|-k)!)

Exemplo: |P|=10, k=3
→ C(10,3) = 120 combinações
→ 120 × 8 = 960 operações

Para |P|=20, k=5
→ C(20,5) = 15504 combinações (inviável!)
```

---

## ESTRUTURA DA APRESENTAÇÃO

### **Slide 1: Motivação** (2 min)
- Problema: Redução de árvores em centros urbanos
- Consequência: Ilhas de calor, menor qualidade de vida
- Solução: Plantio estratégico com recursos limitados

### **Slide 2: Modelagem** (3 min)
```
┌─────────────────────────────────────┐
│  Entrada:                           │
│  • Candidatos ao plantio (P)        │
│  • Pontos de interesse (I)          │
│  • Pesos de relevância (w)          │
│  • Raio de sombra (r)               │
│  • Limite de árvores (k)            │
│                                     │
│  Objetivo:                          │
│  Maximizar Σ w_i × coberto(i)       │
│                                     │
│  Restrição: usar no máximo k árvores│
└─────────────────────────────────────┘
```

### **Slide 3: Grafo Bipartido** (2 min)
```
  Candidatos          Pontos de Interesse
      (P)                    (I)
      
      p₁ ────────────────── i₁ (peso=2)
       │  \              /
       │    \          /
      p₂ ────────────────── i₂ (peso=4)
       │        \    /
       │          \/
      p₃ ────────────────── i₃ (peso=5)


Aresta existe se dist(p,i) ≤ r
