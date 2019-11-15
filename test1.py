
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_frozen_graph("aIN256.pb", ["Placeholder_1"], ["Squeeze"])
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
tflite_model = converter.convert()
open("aOUT256" + ".tflite", "wb").write(tflite_model)
