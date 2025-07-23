import networkx
# Link permanente do grafo original: https://version-12-0.string-db.org/cgi/network?networkId=bKQZEePSoQZu
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
def main() -> None:
  grafo = construirGrafo()
  print(f"Centralidade de grau: {(networkx.degree_centrality(grafo)['MMP13'] * 100):.2f}%")
  # Preferimos analisar algumas métricas utilizando porcentagens, pois indicam melhor a quantidade de nós relacionados com a métrica utilizada.
  print(f"Excentricidade do nó: {networkx.eccentricity(grafo)['MMP13']}")
  print(f"Radialidade de grafo: {networkx.radius(grafo)}")
  # Note que as duas métricas acima são iguais, o que indica que o MMP13 possui a menor excentricidade, e então pode ser considerado o "centro" do grafo

  print(f"Centralidade de intermediação: {(networkx.betweenness_centrality(grafo)['MMP13'] * 100):.2f}%")
  print(f"Centralidade de autovetor: {(networkx.eigenvector_centrality(grafo)['MMP13'] * 100):.2f}%")
main()
