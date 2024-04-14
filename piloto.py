from datetime import datetime

class ManicureAgenda:
    def __init__(self):
        self.agenda = {}

    def agendar_horario(self, cliente, data_horario):
        if data_horario in self.agenda:
            print("Desculpe, este horário já está agendado. Por favor, escolha outro horário.")
        else:
            self.agenda[data_horario] = cliente
            print("Agendamento realizado com sucesso para {} no horário {}".format(cliente, data_horario))

    def desmarcar_horario(self, data_horario):
        if data_horario in self.agenda:
            del self.agenda[data_horario]
            print("Horário desmarcado com sucesso.")
        else:
            print("Desculpe, este horário não está agendado.")

    def mostrar_agenda(self):
        if self.agenda:
            print("Agenda de Horários:")
            for data_horario, cliente in self.agenda.items():
                print("- {}: {}".format(data_horario.strftime("%d/%m/%Y %H:%M"), cliente))
        else:
            print("Não há horários agendados.")

def menu():
    print("\n--- Menu ---")
    print("1. Agendar Horário")
    print("2. Desmarcar Horário")
    print("3. Mostrar Agenda")
    print("4. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    agenda = ManicureAgenda()

    while True:
        escolha = menu()

        if escolha == "1":
            cliente = input("Digite o nome do cliente: ")
            data_str = input("Digite a data e hora no formato (dd/mm/yyyy hh:mm): ")
            data_horario = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
            agenda.agendar_horario(cliente, data_horario)
        elif escolha == "2":
            data_str = input("Digite a data e hora do horário a ser desmarcado (dd/mm/yyyy hh:mm): ")
            data_horario = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
            agenda.desmarcar_horario(data_horario)
        elif escolha == "3":
            agenda.mostrar_agenda()
        elif escolha == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
