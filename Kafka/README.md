# KAFKA
Um `tópico KAFKA` é um **canal** onde os dados são *publicados* e *consumidos*. É como se fosse uma fila ou um stream contínuo de eventos, as *mensagens chegam* e as mensagens são *consumidas*. Ele é formado por esses **3** componentes:
1. **Producer**: Envia dados para um tópico;
2. **Tópico**: Armazena e organiza esses dados;
3. **Consumer**: Lê os dados do tópico.

Por exemplo, Tópico de pedidos:
#### Producer (backend)
```json
{"pedido_id": 1, "valor": 100}
{"pedido_id": 2, "valor": 250}
```
#### Consumers:
- Um salva no banco;
- Outro faz análise;
- Outro dispara notificação.
Todos lêem o mesmo **tópico**, sem interferir um no outro.

Um tópico KAFKA serve para **Desacoplar Sistemas**
Sem o kafka esse seria o fluxo:
```txt
Sistema A → chama API do Sistema B
```
Com `KAFKA`:
```txt
Sistema A → publica no tópico
Sistema B → consome quando quiser
```
Isso evita dependencia direta e sistema quebrando em cadeia.

## Buffer
O `KAFKA` também serve como **Buffer de dados**, por exemplo:
- 10mil eventos chegam de uma vez.
O tópico kafka:
- Segura no tópico;
- Consumidores processam no ritmo deles.
Isso evita colapso do sistema.

## Streaming de Dados
Dados chegam o tempo todo e são processados.

## Reprocessamento
O `KAFKA` guarda os dados por um tempo, você pode ler tudo de novo desde o inicio.