import paho.mqtt.client as mqtt
import json
import time

broker = "broker.hivemq.com"


def on_message(client, userdata, msg):
    pedido = json.loads(msg.payload.decode())
    pedido_id = pedido["id"]
    print("Pedido recebido:", pedido)

    time.sleep(2)
    client.publish(f"delivery/pedidos/{pedido_id}/status", "preparando", qos=0)
    print("Status: preparando")

    time.sleep(2)
    client.publish(f"delivery/pedidos/{pedido_id}/status", "pronto", qos=0)
    print("Status: pronto")


client = mqtt.Client()
client.connect(broker, 1883, 60)
client.subscribe("delivery/pedidos/novo")

client.on_message = on_message
client.loop_forever()
