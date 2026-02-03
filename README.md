# T-1000 (T de Tradutor, btw)

O T-1000 permite traduzir qualquer texto diretamente da sua caixa de input. Ele foi criado para eliminar o "copia e cola" entre editores e navegadores, agilizando seu fluxo de escrita com traduções instantâneas via Google ou OpenAI.

## Instalação

Você pode instalar o T-1000 de duas formas:

### Opção 1: Via pipx (Recomendado)

Ideal para usar o comando globalmente em qualquer lugar do sistema sem se preocupar com ambientes virtuais (requer pipx).

```Bash
pipx install git+https://github.com/slenderb13/t-1000.git
```

## Opção 2: Desenvolvimento (Manual)

1. Clone o repositório e acesse a pasta.
2. Crie e ative uma venv:
```Bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou .\.venv\Scripts\activate no Windows
```
3. Instale em modo editável:
```Bash
pip install -e .
```

## Configuração
É necessário que sua chave de API esteja no arquivo de configuração. Para isso:
1. Execute o programa passando a flag de configuração:
```bash
t1000 --configure # ou [-c]
```
2. O arquivo de configuração se abrirá automaticamente.
3. Cole sua chave de API no local indicado.

## Rodando o programa

Para iniciar o programa, utilize uma das flags de provedor:

```Bash
# Usando Google Tradutor (Padrão)
t1000 --google

# Usando OpenAI (Requer chave de API configurada)
t1000 --openai
```
> [!TIP]
> Você pode usar os atalhos curtos -g ou -o.
> Se nenhuma flag for passada, o Google será o provedor padrão.

## Como usar
O T-1000 funciona monitorando seu clipboard e simulando comandos de teclado.

1. Comece o texto com o idioma de destino e dois pontos:
```
it: Bom dia! Como vai?
ou
italiano: Bom dia! Como vai?
```
2. Selecione o texto, com o mouse ou Ctrl + A.
3. Pressione o atalho Ctrl + Alt + R.
4. Resultado: O texto selecionado será automaticamente substituído pela versão traduzida.
