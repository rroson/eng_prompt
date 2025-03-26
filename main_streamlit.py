import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if GROQ_API_KEY is None:
    raise ValueError('GROQ_API_KEY not found in environment variables')

assistant_msg = 'Você é um assistente inteligente que produz respostas lógicas, honestas e úteis para usuários humanos.'
assistant_convo = [{'role': 'system', 'content': assistant_msg}]

optimize_msg = (
    'Como um engenheiro especialista em prompts de IA que sabe como interpretar um prompt humano médio e reescrevê-lo de '
    'forma a aumentar a probabilidade do modelo gerar a resposta mais útil possível para qualquer solicitação humana específica. '
    'Em resposta aos prompts do usuário, você não responde como um assistente de IA. Você só responde com uma variação melhorada '
    'do prompt do usuário, sem explicações antes ou depois do prompt sobre o porquê de ele ser melhor. Não gere nada além da versão '
    'modificada do prompt do usuário feita pelos engenheiros especialistas. Se o prompt estiver em uma conversa com mais de um '
    'prompt humano, toda a conversa será fornecida como contexto para você avaliar como construir a melhor resposta possível naquela '
    'parte da conversa. Não gere nada além do prompt otimizado, sem cabeçalhos ou explicações do prompt otimizado.'
)

optimize_convo = [{'role': 'system', 'content': optimize_msg}]


def generate_groq_response(convo):
    client = Groq(api_key=GROQ_API_KEY)
    completion = client.chat.completions.create(
        messages=convo,
        model='deepseek-r1-distill-llama-70b',
        reasoning_format='hidden'
    )
    response_text = completion.choices[0].message.content
    return response_text

def main():
    st.title("Engenharia de Prompt")
    st.write(f"Modelo utilizado: deepseek-r1-distill-llama-70b")

    global assistant_convo, optimize_convo

    user_prompt = st.text_area("Prompt do Usuário:", "")

    if st.button("Otimizar Prompt"):
        if user_prompt:
            with st.spinner("Otimizando o prompt..."):
                optimized_prompt = generate_groq_response(optimize_convo + [{'role': 'user', 'content': f'HUMAN PROMPT:\n{user_prompt}'}])
            st.text_area("Prompt Otimizado:", value=optimized_prompt, height=200)
            assistant_convo.append({'role': 'user', 'content': optimized_prompt})
        else:
            st.warning("Por favor, insira um prompt.")


if __name__ == "__main__":
    main()
