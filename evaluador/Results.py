import pandas as pd
import os

response_map = {
 'Si. Me ha dado la mejor respuesta' : 3,
 'Si. Me ha dado una respuesta correcta, pero menos completa que otras IAs': 2,
 'No. Me ha contestado correctamente, pero no responde a la pregunta que le he hecho': 1,
 'No. Me ha contestado de forma errónea': 0
}

SAVE_PATH="results/Results_graded.xlsx"

class Results():
    def __init__(self):
        if os.path.exists(SAVE_PATH):
            self.results = pd.read_excel(SAVE_PATH, dtype = str)
            self.results_dict = self.results.to_dict()
        else:
            results_path = 'results/Results.xlsx'
            results_aux = pd.read_excel(results_path, dtype = str)
            self.results_dict = results_aux.to_dict()
            old_columns = results_aux.columns
            self.results = results_aux.rename(columns={
                'ID': 'id',
                'Hora de inicio': 'start_date',
                'Hora de finalización': 'end_date',
                'Selecciona la asignatura':'subject',
                'Selecciona la pregunta': 'question',
                'Conversación con ChatGPT': 'conversation_ChatGPT',
                '¿Cuántas preguntas has realizado a ChatGPT para obtener la mejor respuesta?': 'numTries_ChatGPT',
                'Conversación con Gemini': 'conversation_Gemini',
                '¿Cuántas preguntas has realizado a Gemini para obtener la mejor respuesta?': 'numTries_Gemini',
                'Conversación con Copilot': 'conversation_Copilot',
                '¿Cuántas preguntas has realizado a Copilot para obtener la mejor respuesta?': 'numTries_Copilot',
                '¿Te ha ayudado ChatGPT a responder a la pregunta?': 'rating_ChatGPT',
                '¿Te ha ayudado Gemini a responder a la pregunta?': 'rating_Gemini',
                '¿Te ha ayudado Copilot a responder a la pregunta?': 'rating_Copilot',
                'Indica tu respuesta a la pregunta ':'final_answer'
            }).drop(columns=old_columns, errors='ignore')
            
            self.results['rating_ChatGPT_reduced'] = self.results['rating_ChatGPT'].apply(lambda rating: response_map[rating])
            self.results['rating_Gemini_reduced'] = self.results['rating_Gemini'].apply(lambda rating: response_map[rating])
            self.results['rating_Copilot_reduced'] = self.results['rating_Copilot'].apply(lambda rating: response_map[rating])
        
            self.results['date'] = pd.to_datetime(self.results['start_date'], errors='coerce')
            self.results.loc[(self.results["date"]>"2024-03-15") & (self.results["date"]<"2024-04-15"), "subject"] = "Lenguajes de Programación - Haskell"
            self.results.loc[self.results["subject"]=="Lenguajes de Programación", "subject"] = "Lenguajes de Programación - Python"
            self.results['comment'] = " "
            self.results['grade'] = "-"
        self.applySelection("All")
    
    def applySelection(self, choice):
        if choice == "All":
            self.selection = self.results
        else:
            self.selection = self.results[self.results['subject'] == choice]
    
    def withColors(self):
        return self.selection[['id','question']].style.apply(self.color_cells, axis=1)
    
    def color_cells(self, reduced_row):
        row = self.getResultById(reduced_row['id'])
        style=pd.Series()
        if row['grade'] == '-':
            style['id'] = 'color: red'
            style['question'] = 'color: red'
        else:
            style['id'] = 'color: green'
            style['question'] = 'color: green'
        return style
    
            
    def asDataFrame(self):
        return self.results
    
    def getResultById(self, id):
        index = self.results.loc[self.results['id'] == id].index[0]
        return self.results.loc[index]
    
    def updateResult(self,id, grade, comment):
        index = self.results.loc[self.results['id'] == id].index[0]
        self.results.loc[index, 'grade'] = grade
        self.results.loc[index, 'comment'] = comment
        
    def save(self):
        self.results.to_excel(SAVE_PATH, index=False)
    
    @staticmethod
    def getStudentAnswer(result):
        return "<h2>["+result['id']+"] "+result['question']+" - "+result['subject']+ "</h2> <br>" + result['final_answer']
    
    @staticmethod
    def getBestAnswerIA(result):
        best = result['rating_ChatGPT_reduced']
        best_ia = 'ChatGPT'
        best_response = result['conversation_ChatGPT']
        if result['rating_Gemini_reduced'] > best:
            best = result['rating_Gemini_reduced']
            best_ia = 'Gemini'
            best_response = result['conversation_Gemini']
        if result['rating_Copilot_reduced'] > best:
            best = result['rating_Copilot_reduced']
            best_ia = 'Copilot'
            best_response = result['conversation_Copilot']
        return "<h2>"+best_ia + "</h2> <br>" + best_response
    
    @staticmethod
    def getAnswersByIA(result, ia):
        return "<h2>"+ia + "</h2> <br>" + result['conversation_' + ia]

    def __str__(self):
        return str(self.results)