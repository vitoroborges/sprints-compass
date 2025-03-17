def parse_csv_line(line):
    fields = []
    current_field = ""
    inside_quotes = False
    
    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes  
        elif char == ',' and not inside_quotes:
            fields.append(current_field.strip())
            current_field = ""
        else:
            current_field += char
    
    fields.append(current_field.strip())  
    return fields

with open("actors.csv", "r") as file:
    lines = file.readlines()
    data = lines[1:]

    total_gross = 0
    aux = 0


    for line in data:
        fields = parse_csv_line(line.strip())
        gross = float(fields[-1])
        total_gross += gross
        aux += 1

    media = total_gross / aux if aux > 1 else 0

    result = f"A média de receita bruta dos principais filmes é {media:.2f} bilhões de dólares."

print(result)

with open("etapa-2.txt", "w", encoding="utf-8") as output:
    output.write(result)