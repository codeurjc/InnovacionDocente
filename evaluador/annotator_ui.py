import gradio as gr
import pandas as pd
from Results import Results

results = Results('../Results.xlsx')
subjects = [
    "All",
    "Ampliación de Ingeniería del Software",
    "Desarrollo de Aplicaciones Distribuidas",
    "Desarrollo de Aplicaciones Web",
    "Estructura de datos II",
    "Lenguajes de Programación - Haskell",
    "Lenguajes de Programación - Python",
]

current_result = results.asDataFrame().iloc[0]

with (gr.Blocks() as demo):
    
    # VISTA
    
    with gr.Row():
        with gr.Column(scale=2):
            subject_filter = gr.Dropdown(label="Subject", choices=subjects, value="All")
            results_view = gr.Dataframe(value=results.asDataFrame()[['id','question']],height=600,interactive=False)
        
        with gr.Column(scale=4):
            with gr.Accordion("Student answer", open=True):
                final_answer = gr.Markdown(value=Results.getStudentAnswer(current_result))
            with gr.Accordion("Best IA conversation", open=True):
                best_ia_answer = gr.Markdown(value=Results.getBestAnswerIA(current_result))
            with gr.Accordion("ChatGPT conversation", open=False):
                chatgpt_answer = gr.Markdown(value=Results.getAnswersByIA(current_result, 'ChatGPT'))
            with gr.Accordion("Gemini conversation", open=False):
                gemini_answer = gr.Markdown(value=Results.getAnswersByIA(current_result, 'Gemini'))
            with gr.Accordion("Copilot conversation", open=False):
                copilot_answer = gr.Markdown(value=Results.getAnswersByIA(current_result, 'Copilot'))
                
    # CALLBACKS
    
    # Filter by subject
    
    @subject_filter.change(inputs=[subject_filter], outputs=[results_view])
    def filter_by_subject(choice):
        if choice == "All":
            selection = results.asDataFrame()
        else:
            selection = results.asDataFrame()[results.asDataFrame()['subject'] == choice]
        return selection[['id', 'question']]

    # On result selection from the list
    
    @results_view.select(inputs=[results_view], outputs=[
        final_answer, best_ia_answer, chatgpt_answer, gemini_answer, copilot_answer
    ])
    def select_result(event: gr.SelectData, data):
        id = data.iloc[event.index[0]]['id']
        current_result = results.getResultById(id)
        return ( 
            gr.update(value=Results.getStudentAnswer(current_result)), 
            gr.update(value=Results.getBestAnswerIA(current_result)),
            gr.update(value=Results.getAnswersByIA(current_result, 'ChatGPT')),
            gr.update(value=Results.getAnswersByIA(current_result, 'Gemini')),
            gr.update(value=Results.getAnswersByIA(current_result, 'Copilot'))
        )

demo.launch(server_name='localhost')
