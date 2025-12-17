# Sistema de Gerenciamento de Pedidos Distribuídos (MQTT)

Este projeto implementa um **sistema distribuído de gerenciamento de pedidos no estilo delivery**, utilizando o protocolo **MQTT** e o **broker público HiveMQ**, conforme proposto no material da disciplina.

O sistema simula a comunicação entre **Cliente**, **Restaurante** e **Entregador**, explorando o modelo *publish/subscribe* e conceitos de sistemas distribuídos.

---

## Conceitos Utilizados

* Protocolo **MQTT**
* Arquitetura **Publish/Subscribe**
* **Broker MQTT** (HiveMQ público)
* Comunicação assíncrona
* Sistemas distribuídos

---

## Arquitetura do Sistema

O sistema é composto por três entidades principais:

* **Cliente**: cria e envia pedidos
* **Restaurante**: recebe pedidos e atualiza o status
* **Entregador**: acompanha o status e finaliza a entrega

Toda a comunicação ocorre **exclusivamente via broker MQTT**, não havendo comunicação direta entre os componentes.

---

## Broker MQTT

* **Broker utilizado:** HiveMQ público
* **Endereço:** `broker.hivemq.com`
* **Porta:** `1883`

Para evitar conflitos com outros usuários do broker público, foi adotado um **namespace exclusivo de tópicos**.

---

## Estrutura de Tópicos

Prefixo utilizado:

```
delivery/PSD_3VA/iago
```

Tópicos do sistema:

| Função           | Tópico                                      |
| ---------------- | ------------------------------------------- |
| Novo pedido      | `delivery/PSD_3VA/iago/pedidos/novo`        |
| Status do pedido | `delivery/PSD_3VA/iago/pedidos/{id}/status` |

O caractere `+` é utilizado como *wildcard* para capturar qualquer identificador de pedido.

---

## Ordem de Execução (IMPORTANTE)

Devido ao funcionamento do MQTT e ao uso de broker público, a **ordem de execução dos scripts é fundamental**:

1. **restaurante.py**
2. **entregador.py**
3. **cliente.py**

Caso o cliente seja executado antes dos subscribers, a mensagem pode não ser entregue.

---

## Funcionamento do Sistema

1. O **Cliente** publica um novo pedido
2. O **Restaurante** recebe o pedido e publica atualizações de status
3. O **Entregador** recebe o status "pronto" e finaliza a entrega

Todo o fluxo pode ser monitorado em tempo real utilizando ferramentas como **MQTT Explorer**.

---

## Tecnologias Utilizadas

* Python 3
* Biblioteca `paho-mqtt`
* HiveMQ Public Broker

---

## Instalação da Dependência

```bash
python -m pip install paho-mqtt
```

---

Projeto desenvolvido para fins acadêmicos na disciplina de Projeto Sistemas Distribuídos 
2025.2 Universidade Federal Rural de Pernambuco - Unidade Acadêmica de Serra-Talhada
Feito por: Caio César Lima Diniz, Iago Felipe Freire Nascimento
Sobre a supervisão do Professor: Celso Augusto R. L Brennand.
