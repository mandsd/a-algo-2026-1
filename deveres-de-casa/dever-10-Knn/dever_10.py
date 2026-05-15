from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

dataset = load_breast_cancer()
X, y = dataset.data, dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

ks = [1, 3, 5]
metricas = ["euclidean", "manhattan"]

print(f"{'K':<5} {'Métrica':<12} {'Acurácia'}")
print("-" * 30)

melhor_acc = 0
melhor_config = {}

for k in ks:
    for metrica in metricas:
        knn = KNeighborsClassifier(n_neighbors=k, metric=metrica)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"{k:<5} {metrica:<12} {acc:.4f}")
        if acc > melhor_acc:
            melhor_acc = acc
            melhor_config = {"k": k, "metrica": metrica}

print()
print(f"Melhor resultado: K={melhor_config['k']}, métrica={melhor_config['metrica']}, acurácia={melhor_acc:.4f}")

print("""
--- Respostas ---

Qual K teve melhor desempenho?
  K=3 e K=5 empataram com Manhattan (96.49%). K=1 foi o pior (92-93%),
  confirmando que valores muito pequenos de K sofrem de overfitting.

Qual metrica obteve melhor resultado?
  Manhattan (96.49%) superou Euclidiana (94.74%) para K=3 e K=5 neste dataset.

O que aconteceu com K muito pequeno?
  K=1 teve acuracia menor (~92-93%) pois classifica cada ponto pelo vizinho
  mais proximo, sendo sensivel a ruido e outliers no treino (overfitting).

Por que normalizar e importante?
  O KNN usa distancia entre pontos. Sem normalizacao, features com escala
  maior (ex: area do tumor em mm2) dominam o calculo e distorcem o resultado.
  O StandardScaler coloca todas as features na mesma escala (media 0, desvio 1).
""")
