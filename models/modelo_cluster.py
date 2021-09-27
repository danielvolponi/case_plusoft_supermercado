# Importando os pacotes
import pandas as pd
from sklearn.preprocessing import Normalizer
import numpy as np
from sklearn.cluster import KMeans


def cluster_cidade(csv_municipio):
    municipio = pd.read_csv(csv_municipio,
                            decimal=".",
                            sep=";")
    df_modelo = pd.read_csv('../data/model/base_modelo.csv',
                            decimal=".",
                            sep=";")
    norm_df = df_modelo.drop(columns=['Código', 'Município'])
    norm_df = norm_df.dropna()
    norm_df = Normalizer().fit_transform(norm_df)
    norm_municipio = municipio.drop(columns=['Código', 'Município'])
    norm_municipio = norm_municipio.dropna()
    transform = Normalizer().fit(norm_df)
    transform = transform.fit_transform(norm_municipio)
    np.random.seed(75243)
    agrupador = KMeans(n_clusters=4)
    agrupador.fit(norm_df)
    label_cluster = {
        0: "Populoso",
        1: "Metropolitano",
        2: "Competitivo",
        3: "Oportuno",
    }
    predict = agrupador.predict(transform)
    return f'O município {municipio["Município"][0:1].values[0]}, faz parte do cluster {label_cluster[predict[0]]} '


if __name__ == '__main__':
    csv_municipio = '../data/model/base_modelo_teste.csv'
    print(cluster_cidade(csv_municipio))
