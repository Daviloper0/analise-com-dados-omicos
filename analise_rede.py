import networkx
import tabulate
# Link permanente do grafo original: https://version-12-0.string-db.org/cgi/network?networkId=bKQZEePSoQZu
# Link do Google Collab para executar o código: https://colab.research.google.com/drive/1a2C0oMAIWLfMDW-0lni1bCttN_BkneYy?usp=sharing
def pegarVertices() -> list:
  vertices = [
    "MMP13", # Colagenase 3
    "COL18A1", # Cadeia de colágeno alfa-1(XVIII)
    "COL14A1", # Cadeia de colágeno alfa-1(XIV)
    "RUNX2", # Fator de transcrição 2 relacionado a Runt
    "CBFB", # Subunidade beta do fator de ligação ao núcleo
    "OPTC", # Opticina
    "PRSS1", # Cadeia alfa-tripsina 1
    "PLG", # Cadeia pesada A da plasmina
    "HSPG2", # Proteína central proteoglicana de sulfato de heparana
    "MMP14", # Metaloproteinase-14
    "MMP16" # Metaloproteinase-16
  ]
  return vertices

def pegarArestas() -> list:
  arestas = [
    ("MMP13", "COL18A1"),
    ("MMP13", "COL14A1"),
    ("MMP13", "RUNX2"),
    ("MMP13", "CBFB"),
    ("MMP13", "OPTC"),
    ("MMP13", "PLG"),
    ("MMP13", "PRSS1"),
    ("MMP13", "HSPG2"),
    ("MMP13", "MMP14"),
    ("MMP13", "MMP16"),
    ("COL18A1", "COL14A1"),
    ("MMP14", "MMP16"),
    ("HSPG2", "MMP14"),
    ("PLG", "HSPG2"),
    ("PRSS1", "PLG"),
    ("RUNX2", "CBFB")
  ]
  return arestas

def construirGrafo() -> networkx.classes.graph.Graph:
  grafo = networkx.Graph()
  grafo.add_nodes_from(pegarVertices())
  grafo.add_edges_from(pegarArestas())
  return grafo

def resultadoAnaliseVertices(grafo) -> None:
  resultado = {
      "Proteína": [],
      "Centralidade de Grau": [],
      "Excentricidade do Nó": [],
      "Centralidade de Intermediação": [],
      "Centralidade de Autovetor": []
      }
  for vertice in grafo.nodes:
    resultado["Proteína"].append(vertice)
    resultado["Centralidade de Grau"].append(f" {(networkx.degree_centrality(grafo)[vertice] * 100):.2f} %")
    # Preferimos analisar algumas métricas utilizando porcentagens, pois indicam melhor a quantidade de nós relacionados com a métrica utilizada.
    resultado["Excentricidade do Nó"].append(f"{networkx.eccentricity(grafo)[vertice]}")
    resultado["Centralidade de Intermediação"].append(f"{(networkx.betweenness_centrality(grafo)[vertice] * 100):.2f}%")
    resultado["Centralidade de Autovetor"].append(f"{(networkx.eigenvector_centrality(grafo)[vertice] * 100):.2f}%")

  print(tabulate.tabulate(resultado, headers = ["Proteína", "Centralidade de Grau", "Excentricidade do Nó", "Centralidade de Intermediação", "Centralidade de Autovetor"], tablefmt = "fancy_grid"))

def main() -> None:
  grafo = construirGrafo()
  print(f"Informações sobre o grafo:")
  print(f"* Radialidade do grafo: {networkx.radius(grafo)}\n")
  resultadoAnaliseVertices(grafo)
main()
