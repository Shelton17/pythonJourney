def is_criticality_balanced (temperature, neurons_emitted):
    productState = temperature * neurons_emitted
    if temperature < 800 and neurons_emitted > 500 and productState < 500000:
        return True
    else:
        return False

testCritically = is_criticality_balanced ( 750,600)
print(testCritically)

def reactor_efficiency (voltage, current, maxPower):
    generated_power = voltage *current
    efficiency = (generated_power / maxPower) * 100
    if efficiency >= 80:
        band = 'green'
    elif efficiency >= 60 and efficiency < 80:
        band = 'orange'
    elif efficiency >= 30 and efficiency <60:
        band = 'red'
    elif efficiency < 30:
        band = 'black'
    
    return band

testOutputRange = reactor_efficiency(200, 50, 15000)
print(testOutputRange)

def fail_safe (temperature, neutrons_produced_per_second, threshold):
    prodNeutronsTemp = temperature *neutrons_produced_per_second
    if prodNeutronsTemp < threshold * 0.9:
        return 'LOW'
    elif prodNeutronsTemp < threshold * 0.1 or prodNeutronsTemp < threshold * -0.1:
        return 'NORMAL'
    else:
        return 'DANGER'

testFailSafe  = fail_safe(temperature=1000, neutrons_produced_per_second=30,threshold=5000)
print (testFailSafe)