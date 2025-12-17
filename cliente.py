import paho.mqtt.client as mqtt
import json
import time

broker = "broker.hivemq.com"
pedido_id = 1

cliente = mqtt.Client()
cliente.connect(broker, 1883, 60)

pedido = {
    "id": pedido_id,
    "cliente": "João",
    "itens": ["Pizza", "Refrigerante"]
}

cliente.publish("delivery/pedidos/novo", json.dumps(pedido), qos=1)
print("Pedido enviado:", pedido)

time.sleep(1)
cliente.disconnect()
