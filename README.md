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
