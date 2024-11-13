import google.generativeai as genai
import re

from core.settings import GEMINI_KEY


genai.configure(api_key=GEMINI_KEY)


def find_attendants(text):

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(f"""
        Gemini, o texto abaixo é referente a uma ata sobre a conversa de gestores quanto ao desempenho nas ligações dos atendentes:

        {text}

        A tarefa que esperamos que realize é pegar os nomes dos atendentes e retornar APENAS os nomes em formato de lista conforme o exemplo abaixo:

        ["Nome Um", "Nome Dois"]

        Não adicione nenhum texto que não seja esta lista e caso o nome já esteja na lista, não adicionar novamente. No caso de não encontrar nenhum nome, retorne: []
    """)

    response = f"teste{response.text}teste"
    
    response = re.search(r'\[(.*?)\]', response)
    
    if response:
        list_names = [item.strip().strip('"') for item in response.group(1).split(',')]
        return list_names
    
    else:
        return []


# if __name__ == "__main__":
#     find_attendants("""
#         Resumo da Reunião - Chamadas Legais
#         Na reunião entre os gestores de "Chamadas Legais", discutiram-se aspectos fundamentais
#         sobre a performance dos atendimentos, estratégias de melhoria e feedbacks dos clientes.
#         Presentes estavam os gestores Paulo, Laura, Ricardo, Fernanda e Thiago, que compartilharam
#         suas visões sobre a qualidade dos serviços prestados e as áreas de oportunidade. Paulo abriu
#         a reunião destacando as estatísticas gerais de satisfação, mostrando que a média dos
#         atendimentos ainda estava dentro do aceitável, mas poderia melhorar em certos aspectos,
#         especialmente na resolução de problemas em primeira chamada. Durante a apresentação dos
#         dados, Laura comentou que a questão da empatia no atendimento deveria ser mais trabalhada
#         e apresentou um exemplo de conversa onde o cliente demonstrava insatisfação, mencionando
#         que a atendente Amanda tentou contornar a situação explicando que os procedimentos
#         precisavam ser seguidos. Ricardo, por sua vez, enfatizou a importância de entender as
#         métricas em detalhes e solicitou a inserção de mais conversas no banco de dados para análise.
#         Fernanda sugeriu que fosse realizada uma revisão nas etapas de treinamento dos atendentes
#         para garantir que todos seguissem o mesmo padrão e mencionou uma conversa em que o
#         atendente Carlos precisou esclarecer dúvidas sobre o uso do aplicativo da empresa,
#         mencionando que alguns clientes têm dificuldades em navegar por certas funções. Thiago
#         trouxe à tona a importância de revisar o feedback dos clientes insatisfeitos e sugeriu a criação
#         de relatórios específicos para esses casos, o que foi apoiado por Laura, que citou uma
#         conversa com um cliente insatisfeito, onde o atendente Carlos foi mencionado. Paulo também
#         enfatizou a importância de aumentar a proatividade dos atendentes, considerando que muitas
#         vezes eles esperam que o cliente peça ajuda em vez de antecipar possíveis questões que
#         surgem. Ricardo mencionou um caso recente em que um cliente solicitou suporte sobre o
#         pagamento de uma fatura, onde a atendente Amanda estava em uma conversa prolongada
#         para explicar o processo. O diálogo entre os gestores continuou com Paulo ressaltando a
#         necessidade de uma maior integração entre os sistemas de atendimento e o banco de dados
#         de clientes, a fim de otimizar a recuperação de informações e reduzir o tempo de resposta.
#         Laura sugeriu, como alternativa, criar uma interface de uso mais intuitivo no aplicativo. Thiago,
#         então, relatou uma conversa entre a atendente Amanda e um cliente, na qual se destacou a
#         falta de clareza na explicação dos procedimentos de cancelamento, o que, segundo ele,
#         poderia ser resolvido com um treinamento específico para casos de cancelamento. Fernanda
#         concluiu a reunião enfatizando a necessidade de realizar uma análise mensal dos
#         atendimentos com base nas conversas gravadas para identificar os principais pontos de
#         melhoria e ressaltou que um processo de feedback mais frequente e assertivo poderia ajudar a
#         corrigir rapidamente as falhas.
#     """)