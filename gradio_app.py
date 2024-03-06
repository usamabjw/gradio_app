import numpy as np
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * intensity

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(
    fn=[greet, sepia],  # Combine both functions
    inputs=[
        ["text", gr.Slider(value=2, minimum=1, maximum=10, step=1)],
        gr.Image()
    ],
    outputs=[gr.Textbox(label="greeting", lines=3), gr.Image()],
)

demo.launch()
