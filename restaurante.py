import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883

def on_message(client, userdata, msg):
    status = msg.payload.decode()
    print(f"{msg.topic} -> {status}")

    if status == "pronto":
        pedido_id = msg.topic.split("/")[2]
        client.publish(f"delivery/entrega/{pedido_id}/status", "entregue", qos=0)
        print("Entrega finalizada")


client = mqtt.Client()
client.connect(broker, 1883, 60)
client.subscribe("delivery/pedidos/+/status")

client.on_message = on_message
client.loop_forever()
