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
    
    dataset = {}

    for line in data:
        fields = parse_csv_line(line.strip()) 
        actor = fields[0]
        total_gross = fields[1]
        dataset[actor] = total_gross

sorted_dataset = sorted(dataset.items(), key=lambda x: x[1], reverse=True)

result = ""
for actor, total in sorted_dataset:
    result += f"{actor} - {total}\n"

print(result)

with open("etapa-4.txt", "w", encoding="utf-8") as output:
    output.write(result)
    


