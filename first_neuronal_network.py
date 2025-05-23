import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius = np.array([-40,-10,0,8,15,22,38],dtype = float)
fahrenheit = np.array([-40,14,32,46,59,72,100],dtype = float)

"""
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])
"""
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1,oculta2,salida])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)
print('Comenzando entrenamiento')
historial = modelo.fit(celsius,fahrenheit,epochs=1000, verbose = False)
print("modelo entrenado")


plt.xlabel("# epoca")
plt.ylabel("magnitud de perdida")
plt.plot(historial.history["loss"])
plt.show()


print("hagamos prediccion")
resultado = modelo.predict(np.array([100.0]))
print("resuultado es " + str(resultado) +"fahrenhait")

"""
print("variables inernas del modelo")
print(capa.get_weights()) #know the weights assigned to the neuronal
"""