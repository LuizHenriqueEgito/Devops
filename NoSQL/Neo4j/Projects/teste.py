from neo4j import GraphDatabase

# Configurações de conexão
uri = "bolt://localhost:7687"  # endereço do Bolt
user = "neo4j"                 # usuário
password = "neo4j1234"         # senha que você definiu

# Cria o driver
driver = GraphDatabase.driver(uri, auth=(user, password))

# Query para quem conhece Maria
query = """
MATCH (p:Pessoa)-[:CONHECE]->(m:Pessoa {nome: "Maria"})
RETURN p.nome AS QuemConheceMaria
"""
query_2 = '''
MATCH (p:Pessoa)
WHERE p.idade > 30
RETURN p.nome, p.idade;
'''

# Executa a query
with driver.session() as session:
    result = session.run(query)
    for record in result:
        print(record["QuemConheceMaria"])
    result = session.run(query_2)
    print(result)
    print(result.to_df())
# Fecha o driver
driver.close()
