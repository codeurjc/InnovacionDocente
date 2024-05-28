import gradio as gr
from Results import Results

results = Results()

subjects = [
    "All",
    "Ampliación de Ingeniería del Software",
    "Desarrollo de Aplicaciones Distribuidas",
    "Desarrollo de Aplicaciones Web",
    "Estructura de datos II",
    "Lenguajes de Programación - Haskell",
    "Lenguajes de Programación - Python",
]

with (gr.Blocks() as demo):
    
    # VISTA
    
    with gr.Row():
        with gr.Column(scale=2):
            subject_filter = gr.Dropdown(label="Subject", choices=subjects, value="All")
            results_view = gr.Dataframe(value=results.withColors(),height=600,interactive=False)
            current_result = gr.Textbox(label="Current result id",value=4)
            
        with gr.Column(scale=4):
            with gr.Accordion("Student answer", open=True):
                final_answer = gr.Markdown()
            
            with gr.Row():
                with gr.Column(scale=4):
                    comment = gr.Textbox(label="Comentario de la calificación",
                           lines=10, interactive=True)
                with gr.Column(scale=4):
                    grade = gr.Dropdown(label="Calificación",
                                            choices=["-", "Buena", "Regular", "Mala"])
                    copy_paste = gr.Checkbox(label="El estudiante ha copiado y pegado la respuesta de la IA")
                    misunderstood = gr.Checkbox(label="El estudiante ha malinterpretado la respuesta de la IA")
                    bad_ia_answer = gr.Checkbox(label="La respuesta de la IA es incorrecta")
                    save = gr.Button("Guardar",interactive=True, variant="primary")
                
            
            with gr.Accordion("Best IA conversation", open=True):
                best_ia_answer = gr.Markdown()
            with gr.Accordion("ChatGPT conversation", open=False):
                chatgpt_answer = gr.Markdown()
            with gr.Accordion("Gemini conversation", open=False):
                gemini_answer = gr.Markdown()
            with gr.Accordion("Copilot conversation", open=False):
                copilot_answer = gr.Markdown()
                
    # CALLBACKS
    
    # Filter by subject
    
    @subject_filter.change(inputs=[subject_filter], outputs=[results_view])
    def filter_by_subject(choice):
        results.applySelection(choice)
        return gr.update(value=results.withColors())

    # On result selection from the list
    
    @results_view.select(inputs=[results_view], outputs=[
        current_result, final_answer, best_ia_answer, 
        chatgpt_answer, gemini_answer, copilot_answer, 
        comment, grade, copy_paste, misunderstood, bad_ia_answer
    ])
    def select_result(event: gr.SelectData, data):
        id = data.iloc[event.index[0]]['id']
        
        current_result = results.getResultById(id)
        return ( 
            gr.update(value=current_result['id']),
            gr.update(value=Results.getStudentAnswer(current_result)), 
            gr.update(value=Results.getBestAnswerIA(current_result)),
            gr.update(value=Results.getAnswersByIA(current_result, 'ChatGPT')),
            gr.update(value=Results.getAnswersByIA(current_result, 'Gemini')),
            gr.update(value=Results.getAnswersByIA(current_result, 'Copilot')),
            gr.update(value=current_result['comment']),
            gr.update(value=current_result['grade']),
            gr.update(value=current_result['copy_paste']),
            gr.update(value=current_result['misunderstood']),
            gr.update(value=current_result['bad_ia_answer'])
        )
        
    @save.click(inputs=[current_result, comment, grade, copy_paste, misunderstood, bad_ia_answer], 
                outputs=[results_view])
    def save_grade(id,comment, grade, copy_paste, misunderstood, bad_ia_answer):
        results.updateResult(id, grade, comment, copy_paste, misunderstood, bad_ia_answer)
        results.save()
        return gr.update(value=results.withColors())

demo.launch(server_name='0.0.0.0')
