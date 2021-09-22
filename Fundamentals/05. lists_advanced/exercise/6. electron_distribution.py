total_electrons = int(input())
electron_configuration = []
current_layer = 1

while total_electrons > 0:
    current_layer_electrons = 2 * pow(current_layer, 2)

    if total_electrons >= current_layer_electrons:
        electron_configuration.append(current_layer_electrons)
    else:
        electron_configuration.append(total_electrons)

    total_electrons -= current_layer_electrons
    current_layer += 1

electron_configuration_str = [layer for layer in electron_configuration]
print(electron_configuration)