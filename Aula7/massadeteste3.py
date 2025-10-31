from faker import Faker
import csv
 
# Criando uma instância do Faker
fake = Faker('pt_BR')
 
 
def criar_personas(num_personas=15):
    personas = []  # Lista para armazenar as personas
 
    for _ in range(15):
        persona = {
            "nome": fake.first_name() + " " + fake.last_name(),            # Nome da persona sem sr e sra
            "email": fake.email(),          # Email da persona
            "data_nascimento": fake.date_of_birth()  # Data de nascimento
        }
        personas.append(persona)  # Adiciona o dicionário à lista
 
    return personas  # Retorna a lista de personas
 
def exportar_para_csv(personas, nome_arquivo='personas.csv'):
    caminho = r"C:\Users\Dione\Desktop\Aula_QA_2025\Atv 05 - Massa de teste\personas.csv"
    with open(nome_arquivo, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=personas[0].keys())
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)
           
# Gerando as personas
lista_personas = criar_personas()
 
# Exportando para um arquivo CSV
exportar_para_csv(lista_personas)
 
print("Personas criadas e exportada para 'personas.csv' com sucesso!")
