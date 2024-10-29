class RelogioDigitalSimples:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def ajustar_horas(self, horas):
        if 0 <= horas < 24:
            self.horas = horas
        else:
            print("Horas devem estar entre 0 e 23.")

    def ajustar_minutos(self, minutos):
        if 0 <= minutos < 60:
            self.minutos = minutos
        else:
            print("Minutos devem estar entre 0 e 59.")

    def ajustar_segundos(self, segundos):
        if 0 <= segundos < 60:
            self.segundos = segundos
        else:
            print("Segundos devem estar entre 0 e 59.")

    def exibir_horario(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"

relogio1 = RelogioDigitalSimples(12, 30, 45)
relogio2 = RelogioDigitalSimples(8, 15, 30)

print("Relógio 1 - Hora inicial:", relogio1.exibir_horario())
print("Relógio 2 - Hora inicial:", relogio2.exibir_horario())

relogio1.ajustar_horas(14)
relogio1.ajustar_minutos(45)
relogio1.ajustar_segundos(50)

relogio2.ajustar_horas(9)
relogio2.ajustar_minutos(0)
relogio2.ajustar_segundos(15)

print("Relógio 1 - Hora ajustada:", relogio1.exibir_horario())
print("Relógio 2 - Hora ajustada:", relogio2.exibir_horario())
