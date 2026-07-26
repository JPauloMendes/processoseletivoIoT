from machine import Pin, I2C
import time
import struct

print("Sistema de Monitoramento Inicializado")

# Configuração Padrão do I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
btn1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
MPU6050_ADDR = 0x68

def inicializar_mpu():
    i2c.writeto_mem(MPU6050_ADDR, 0x6B, b'\x00')

def ler_temperatura():
    temp_bytes = i2c.readfrom_mem(MPU6050_ADDR, 0x41, 2)
    temp_raw = struct.unpack(">h", temp_bytes)[0]
    return (temp_raw / 340.0) + 36.53

try:
    inicializar_mpu()
except:
    pass

# Captura inicial fixa da referência térmica
time.sleep(0.5)
temperatura_referencia = ler_temperatura()

LIMITE_TEMPO_X = 5000
LIMITE_VARIACAO_Y = 3.0

alarme_porta_ativo = False
alarme_temp_ativo = False
porta_estava_aberta = False
tempo_abertura_inicio = 0

while True:
    estado_porta = btn1.value()

    try:
        temp_atual = ler_temperatura()
    except:
        temp_atual = temperatura_referencia

    # 1. Checagem da Porta (1 = Fechada, 0 = Aberta de acordo com o teste)
    if estado_porta == 0:
        if not porta_estava_aberta:
            tempo_abertura_inicio = time.ticks_ms()
            porta_estava_aberta = True

        if not alarme_porta_ativo:
            tempo_decorrido = time.ticks_diff(time.ticks_ms(), tempo_abertura_inicio)
            if tempo_decorrido >= LIMITE_TEMPO_X:
                print("ALERTA: Porta aberta por muito tempo!")
                alarme_porta_ativo = True
    else:
        porta_estava_aberta = False
        tempo_abertura_inicio = time.ticks_ms()

    # 2. Checagem da Temperatura
    delta_t = abs(temp_atual - temperatura_referencia)
    if delta_t >= LIMITE_VARIACAO_Y and not alarme_temp_ativo:
        print("ALERTA: Degradacao termica detectada!")
        alarme_temp_ativo = True

        # 3. Checagem de Normalização
    if alarme_porta_ativo or alarme_temp_ativo:
        porta_ok = (estado_porta == 1)
        temp_ok = (abs(temp_atual - temperatura_referencia) < LIMITE_VARIACAO_Y)

        if porta_ok and temp_ok:
            time.sleep(0.6) 
            
            print("Status: Sistema Normalizado.")
            alarme_porta_ativo = False
            alarme_temp_ativo = False
            porta_estava_aberta = False