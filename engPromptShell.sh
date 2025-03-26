#!/bin/bash

# Define o caminho para o diretório do projeto
PROJECT_DIR="/home/ninja/Desenvolvimento/Python/IA/eng_prompt"

# Define o caminho para o ambiente virtual
VENV_DIR="$PROJECT_DIR/.venv"

# Define o caminho para o script Streamlit
STREAMLIT_SCRIPT="$PROJECT_DIR/main_streamlit.py"

# Verifica se o ambiente virtual existe
if [ ! -d "$VENV_DIR" ]; then
  echo "Erro: Ambiente virtual não encontrado em $VENV_DIR"
  exit 1
fi

# Ativa o ambiente virtual
source "$VENV_DIR/bin/activate"

# Verifica se o ambiente virtual foi ativado corretamente
if [ -z "$VIRTUAL_ENV" ]; then
  echo "Erro: Falha ao ativar o ambiente virtual."
  exit 1
fi

# Navega para o diretório do projeto
cd "$PROJECT_DIR" || exit

# Executa o script Streamlit
echo "Iniciando Streamlit..."
streamlit run "$STREAMLIT_SCRIPT"

# Desativa o ambiente virtual (opcional, pois o script Streamlit provavelmente manterá o ambiente ativo)
deactivate

echo "Streamlit encerrado."
