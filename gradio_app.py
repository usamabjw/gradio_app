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

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            greeting = gr.Textbox(label="Name")
            greet_intensity=gr.Slider(value=2, minimum=1, maximum=10, step=1)
            greet_button=gr.Button(value="Greet")
        with gr.Column():
            out_greet= gr.Textbox(label="Greeting", lines=3)
    with gr.Row():
        with gr.Column():
            in_img = gr.Image()
            filter_button=gr.Button(value="Apply Filter")
        with gr.Column():
            out_img = gr.Image()

    greet_button.click(greet, inputs=[greeting,greet_intensity], outputs=out_greet, api_name="greeting the user")
    filter_button.click(sepia,inputs=in_img, outputs=out_img, api_name="applying filter")
    

demo.launch()
